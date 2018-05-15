
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
serialName2 = "COM3"                  # Windows(variacao de)
print("abriu com")

def main():
    # Inicializa enlace ... variavel com possui todos os metodos e propriedades do enlace, que funciona em threading
    com = enlace(serialName)
    com2 = enlace(serialName2)

    # Ativa comunicacao
    com.enable()
    com2.enable()

    # Endereco da imagem a ser transmitida
    imageR = "./imgs/imageC.png"

    # Endereco da imagem a ser salva
    imageW = "./imgs/recebidaTeste.png"

while True:
    print("HandShake")
    print("Criando sinal Syn")
    syn = bytes([0,0,0,7])
    ack = bytes([0,0,2,8])
    nack = bytes([0,1,2,2])
    dados = bytes[5,5,5,5]
    com.sendData(data,syn) #Enviando Syn
    sleep(0.5)
    tipo = bytes[0,0,0,0]
    rxBuffer,tipo,tamanho == com2.getData()
    while tipo == bytes[0,0,0,0]: # Reconhecendo o Syn   
        rxBuffer,tipo,tamanho == com2.getData()
        if tipo == ack:  # Se o rxBuffer estiver com o Syn!
            print("Client recebeu o ack, esperando syn")           
        sleep(1)
    while tipo == bytes[0,0,0,0]: # Esperando Ackfinal   
        rxBuffer,tipo,tamanho == com2.getData()
        if tipo == syn:  # Se o rxBuffer estiver com o Syn!
            print("Client recebeu o syn, vou te mandar um ack")
            com.sendData(data,ack)
        sleep(1)
             # Enviando syn e ack para o client
            '''else:  # Caso em que houve problemas na comunicacao 
            prin("Houve um erro na comunicacao, reevie o syn novamente por favor")
            com.sendData(nack) # Envia Nack
            rxBuffer, nRx == com2.getData(nack)
             rxBuffer = nack'''
        '''com.sendData(syn) # com.sendData(ack)  # Reenvia os pacotes
        rxBuffer, nRx = com2.getData(syn) # and com2.getData(ack) # rxBuffer recebe o Ack
            if rxBuffer == syn : #  se o rxBuffer estiver com o Ack!
                print("O client recebeu o syn mande-me o ack")
                
                print("Transmitindo Ack para o server")
                com.sendData(ack)
            else: 
                print("Houve um problema na comunicacao, reevie os pacotes syn e ack")
                com.sendData(nack)
                if rxBuffer,nRx == com2.getData(nack):
                        com.sendData(ack) and com.sendData(nack)
            if rxBuffer, nRx == com2.getData(ack):
                print("Estamos prontos para inicializar a comunicacao")'''
                
            
              
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

        
            
        
  