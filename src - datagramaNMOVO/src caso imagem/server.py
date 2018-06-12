
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
#Carareto
#17/02/2018
#  Aplicação
####################################################

print("comecou")

from enlace import *
import time


# Serial Com Port
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports

#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM1"                  # Windows(variacao de)
                                      # Windows(variacao de)
print("abriu com")

def main():
    # Inicializa enlace ... variavel com possui todos os metodos e propriedades do enlace, que funciona em threading
    com = enlace(serialName)
    

    # Ativa comunicacao
    com.enable()
    

    # Endereco da imagem a ser transmitida
    imageR = "./imgs/imageC.png"

    # Endereco da imagem a ser salva
    imageW = "./imgs/recebidaTeste.png"

while True:
    print("HandShake")    
    syn   = bytes([0,0,0,7])
    ack   = bytes([0,0,2,8])
    nack  = bytes([0,1,2,2])
    dados = bytes([5,5,5,5])
    tipo  = bytes([0,0,0,0])

    while tipo == bytes[0,0,0,0]: # Reconhecendo o Syn   
        rxBuffer,tipo,tamanho == com.getData()
        if tipo == syn:  # Se o rxBuffer estiver com o Syn!
            print("Server recebeu o syn, enviado ack")           
        sleep(1)
            com.sendData(data,ack)
            print("Server enviando o Syn")
        sleep(1)
            com.sendData(data,syn)
            print("Server enviou o syn, esperando ack final")    
    while tipo == bytes[0,0,0,0]: # Esperando Ackfinal   
        rxBuffer,tipo,tamanho == com.getData()
        if tipo == ack:  # Se o rxBuffer estiver com o Syn!
            print("Server recebeu o ack, pronto para iniciar comunicação")

               
    # Log
    print("-------------------------")
    print("Comunicação inicializada")
    print("  porta : {}".format(com.fisica.name))
    print("-------------------------")

    # Carrega imagem
    print ("Carregando imagem para transmissão :")
    print (" - {}".format(imageR))
    print("-------------------------")
    txBuffer = open(imageR, 'rb').read()
    txLen    = len(txBuffer) 
    print(txLen)

    # Transmite imagem
    print("Transmitindo .... {} bytes".format(txLen))
    com.sendData(txBuffer)

    
    # Atualiza dados da transmissão ... na verdade nao funciona fora do thread ..
    txSize = com.tx.getStatus()
    print ("Transmitido       {} bytes ".format(txSize))

    # Faz a recepção dos dados
    print ("Recebendo dados .... ")
    #bytesSeremLidos=com2.rx.getBufferLen()
    #print("tamanho do buffer a ser lido {}".format(bytesSeremLidos))
        
    rxBuffer, nRx = com2.getData(txLen)

    # log
    print ("Lido              {} bytes ".format(nRx))

    # Salva imagem recebida em arquivo
    print("-------------------------")
    print ("Salvando dados no arquivo :")
    print (" - {}".format(imageW))
    f = open(imageW, 'wb')
    f.write(rxBuffer)

    # Fecha arquivo de imagem
    f.close()

    # Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")
    com.disable()
    com2.disable()

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()


    

  