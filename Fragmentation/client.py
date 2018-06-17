
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
        #pacotesAtual = 1 (1byte = 1, 00000001)
        #pacotesTotal = 1 (1byte = 1, 00000001)
        pacotesAtual =(1).to_bytes(1,byteorder='big')
        pacotesTotal =(1).to_bytes(1,byteorder='big')

        print("HandShake working with fragmentation ") 
        #Enviando Syn1
        print("Criando sinal Syn1")
        data = (8).to_bytes(1,byteorder = 'big')
        tipo = (1).to_bytes(1,byteorder = 'big')
        com.sendData(data,tipo,pacotesAtual,pacotesTotal) #Enviando Syn
        print("SYNC1...ENVIADO!!")

        #Recebendo Ack1
        print("Esperando Ack1.....")
        rxBuffer,tipo = com.getData()
        print("Recebido Ack1")

        #Recebendo Syn2
        print("Esperando Syn2....") 
        rxBuffer, tipo = com.getData()
        if tipo == 3:
            print("***SYN2 RECEBIDO***...")
            print("***ACK2 SENDO ENVIADO PARA ESTABELECER CONECÇÃO")
            #Criando ACK2
            data = (8).to_bytes(1,byteorder='big')
            tipo = (5).to_bytes(1,byteorder='big')
            com.sendData(data,tipo,pacotesAtual,pacotesTotal)
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
    foto = open("./imgs/main-qimg-2d5b151a8b81bb7ad6a2d43be3268944.png", 'rb').read()
    print("-------------------------")
    txSize    = len(foto) #Foto = txBuffer
    print(txSize)

    # Transmite imagem
    print("Transmitindo .... {} bytes".format(txSize))
    tipo = (7).to_bytes(1,byteorder='big')

    #Criar função que divide o payload
    if txSize > 1000:
        divisaoPacotes = (txSize//1000) + 1 #Quantos pacotes com o maximo de 1000bytes
        pacotesAtual   = (divisaoPacotes).to_bytes(1,byteorder='big')
        print("O pacote será divido em {}".format(divisaoPacotes)) 
        # Concatenar e percorrer o indice para dizer qual é o pacoteAtual
        indice         =  0
        pacoteCompleto =  b""
        while indice < divisaoPacotes:
            txBuffer        = foto[indice*1000 : (indice*1000 + 1000)]
            pacotesAtual    = (indice).to_bytes(1,byteorder='big')
            pacoteCompleto += com.constructPack(txBuffer,tipo,pacotesAtual,pacotesTotal)  
            indice          = indice + 1 
        com.sendBufferAfterFragmentation(pacoteCompleto,tipo,pacotesAtual,pacotesTotal)
    else:
        divisaoPacotes     =   1
        pacotesTotal       = (divisaoPacotes).to_bytes(1,byteorder='big')
        print("A divisão de pacotes não ocorreu")
        com.sendData(foto,tipo,pacotesAtual,pacotesTotal)

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

            
            
        
  