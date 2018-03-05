from construct import *
import os
import binascii
import struct
import codecs
import time

class Packing():




    def __init__(self):
        self.headSTART = 0xAF
        self.headStruct = Struct("start"  /Int16ub,
                                "size " / Int8ub)

    def headBuild(self,dataLen): 
        header = self.headStruct.build(dict(
            start = self.headSTART
            size = dataLen))
            return(header)

    def eopBuild(self):
        eop = "d1eeb02f2d34d1aa8ecb7b3ed35cd090"
        eopOfficial = bytearray(eop, enconding = "ascii")
        return binascii.hexlify(eopOfficial)

    def dataPackBuild(self,data):
        