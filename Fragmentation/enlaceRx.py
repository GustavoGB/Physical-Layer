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


    def getBuffer(self, nData):
        """ Remove n data from buffer
        """
        self.threadPause()
        allPacket    =   self.buffer[0:nData]
        endofPacket  =   self.buffer.find(b'111111111111') #Tirou-se o Extract header e Eop para ficar mais simples
        headofPacket =   self.buffer[0:7]
        tipo         =   self.buffer[7:8]
        payload      =   allPacket[8:endofPacket]

        if int.from_bytes(tipo, byteorder='big') == 7 :
            print("Payload esperado de :",
                int.from_bytes(headofPacket,byteorder='big'),"bytes")

        self.clearBuffer()
        self.threadResume()
        return(payload,tipo)

    def getNData(self):
        self.clearBuffer()
        tamanho = 0

        start = time.time() #Tick

        while (self.getBufferLen() > tamanho or self.getBufferLen() == 0):
            tamanho = self.getBufferLen()
            time.sleep(0.5)

            end = time.time()  #Tock fim
            print("%.2f" % (end-start), '/ 10 seg')

            if (end - start) > 15:
                return ()

        return(self.getBuffer(tamanho)) 
      

    def clearBuffer(self):
        """ Clear the reception buffer
        """
        self.buffer = b""


        