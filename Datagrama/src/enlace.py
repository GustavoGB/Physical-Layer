
#REALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
# Importa pacote de tempo
import time

# Construct Struct
from construct import *

# Interface física
from interfaceFisica import fisica

# enlace Tx e Rx
from enlaceRx import RX
from enlaceTx import TX

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


    def sendData(self, data):
        """ Send data over the enlace interface
        """
        
        #Construção do Head

        self.StructEop()
        self.StructHead()
       
        
        #Encapuslamento do arquivo--> ENVIO
        pack = self.buildDataPacket(data)
        
        #Construção do EOP
  

        self.tx.sendBuffer(pack)
        
    def getData(self):
        """ Get n data over the enlace interface
        Return the byte array and the size of the buffer
        """
        data, size = self.rx.UnbuildPack()

        return(data,len(data),size)


    #Estrutura Head
    def StructHead(self):
        self.headStart = 0xAA
        self.headStruct = Struct("start"/ Int16ub, "size"/ Int16ub)

    #Implementa o Head
    def buildHead(self, datalen):

        head = self.headStruct.build(dict(start = self.headStart, size = datalen))

        return head

    #Estrutura EOP
    def StructEop(self):

        self.endStart = 0xFF
        self.endStruct = Struct("g1"/Int8ub, "g2"/Int8ub, "g3"/Int8ub,"g4"/Int8ub)


    #Implementa o EOP

    def buildEop(self):

        end = self.endStruct.build(dict(g1 = 0x21, g2 = 0x42, g3 = 0x63,g4 = 0x04))

        return end


    def buildDataPacket(self, data):


        #Gerar Head

        pack = self.buildHead(len(data))

        print(len(data)) # Printar o tamanho do arquivo (payload)

        
        #Concatenação do Header, payload e EOP
        pack += data
        pack += self.buildEop()
        
        return pack
