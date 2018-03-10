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
#   com2 = enlace(serialName2)

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

    # Transmite imagem
    print("Transmitindo .... {} bytes".format(txLen))
    start = time.time()
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

    # Salva imagem recebida em arquivo
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
    com2.disable()

if __name__ == "__main__":
    main()