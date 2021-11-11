# Modulação AM

## Sobre o projeto

O objetivo é transmitir um áudio que ocupe bandas de baixas frequências (entre 20 Hz e 4kHz) através de um canal de transmissão em que se possa utilizar apenas as bandas entre 10kHz e 18KHz. Após a transmissão via sinal acústico, o receptor, que gravou o sinal transmitido, deverá demodular o sinal e reproduzi-lo, de maneira audível novamente.

As dependências necessárias encontram-se no arquivo `requirements.txt`. Crie um ambiente virtual, ative-o e dentro dele, faça:

```
pip install -r requirements.txt
```

Após isso, basta executar os arquivos `encoder.py` inicialmente e `decoder.py` depois.