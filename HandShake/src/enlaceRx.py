#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
# Prof. Rafael Corsi
#  Abril/2017
#  Camada de Enlace
####################################################

# Importa pacote de tempo
import time
from packing import *
import enlace 

# Threads
import threading
import codecs

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
        self.found       = False
       # self.enlace      = self.head_Syn1 
        
    def thread(self):
        """ RX thread, to send data in parallel with the code
        """
        while not self.threadStop:
            if(self.threadMutex == True):
                rxTemp, nRx = self.fisica.read(self.READLEN)
                if (nRx > 0):
                    self.buffer += rxTemp
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

    def getNData(self):
        """ Read N bytes of data from the reception buffer

        This function blocks until the number of bytes is received
        """
           
        grandeza = 0 # Tamanho inicial da recepção 
        while(self.getBufferLen() > grandeza or self.getBufferLen()==0 ):
            grandeza = self.getBufferLen()
            print('tamanho dos dados'  .format(grandeza))
            time.sleep(2.0)
        
        kind = self.getBuffer()
        kind = kind[23:32]
        print("plotando a parte kind da mensagem recebida {}" .format(kind))
        #Rx define Syn1
        
        if kind == synOfficial:
            kind = "syn1"
            print(kind)
            return kind
        # ''  Syn2    
        if(self.getBuffer == self.enlace.head_Syn2):
            kind = "syn2"
            return(self.getBuffer())
        # '' Ack1    
        if (self.getBufferLen() == self.enlace.head_Ack1):
            kind = "ack1"
            return(self.getBuffer())
        # '' Ack2   
        if(self.getBuffer == self.enlace.head_Ack2):
            kind = "ack2"
            return(self.getBuffer())
        # '' Nack
        if(self.getBuffer == self.enlace.head_Nack):
            kind = "nack"
            return(self.getBuffer())
       


    def clearBuffer(self):
        """ Clear the reception buffer
        """
        self.buffer = b""


   