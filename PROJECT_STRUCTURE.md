# Estrutura do Projeto - AI Face Emotion Persona Overlay

## 📁 Árvore de Diretórios Completa

```
ai-face-emotion/
│
├── 📄 README.md                    # Documentação principal do projeto
├── 📄 PROJECT_STRUCTURE.md         # Este arquivo
├── 📄 .gitignore                   # Arquivos ignorados pelo Git
├── 📄 requirements.txt             # Dependências Python
│
├── 📁 docs/                        # Documentação técnica completa
│   ├── 📄 README.md                # Índice da documentação
│   ├── 📄 EXECUTIVE_SUMMARY.md     # Resumo executivo
│   ├── 📄 ARCHITECTURE.md          # Arquitetura em camadas
│   ├── 📄 MODULES.md               # Módulos e componentes
│   ├── 📄 DATA_FLOW.md             # Fluxo de dados
│   ├── 📄 TECH_STACK.md            # Stack tecnológico
│   ├── 📄 MVP.md                   # Plano do MVP
│   ├── 📄 ROADMAP.md               # Roadmap de desenvolvimento
│   └── 📄 DIAGRAMS.md              # Diagramas visuais
│
├── 📁 src/                         # Código fonte Python (Backend)
│   ├── 📄 __init__.py              # Inicialização do pacote
│   ├── 📄 main.py                  # Entry point principal
│   │
│   ├── 📁 capture/                 # Módulo de captura
│   │   ├── 📄 __init__.py
│   │   ├── 📄 camera.py            # CameraCapture (a implementar)
│   │   ├── 📄 face_detector.py     # FaceDetector (a implementar)
│   │   └── 📄 landmark_extractor.py # LandmarkExtractor (a implementar)
│   │
│   ├── 📁 detection/               # Módulo de detecção (alias para capture)
│   │   └── 📄 __init__.py
│   │
│   ├── 📁 emotion/                 # Módulo de análise emocional
│   │   ├── 📄 __init__.py
│   │   ├── 📄 classifier.py        # EmotionClassifier (a implementar)
│   │   ├── 📄 state_calculator.py  # StateCalculator (a implementar)
│   │   ├── 📄 history.py           # EmotionHistory (a implementar)
│   │   └── 📄 attention_tracker.py # AttentionTracker (a implementar)
│   │
│   ├── 📁 persona/                 # Módulo de persona
│   │   ├── 📄 __init__.py
│   │   ├── 📄 engine.py            # PersonaEngine (a implementar)
│   │   ├── 📄 behavior_rules.py    # BehaviorRules (a implementar)
│   │   └── 📄 state_machine.py     # PersonaStateMachine (a implementar)
│   │
│   └── 📁 communication/           # Módulo de comunicação
│       ├── 📄 __init__.py
│       ├── 📄 websocket_server.py  # WebSocketServer (a implementar)
│       └── 📄 message_bus.py       # MessageBus (a implementar)
│
├── 📁 renderer/                    # Renderer (Frontend)
│   ├── 📄 package.json             # Dependências Node.js/Electron
│   │
│   ├── 📁 src/                     # Código fonte do renderer
│   │   ├── 📄 main.js              # Processo principal Electron
│   │   └── 📄 index.html           # Interface HTML do avatar
│   │
│   └── 📁 assets/                  # Assets do renderer
│       └── 📁 avatar/               # Sprites/imagens do avatar
│           ├── 📄 happy.png         # (a criar)
│           ├── 📄 sad.png           # (a criar)
│           └── 📄 neutral.png       # (a criar)
│
├── 📁 models/                      # Modelos de IA pré-treinados
│   └── 📄 emotion_model.onnx       # Modelo de emoções (a baixar)
│
├── 📁 config/                      # Arquivos de configuração
│   ├── 📄 default.yaml             # Configuração padrão do sistema
│   │
│   └── 📁 personas/                # Configurações de personas
│       └── 📄 default.yaml         # Persona padrão
│
├── 📁 tests/                       # Testes unitários e integração
│   ├── 📄 __init__.py
│   ├── 📄 test_capture.py          # (a criar)
│   ├── 📄 test_emotion.py          # (a criar)
│   └── 📄 test_persona.py          # (a criar)
│
└── 📁 assets/                     # Assets gerais do projeto
    └── (imagens, ícones, etc.)
```

---

## 📊 Estatísticas do Projeto

### Documentação Criada
- ✅ **9 documentos técnicos** completos
- ✅ **~15.000 palavras** de documentação
- ✅ **Diagramas ASCII** detalhados
- ✅ **Especificações técnicas** completas

### Código Base Criado
- ✅ **Estrutura de pastas** completa
- ✅ **Entry point** (`main.py`) com skeleton
- ✅ **Configurações** YAML prontas
- ✅ **Renderer básico** Electron configurado
- ✅ **Requirements.txt** com todas as dependências

### Arquivos de Configuração
- ✅ `.gitignore` configurado
- ✅ `requirements.txt` completo
- ✅ `package.json` para Electron
- ✅ Configurações YAML (default + persona)

---

## 🎯 Status de Implementação

### ✅ Completo (Documentação e Estrutura)
- [x] Arquitetura do sistema
- [x] Documentação técnica completa
- [x] Estrutura de pastas
- [x] Arquivos de configuração
- [x] Skeleton do código base

### 🚧 A Implementar (MVP)
- [ ] Módulo de captura (`src/capture/`)
- [ ] Módulo de detecção facial
- [ ] Módulo de classificação emocional
- [ ] Módulo de persona
- [ ] Comunicação WebSocket
- [ ] Renderização do avatar
- [ ] Integração completa

---

## 🔄 Fluxo de Desenvolvimento Recomendado

### Fase 1: Setup (✅ Completo)
1. ✅ Estrutura de pastas criada
2. ✅ Documentação escrita
3. ✅ Configurações definidas

### Fase 2: Implementação MVP (🚧 Próximo)
1. Implementar `CameraCapture`
2. Implementar `FaceDetector`
3. Integrar modelo de emoções
4. Implementar `PersonaEngine` básico
5. Conectar WebSocket
6. Criar avatar visual básico
7. Testar pipeline completo

### Fase 3: Refinamento
1. Otimizar performance
2. Melhorar precisão
3. Adicionar mais emoções
4. Polir UX

---

## 📝 Convenções do Projeto

### Nomenclatura
- **Módulos Python**: snake_case (`camera_capture.py`)
- **Classes**: PascalCase (`CameraCapture`)
- **Funções**: snake_case (`read_frame()`)
- **Constantes**: UPPER_SNAKE_CASE (`MAX_FPS`)

### Estrutura de Commits
```
tipo(escopo): descrição

Exemplos:
feat(capture): implementa CameraCapture
fix(emotion): corrige cálculo de estados derivados
docs(architecture): atualiza diagramas
```

### Branches
- `main`: Código estável
- `develop`: Desenvolvimento ativo
- `feature/nome`: Novas funcionalidades
- `fix/nome`: Correções de bugs

---

## 🚀 Próximos Passos

1. **Instalar dependências**:
   ```bash
   pip install -r requirements.txt
   cd renderer && npm install
   ```

2. **Baixar modelo de emoções**:
   - FER+ ou AffectNet
   - Converter para ONNX se necessário
   - Colocar em `models/`

3. **Implementar módulos** conforme [MVP.md](./docs/MVP.md)

4. **Testar incrementalmente** cada módulo

5. **Integrar e validar** pipeline completo

---

## 📚 Referências Rápidas

- **Documentação principal**: [README.md](./README.md)
- **Índice da documentação**: [docs/README.md](./docs/README.md)
- **Arquitetura**: [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md)
- **Plano MVP**: [docs/MVP.md](./docs/MVP.md)
- **Roadmap**: [docs/ROADMAP.md](./docs/ROADMAP.md)

---

**Última atualização**: Fevereiro 2025  
**Versão**: 0.1.0 (Documentação e Estrutura)
