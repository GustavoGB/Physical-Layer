from enlace import *
import time
 


# Serial Com Port
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
serialName = "COM4"           # Ubuntu (variacao de)
#serialName2 = "COM3"  
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
#serialName = "COM3"                  # Windows(variacao de)

def main():
    # Inicializa enlace
    com = enlace(serialName)
           
    # Ativa comunicacao
    com.enable()
#   com2.enable()
    # Endereco da imagem a ser transmitida
    imageR = "./imgs/panda.jpg"
    # Endereco da imagem a ser salva
    #SERVER--imageW = "./imgs/recebida.png"

    # Log
    print("-------------------------")
    print("Comunicação inicializada")
    print("  porta : {}".format(com.fisica.name))
    print("-------------------------")

    # Carrega imagem
    print ("Carregando imagem para transmissão :")
    print (" - {}".format(imageR))
    print("-------------------------")
    txBuffer = open(imageR, 'rb').read()
    txLen    = len(txBuffer)
    print(txLen)
    
    txLen = 0
    
    while txLen == 0:
        
        "Tentando estabelecer 
        "conexão com o servidor
        "enviando Synchronize packet
         com.sendData(packetSyn)
         
    

    # Transmite imagem
    print("Transmitindo .... {} bytes".format(txLen))
    start = time.time()
    
        

    #ACK CASE
    if (txBuffer == "82d7ba7ea655a2bbde5a4e2153a66dae"):        
        print("Este pacote é um Ack e está sendo enviado para estabelecer conexão")
        com.sendData(packetAck)
    
    #NACK CASE
    if (txBuffer == "ab678d51f0c329ac3031dd92367959a5"):
        print("Este pacote é um Nack e está sendo enviado para dizer que houve falhas na conexão")
        com.sendData(packetNack)

    #SYN CASE    
    if (txBuffer == "d726760b0467b77803d6d1f3585deb6e"):
        print("Este pacote é um Syn e está sendo enviado para iniciar a conexão")
        com.sendData(packetSyn)
    
        
    
    com.sendData(txBuffer)

    # espera o fim da transmissão
    while(com.tx.getIsBussy()):
        pass
   
######################################3teste de recebimento
    print ("Recebendo dados .... ")

   
    rxBuffer, nRx = com.getData()
    start = time.time()

    # log
    end = time.time()

    print ("Lido              {} bytes ".format(nRx))

    # Salva imagem recebida em arquivo1
    print("-------------------------")
    print ("Salvando dados no arquivo :")
    print (" - {}".format(imageW))
    f = open(imageW, 'wb')
    f.write(rxBuffer)

    # Fecha arquivo de imagem
    f.close()
####################################################################
   
   
   
    end = time.time()
    tempo = (end-start)

    #Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")
    print("Tempo de transmissão:","{0:.2f}".format(tempo),"segundos")
    com.disable()


if __name__ == "__main__":
    main()