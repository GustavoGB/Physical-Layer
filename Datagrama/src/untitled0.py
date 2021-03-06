# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:12:51 2018

@author: Gustavo Gobetti
"""

from construct import *
import os
import binascii
import struct
import codecs
import time

class Packing():




    def __init__(self):
    
        l        

        def headBuild(self): 

            head = " 96e89a298e0a9f469b9ae458d6afae9f"
            headOffical = bytearray(head,'utf-8')
            return binascii.hexlify(headOfficial)         

        def eopBuild(self):
            eop = "d1eeb02f2d34d1aa8ecb7b3ed35cd090"
            eopOfficial = bytearray(eop, 'utf-8')
            return binascii.hexlify(eopOfficial)

        def dataPackBuild(self,data):
            
            header = headOfficial(len(data))  # This line defines that the header contains the range of the payload and the inicial data is set to 0.
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
            else:
                 return payLoad        