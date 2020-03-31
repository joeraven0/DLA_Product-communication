#TCP client to ascii character - with function keys.
#Joakim Ringstad - Python 3.8

#!/usr/bin/env python

import socket


printChar = 1
printDec = 0
printHex = 0

Interface = 0 #0=TCP, 1=RS

COM_PORT = 'COM1'
COM_BAUD = '115200'


asciiTable = [
            '<NUL>', '<SOH>', '<STX>', '<ETX>', '<EOT>', '<ENQ>', '<ACK>', '<BEL>',
            '<BS>', '<HT>', '<LF>', '<VT>', '<FF>', '<CR>', '<SO>', '<SI>',
            '<DLE>', '<DC1>', '<DC2>', '<DC3>', '<DC4>', '<NAK>', '<SYN>', '<ETB>',
            '<CAN>', '<EM>', '<SUB>', '<ESC>', '<FS>', '<GS>', '<RS>', '<US>']   
   


def tcpConnect(TCP_IP,TCP_PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    
    dataRead = s.recv(1024)
    s.close()
    return dataRead

def rsConnect():
    
    ser = serial.Serial('/dev/ttyACM0')
    ser_bytes = ser.readline()
    
data = tcpConnect('127.0.0.1',51236)  


hexData = []
asciiDecStrArr = []
asciiDecStr, asciiHexStr, asciiCharStr = ("",)*3


i=0
while i < len(data):
    #To hex list
    hexData.append((data[i].encode('hex'), 16))    
    #Hex list to two digits decimal string list
    asciiDecStrArr.append(("%02d" % (hexData[i],)))
    asciiHexStr += hex(hexData[i]) + " "
    
    if int(asciiDecStrArr[i]) <= 31:        
        asciiCharStr+=asciiTable[int(asciiDecStrArr[i])]
    else:
        asciiCharStr+=data[i]
    asciiDecStr += asciiDecStrArr[i] + " "
    i += 1


if printChar:
    print("Char:", asciiCharStr)
if printDec:
    print("ASCII (dec):", asciiDecStr)
if printHex:
    print("ASCI (hex):", asciiHexStr)
