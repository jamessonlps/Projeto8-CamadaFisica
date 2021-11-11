from scipy import signal as window
from scipy.fftpack import fft
import numpy as np

def calcFFT(signal, fs):
  # https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
  N  = len(signal)
  W = window.hamming(N)
  T  = 1/fs
  xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
  yf = fft(signal*W)
  return(xf, np.abs(yf[0:N//2]))

def LPF(signal, cutoff_hz, fs):
  #####################
  # Filtro
  #####################
  # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
  nyq_rate = fs/2
  width = 5.0/nyq_rate
  ripple_db = 60.0 #dB
  N , beta = window.kaiserord(ripple_db, width)
  taps = window.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
  
  return(window.lfilter(taps, 1.0, signal))