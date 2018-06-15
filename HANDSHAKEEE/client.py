
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
#Carareto
#17/02/2018
#  Aplicação
####################################################

from enlace import *
import time


# Serial Com Port
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports

#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1451" # Mac    (variacao de)
serialName = "COM3"                  # Windows(variacao de)

def main():
   
    while True:
        com = enlace(serialName)
        com.enable()
        imageR = "./imgs/imageC.png"

        #Tipos:
        # Syn 1  = 1
        # Syn 2  = 3
        # Ack 1  = 4 
        # Ack 2  = 5 
        # Dados  = 7 
        # Bugs   = 9 
        #
        print("HandShake")
        
        #Enviando Syn1
        print("Criando sinal Syn1")
        data = (8).to_bytes(1,byteorder = 'big')
        tipo = (1).to_bytes(1,byteorder='big')
        com.sendData(data,tipo) #Enviando Syn
        print("SYNC1...ENVIADO!!")

        rxBuffer,tipo = com.getData()
        tipo = (int.from_bytes(tipo,byteorder='big'))
        if tipo == 9:
            print("Client recebeu o Nack, reenviando Syn1")
            data = (8).to_bytes(1,byteorder = 'big')
            tipo = (1).to_bytes(1,byteorder='big')
            com.sendData(data,tipo)
        #Recebendo Ack1
        print("Esperando Ack1.....")
        rxBuffer,tipo = com.getData()
        tipo = (int.from_bytes(tipo, byteorder='big'))

        if tipo == 4:
            print("ACK1...RECEBIDO COM SUCESSO")    
            time.sleep(2)
        if tipo == 9:
            print("Recebi o Nack, reevinado o Syn1...")   
            data = (8).to_bytes(1,byteorder = 'big')
            tipo = (1).to_bytes(1,byteorder='big')
            com.sendData(data,tipo) #Enviando Syn
            time.sleep(2)
        else :
            print("***ERRO***")
            print("***INICIANDO HS NOVAMENTE")
            continue
        #Recebendo Syn2
        print("Esperando Syn2....") 
        rxBuffer, tipo = com.getData()
        tipo = (int.from_bytes(tipo, byteorder='big'))
        if tipo == 3:
            print("***SYN2 RECEBIDO***...")
            print("***ACK2 SENDO ENVIADO PARA ESTABELECER CONECÇÃO")
            #Criando ACK2
            data = (8).to_bytes(1,byteorder='big')
            tipo = (5).to_bytes(1,byteorder='big')
            print("***ACK2 ENVIADO***")
            print("________________________________________")
            print("Conecção estabelecida")
        
            time.sleep(3) # Continuar varrendo
            break
        if tipo == 9 :
            print("Recebi o Nack, vou reenviar o Ack2...")
            data = (8).to_bytes(1,byteorder='big')
            tipo = (4).to_bytes(1,byteorder='big')
            com.sendData(data,tipo)
        else:
            print("***ERRO***")
            print("***INICIANDO HS NOVAMENTE")
            continue
                
             

            
    # Carrega imagem
    print ("Carregando imagem para transmissão :")
    print (" - {}".format(imageR))
    txBuffer = open(imageW, 'rb').read()
    print("-------------------------")
    txLen    = len(txBuffer)
    print(txLen)

    # Transmite imagem
    print("Transmitindo .... {} bytes".format(txLen))
    tipo = (7).to_bytes(1,byteorder='big')
    com.sendData(txBuffer,tipo)


    #Loop fim 
    while(com.tx.getIsBussy):
        pass

    # Faz a recepção dos dados
    print ("Recebendo dados .... ")
    
    # Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")
    com.disable()

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()

            
            
        
  