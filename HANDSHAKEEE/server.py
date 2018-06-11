 
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
serialName = "COM1"                  # Windows(variacao de)
                                      # Windows(variacao de)
print("abriu com")

def main():
    
    server = True

    while server == True:
        
        com = enlace(serialName)
        com.enable()
        imageR = "./imgs/imageC.png"
        imageW = "./imgs/recebidaTeste.png"
        txBuffer = open(imageR, 'rb').read()

        print("HandShake")    
        syn   = bytes([0,0,0,7])
        ack   = bytes([0,0,2,8])
        nack  = bytes([0,1,2,2])
        dados = bytes([5,5,5,5])
        data = 0 
        tipo = 0 
        rxBuffer = 0
        tamanho = 0 
        while tipo ==  0 : # Reconhecendo o Syn   
            rxBuffer,tipo,tamanho == com.getData()
            time.sleep(0.5)
            if tipo == syn:  # Se o rxBuffer estiver com o Syn!
                print("Server recebeu o syn, enviando ack")           
                com.sendData(data,ack)
                print("Server enviando o Syn")
                com.sendData(data,syn)
                print("Server enviou o syn, esperando ack final")   
            else:
                print("Enviando Nack, pacote syn perdido")
                com.sendData(data,nack)    
            rxBuffer,tipo,tamanho == com.getData()
            if tipo == ack:  # Se o rxBuffer estiver com o Syn!
                print("Server recebeu o ack, pronto para iniciar comunicação")
                tipo = 1 
                while tipo == 1 :
                    print("Comunicação Inicializada")
                    print("****RECEBENDO DADOS****")
                    rxBuffer, tipo,tamanho == com.getData()
                    print ("Lido              {} bytes ".format(tamanho))
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
                    break
                    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
            else:
                print("Enviando Nack, pacote ack perdido")
                com.sendData(data,nack)
                print("Realizando busca novamente.........")
                rxBuffer,tipo,tamanho == com.getData()      
                time.sleep(0.5)
                




if __name__ == "__main__":
    main()


    

  