from construct import *
import os
import binascii
import struct
import codecs
import time

class Packing():

    class HandShake():

        def __init__(self):
            self.SYN = 0xAA
            self.ACK = 0xAB
            self.NACK = 0xAC

    def __init__(self):
        self.headSTART = 0xAF
        self.headStruct = Struct("start"  /Int16ub,
                                "size " / Int8ub,
                                "type" / Int8ub)

        self.typeHead = self.HandShake()                   
                            
        def HeadStruct(self): 
            head = Struct (
                                "start" / Int16ub,
                                "size" / Int8ub
                                    )
            return(head)
            
        def headBuild(self, dataLen): 
            header = self.headStruct.build(dict(start = self.headSTART, size = dataLen,type = type))
            return (header)                        
            
        
        def eopBuild(self):
            eopOfficial = bytearray(self.eop, 'utf-8')
            return binascii.hexlify(eopOfficial)
    
        def dataPackBuild(self,data):
            header = self.headBuild(len(data))  # This line defines that the header contains the range of the payload and the inicial data is set to 0.
            packet = header
    
            packet += data
            packet += self.eopBuild()
            
            return(packet)
    
        def transf_binary(self, y):
            return format(y,'b').zfill(16) #hexadecimal format
    
        def unbuildPack (self,packet):
            
            header = packet[0:5]
            len_payload = header[1:4]
            size_payload = int.from_bytes(len_payload, byteorder = 'big')
            payLoad = packet[len(header):]
    
            if size_payload == 0 : 
                return header 
            else :
                return payLoad        