#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
# Prof. Rafael Corsi
#  Abril/2017
#  Aplicação
####################################################

from enlace import *
import time
import packing
# Serial Com Port
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
import enlace 
serialName = "COM3"                   # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
#serialName = "COM3"                  # Windows(variacao de)

def main():
    # Inicializa enlace
    com = enlace(serialName)

    # Ativa comunicacao
    com.enable()

    # Endereco da imagem a ser salva
    imageW = "./imgs/recebida.png"

    # Log
    print("-------------------------")
    print("Comunicação inicializada")
    print("  porta : {}".format(com.fisica.name))
    print("-------------------------")


    while true:
        
        rxBuffer = 0
        
        
        if (rxBuffer == "d726760b0467b77803d6d1f3585deb6e"):
            #Confirmação do estabelecimento da conecção
            packetSyn2 = self.End.SynBuild()   
            print("Construindo Syn2{}".format(packetSyn2))
            com.sendData(packetSyn)
            
        
        
        







    # Faz a recepção dos dados
    print ("Recebendo dados .... ")
    rxBuffer, nRx = com.getData()
    start = time.time()

    # log
    end = time.time()

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
    tempo = end - start
    print('Tempo de transmissão:', "{0:.2f}".format(tempo), 'seg')


    com.disable()

if __name__ == "__main__":
    main()