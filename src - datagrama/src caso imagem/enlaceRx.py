#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
#Carareto
#17/02/2018
#  Camada de Enlace
####################################################

# Importa pacote de tempo
import time

# Threads
import threading

# Class
class RX(object):
    """ This class implements methods to handle the reception
        data over the p2p fox protocol
    """
    
    def __init__(self, fisica):
        """ Initializes the TX class
        """
        self.fisica      = fisica
        self.buffer      = bytes(bytearray())
        self.threadStop  = False
        self.threadMutex = True
        self.READLEN     = 1024

    def thread(self):
        """ RX thread, to send data in parallel with the code
        """     
        while not self.threadStop:
            if(self.threadMutex == True):
                rxTemp, nRx = self.fisica.read(self.READLEN)
                if (nRx > 0):
                    self.buffer += rxTemp
                    self.threadKill     # lendo apenas uma vez
                time.sleep(0.001)

    def threadStart(self):
        """ Starts RX thread (generate and run)
        """
        self.thread = threading.Thread(target=self.thread, args=())
        self.thread.start()

    def threadKill(self):
        """ Kill RX thread
        """
        self.threadStop = True

    def threadPause(self):
        """ Stops the RX thread to run

        This must be used when manipulating the Rx buffer
        """
        self.threadMutex = False

    def threadResume(self):
        """ Resume the RX thread (after suspended)
        """
        self.threadMutex = True

    def getIsEmpty(self):
        """ Return if the reception buffer is empty
        """
        if(self.getBufferLen() == 0):
            return(True)
        else:
            return(False)

    def getBufferLen(self):
        """ Return the total number of bytes in the reception buffer
        """
        return(len(self.buffer))

    def getAllBuffer(self, len):
        """ Read ALL reception buffer and clears it
        """
        self.threadPause()
        b = self.buffer[:]
        self.clearBuffer()
        self.threadResume()
        return(b)

    def getBuffer(self, nData):
        """ Remove n data from buffer
        """
        self.threadPause()
        b           = self.buffer[0:nData]
        self.buffer = self.buffer[nData:]
        self.threadResume()
        return(b)

    def getNData(self, size):
        
        """ o size tera de ser removido"""
        
        size = size + 8  #devido ao header e ao EOP
         
        #chegou mensagem, coloca-se um time out .. como espera... e letudo... tem que achar um heaer e um EOP        
        #while(self.getBufferLen() < size):
         #   time.sleep(0.05)
        time.sleep(2)
        data = self.getAllBuffer(len)
        
        cargaUtil = self.extractHeader(data) 
        print("Na leitura no rx extraiu o seguinte tamanho de carga util: {}" .format(cargaUtil)) 
        posicaoEOP = self.localizaEOP(data)
        print("Na leitura no rx localizou o EOP na posicao: {}" .format(posicaoEOP)) 
        return(data)


    def clearBuffer(self):
        """ Clear the reception buffer
        """
        self.buffer = b""


    def extractHeader(self,data):
        cargaUtil = int.from_bytes([data[0],data[1],data[2],data[3]], byteorder = 'big')
        print('No desempacotador, entendeu-se um payload de {}' .format(cargaUtil))
        return cargaUtil
        
    def localizaEOP(self,data):
        cont=0
        posicao = 0
        
        for i in data:
            #print('indo {}' .format(data[cont]))
            if data[cont] == 255 and data[cont+1] == 254 and data[cont+2] == 253 and data[cont+3] == 252:
                print("Achou o EOD  na posicao {}"  .format(cont))
                posicao = cont
                break
            cont += 1    
        return (posicao)
        
        
        