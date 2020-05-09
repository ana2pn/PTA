# -*- coding: cp1252 -*-
from socket import *

serverPort = 11550
#Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
#Socket fica ouvindo conexoes. O valor 1 indica que uma conexao pode ficar na fila
serverSocket.listen(1)

clientes = ['Ana', 'Pedro', 'Amaro', 'Rogerio','Caio']
comands = ['LIST', 'PEGA', 'TERM']
result = True
result2 = True
def verificaSentenca1(sentence_partida):
    if sentence_partida[1] == 'CUMP':
        if sentence_partida[2] in clientes:
            response = 'Ok'
            connectionSocket.send(response)
            result = True
        else:
            response = 'NOK'
            connectionSocket.send(response)
            result = False
    else:
        response = 'NOK'
        connectionSocket.send(response)
        result = False
    return result

def verificaSentenca2(sentence2):
    result2 = True
    if sentence2[1] not in comands:
        result2 = False
    return result2

def receberSentenca2():
    sentence2 = connectionSocket.recv(1024)
    sentence_partida2 = sentence2.split(" ")
    return sentence_partida2

def processamentoFinalSentenca2():
    if novaSentencaPartida2[1] == 'LIST':
        response = 'OK'
        connectionSocket.send(response)
        print("LIST")
    if novaSentencaPartida2[1] == "PEGA":
        pass
    if novaSentencaPartida2[1] == "TERM":
        pass

def processamentoInicialSentenca2():
    if verificaSentenca2(sentencaPartida2[1]) is True:
        if sentencaPartida2[1] == 'LIST':
            response = 'OK'
            connectionSocket.send(response)
            print("LIST")
        if sentencaPartida2[1] == "PEGA":
            pass
        if sentencaPartida2[1] == "TERM":
            pass

while 1:
   try:
        #Cria um socket para tratar a conexao do cliente
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024)
        sentence_partida = sentence.split(" ")
        if verificaSentenca1(sentence_partida):
            print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")
            sentencaPartida2 = receberSentenca2()
        else:
            break
        processamentoInicialSentenca2()
        if verificaSentenca2(sentencaPartida2) is not True:
            print("aqui1!")
            response = 'NOK'
            connectionSocket.send(response)
            novaSentencaPartida2 = receberSentenca2()
            while not verificaSentenca2(novaSentencaPartida2):
                print("aqui2!")
                response = 'NOK'
                connectionSocket.send(response)
                novaSentencaPartida2 = receberSentenca2()
                if verificaSentenca2(novaSentencaPartida2) is True:
                    print("aqui!3")
                    processamentoFinalSentenca2()
                    break
   except (KeyboardInterrupt, SystemExit):
        break
serverSocket.close()