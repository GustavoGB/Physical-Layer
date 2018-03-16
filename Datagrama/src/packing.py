from construct import *
import os
import binascii
import struct
import codecs
import time
from enlaceRx import RX

class Packing():

    class HandShake():
        
        def __init__(self):
            
            self.Syn = 0xAA
            self.Ack = 0xAB
            self.Nack = 0xAC
    

    def __init__(self):
        self.headSTART = 0xAF
        self.head      = self.HeadStruct()    
        self.headLen   = self.head.sizeof()
        self.typeHead  = self.HandShake()
      
        
    def HeadStruct(self): 
        head = Struct(
        "start" / Int8ub,
        "size" / Int16ub,
        "type" / Int8ub)
        return(head)
                
    def headBuild(self,dataLen, self.type): 
        header = self.head.build(dict
        (start = self.headSTART,
         size = dataLen,
         type = self.type)
        return (header)                     
                
            
    def eopBuild(self):
        eop = "d1eeb02f2d34d1aa8ecb7b3ed35cd090"
        eopOfficial = bytearray(eop, 'ascii')
        return binascii.hexlify(eopOfficial)
        
    def dataPackBuild(self,data):
        
        header = self.headBuild(len(data))  # This line defines that the header contains the range of the payload and the inicial data is set to 0.
        bigPack = header        
        bigPack += data
        bigPack += self.eopBuild()              
        return(bigPack)
        
    def transf_binary(self, y):
        return format(y,'b').zfill(16) #hexadecimal format
        
    def unbuildPack (self,packet):
        
       header = packet[0:3]
      # print(header)
      # header = header.sort(header)
       len_payload = header[1:3]
       size_payload = int.from_bytes(len_payload, byteorder = 'big')
       payLoad = packet[len(header):]
        
       if size_payload == 0 : 
           return header 
       else :
           return payLoad      
           
           
    def synPack(self):
        pSyn += self.headBuild(0,self.HandShake.Syn)
        pSyn += self.eopBuild()
        return pSyn
           
    def ackPack(self):
        pAck += self.headBuild(0,self.HandShake.Ack)
        pAck += self.eopBuild()
        return pAck
        
    def nackPack(self):
        pNack += self.headBuild(0,self.HandShake.Nack)
        pNack += self.eopBuild()
        return pNack
        
        