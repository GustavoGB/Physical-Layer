from construct import *
import os
import binascii
import struct
import codecs
import time


class Packing():


    def __init__(self):
        self.headSTART       = 0xAF
        self.head            = self.HeadStruct()    
        self.headLen         = self.head.sizeof()
    
    def HeadStruct(self): 
        head = Struct(
        "start" / Int8ub,
        "size" / Int16ub,
        "sample" / Int8ub)
        return(head)
                
    def headBuild(self,dataLen): 
        header = self.head.build(dict
        (start = self.headSTART,
        size = dataLen
         ))
        return(header)          

    #All the values of the packts can be found just using an md5hash algorithm

    
    def SynBuild(self):
        syn = "d726760b0467b77803d6d1f3585deb6e"
        synOfficial = bytearray(syn,'ascii')
        return binascii.hexlify(synOfficial)
        
    def AckBuild(self):
        ack = "82d7ba7ea655a2bbde5a4e2153a66dae"
        ackOfficial = bytearray(ack,'ascii')
        return binascii.hexlify(ackOfficial)
        
    def NackBuild(self):
        nack = "ab678d51f0c329ac3031dd92367959a5"
        nackOfficial = bytearray(nack,'ascii')
        return binascii.hexlify(nackOfficial)

            
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
       len_payload = header[1:3]
       size_payload = int.from_bytes(len_payload, byteorder = 'big')
       payLoad = packet[len(header):]
        
       if size_payload == 0 : 
           return header 
       else :
           return payLoad      
                                 
           
    