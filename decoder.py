import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

from utils.constants import *
from utils.utils import calcFFT, LPF


def main():
    # Carrega áudio modulado
    audio, _ = sf.read('audios/modulated.wav')
    print("Reproduzindo áudio modulado...")
    sd.play(audio)
    sd.wait()

    # Transformada de Fourier do sinal modulado
    x_fourier, y_fourier = calcFFT(signal=audio, fs=SAMPLE_FREQ)

    # Verificando sinal
    plt.plot(x_fourier, np.abs(y_fourier))
    plt.xlabel("Domínio da frequência")
    plt.ylabel("Intensidade")
    plt.title("Verificando áudio modulado pela Transformada de Fourier")
    plt.grid()
    plt.show()

    # Duração do áudio
    duration = len(audio) / SAMPLE_FREQ
    
    # x e y da portadora
    time_array = np.linspace(start=0, stop=duration, num=len(audio)) # x_carrier
    y_carrier  = AMPLITUDE * np.sin(2 * np.pi * CARRIER * time_array)

    # Demodulação
    demodulated = audio * y_carrier.transpose()

    # Fourier do áudio demodulado
    x_fourier_demodulated, y_fourier_demodulated = calcFFT(signal=demodulated, fs=SAMPLE_FREQ)

    plt.plot(x_fourier_demodulated, np.abs(y_fourier_demodulated))
    plt.xlabel("Domínio da frequência")
    plt.ylabel("Intensidade")
    plt.title("Gráfico 6: sinal de áudio demodulado – domínio da frequência")
    plt.xlim(left=5)
    plt.grid()
    plt.show()

    # Filtrando altas frequências
    filtered = LPF(signal=demodulated, cutoff_hz=CUTOFF, fs=SAMPLE_FREQ)

    print("Tocando som demodulado e filtrado...")
    sd.play(filtered)
    sd.wait()

    # Fourier de novo
    x_fourier_filtered, y_fourier_filtered = calcFFT(signal=filtered, fs=SAMPLE_FREQ)
    plt.plot(x_fourier_filtered, np.abs(y_fourier_filtered))
    plt.xlabel("Domínio da frequência")
    plt.ylabel("Intensidade")
    plt.title("Gráfico 7: sinal de áudio demodulado e filtrado\n domínio da frequência")
    plt.xlim(left=10)
    plt.ylim(top=1000, bottom=0)
    plt.grid()
    plt.show()

    # Fourier de novo (zoom)
    x_fourier_filtered, y_fourier_filtered = calcFFT(signal=filtered, fs=SAMPLE_FREQ)
    plt.plot(x_fourier_filtered, np.abs(y_fourier_filtered))
    plt.xlabel("Domínio da frequência")
    plt.ylabel("Intensidade")
    plt.title("Gráfico 7: sinal de áudio demodulado e filtrado\n domínio da frequência (com zoom)")
    plt.xlim(left=10)
    plt.ylim(top=400, bottom=0)
    plt.grid()
    plt.show()

    # salva áudio demodulado
    sf.write(file='audios/demodulated.wav', data=demodulated, samplerate=SAMPLE_FREQ)


if __name__ == "__main__":
    main()
