
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

#erialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
#serialName = "COM3"                  # Windows(variacao de)

print("abriu com")

def main():
   
    while True:
        com = enlace(serialName)
        com.enable()
        imageR = "./imgs/imageC.png"
        imageW = "./imgs/recebidaTeste.png"
        txBuffer = open(imageR, 'rb').read()
        data = txBuffer

        print("HandShake")
        print("Criando sinal Syn")
        syn = bytes([0,0,0,7])
        ack = bytes([0,0,2,8])
        nack = bytes([0,1,2,2])
        dados = bytes([5,5,5,5])
        com.sendData(data,syn) #Enviando Syn
        time.sleep(0.5)
        tipo = 0 
        rxBuffer,tipo,tamanho = com.getData() 
        while tipo == 0: # Reconhecendo o Syn   
            rxBuffer,tipo,tamanho = com.getData()
        if tipo == ack:  # Se o tipo for ack
            print("Client recebeu o ack, esperando syn")           
            time.sleep(1)
            #else:
            #    com.sendData(data,nack) # envia um nack
            #sleep(1)
            if tipo == nack:
                print("Reenviando pacote ack...")
                com.sendData(dados,ack)
            time.sleep(1) # Reenvia o sinal ack
        while tipo == 0: # Esperando Ack final   
            rxBuffer,tipo,tamanho == com.getData()
            if tipo == syn:  # Se o rxBuffer estiver com o Syn!
                print("Client recebeu o syn, vou te mandar um ack")
                com.sendData(dados,ack)
            else:
                com.sendData(dados,nack)
                if tipo == nack:
                    com.sendData(dados,syn)
            time.sleep(1)

                
        # Log
        print("-------------------------")
        print("Comunicação inicializada")
        print("  porta : {}".format(com.fisica.name))
        print("-------------------------")

            
        # Carrega imagem
        print ("Carregando imagem para transmissão :")
        print (" - {}".format(imageR))
        print("-------------------------")
        txLen    = len(txBuffer)
        print(txLen)

        # Transmite imagem
        print("Transmitindo .... {} bytes".format(txLen))
        com.sendData(data,dados)

        # Atualiza dados da transmissão ... na verdade nao funciona fora do thread ..
        txSize = com.tx.getStatus()
        print ("Transmitido       {} bytes ".format(txSize))

        # Faz a recepção dos dados
        print ("Recebendo dados .... ")
        #bytesSeremLidos=com2.rx.getBufferLen()
        #print("tamanho do buffer a ser lido {}".format(bytesSeremLidos))
            
        rxBuffer,tipo,tamanho = com.getData()

        # log
        print ("Lido              {} bytes ".format(tamanho))

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

        #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()

            
            
        
  