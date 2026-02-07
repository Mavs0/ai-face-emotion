# Arquitetura do Sistema

## Visão Geral da Arquitetura

O **AI Face Emotion Persona Overlay** segue uma arquitetura em camadas com comunicação assíncrona entre módulos, permitindo processamento paralelo e escalabilidade.

## 🏛️ Arquitetura em Camadas

```
┌─────────────────────────────────────────────────────────┐
│              CAMADA DE RENDERIZAÇÃO                      │
│  (Unity/Electron + WebGL) - Avatar Visual               │
└──────────────────┬──────────────────────────────────────┘
                   │ IPC/WebSocket
┌──────────────────▼──────────────────────────────────────┐
│            CAMADA DE PERSONA                             │
│  Engine de Comportamento - Regras e Estados              │
└──────────────────┬──────────────────────────────────────┘
                   │ Dados Emocionais
┌──────────────────▼──────────────────────────────────────┐
│          CAMADA DE ANÁLISE                              │
│  Processamento Emocional - ML Models                    │
└──────────────────┬──────────────────────────────────────┘
                   │ Features Faciais
┌──────────────────▼──────────────────────────────────────┐
│          CAMADA DE CAPTURA                              │
│  Visão Computacional - Face Detection                   │
└─────────────────────────────────────────────────────────┘
```

## 📦 Componentes Principais

### 1. Camada de Captura (`capture/`)

**Responsabilidade**: Aquisição de vídeo e detecção facial básica

**Componentes**:
- `CameraCapture`: Gerencia acesso à câmera
- `FaceDetector`: Detecta rostos no frame
- `LandmarkExtractor`: Extrai landmarks faciais (68 pontos)
- `FrameProcessor`: Pipeline de pré-processamento

**Tecnologias**:
- OpenCV para captura de vídeo
- MediaPipe Face Detection ou dlib para landmarks
- NumPy para processamento de arrays

**Saída**: 
- Frames processados (RGB)
- Coordenadas de bounding box do rosto
- Array de landmarks faciais (68 pontos)

### 2. Camada de Análise (`analysis/`)

**Responsabilidade**: Classificação de emoções e cálculo de estados derivados

**Componentes**:
- `EmotionClassifier`: Modelo de classificação de emoções primárias
- `StateCalculator`: Cálculo de estados emocionais derivados
- `MicroExpressionDetector`: Detecção de microexpressões
- `EmotionHistory`: Timeline e histórico emocional
- `AttentionTracker`: Rastreamento de atenção/foco

**Tecnologias**:
- PyTorch ou ONNX Runtime para inferência
- Modelos pré-treinados (FER+, AffectNet, ou custom)
- Pandas para histórico temporal

**Saída**:
- Distribuição de probabilidades de emoções primárias
- Estados emocionais derivados (stressed, tired, etc.)
- Score de atenção (0-1)
- Histórico temporal de emoções

### 3. Camada de Persona (`persona/`)

**Responsabilidade**: Mapear estados emocionais em comportamentos do avatar

**Componentes**:
- `PersonaEngine`: Motor principal de decisão
- `BehaviorRules`: Sistema de regras comportamentais
- `StateMachine`: Máquina de estados do avatar
- `ReactionCalculator`: Cálculo de intensidade de reação
- `PersonaConfig`: Configurações da persona

**Tecnologias**:
- Python puro (lógica de negócio)
- JSON/YAML para configuração de regras
- NumPy para cálculos de similaridade

**Saída**:
- Estado atual do avatar (expressão, postura, animação)
- Intensidade da reação (0-1)
- Próxima ação/animação a executar

### 4. Camada de Renderização (`renderer/`)

**Responsabilidade**: Visualização do avatar na tela

**Componentes**:
- `Renderer`: Sistema de renderização principal
- `AvatarController`: Controla animações do avatar
- `OverlayManager`: Gerencia overlay/janela flutuante
- `AnimationSystem`: Sistema de animações

**Tecnologias**:
- **Opção A**: Unity (C#) - Melhor para gráficos 3D
- **Opção B**: Electron + Three.js/WebGL - Mais fácil integração web
- **Opção C**: PyQt/PySide + OpenGL - Tudo em Python

**Saída**: 
- Janela/overlay renderizado com avatar animado

## 🔄 Sistema de Comunicação

### IPC (Inter-Process Communication)

Para comunicação entre módulos Python e renderer:

**Opção 1: WebSocket (Recomendado)**
```
Python Backend (localhost:8765) ←→ Electron/Unity Frontend
```

**Opção 2: Named Pipes / Unix Sockets**
```
Python Backend ←→ Renderer Process
```

**Opção 3: Message Queue (Redis/RabbitMQ)**
```
Python Backend ←→ Message Queue ←→ Renderer
```

### Formato de Mensagens

```json
{
  "timestamp": 1234567890.123,
  "type": "emotion_update",
  "data": {
    "emotions": {
      "happy": 0.7,
      "sad": 0.1,
      "neutral": 0.2
    },
    "derived_states": {
      "stressed": 0.3,
      "engaged": 0.8
    },
    "attention_score": 0.85,
    "face_detected": true
  }
}
```

```json
{
  "timestamp": 1234567890.123,
  "type": "persona_action",
  "data": {
    "expression": "happy",
    "intensity": 0.7,
    "animation": "wave",
    "duration": 2.0
  }
}
```

## 🗄️ Armazenamento de Dados

### Em Memória (Tempo Real)
- Buffer de frames recentes (últimos 30 frames)
- Histórico emocional (últimos 5 minutos)
- Estado atual da persona

### Persistência (Opcional)
- Histórico emocional diário (SQLite)
- Configurações do usuário (JSON)
- Modelos de persona customizados

## ⚡ Fluxo de Processamento

1. **Captura** (30ms): Frame capturado da câmera
2. **Detecção** (50ms): Rosto detectado e landmarks extraídos
3. **Análise** (100ms): Emoções classificadas, estados calculados
4. **Persona** (20ms): Comportamento do avatar determinado
5. **Renderização** (33ms): Avatar atualizado na tela

**Total**: ~233ms por ciclo (≈4.3 fps teórico, otimizado para 30fps)

## 🔒 Privacidade e Segurança

- ✅ Processamento 100% local (sem envio para servidores)
- ✅ Dados de vídeo nunca salvos em disco
- ✅ Histórico emocional opcional e local
- ✅ Sem telemetria ou tracking externo

## 📊 Escalabilidade

### Horizontal
- Múltiplas câmeras (futuro)
- Múltiplas personas simultâneas

### Vertical
- Otimização de modelos (quantização, pruning)
- GPU acceleration (CUDA/Metal)
- Processamento em batches

## 🧪 Testabilidade

Cada camada é testável independentemente:
- Mock de câmera para testes sem hardware
- Dados sintéticos para validação de modelos
- Simulação de estados emocionais para persona
- Headless mode para renderização
