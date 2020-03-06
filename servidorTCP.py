# -*- coding: utf-8 -*-
import socket
import sys
import picamera
import time
from datetime import datetime

host = ''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
host = s.getsockname()[0]
s.close()

porta = 5000
tamanhoDaString = 20
servidor = (host, porta)
dado="ok!"

def capturaImagem():
    global dado
    dado = str(dado.decode('utf-8'))
    print('Mensagem recebida:', dado)
    dado = dado.upper()
    
    tempo = datetime.now()
    tempo = tempo.strftime("%Y-%m-%d %H-%M-%S")
    nomeArquivo = dado + " " + tempo + ".jpg"

    camera = picamera.PiCamera(
    resolution=(800,600))
    camera.iso = 1000
    camera.start_preview()
    camera.capture(nomeArquivo)
    camera.stop_preview()
    camera.close()

    print('Imagem Capturada')
    


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('servidor {} iniciado na porta {}'.format(*servidor))
tcp.bind(servidor)

while(True):
    tcp.listen(1)
    print('Aguardando o cliente')
    conexao, cliente = tcp.accept()
    
    try:
        print('Conectado com', cliente[0])

        dado = conexao.recv(tamanhoDaString)
        capturaImagem()
        dado = str.encode(dado)
    
        print('Enviando resposta ao cliente... ')
        if dado:
            conexao.sendall(dado)
        else:
            print('Fim da resposta', cliente)
            break
    
    finally:
        conexao.close()
        del conexao
        print('Finalizado')
