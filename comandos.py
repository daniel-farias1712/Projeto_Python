import subprocess
import os
import psutil
import time
import pyttsx3

CAMINHO_SPOTIFY = r"C:\Users\danie\AppData\Roaming\Spotify\Spotify.exe"

# Inicializa o motor de voz
voz = pyttsx3.init()
voz.setProperty('rate', 170)  # velocidade da fala

def falar(texto):
    print(f"[AION]: {texto}")
    voz.say(texto)
    voz.runAndWait()

def responder_comando(comando):
    comando = comando.strip().lower()

    if comando == "ok jarvis":
        falar("Olá, senhor.")
    elif comando == "abrir navegador":
        falar("Abrindo Microsoft Edge.")
        subprocess.Popen("start msedge", shell=True)
    elif comando == "fechar navegador":
        falar("Fechando navegador.")
        # Verifica todos os processos ativos e tenta encerrar o processo do Edge
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'].lower() == "msedge.exe" and proc.is_running():
                    proc.terminate()  # Encerra o processo do Edge
            except psutil.NoSuchProcess:
                pass  # Ignora se o processo não existir mais
    elif comando == "abrir música":
        try:
            falar("Abrindo Spotify.")
            subprocess.Popen(CAMINHO_SPOTIFY)
        except FileNotFoundError:
            falar("Spotify não encontrado.")
    elif comando == "fechar música":
        falar("Encerrando Spotify.")
        # Verifica todos os processos ativos e tenta encerrar o processo do Spotify
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'].lower() == "spotify.exe" and proc.is_running():
                    proc.terminate()  # Encerra o processo do Spotify
            except psutil.NoSuchProcess:
                pass  # Ignora se o processo não existir mais
    elif comando == "desligar computador":
        falar("Desligando o computador em 5 segundos.")
        time.sleep(5)
        os.system("shutdown /s /t 1")
