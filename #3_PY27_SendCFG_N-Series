#For Python 2.7
#Example - sending files to Matrix N-series scanners by using host mode programming and X-Modem.
#Joakim Ringstad 2020
#!/usr/bin/env python

import socket
import time
import sys, getopt
import os, binascii
import struct


def main(argv):
    
    
    ipAddress = '192.168.3.100'
    filename = 'a.dlcfg'
    confname = 'myFile!'
    ackData = SEND_CFG_TCP(ipAddress,filename,confname)
  
    print ackData



def SEND_CFG_TCP(ipAddress,filename,confname):
    
###OPEN FILE NAME###
    
    #Try to open file and save to databuffer
    try:
        filebuffer = open(filename,'rb').read()
        print "File", filename, "loaded"
    #File could not be found - exit!
    except:
        print "Filename", filename, "does not exist"
        sys.exit()

###BUILD PACKAGE###
        
    #Get file length
    fileSize = len(filebuffer)+4
    #Build file length package
    fileLengthPackage = struct.pack('>L', fileSize)
    #Build crc32 checksum
    crc = (binascii.crc32(fileLengthPackage + filebuffer) & 0xFFFFFFFF)
    #Build crc32 checksum package
    crcPackage = struct.pack('>L', crc)

###OPEN TCP###
    
    #Initialize tcp socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Open connection on HMP port 1023
    s.connect((ipAddress, 1023))
    
###SEND HMP COMMANDS###
    
    #Send hmp programming mode
    s.send('\x1b[C\r')
    time.sleep(0.1)
    data = s.recv(1024)
    s.send('\x1b[B\r')
    time.sleep(0.1)
    data = s.recv(1024)

    #SEND_CFG file XMODEM
    try:
        s.send("SEND_CFG " + confname + '\n')
        time.sleep(0.1)
        print "File", filename, "sent to device with confname \"",confname,"\""
    except:        
        s.send('\x1b[A\r')
        time.sleep(0.1)
        s.close()
        print "SEND_CFG error - connection closed"
        sys.exit()
    s.send(fileLengthPackage)   # send 4 bytes with length field
    s.send(filebuffer)          # send with data buffer
    s.send(crcPackage)          # send 4 byte with CRC field
    cmdout = s.recv(1024)
    time.sleep(0.1)
    #Disable HMP
    s.send('\x1b[A\r')
    time.sleep(0.1)
    #Close connection
    s.close()
    return cmdout

if __name__ == "__main__":
   main(sys.argv[1:])
