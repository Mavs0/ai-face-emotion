# MVP (Minimum Viable Product)

## 🎯 Objetivo do MVP

Criar uma versão funcional mínima que demonstre o conceito core: **detectar emoções do usuário e fazer um avatar reagir visualmente**.

## ✅ Escopo do MVP

### Funcionalidades Incluídas

1. ✅ **Captura básica de vídeo**
   - Acesso à câmera padrão
   - Resolução: 640x480 (suficiente para MVP)
   - FPS: 15-20 fps (aceitável para MVP)

2. ✅ **Detecção de rosto**
   - Detecção simples de rosto (MediaPipe ou OpenCV Haar)
   - Seleção do rosto principal (maior/mais central)

3. ✅ **Classificação de 3 emoções**
   - Happy (Feliz)
   - Sad (Triste)
   - Neutral (Neutro)
   - Usar modelo leve pré-treinado (FER+ ou similar)

4. ✅ **Avatar simples**
   - Avatar 2D básico (sprite ou SVG)
   - 3 estados visuais correspondentes às 3 emoções
   - Transições simples entre estados

5. ✅ **Janela flutuante**
   - Janela sempre no topo (always on top)
   - Posição configurável (canto da tela)
   - Tamanho: 200x200px (compacto)

6. ✅ **Comunicação básica**
   - WebSocket local entre Python e Renderer
   - Mensagens JSON simples

### Funcionalidades Excluídas (para depois)

- ❌ Estados emocionais derivados (stressed, tired, etc.)
- ❌ Microexpressões
- ❌ Histórico emocional detalhado
- ❌ Sistema de regras complexo da persona
- ❌ Múltiplas personas
- ❌ Overlay transparente (apenas janela)
- ❌ Animações complexas
- ❌ Personalização avançada

---

## 🏗️ Arquitetura Simplificada do MVP

```
┌──────────────┐
│   Câmera     │
└──────┬───────┘
       │
┌──────▼──────────────┐
│  Python Backend     │
│  - Capture          │
│  - Detect Face      │
│  - Classify Emotion │
└──────┬──────────────┘
       │ WebSocket
┌──────▼──────────────┐
│  Electron Renderer  │
│  - Simple Avatar    │
│  - 3 States         │
└─────────────────────┘
```

---

## 📁 Estrutura de Arquivos MVP

```
ai-face-emotion/
├── src/
│   ├── capture/
│   │   ├── __init__.py
│   │   └── camera.py          # Captura básica
│   ├── detection/
│   │   ├── __init__.py
│   │   └── face_detector.py   # Detecção simples
│   ├── emotion/
│   │   ├── __init__.py
│   │   └── classifier.py      # Classificação 3 emoções
│   ├── communication/
│   │   ├── __init__.py
│   │   └── websocket_server.py # Servidor WebSocket
│   └── main.py                 # Entry point
├── renderer/
│   ├── main.js                 # Processo principal Electron
│   ├── renderer.js             # Renderização Three.js
│   ├── avatar.js               # Lógica do avatar
│   └── package.json
├── models/
│   └── emotion_model.onnx      # Modelo pré-treinado
├── assets/
│   └── avatar/                 # Sprites do avatar
│       ├── happy.png
│       ├── sad.png
│       └── neutral.png
├── config/
│   └── mvp_config.yaml         # Configurações MVP
└── requirements.txt
```

---

## 🚀 Plano de Implementação

### Fase 1: Setup Básico (1-2 dias)
- [ ] Configurar estrutura de pastas
- [ ] Setup ambiente Python (venv, requirements.txt)
- [ ] Setup Electron básico
- [ ] Testar captura de câmera

### Fase 2: Detecção e Classificação (2-3 dias)
- [ ] Implementar detecção de rosto (MediaPipe)
- [ ] Integrar modelo de emoções (FER+ ou similar)
- [ ] Testar pipeline: câmera → rosto → emoção
- [ ] Validar precisão básica

### Fase 3: Avatar e Renderização (2-3 dias)
- [ ] Criar assets do avatar (3 estados)
- [ ] Implementar renderização básica (Electron + Canvas/Three.js)
- [ ] Conectar estados do avatar às emoções
- [ ] Testar transições visuais

### Fase 4: Comunicação e Integração (1-2 dias)
- [ ] Implementar WebSocket server (Python)
- [ ] Implementar WebSocket client (Electron)
- [ ] Integrar tudo: Python → WebSocket → Electron
- [ ] Testar fluxo completo

### Fase 5: Polimento (1-2 dias)
- [ ] Ajustar performance (FPS, latência)
- [ ] Melhorar UI da janela
- [ ] Adicionar controles básicos (fechar, minimizar)
- [ ] Testes finais

**Total estimado**: 7-12 dias de desenvolvimento

---

## 🎨 Especificações do Avatar MVP

### Design
- **Tipo**: 2D sprite simples ou SVG
- **Estilo**: Minimalista, amigável
- **Cores**: Vibrantes, contrastantes

### Estados

1. **Happy** 😊
   - Expressão: Sorriso largo
   - Cor: Amarelo/Laranja
   - Animação: Leve movimento (bounce)

2. **Sad** 😢
   - Expressão: Sobrancelhas caídas, boca triste
   - Cor: Azul acinzentado
   - Animação: Leve movimento para baixo

3. **Neutral** 😐
   - Expressão: Neutra, calma
   - Cor: Cinza claro
   - Animação: Estático ou respiração sutil

### Transições
- Duração: 0.5-1.0 segundo
- Tipo: Fade ou slide simples

---

## 📊 Métricas de Sucesso do MVP

### Funcionais
- ✅ Detecta rosto do usuário consistentemente
- ✅ Classifica emoções com >70% de precisão
- ✅ Avatar reage às mudanças de emoção
- ✅ Sistema roda sem crashes por 10+ minutos

### Performance
- ✅ FPS mínimo: 15 fps
- ✅ Latência: <200ms (captura → avatar)
- ✅ Uso CPU: <50% em máquina média

### UX
- ✅ Avatar visível e responsivo
- ✅ Janela não interfere com outras aplicações
- ✅ Início rápido (<5 segundos)

---

## 🧪 Testes do MVP

### Testes Manuais
1. **Teste de Detecção**
   - Usuário sorri → Avatar muda para "happy"
   - Usuário faz cara triste → Avatar muda para "sad"
   - Usuário fica neutro → Avatar muda para "neutral"

2. **Teste de Performance**
   - Monitorar FPS durante uso
   - Verificar uso de CPU/RAM
   - Testar com diferentes condições de iluminação

3. **Teste de Estabilidade**
   - Rodar por 30 minutos contínuos
   - Testar com câmera desconectada/reconectada
   - Testar com múltiplos rostos na tela

### Testes Automatizados (Opcional para MVP)
- Testes unitários dos módulos principais
- Mock de câmera para testes sem hardware
- Testes de integração do pipeline

---

## 🔄 Próximos Passos Após MVP

### Versão 1.1 (Melhorias Imediatas)
- Adicionar mais 2-3 emoções (angry, surprise)
- Melhorar precisão do modelo
- Adicionar histórico emocional básico
- Overlay transparente opcional

### Versão 2.0 (Funcionalidades Avançadas)
- Estados emocionais derivados
- Sistema de regras da persona
- Múltiplas personas
- Animações mais complexas
- Personalização do avatar

### Versão 3.0 (Evolução)
- Suporte a múltiplas câmeras
- Modo AR/VR
- Integração com voz
- Analytics emocional
- Modo aprendizado adaptativo

---

## 📝 Notas de Implementação

### Modelo de Emoções para MVP

**Opção 1: FER+ (Recomendado)**
- Leve (~5MB)
- Boa precisão para 3 emoções
- Fácil de integrar

**Opção 2: Modelo Custom Simples**
- Treinar modelo pequeno (MobileNet) em dataset reduzido
- Mais controle, mas requer treinamento

### Renderização para MVP

**Opção A: Canvas 2D (Mais Simples)**
- HTML5 Canvas
- Sprites estáticos
- Transições CSS

**Opção B: Three.js (Mais Flexível)**
- Permite evoluir para 3D depois
- Melhor para animações

**Recomendação**: Canvas 2D para MVP, migrar para Three.js depois se necessário.

---

## ✅ Checklist de Lançamento MVP

- [ ] Código funcional e testado
- [ ] Documentação básica (README)
- [ ] Instruções de instalação
- [ ] Build executável (opcional)
- [ ] Screenshots/demo video
- [ ] Lista de limitações conhecidas
- [ ] Feedback mechanism (GitHub Issues)

---

## 🎉 Resultado Esperado

Um aplicativo desktop funcional onde:
1. Usuário abre o app
2. Câmera detecta rosto
3. Avatar aparece na janela flutuante
4. Avatar reage quando usuário sorri/faz cara triste
5. Experiência básica mas funcional do conceito

**Isso valida a ideia e permite coletar feedback para próximas versões!**
