import asyncio
import edge_tts
import os

async def gerar_arquivos_audio():
    # Nome da voz que você quer usar
    voz_selecionada = "pt-BR-ThalitaMultilingualNeural"
    
    # Criar pasta para salvar o áudio
    pasta_destino = "vozes_ptbr"
    os.makedirs(pasta_destino, exist_ok=True)

    print(f"🔊 Gerando áudio com a voz: {voz_selecionada}")

    # Texto para gerar o áudio
    texto = f"Olá, Daniel. Eu sou a voz {voz_selecionada}."

    # Gerar áudio com a voz selecionada
    communicate = edge_tts.Communicate(texto, voice=voz_selecionada)

    # Nome do arquivo de áudio
    caminho_arquivo = os.path.join(pasta_destino, f"{voz_selecionada}.mp3")

    # Salvar o áudio em arquivo
    await communicate.save(caminho_arquivo)
    print(f"Áudio salvo como: {caminho_arquivo}")

    await asyncio.sleep(5)  # Espera para evitar sobrecarga

# Corrigir o erro de 'Event loop is closed' garantindo que o loop seja controlado corretamente
def main():
    try:
        asyncio.run(gerar_arquivos_audio())
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executa o script de geração de áudios
if __name__ == "__main__":
    main()
