# Fluxo de Dados

## 🔄 Fluxo Principal: Rosto → Avatar

```
┌─────────────┐
│   Câmera    │
│  (Hardware) │
└──────┬──────┘
       │ Frame RGB (30fps)
       ▼
┌─────────────────────┐
│  CameraCapture      │
│  - read_frame()      │
└──────┬──────────────┘
       │ np.ndarray [H, W, 3]
       ▼
┌─────────────────────┐
│  FaceDetector       │
│  - detect_faces()   │
└──────┬──────────────┘
       │ FaceBoundingBox {x, y, w, h}
       ▼
┌─────────────────────┐
│  LandmarkExtractor  │
│  - extract_landmarks │
└──────┬──────────────┘
       │ Landmarks {68 pontos: [(x,y), ...]}
       ▼
┌─────────────────────┐
│  FrameProcessor     │
│  - normalize_face() │
└──────┬──────────────┘
       │ Face ROI [224, 224, 3] (normalizado)
       ▼
┌─────────────────────┐
│  EmotionClassifier  │
│  - predict()        │
└──────┬──────────────┘
       │ EmotionDistribution {
       │   "happy": 0.7,
       │   "sad": 0.1,
       │   "neutral": 0.2,
       │   ...
       │ }
       ▼
┌─────────────────────┐
│  AttentionTracker   │
│  - calculate_score() │
└──────┬──────────────┘
       │ attention_score: 0.85
       ▼
┌─────────────────────┐
│  EmotionHistory     │
│  - add_emotion()    │
└──────┬──────────────┘
       │ history: List[EmotionRecord]
       ▼
┌─────────────────────┐
│  StateCalculator    │
│  - calculate_derived │
└──────┬──────────────┘
       │ DerivedStates {
       │   "stressed": 0.3,
       │   "tired": 0.1,
       │   "engaged": 0.8,
       │   "bored": 0.0,
       │   "confident": 0.6
       │ }
       ▼
┌─────────────────────┐
│  PersonaEngine      │
│  - update()         │
└──────┬──────────────┘
       │ PersonaState {
       │   "expression": "happy",
       │   "animation": "wave",
       │   "intensity": 0.7,
       │   "duration": 2.0
       │ }
       ▼
┌─────────────────────┐
│  WebSocketServer    │
│  - send_to_client() │
└──────┬──────────────┘
       │ JSON Message
       ▼
┌─────────────────────┐
│  Renderer           │
│  (Unity/Electron)   │
│  - update_avatar()  │
└──────┬──────────────┘
       │
       ▼
   ┌───────┐
   │ Avatar│
   │Visual │
   └───────┘
```

## 📊 Estrutura de Dados Detalhada

### 1. Frame (Captura)
```python
frame: np.ndarray
Shape: [height, width, 3]  # RGB
Dtype: uint8
Range: 0-255
Exemplo: [480, 640, 3] para 640x480
```

### 2. Face Bounding Box
```python
FaceBoundingBox = {
    "x": int,           # Coordenada X do canto superior esquerdo
    "y": int,           # Coordenada Y do canto superior esquerdo
    "width": int,       # Largura do bounding box
    "height": int,      # Altura do bounding box
    "confidence": float  # Confiança da detecção (0.0-1.0)
}
```

### 3. Landmarks Faciais
```python
Landmarks = {
    "points": List[Tuple[int, int]],  # 68 pontos [(x, y), ...]
    "normalized": bool,               # Se coordenadas estão normalizadas
    "regions": {
        "jaw": List[int],             # Índices 0-16
        "right_eyebrow": List[int],   # Índices 17-21
        "left_eyebrow": List[int],    # Índices 22-26
        "nose": List[int],            # Índices 27-35
        "right_eye": List[int],       # Índices 36-41
        "left_eye": List[int],        # Índices 42-47
        "mouth": List[int]            # Índices 48-67
    }
}
```

### 4. Emotion Distribution
```python
EmotionDistribution = {
    "happy": float,      # 0.0-1.0
    "sad": float,
    "angry": float,
    "fear": float,
    "surprise": float,
    "disgust": float,
    "neutral": float,
    "timestamp": float,  # Unix timestamp
    "confidence": float  # Confiança geral da predição
}

# Soma de todas as emoções ≈ 1.0 (distribuição de probabilidades)
```

### 5. Derived States
```python
DerivedStates = {
    "stressed": float,   # 0.0-1.0
    "tired": float,
    "engaged": float,
    "bored": float,
    "confident": float,
    "timestamp": float
}
```

### 6. Persona State
```python
PersonaState = {
    "expression": str,        # "happy", "sad", "empathetic", etc.
    "animation": str,         # "wave", "comfort", "celebrate", "idle"
    "intensity": float,       # 0.0-1.0
    "position": {
        "x": float,           # Posição X na tela (0.0-1.0)
        "y": float            # Posição Y na tela (0.0-1.0)
    },
    "scale": float,          # Escala do avatar (0.5-2.0)
    "rotation": float,       # Rotação em graus
    "duration": float,       # Duração da animação em segundos
    "transition": str        # Tipo de transição: "smooth", "instant"
}
```

## ⏱️ Timeline de Processamento

### Ciclo Completo (30fps = 33ms por frame)

```
T+0ms    ──► Captura de frame
T+5ms    ──► Detecção de rosto
T+15ms   ──► Extração de landmarks
T+20ms   ──► Normalização do rosto
T+50ms   ──► Classificação de emoções (GPU)
T+55ms   ──► Cálculo de atenção
T+60ms   ──► Atualização de histórico
T+65ms   ──► Cálculo de estados derivados
T+70ms   ──► Decisão da persona
T+75ms   ──► Serialização JSON
T+80ms   ──► Envio via WebSocket
T+85ms   ──► Renderização do avatar
T+90ms   ──► Exibição na tela
```

**Nota**: Com otimizações e processamento paralelo, podemos reduzir para ~30-40ms total.

## 🔀 Fluxos Paralelos

### Processamento Assíncrono

```
Thread 1: Captura
  └─► Queue ──► Thread 2: Detecção/Analise
                  └─► Queue ──► Thread 3: Persona
                                  └─► WebSocket ──► Renderer
```

### Buffer de Frames

```
[Frame T-2] [Frame T-1] [Frame T] ──► Processamento
     │           │           │
     └───────────┴───────────┘
         Histórico para análise temporal
```

## 📡 Mensagens WebSocket

### Mensagem: Emotion Update
```json
{
  "type": "emotion_update",
  "timestamp": 1234567890.123,
  "data": {
    "emotions": {
      "happy": 0.7,
      "sad": 0.1,
      "neutral": 0.2
    },
    "primary_emotion": "happy",
    "derived_states": {
      "stressed": 0.3,
      "engaged": 0.8
    },
    "attention_score": 0.85,
    "face_detected": true,
    "confidence": 0.92
  }
}
```

### Mensagem: Persona Action
```json
{
  "type": "persona_action",
  "timestamp": 1234567890.123,
  "data": {
    "expression": "happy",
    "animation": "wave",
    "intensity": 0.7,
    "position": {"x": 0.8, "y": 0.2},
    "scale": 1.0,
    "duration": 2.0,
    "transition": "smooth"
  }
}
```

### Mensagem: System Status
```json
{
  "type": "system_status",
  "timestamp": 1234567890.123,
  "data": {
    "fps": 29.5,
    "face_detected": true,
    "processing_time_ms": 85,
    "camera_status": "connected"
  }
}
```

## 🔄 Feedback Loop

### Persona Reage → Usuário Reage → Persona Reage

```
Usuário sorri (happy: 0.8)
    │
    ▼
Persona reage com animação "celebrate"
    │
    ▼
Usuário vê reação e sorri mais (happy: 0.9)
    │
    ▼
Persona intensifica reação (intensity: 0.9)
```

Este feedback loop cria uma experiência mais imersiva e responsiva.

## 🎯 Otimizações de Fluxo

### 1. Skip Frames
Se processamento está lento, pular frames intermediários:
```
Frame 1 ──► Processar
Frame 2 ──► Pular
Frame 3 ──► Processar
```

### 2. Batch Processing
Processar múltiplos frames juntos quando possível:
```
[Frame 1, Frame 2, Frame 3] ──► Batch inference
```

### 3. Caching
Cachear resultados de detecção se rosto não mudou muito:
```
Se movimento < threshold:
    Reusar landmarks anteriores
```

### 4. Adaptive Quality
Reduzir qualidade quando FPS cai:
```
FPS < 20 ──► Reduzir resolução de captura
FPS < 15 ──► Reduzir qualidade de renderização
```
