import sys
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

from utils.utils import calcFFT, LPF
from utils.constants import *


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


def main():
    print("Inicializando encoder...")
    
    audio, frequency_sample = sf.read('audios/audio.wav')
    y_max = np.max(abs(audio))
    
    # Toca áudio gravado
    sd.play(audio)
    sd.wait()

    # Normalização
    audio = audio / y_max

    # plota gráfico 1 - áudio original normalizado
    plt.plot(audio)
    plt.xlabel("Sample")
    plt.ylabel("Intensidade")
    plt.title("Gráfico 1: Sinal de áudio original normalizado – domínio do tempo")
    plt.grid()
    plt.show()

    # Filtro
    filter_audio = LPF(signal=audio, cutoff_hz=CUTOFF, fs=SAMPLE_FREQ)

    # plota gráfico 2 - áudio filtrado
    plt.plot(filter_audio)
    plt.xlabel("Sample")
    plt.ylabel("Intensidade")
    plt.title("Gráfico 2: Sinal de áudio filtrado – domínio do tempo.")
    plt.grid()
    plt.show()

    # Domínio do tempo - Fourier
    x_fourier, y_fourier = calcFFT(signal=filter_audio, fs=SAMPLE_FREQ)

    # Plota gráfico 3 - áudio filtrado no domínio da frequência
    plt.plot(x_fourier, np.abs(y_fourier))
    plt.xlabel("Domínio da frequência")
    plt.ylabel("Intensidade")
    plt.title("Gráfico 3: Sinal de áudio filtrado – domínio da frequência")
    plt.grid()
    plt.show()

    print("Reproduzindo som novamente...")
    sd.play(filter_audio)
    sd.wait()

    # Sinal da portadora
    duration = len(filter_audio) / SAMPLE_FREQ
    
    time_array = np.linspace(start=0, stop=duration, num=len(filter_audio)) # x_carrier
    y_carrier  = AMPLITUDE * np.sin(2 * np.pi * CARRIER * time_array)

    # Modula o sinal de envio
    modulated = ([0.25]*len(y_carrier) + np.array(filter_audio)) * np.array(y_carrier).transpose()
    
    # Plota gráfico 4 - sinal modulado
    plt.plot(modulated)
    plt.xlabel("Domínio do tempo")
    plt.ylabel("Intensidade")
    plt.title("Gráfico 4: sinal de áudio modulado – domínio do tempo")
    plt.grid()
    plt.show()

    # Domínio do tempo - Fourier para o sinal modulado
    x_modulated_fourier, y_modulated_fourier = calcFFT(signal=modulated, fs=SAMPLE_FREQ)

    plt.plot(x_modulated_fourier, np.abs(y_modulated_fourier))
    plt.xlabel("Domínio da frequência")
    plt.ylabel("Intensidade")
    plt.title("Gráfico 5: sinal de áudio modulado – domínio da frequência")
    plt.grid()
    plt.show()

    print("Tocando áudio modulado...")
    sd.play(modulated)
    sd.wait()

    # Salvando arquivo de som modulado
    sf.write('audios/modulated.wav', data=modulated, samplerate=SAMPLE_FREQ)

if __name__ == "__main__":
    main()
