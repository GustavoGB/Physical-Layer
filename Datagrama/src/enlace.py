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
    def sendData(self, data,head_Syn,head,packetNack):
        """ Send data over the enlace interface
        """

        #print("vai contruir o head")
        #head2 = self.End.head(len(data))     
        #print("print do head contruido pela classe {}" .format(head2))
        ###
        ### Construindo efetivamente ACK,NACK,SYN        
        
    
        #Primeiro a ser enviado pelo cliente!
        packetSyn1 = self.End.SynBuild()  #LOGO packets[0]
        print("Construindo Syn{}".format(packetSyn1))
        #Confirmação do estabelecimento da conecção
        packetSyn2 = self.End.SynBuild()   #LOGO packets[1]
        print("Construindo Syn2{}".format(packetSyn2))
        #Primeio a ser enviado pelo server apóis receber o pacote Syn1 do cliente          
        packetAck3 = self.End.AckBuild()   #LOGO packets[2]
        print("Construindo Ack1{}".format(packetAck3))
        #Enviado pelo client quando recebe confimação através do primeiro ACK entregue pelo server
        packetAck4 = self.End.AckBuild()    #LOGO packets[3]
        print("Construindo Ack2{}".format(packetAck4))
        #Enviado caso a conecção tenha problemas
        packetNack5 = self.End.NackBuild()  #LOGO packets[4]
        print("Construindo Nack{}".format(packetNack5))


                
        #head_Syn1 = self.End.headBuild(len(data),01)  + packetSyn1
        #print(head_Syn1)
        #head_Ack1 = self.End.headBuild(len(data),11)  + packetAck1 
        #head_Syn2 = self.End.headBuild(len(data),02)  + packetSyn2 
        #head_Ack2 = self.End.headBuild(len(data),12)  + packetSyn2
        #head_Nack = self.End.headBuild(len(data),22)  + packetNack
        
                
        
        lastHead = self.End.headBuild(len(data))
        print("vai construir o Head {}".format(lastHead))
   
        lastEop = self.End.eopBuild()  
        print("vai construir o Eop {}".format(lastEop))
  
        packet = self.End.dataPackBuild(data) # Usa a função do packing para construir o pacote
        packet = data
        
        self.tx.sendBuffer(data)
        
    def getData(self,type):
        # Get n data over the enlace interface
        #Return the byte array and the size of the buffer
        
        
        print('entrou na tentativa de ler')   
        print('tamanho do buffer no enlac {}'  .format(self.rx.getBufferLen()))
        
        

       # package_payload = self.rx.packageSearch()
       # data = self.End.unbuildPack(package_payload)
        data = self.rx.getNData(1)
        return(data, len(data))

    
