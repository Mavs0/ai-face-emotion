# AI Face Emotion Persona Overlay

Sistema desktop de reconhecimento emocional em tempo real que controla um avatar/persona visual baseado nas emoções detectadas do usuário através da câmera.

## 🎯 Visão Geral

O **AI Face Emotion Persona Overlay** é uma aplicação desktop que:

- Captura vídeo em tempo real da câmera do usuário
- Detecta e analisa expressões faciais, emoções e microexpressões
- Mantém um estado emocional contínuo do usuário
- Controla uma persona (avatar visual) que reage às emoções detectadas
- Renderiza o avatar como overlay na tela ou em janela flutuante

## 🏗️ Arquitetura

O sistema é composto por 4 camadas principais:

1. **Camada de Captura** - Aquisição de vídeo e detecção facial
2. **Camada de Análise** - Processamento de emoções e estados derivados
3. **Camada de Persona** - Engine de comportamento do avatar
4. **Camada de Renderização** - Visualização do avatar

Veja a [Documentação de Arquitetura](./docs/ARCHITECTURE.md) para detalhes completos.

## 📋 Requisitos Funcionais

### Emoções Primárias Detectadas

- 😊 Happy (Feliz)
- 😢 Sad (Triste)
- 😠 Angry (Raiva)
- 😨 Fear (Medo)
- 😲 Surprise (Surpresa)
- 🤢 Disgust (Nojo)
- 😐 Neutral (Neutro)

### Estados Emocionais Derivados

- 😰 Stressed (Estressado)
- 😴 Tired (Cansado)
- 🎯 Engaged (Engajado)
- 😑 Bored (Entediado)
- 💪 Confident (Confiante)

### Funcionalidades Core

- ✅ Captura de câmera em tempo real (30fps)
- ✅ Detecção de rosto e landmarks faciais
- ✅ Classificação de emoções primárias
- ✅ Cálculo de estados emocionais derivados
- ✅ Histórico emocional (timeline)
- ✅ Engine de persona com regras comportamentais
- ✅ Renderização de avatar reativo
- ✅ Processamento local (privacidade)

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.9+
- Node.js 18+ (para renderização Electron, se aplicável)
- Câmera webcam funcional

### Instalação

```bash
# Clone o repositório
git clone https://github.com/Mavs0/ai-face-emotion.git
cd ai-face-emotion

# Instale dependências Python
pip install -r requirements.txt

# Instale dependências do renderer (se usando Electron)
cd renderer && npm install
```

### Execução

```bash
# Inicie o sistema completo
python src/main.py
```

## 🎮 MVP (Minimum Viable Product)

O MVP inicial inclui:

- Captura básica de vídeo
- Detecção de 3 emoções principais (happy, sad, neutral)
- Avatar simples com 3 estados visuais
- Janela flutuante para exibição

Veja [MVP.md](./docs/MVP.md) para detalhes completos.

## 📚 Documentação Completa

### Documentação Técnica
- [📋 Resumo Executivo](./docs/EXECUTIVE_SUMMARY.md) - Visão geral do projeto
- [🏛️ Arquitetura do Sistema](./docs/ARCHITECTURE.md) - Arquitetura detalhada em camadas
- [📦 Módulos e Componentes](./docs/MODULES.md) - Descrição completa de cada módulo
- [🔄 Fluxo de Dados](./docs/DATA_FLOW.md) - Pipeline de processamento e estruturas de dados
- [🛠️ Stack Tecnológico](./docs/TECH_STACK.md) - Tecnologias, dependências e requisitos
- [📊 Diagramas Visuais](./docs/DIAGRAMS.md) - Diagramas ASCII da arquitetura

### Planejamento
- [🚀 Plano MVP](./docs/MVP.md) - Especificação do Minimum Viable Product
- [🛣️ Roadmap](./docs/ROADMAP.md) - Evolução futura do produto
