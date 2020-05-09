# -*- coding: cp1252 -*-
from socket import *

#serverName = '127.0.0.1'
serverName = '127.0.0.1'
serverPort = 11550
clientSocket = socket(AF_INET, SOCK_STREAM)

#Conecta ao servidor
clientSocket.connect((serverName,serverPort))
message = raw_input('Digite a mensagem:')
clientSocket.send(message)
modifiedMessage, addr = clientSocket.recvfrom(2048)
print("Retorno do Servidor:" + modifiedMessage)

def digitarMensagem2():
    message2 = raw_input('Digite a mensagem:')
    return message2

if modifiedMessage == 'NOK':
    clientSocket.close()
else:
    while 1:
        try:
            #Recebe mensagem do usuario e envia ao servidor
            message2 = digitarMensagem2()
            clientSocket.send(message2)

            #Aguarda mensagem de retorno e a imprime
            modifiedMessagem, addr = clientSocket.recvfrom(2048)
            print("Retorno do Servidor:" + modifiedMessagem)

        except (KeyboardInterrupt, SystemExit):
            break

clientSocket.close()
