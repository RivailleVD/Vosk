#ativar o ambiente virtual com "ambienteVirt\Scripts\activate" no terminal

import pyaudio
from vosk import Model, KaldiRecognizer
import json


def ouvir():
    # Substitua pelo caminho do seu modelo acústico
    model = Model(r'E:\Projetos-de-IA-e-Automacao\vosk02\vosk-model-small-pt-0.3')
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("Iniciando o reconhecimento de voz...")

    try:
        while True:
            data = stream.read(4096)
            
            if recognizer.AcceptWaveform(data):
                result_json = recognizer.Result()
                result = json.loads(result_json)
                recognized_text = result.get("text", "")
                
                print(f"Você disse: {recognized_text}")

                # Verifica se o texto contém "paz do senhor"
                if "paz do senhor" in recognized_text:
                    print("Deus abençoe")

    except KeyboardInterrupt:
        print("Interrompido pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        mic.terminate()
        print("Stream encerrado.")


# Chama a função para iniciar o reconhecimento
ouvir()

