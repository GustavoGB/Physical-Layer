
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
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM3"                  # Windows(variacao de)
                                      # Windows(variacao de)
print("abriu com")

def main():

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
            tipo = (7).from_bytes(tipo,byteorder='big'
            #Recepção Syn1
            if tipo == 1 :
                ("***SYN1 ENCONTRADO***")
                ("___Enviando ACK1___")
                print(rxBuffer,tipo)
                data = (8).to_bytes(1,byteorder='big')
                tipo = (5).to_bytes(1,byteorder='big')
                #Enviar (data,tipo)
                print(data,tipo)
                com.sendData(data,tipo)
            else:
                print("FALHA..Tentando estabelecer conecção novamente")
                continue
             #Recepção Ack2
            rxBuffer,tipo = com.getData()
            tipo = (int.from_bytes(tipo,byteorder='big'))
            #Teste
            print(tipo)
            if tipo == 5:
                print("***ACK2 RECEBIDO***")
                print("Comunicação Estabelecida")
                break
            else:
                print("Enviando NACK, ocorreu um erro...")
                tipo = (9).to_bytes(1,byteorder='big')
                com.sendData(data,tipo)
                continue
        print("__________________________________________________")

        # Faz a recepção dos dados
        print("Recebendo pacote com payload... ")
        rxBuffer, tipo = com.getData()

        # Salva o dado recebido em arquivo
        print("__________________________________________________")
        print("Salvando dados no arquivo :")
        print("{}".format(dadoW))
        f = open(dadoW, 'wb')
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
         
                    



    

  