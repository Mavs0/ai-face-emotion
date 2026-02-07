/**
 * Processo principal do Electron
 * Gerencia a janela e comunicação com backend Python
 */

const { app, BrowserWindow } = require('electron');
const path = require('path');
const WebSocket = require('ws');

let mainWindow;
let wsClient;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 300,
    height: 300,
    alwaysOnTop: true,
    frame: false,
    transparent: true,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  mainWindow.loadFile(path.join(__dirname, 'index.html'));

  // Conectar ao WebSocket do backend Python
  connectToBackend();

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

function connectToBackend() {
  wsClient = new WebSocket('ws://localhost:8765');

  wsClient.on('open', () => {
    console.log('Conectado ao backend Python');
  });

  wsClient.on('message', (data) => {
    try {
      const message = JSON.parse(data);
      // Enviar mensagem para o renderer process
      if (mainWindow && mainWindow.webContents) {
        mainWindow.webContents.send('persona-update', message);
      }
    } catch (error) {
      console.error('Erro ao processar mensagem:', error);
    }
  });

  wsClient.on('error', (error) => {
    console.error('Erro WebSocket:', error);
  });

  wsClient.on('close', () => {
    console.log('Conexão WebSocket fechada. Tentando reconectar...');
    setTimeout(connectToBackend, 3000);
  });
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('before-quit', () => {
  if (wsClient) {
    wsClient.close();
  }
});
