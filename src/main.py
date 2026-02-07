#!/usr/bin/env python3
"""
Entry point principal do AI Face Emotion Persona Overlay
"""

import asyncio
import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from loguru import logger
import yaml

# TODO: Implementar módulos quando criados
# from src.capture import CameraCapture
# from src.detection import FaceDetector
# from src.emotion import EmotionClassifier
# from src.persona import PersonaEngine
# from src.communication import WebSocketServer


def load_config(config_path: str = "config/default.yaml") -> dict:
    """Carrega configuração do arquivo YAML"""
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


async def main():
    """Função principal assíncrona"""
    logger.info("Iniciando AI Face Emotion Persona Overlay")
    
    # Carregar configuração
    try:
        config = load_config()
        logger.info(f"Configuração carregada de {config_path}")
    except Exception as e:
        logger.error(f"Erro ao carregar configuração: {e}")
        return
    
    # TODO: Inicializar módulos
    # camera = CameraCapture(config["capture"])
    # face_detector = FaceDetector(config["detection"])
    # emotion_classifier = EmotionClassifier(config["emotion"])
    # persona_engine = PersonaEngine(config["persona"])
    # websocket_server = WebSocketServer(config["communication"])
    
    logger.info("Sistema inicializado. Aguardando implementação dos módulos...")
    
    # Loop principal (placeholder)
    try:
        while True:
            await asyncio.sleep(1)
            # TODO: Implementar loop de processamento
    except KeyboardInterrupt:
        logger.info("Encerrando aplicação...")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Aplicação encerrada pelo usuário")
    except Exception as e:
        logger.exception(f"Erro fatal: {e}")
        sys.exit(1)
