
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
#serialName = "/dev/tty.usbmodem1451" # Mac    (variacao de)
serialName = "COM1"                  # Windows(variacao de)

print("abriu com")

def main():
   
    while True:
        com = enlace(serialName)
        com.enable()
        imageR = "./imgs/imageC.png"
        txBuffer = open(imageR, 'rb').read()
        data = txBuffer

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
        print(data,tipo)
        #Recebendo Ack1
        print("Esperando Ack1.....")
        rxBuffer,tipo = com.getData()
        tipo = (int.from_bytes(tipo, byteorder='big'))
        print("ACK1...RECEBIDO COM SUCESSO")
        
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
        else:
            if tipo == 9 :
                print("Recebi o Nack, vou reenviar o Ack2...")
                data = (8).to_bytes(1,byteorder='big')
                tipo = (9).to_bytes(1,byteorder='big')
                com.sendData(data,tipo)
                else:
                    print("***ERRO***")
                    print("***INICIANDO HS NOVAMENTE")
                    continue
                
            
        

        time.sleep(0.5)
        tipo = 0 #Só uma variável para setar o estado e aplicar a varredura
        while tipo == 0: # Reconhecendo o Syn   
            rxBuffer,tipo,tamanho = com.getData()
            time.sleep(0.5)
            if tipo == ack:  # Se o tipo for ack
                print("Client recebeu o ack, esperando syn")           
            if tipo == nack:
                print("Reenviando pacote ack...")
                com.sendData(dados,ack)
                tipo = 0 # Reenvia o sinal ack
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
        tipo = (7).to_bytes(1,byteorder='big')
        com.sendData(data,tipo)


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

            
            
        
  