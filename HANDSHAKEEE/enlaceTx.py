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
class TX(object):
    """ This class implements methods to handle the transmission
        data over the p2p fox protocol
    """

    def __init__(self, fisica):
        """ Initializes the TX class
        """
        self.fisica      = fisica
        self.buffer      = bytes(bytearray())
        self.transLen    = 0
        self.empty       = True
        self.threadMutex = False
        self.threadStop  = False

    def thread(self):
        """ TX thread, to send data in parallel with the code
        """
        while not self.threadStop:
            if(self.threadMutex):
                self.transLen    = self.fisica.write(self.buffer)
                print ("Transmitido       {} bytes ".format(self.transLen))
                self.threadMutex = False

    def threadStart(self):
        """ Starts TX thread (generate and run)
        """
        self.thread = threading.Thread(target=self.thread, args=())
        self.thread.start()

    def threadKill(self):
        """ Kill TX thread
        """
        self.threadStop = True

    def threadPause(self):
        """ Stops the TX thread to run

        This must be used when manipulating the tx buffer
        """
        self.threadMutex = False

    def threadResume(self):
        """ Resume the TX thread (after suspended)
        """
        self.threadMutex = True

    def packMessage(self,data,tipo):
        #Cria Head
        headofPacket = (len(data)).to_bytes(7, byteorder = 'big')
        #Concatena o head com o tipo da msg 
        headofPacket += tipo
        #Cria Eop
        endofPacket = (111111111111).to_bytes(5, byteorder = 'big')
        print(endofPacket)
        #Concatena o pacote completo
        allPacket = headofPacket + data + endofPacket
        
        #Igual RX
        if int.from_bytes(tipo, byteorder ='big') == 7:
            print("Payload = ", len(data))

        return allPacket

    def sendBuffer(self, data,tipo):
        """ Write a new data to the transmission buffer.
            This function is non blocked.

        This function must be called only after the end
        of transmission, this erase all content of the buffer
        in order to save the new value.
        """
        
        self.transLen   = 0
        #Chama o packet maker   
        self.buffer = self.packMessage(data,tipo) 
        self.threadMutex  = True
        

    def getBufferLen(self):
        """ Return the total size of bytes in the TX buffer
        """
        return(len(self.buffer))

    def getStatus(self):
        """ Return the last transmission size
        """
        return(self.transLen)

    def getIsBussy(self):
        """ Return true if a transmission is ongoing
        """
       
        return(self.threadMutex)
        

            
        #constroi EOP
        #eop = bytes([255,254,253,252])
        #eopBruto  = len(str(eop))
        #cargaUtil = len(str(data))
        #print(data)
        #constroi Head
        #head = (cargaUtil).to_bytes(4, byteorder='big') + tipo   
        #Concatena o payload com o eop
        #dataEop = data + eopBruto
        #Concatena o head com o payload e o Eop
        #data =  head + dataEop

        #return data,tipo    
        
        
        

