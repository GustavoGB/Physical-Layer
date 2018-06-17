
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
        imageR = "./imgs/main-qimg-2d5b151a8b81bb7ad6a2d43be3268944.png"
         # Log
        print("__________________________________________________")
        print("Comunicação inicializada")
        print("  porta : {}".format(com.fisica.name))
        print("__________________________________________________")
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
        tipo = (1).to_bytes(1,byteorder = 'big')
        com.sendData(data,tipo) #Enviando Syn
        print("SYNC1...ENVIADO!!")

        #Recebendo Ack1
        print("Esperando Ack1.....")
        rxBuffer,tipo = com.getData()
        tipo = (int.from_bytes(tipo, byteorder='big'))
        print("Recebido Ack1")

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
            com.sendData(data,tipo)
            print("***ACK2 ENVIADO***")
            print("________________________________________")
            print("Conecção estabelecida")
        
            time.sleep(3) # Continuar varrendo
            break
        else:
            print("***ERRO***")
            print("***INICIANDO HS NOVAMENTE")
            continue
                
             

            
    # Carrega imagem
    print ("Carregando imagem para transmissão :")
    print (" - {}".format(imageR))
    txBuffer = open("./imgs/main-qimg-2d5b151a8b81bb7ad6a2d43be3268944.png", 'rb').read()
    print("-------------------------")
    txLen    = len(txBuffer)
    print(txLen)

    # Transmite imagem
    print("Transmitindo .... {} bytes".format(txLen))
    tipo = (7).to_bytes(1,byteorder='big')
    

    #Criar função que divide o payload
    def dividePayload(txLen,tipo,pacotesTotal,pacotesAtual):
        
    #Loop fim 
    while(com.tx.getIsBussy):
        pass
    
    #Atualiza data
    txSize = com.tx.getStatus()
    print("Transmitido {} bytes ".format(txSize))

    # Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")
    com.disable()

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()

            
            
        
  