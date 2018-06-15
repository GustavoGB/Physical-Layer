
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
#Inicializa Enlace, ativa a comunicação e arquivo a ser recebifo
def main():
    serialName = "COM4"                  # Windows(variacao de)
    com = enlace(serialName)
    com.enable()
    imageW = "./imgs/recebidaTeste.png"
    while (True):
        print("HandShake")    

        #Tipos:
        # Syn 1  = 1
        # Syn 2  = 3
        # Ack 1  = 4 
        # Ack 2  = 5 
        # Dados  = 7 
        # Bugs(Nack)   = 9 

        print("***RECEBENDO.....***")

        rxBuffer,tipo = com.getData()
        tipo = int.from_bytes(tipo,byteorder='big')
        print("Esperando Syn 1 para estabelecer contato......")
        
        #Recepção Syn1
        if tipo == 1 :
            ("***SYN1 ENCONTRADO***")
            ("___Enviando ACK1___")
            print(rxBuffer,tipo)
            data = (8).to_bytes(1,byteorder='big')
            tipo = (4).to_bytes(1,byteorder='big')
            #Enviar Ack1!!
            print(data,tipo)
            com.sendData(data,tipo)
            print("...........Ack1 enviado")
            time.sleep(2.5)

            #Enviando Syn2!!!
            data(8).to_bytes(1,byteorder='big')
            tipo(3).to_bytes(1,byteorder='big')
            com.sendData(data,tipo)
            print("...enviando Syn2...")
        if tipo ==9 :
            print("FALHA..Tentando estabelecer conecção novamente")
            data = (8).to_bytes(1,byteorder='big')
            tipo = (9).to_bytes(1,byteorder='big')
            #Enviando Nack
            com.sendData(data,tipo)
            print("Nack enviado...Esperando receber Syn1 novamente...")
            time.sleep(2)
        else:
            print("***ERRO***")
            print("***INICIANDO HS NOVAMENTE")
            rxBuffer,tipo = com.getData()
            tipo = int.from_bytes(tipo,byteorder='big')
            print("Esperando Syn 1 para estabelecer contato......")
            

            #Recepção Ack2

        rxBuffer,tipo = com.getData()
        tipo = (int.from_bytes(tipo,byteorder='big'))

        if tipo == 5:
            print("***ACK2 RECEBIDO***")
            print("Comunicação Estabelecida")
            break
        if tipo ==9:
            print("Enviando NACK, ocorreu um erro...")
            data = (8).to_bytes(1,byteorder='big')
            tipo = (9).to_bytes(1,byteorder='big')
            com.sendData(data,tipo)
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
         
                    



    

  