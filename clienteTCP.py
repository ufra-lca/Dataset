# -*- coding: utf-8 -*-
import socket
import threading
from random import randint

#dados do servidor
servidores = ['IP Rasp']
porta = 5000
tamanhoDaString = 20

servicos = []
for s in servidores:
    servicos.append((s, porta))

def enviaSolicitacao(servico,requisicao):
    #criando o socket
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_.connect(servico)
    print('conectado com {} na porta {}'.format(*servico))
    
    try:
        requisicaoEnc = str.encode(requisicao)
    
        # Enviando a solicitação
        socket_.sendall(requisicaoEnc)
        print('Enviado: ', requisicao)
    
        # Recebendo a resposta
        recebido = 0
        esperado = len(requisicao)
        esperado = 3
    
        #while recebido < esperado:
        resposta = socket_.recv(tamanhoDaString)
        recebido += len(resposta)
        print('Resposta: ', resposta.decode('utf-8'))
    
    finally:
        # Encerrando a conexão
        socket_.close()
        print('Encerrando a conexao')
       
palavra =['SALADA',
          'MACARRÃO',
          'FAROFA',
          'FEIJÃO',
          'ARROZ'] 

p = palavra[randint(0,len(palavra)-1)]

for s in servicos:
    thread = threading.Thread(target= enviaSolicitacao, args=(s,p))
    thread.start()
