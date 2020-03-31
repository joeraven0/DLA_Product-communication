#TCP client to ascii character - with function keys & good/bad read counter
#Joakim Ringstad - Python 3.8


#!/usr/bin/env python

import socket, time


outputFormat = True #False=ascii char, True=ascii hex
NO_READ_STRING = "<STX><CAN><CR><LF>"
[TCP_IP, TCP_PORT] = ['127.0.0.1',51236]
goodCount, badCount = (0,)*2

asciiTable = [
            '<NUL>','<SOH>','<STX>','<ETX>','<EOT>','<ENQ>','<ACK>','<BEL>',
            '<BS>','<HT>','<LF>','<VT>', '<FF>','<CR>','<SO>','<SI>',
            '<DLE>','<DC1>','<DC2>','<DC3>','<DC4>','<NAK>','<SYN>','<ETB>',
            '<CAN>','<EM>','<SUB>','<ESC>','<FS>','<GS>','<RS>','<US>']   
   

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while 1:
    data=s.recv(1024)
    if not data:
        print("No data")        
        break
    ascii_char=""
    ascii_char_buffer = data.decode("utf-8")
    ascii_hex = " ".join([hex(data[n]) for n in range(len(data))])
    for n in range (len(data)):
        if data[n]<=31:
            ascii_char+=asciiTable[data[n]]
        else:
            ascii_char+=ascii_char_buffer[n]
    if not outputFormat:
        print(ascii_char)        
    if outputFormat:
        print(ascii_hex)
    if ascii_char==NO_READ_STRING:
        badCount +=1
    else:
        goodCount +=1
        goodbadread = "Good: " + str(goodCount) + " Bad: " + str(badCount)
    print(goodbadread)

s.close()

