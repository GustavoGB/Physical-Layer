
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
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)                                      # Windows(variacao de
serialName = "COM4" 
#Inicializa Enlace, ativa a comunicação e arquivo a ser recebifo
def main():
    com = enlace(serialName)
    com.enable()
    imageW = "./imgs/recebida/recebidaTeste.png"

    while (True):
        print("HandShake working with fragmentation")    
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

        print("***RECEBENDO.....***")
        rxBuffer,tipo = com.getData()
        print("Esperando Syn 1 para estabelecer contato......")
      
        #Recepção Syn1
        if tipo == 1 :
            ("***SYN1 ENCONTRADO***")
            ("___Enviando ACK1___")
            data = (8).to_bytes(1,byteorder='big')
            tipo = (4).to_bytes(1,byteorder='big')
            #Enviar Ack1!!
            com.sendData(data,tipo,pacotesAtual,pacotesTotal)
            print("...........Ack1 enviado")
            time.sleep(2.0)
            #Enviando Syn2!!!
            data = (8).to_bytes(1,byteorder='big')
            tipo = (3).to_bytes(1,byteorder='big')
            com.sendData(data,tipo,pacotesAtual,pacotesTotal)
            print("...enviando Syn2...")
        else:
            print("***ERRO***")
            print("***INICIANDO HS NOVAMENTE")
            continue
            #Recepção Ack2
        print("***Esperando ACK2***")

        rxBuffer, tipo = com.getData()

        if tipo == 5:
            print("***ACK2 RECEBIDO***")
            print("Comunicação Estabelecida")
            break
        else :
            print("***ERRO***")
            print("***INICIANDO HS NOVAMENTE")
            continue
    print("__________________________________________________")

    # Faz a recepção dos dados
    print("Recebendo pacote com payload... ")
    rxBuffer, tipo = com.getData()
    

    # Salva o dado recebido em arquivo
    print("__________________________________________________")
    print("Salvando dados no arquivo :")
    print("{}".format(imageW))
    f = open(imageW, 'wb')
    f.write(rxBuffer)

    # Fecha arquivo de imagem
    f.close()

    # Encerra comunicação
    print("__________________________________________________")
    print("Comunicação encerrada")
    print("__________________________________________________")
    com.disable()


if __name__ == "__main__":
    main()
         
                    



    

  