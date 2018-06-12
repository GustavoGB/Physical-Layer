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
import packing
# Construct Struct
from construct import *
import binascii

# Interface Física
from interfaceFisica import fisica

# enlace Tx e Rx
from enlaceRx import RX
from enlaceTx import TX

import math

class enlace(object):
    """ This class implements methods to the interface between Enlace and Application
    """

    def __init__(self, name):
        """ Initializes the enlace class
        """
        self.fisica      = fisica(name)
        self.rx          = RX(self.fisica)
        self.tx          = TX(self.fisica)
        self.connected   = False
        self.End         = packing.Packing()

    def enable(self):
        """ Enable reception and transmission
        """
        self.fisica.open()
        self.rx.threadStart()
        self.tx.threadStart()

    def disable(self):
        """ Disable reception and transmission
        """
        self.rx.threadKill()
        self.tx.threadKill()
        time.sleep(1)
        self.fisica.close()

    ################################
    # Application  interface       #
    ################################
    def sendData(self, data,packetSyn,packetAck,packetNack):
        """ Send data over the enlace interface
        """

        #print("vai contruir o head")
        #head2 = self.End.head(len(data))     
        #print("print do head contruido pela classe {}" .format(head2))
        ###
        ### Construindo efetivamente ACK,NACK,SYN        
        
    

        packetSyn = self.End.SynBuild()
        print("Construindo Syn{}".format(packetSyn))
                  
        
        packetAck = self.End.AckBuild()
        print("Construindo Ack{}".format(packetAck))
        
        packetNack = self.End.NackBuild()
        print("Construindo Nack{}".format(packetNack))
        
        
        lastHead = self.End.headBuild(len(data))
        print("vai construir o Head {}".format(lastHead))
   
        lastEop = self.End.eopBuild()  
        print("vai construir o Eop {}".format(lastEop))
  
        packet = self.End.dataPackBuild(data) # Usa a função do packing para construir o pacote
        packet = data
        
        
        self.tx.sendBuffer(data)
    def getData(self):
        # Get n data over the enlace interface
        #Return the byte array and the size of the buffer
        
        
        print('entrou na tentativa de ler')   
        print('tamanho do buffer no enlac {}'  .format(self.rx.getBufferLen()))
        
        

       # package_payload = self.rx.packageSearch()
       # data = self.End.unbuildPack(package_payload)
        data = self.rx.getNData(1)
        return(data, len(data))

    