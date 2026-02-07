# Stack Tecnológico

## 🛠️ Tecnologias Recomendadas

### Camada de Captura e Visão Computacional

#### **OpenCV** (Python)
- **Versão**: 4.8+
- **Uso**: Captura de vídeo, pré-processamento de frames
- **Por quê**: Biblioteca madura, bem documentada, suporte multiplataforma
- **Alternativas**: PyAV, imageio

#### **MediaPipe** (Google)
- **Versão**: 0.10+
- **Uso**: Detecção de rosto e extração de landmarks
- **Por quê**: 
  - Rápido e otimizado (pode rodar em CPU)
  - Suporta 468 pontos de landmarks faciais
  - Boa precisão em tempo real
- **Alternativas**: dlib, face_recognition

#### **dlib** (C++/Python)
- **Versão**: 19.24+
- **Uso**: Alternativa para landmarks faciais (68 pontos)
- **Por quê**: Precisão alta, modelo pré-treinado disponível
- **Nota**: Mais pesado que MediaPipe, mas mais preciso

---

### Camada de Análise e Machine Learning

#### **PyTorch** (Recomendado)
- **Versão**: 2.0+
- **Uso**: Modelos de classificação de emoções
- **Por quê**:
  - Flexível para treinamento customizado
  - Boa integração com Python
  - Suporte GPU (CUDA/Metal)
- **Alternativas**: TensorFlow, ONNX Runtime

#### **ONNX Runtime**
- **Versão**: 1.15+
- **Uso**: Inferência de modelos ONNX (mais leve que PyTorch)
- **Por quê**:
  - Menor overhead para inferência
  - Suporta múltiplos backends (CPU, GPU, TensorRT)
  - Modelos podem ser exportados de PyTorch/TensorFlow
- **Quando usar**: Para produção, quando não precisa treinar

#### **Modelos Pré-treinados Sugeridos**

1. **FER+** (Facial Expression Recognition Plus)
   - Dataset: FER+ (35k imagens)
   - Emoções: 7 classes básicas
   - Tamanho: ~5MB
   - Precisão: ~85%

2. **AffectNet**
   - Dataset: AffectNet (1M+ imagens)
   - Emoções: 7 classes + valência/arousal
   - Tamanho: ~50MB
   - Precisão: ~90%

3. **EmotiW** (Emotion Recognition in the Wild)
   - Focado em condições não controladas
   - Boa para uso em ambiente real

#### **NumPy & SciPy**
- **Uso**: Processamento numérico, cálculos de estados derivados
- **Versão**: 1.24+

#### **Pandas**
- **Uso**: Gerenciamento de histórico emocional temporal
- **Versão**: 2.0+

---

### Camada de Persona (Lógica de Negócio)

#### **Python Puro**
- **Uso**: Engine de persona, sistema de regras
- **Bibliotecas**:
  - `pyyaml` ou `toml`: Configuração de regras
  - `json`: Serialização de dados
  - `dataclasses`: Estruturas de dados

---

### Camada de Comunicação

#### **WebSocket** (Recomendado)
- **Biblioteca Python**: `websockets` ou `python-socketio`
- **Versão**: websockets 11.0+
- **Uso**: Comunicação Python ↔ Renderer
- **Por quê**: 
  - Baixa latência
  - Bidirecional
  - Suporta JSON nativamente

#### **Alternativas IPC**
- **Named Pipes** (Windows): `win32pipe`
- **Unix Sockets** (Linux/macOS): `socket` (built-in)
- **Message Queue**: Redis/RabbitMQ (para arquitetura distribuída)

---

### Camada de Renderização

#### **Opção A: Electron + Three.js** (Recomendado para MVP)
- **Electron**: 27+
- **Three.js**: r150+
- **Por quê**:
  - Fácil integração com web technologies
  - Grande ecossistema de bibliotecas
  - Desenvolvimento rápido
- **Desvantagens**: Maior consumo de memória

#### **Opção B: Unity** (Recomendado para gráficos avançados)
- **Versão**: Unity 2022.3 LTS+
- **Por quê**:
  - Excelente para gráficos 3D
  - Sistema de animação robusto
  - Performance otimizada
- **Desvantagens**: Curva de aprendizado, build maior

#### **Opção C: PyQt/PySide + OpenGL**
- **PySide6**: 6.5+
- **PyOpenGL**: 3.1+
- **Por quê**:
  - Tudo em Python (mesma linguagem)
  - Controle total
  - Sem dependências externas pesadas
- **Desvantagens**: Mais trabalho manual

#### **Opção D: WebGL Standalone**
- **Three.js** + servidor HTTP local
- **Por quê**: Leve, rápido de desenvolver
- **Desvantagens**: Menos controle sobre janela/overlay

---

### Ferramentas de Desenvolvimento

#### **Gerenciamento de Dependências**
- **pip**: Gerenciador padrão Python
- **poetry** ou **pipenv**: Alternativas modernas (recomendado)

#### **Ambiente Virtual**
- **venv** (built-in Python) ou **conda**

#### **Type Checking**
- **mypy**: Type hints para Python

#### **Linting & Formatting**
- **black**: Formatação de código
- **flake8** ou **pylint**: Linting
- **isort**: Organização de imports

#### **Testing**
- **pytest**: Framework de testes
- **pytest-asyncio**: Testes assíncronos
- **pytest-cov**: Coverage

#### **Build & Packaging**
- **PyInstaller** ou **cx_Freeze**: Executáveis standalone
- **setuptools**: Distribuição via pip

---

## 📦 Estrutura de Dependências

### `requirements.txt` (Python)

```txt
# Visão Computacional
opencv-python>=4.8.0
mediapipe>=0.10.0
dlib>=19.24.0

# Machine Learning
torch>=2.0.0
torchvision>=0.15.0
onnxruntime>=1.15.0
numpy>=1.24.0
scipy>=1.10.0

# Processamento de Dados
pandas>=2.0.0

# Comunicação
websockets>=11.0
python-socketio>=5.8.0

# Configuração
pyyaml>=6.0
toml>=0.10.2

# Utilitários
python-dotenv>=1.0.0
loguru>=0.7.0

# Desenvolvimento (opcional)
pytest>=7.4.0
pytest-asyncio>=0.21.0
black>=23.7.0
mypy>=1.5.0
```

### `package.json` (Renderer - Electron)

```json
{
  "dependencies": {
    "electron": "^27.0.0",
    "three": "^0.150.0",
    "ws": "^8.14.0"
  },
  "devDependencies": {
    "electron-builder": "^24.6.0",
    "typescript": "^5.2.0",
    "@types/three": "^0.150.0"
  }
}
```

---

## 🖥️ Requisitos de Sistema

### Mínimos
- **OS**: Windows 10+, macOS 10.15+, Ubuntu 20.04+
- **CPU**: Dual-core 2.0GHz+
- **RAM**: 4GB
- **GPU**: Opcional (CPU funciona, mas mais lento)
- **Câmera**: Webcam USB ou integrada

### Recomendados
- **CPU**: Quad-core 3.0GHz+ (Intel i5/AMD Ryzen 5 ou superior)
- **RAM**: 8GB+
- **GPU**: NVIDIA GTX 1050+ ou equivalente (para aceleração ML)
- **Câmera**: 720p ou superior

---

## 🚀 Performance Esperada

### Com CPU apenas
- **FPS**: 15-20 fps
- **Latência**: 100-150ms
- **Uso CPU**: 40-60%

### Com GPU (CUDA/Metal)
- **FPS**: 25-30 fps
- **Latência**: 50-80ms
- **Uso GPU**: 30-50%
- **Uso CPU**: 20-30%

### Otimizações
- Quantização de modelos (INT8): 2-3x mais rápido
- TensorRT (NVIDIA): 3-5x mais rápido
- Batch processing: Melhor utilização de GPU

---

## 🔒 Privacidade e Segurança

### Processamento Local
- ✅ Tudo roda localmente (sem cloud)
- ✅ Modelos baixados uma vez, usados offline
- ✅ Dados de vídeo nunca salvos

### Dependências Seguras
- Verificar vulnerabilidades: `pip-audit` ou `safety`
- Manter dependências atualizadas
- Usar versões LTS quando possível

---

## 📚 Recursos e Documentação

### Documentação Oficial
- [OpenCV Docs](https://docs.opencv.org/)
- [MediaPipe Face](https://google.github.io/mediapipe/solutions/face_mesh)
- [PyTorch Docs](https://pytorch.org/docs/)
- [ONNX Runtime](https://onnxruntime.ai/docs/)
- [Electron Docs](https://www.electronjs.org/docs)
- [Three.js Docs](https://threejs.org/docs/)

### Modelos e Datasets
- [FER+ Dataset](https://github.com/Microsoft/FERPlus)
- [AffectNet](http://mohammadmahoor.com/affectnet/)
- [Model Zoo](https://pytorch.org/vision/stable/models.html)

---

## 🎯 Recomendação Final

**Para MVP**:
- Python + OpenCV + MediaPipe + PyTorch (ONNX Runtime)
- Electron + Three.js para renderização
- WebSocket para comunicação

**Para Produção**:
- Considerar Unity para melhor performance gráfica
- ONNX Runtime com TensorRT (NVIDIA) ou CoreML (Apple)
- Otimização de modelos (quantização, pruning)
