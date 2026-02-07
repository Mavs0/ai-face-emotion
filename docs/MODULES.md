# Módulos e Componentes

## 📦 Estrutura Modular Detalhada

### 1. Módulo de Captura (`src/capture/`)

#### `camera_capture.py`
```python
class CameraCapture:
    - open_camera(device_id: int) -> bool
    - read_frame() -> np.ndarray
    - release()
    - get_fps() -> float
    - set_resolution(width: int, height: int)
```

**Responsabilidades**:
- Gerenciar conexão com câmera USB/webcam
- Capturar frames em resolução configurável
- Controlar taxa de frames (FPS)
- Tratamento de erros (câmera desconectada, etc.)

#### `face_detector.py`
```python
class FaceDetector:
    - detect_faces(frame: np.ndarray) -> List[FaceBoundingBox]
    - get_primary_face(faces: List) -> FaceBoundingBox
```

**Responsabilidades**:
- Detectar múltiplos rostos no frame
- Selecionar rosto principal (maior, mais central)
- Retornar bounding boxes normalizadas

**Tecnologias**: MediaPipe Face Detection ou MTCNN

#### `landmark_extractor.py`
```python
class LandmarkExtractor:
    - extract_landmarks(frame: np.ndarray, bbox: FaceBoundingBox) -> Landmarks
    - get_eye_landmarks(landmarks: Landmarks) -> Tuple[EyeLandmarks, EyeLandmarks]
    - get_mouth_landmarks(landmarks: Landmarks) -> MouthLandmarks
```

**Responsabilidades**:
- Extrair 68 pontos de landmarks faciais
- Normalizar coordenadas relativas ao rosto
- Extrair regiões específicas (olhos, boca, sobrancelhas)

**Tecnologias**: dlib ou MediaPipe Face Mesh

#### `frame_processor.py`
```python
class FrameProcessor:
    - preprocess(frame: np.ndarray) -> np.ndarray
    - normalize_face(face_roi: np.ndarray) -> np.ndarray
    - augment(frame: np.ndarray) -> np.ndarray  # Para treinamento
```

**Responsabilidades**:
- Pré-processamento de frames (redimensionamento, normalização)
- Extração de ROI (Region of Interest) do rosto
- Normalização de iluminação e contraste

---

### 2. Módulo de Análise (`src/analysis/`)

#### `emotion_classifier.py`
```python
class EmotionClassifier:
    - __init__(model_path: str)
    - predict(frame: np.ndarray, landmarks: Landmarks) -> EmotionDistribution
    - get_primary_emotion(distribution: EmotionDistribution) -> str
```

**Responsabilidades**:
- Carregar modelo de classificação de emoções
- Prever distribuição de probabilidades das 7 emoções primárias
- Retornar emoção dominante

**Modelos Sugeridos**:
- FER+ (Facial Expression Recognition Plus)
- AffectNet (mais preciso, maior)
- Modelo custom treinado em dataset próprio

**Input**: Face ROI normalizado (224x224 ou 48x48)
**Output**: `{"happy": 0.7, "sad": 0.1, "neutral": 0.2, ...}`

#### `state_calculator.py`
```python
class StateCalculator:
    - calculate_derived_states(
        emotion_history: List[EmotionDistribution],
        landmarks: Landmarks,
        attention_score: float
    ) -> DerivedStates
    
    - is_stressed(history: List) -> float
    - is_tired(landmarks: Landmarks, history: List) -> float
    - is_engaged(attention: float, history: List) -> float
    - is_bored(history: List, attention: float) -> float
    - is_confident(emotions: EmotionDistribution, posture: Posture) -> float
```

**Responsabilidades**:
- Calcular estados emocionais derivados baseados em:
  - Histórico de emoções (últimos N frames)
  - Features faciais (olhos fechados, boca, etc.)
  - Score de atenção
  - Padrões temporais

**Lógica de Exemplo**:
- **Stressed**: Alta variância emocional + tensão facial
- **Tired**: Olhos semi-fechados + baixa energia emocional
- **Engaged**: Alta atenção + emoções positivas/ativas
- **Bored**: Baixa atenção + neutralidade prolongada
- **Confident**: Postura ereta (landmarks) + emoções positivas

#### `micro_expression_detector.py`
```python
class MicroExpressionDetector:
    - detect_microexpressions(
        current_frame: np.ndarray,
        previous_frames: List[np.ndarray]
    ) -> List[MicroExpression]
```

**Responsabilidades**:
- Detectar microexpressões (expressões muito rápidas, <500ms)
- Analisar diferenças sutis entre frames consecutivos
- Identificar tentativas de suprimir emoções

**Tecnologias**: Optical Flow + análise temporal

#### `attention_tracker.py`
```python
class AttentionTracker:
    - calculate_attention_score(
        landmarks: Landmarks,
        head_pose: HeadPose,
        eye_gaze: EyeGaze
    ) -> float  # 0.0 a 1.0
    
    - is_looking_at_camera(head_pose: HeadPose) -> bool
    - calculate_eye_openness(landmarks: Landmarks) -> float
```

**Responsabilidades**:
- Calcular score de atenção baseado em:
  - Direção do olhar (gaze tracking)
  - Pose da cabeça (head pose estimation)
  - Abertura dos olhos
  - Movimento da cabeça

#### `emotion_history.py`
```python
class EmotionHistory:
    - add_emotion(timestamp: float, emotions: EmotionDistribution)
    - get_recent_history(duration_seconds: float) -> List[EmotionRecord]
    - get_emotion_trend(emotion: str, window: int) -> float
    - get_dominant_emotion_period(start: float, end: float) -> str
```

**Responsabilidades**:
- Manter buffer circular de histórico emocional
- Calcular tendências temporais
- Identificar padrões emocionais recorrentes
- Suportar queries temporais

**Armazenamento**: Buffer em memória (últimos 5 minutos a 30fps = 9000 registros)

---

### 3. Módulo de Persona (`src/persona/`)

#### `persona_engine.py`
```python
class PersonaEngine:
    - __init__(config_path: str)
    - update(emotion_data: EmotionData, derived_states: DerivedStates) -> PersonaState
    - get_current_state() -> PersonaState
    - reset()
```

**Responsabilidades**:
- Coordenar todos os componentes da persona
- Manter estado atual do avatar
- Decidir transições de estado
- Calcular intensidade de reações

#### `behavior_rules.py`
```python
class BehaviorRules:
    - evaluate_rule(rule: Rule, context: Context) -> bool
    - get_applicable_rules(context: Context) -> List[Rule]
    - execute_rule(rule: Rule) -> Action
```

**Sistema de Regras**:
```yaml
rules:
  - name: "happy_reaction"
    condition:
      primary_emotion: "happy"
      intensity: "> 0.6"
    action:
      expression: "happy"
      animation: "wave"
      intensity: 0.8
      
  - name: "comfort_sad"
    condition:
      primary_emotion: "sad"
      duration: "> 3s"
    action:
      expression: "empathetic"
      animation: "comfort"
      message: "Está tudo bem?"
```

**Responsabilidades**:
- Definir regras comportamentais da persona
- Avaliar condições contextuais
- Selecionar ações apropriadas

#### `state_machine.py`
```python
class PersonaStateMachine:
    - transition_to(state: PersonaState)
    - can_transition(from_state: PersonaState, to_state: PersonaState) -> bool
    - get_available_transitions() -> List[PersonaState]
```

**Estados da Persona**:
- `idle`: Estado neutro, aguardando
- `reacting`: Reagindo a emoção atual
- `comforting`: Tentando confortar (emoção negativa prolongada)
- `celebrating`: Celebrando (emoção positiva)
- `observing`: Observando silenciosamente

**Responsabilidades**:
- Gerenciar transições de estado
- Validar transições permitidas
- Manter histórico de estados

#### `reaction_calculator.py`
```python
class ReactionCalculator:
    - calculate_intensity(
        emotion_intensity: float,
        emotion_duration: float,
        emotion_change: float
    ) -> float
    
    - should_react(
        current_emotion: str,
        previous_emotion: str,
        time_since_change: float
    ) -> bool
```

**Responsabilidades**:
- Calcular intensidade da reação (0.0 a 1.0)
- Decidir se deve reagir (evitar reações excessivas)
- Considerar mudanças súbitas vs. mudanças graduais

---

### 4. Módulo de Comunicação (`src/communication/`)

#### `message_bus.py`
```python
class MessageBus:
    - publish(topic: str, message: dict)
    - subscribe(topic: str, callback: Callable)
    - unsubscribe(topic: str, callback: Callable)
```

**Tópicos**:
- `capture.frame`: Novos frames capturados
- `analysis.emotion`: Resultados de análise emocional
- `persona.action`: Ações da persona
- `renderer.command`: Comandos para renderização

#### `websocket_server.py`
```python
class WebSocketServer:
    - start(host: str, port: int)
    - send_to_client(message: dict)
    - on_client_connect(callback: Callable)
    - on_client_disconnect(callback: Callable)
```

**Responsabilidades**:
- Servir WebSocket para comunicação com renderer
- Serializar/deserializar mensagens JSON
- Gerenciar conexões de clientes

#### `ipc_manager.py`
```python
class IPCManager:
    - send_message(process: str, message: dict)
    - receive_message() -> dict
    - create_pipe(name: str) -> Pipe
```

**Responsabilidades**:
- Gerenciar comunicação inter-processo
- Suportar múltiplos métodos (pipes, sockets, queues)

---

### 5. Módulo Principal (`src/`)

#### `main.py`
```python
def main():
    # Inicialização
    camera = CameraCapture()
    face_detector = FaceDetector()
    emotion_classifier = EmotionClassifier()
    persona_engine = PersonaEngine()
    renderer_client = WebSocketClient()
    
    # Loop principal
    while running:
        frame = camera.read_frame()
        faces = face_detector.detect_faces(frame)
        if faces:
            landmarks = extract_landmarks(frame, faces[0])
            emotions = emotion_classifier.predict(frame, landmarks)
            states = calculate_derived_states(emotions, landmarks)
            persona_state = persona_engine.update(emotions, states)
            renderer_client.send(persona_state)
```

**Responsabilidades**:
- Orquestrar todos os módulos
- Gerenciar ciclo de vida da aplicação
- Tratamento de erros global
- Logging e monitoramento

---

## 🔌 Interfaces entre Módulos

### Capture → Analysis
```python
FrameData = {
    "frame": np.ndarray,
    "face_bbox": BoundingBox,
    "landmarks": Landmarks,
    "timestamp": float
}
```

### Analysis → Persona
```python
EmotionData = {
    "emotions": Dict[str, float],
    "primary_emotion": str,
    "derived_states": Dict[str, float],
    "attention_score": float,
    "microexpressions": List[MicroExpression],
    "timestamp": float
}
```

### Persona → Renderer
```python
PersonaState = {
    "expression": str,
    "animation": str,
    "intensity": float,
    "position": Tuple[float, float],
    "scale": float,
    "duration": float
}
```

## 🧩 Extensibilidade

Cada módulo pode ser estendido sem afetar outros:

- **Novos modelos de emoção**: Implementar interface `EmotionClassifier`
- **Novas personas**: Criar novo arquivo de configuração em `persona/configs/`
- **Novos renderers**: Implementar interface `RendererClient`
- **Novos estados derivados**: Adicionar métodos em `StateCalculator`
