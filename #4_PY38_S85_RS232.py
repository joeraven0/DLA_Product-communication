import serial
import time
import sys
import datetime
ser = serial.Serial("COM8",baudrate=115200)
baddataCounter = 0
while True:
    byteQueInput = ser.in_waiting
    
    if byteQueInput>0:
        msg = ''
        output = ''
        print("Bytes in input que: "+str(byteQueInput))
        
        #Read three bytes from serial port
        msg = ser.read(3)

        #Verify byte packages on input are synced. Modulo verifies always minimum 3 byte sized packages in que
        if byteQueInput%3==0:
            sliced = []
            
            #1. Read each byte (tot 3) and make binary
            #2. Remove first 4 and 5 bytes according to S85_communication_guide.pdf
            #3. Append binary string to list named "sliced"
            sliced.append(bin(msg[0])[5:len(bin(msg[0]))])
            sliced.append(bin(msg[1])[4:len(bin(msg[1]))])
            sliced.append(bin(msg[2])[4:len(bin(msg[2]))])
            #Save list to string
            joinedSliced = ''.join(sliced)
            #Sensor int value in millimeter
            intValue = int(''.join(sliced),2)
            #Print raw data(binary) & sensor value(int in millimeter)
            output = str("RAW INPUT: "+bin(msg[0]))+str(bin(msg[1]))+str(bin(msg[2])) + '\n' + 'Sensor value (bin): ' + joinedSliced + 'mm\n' + 'Sensor value (int): '+str(intValue) + 'mm\n'
            print(output)
            #time.sleep(2)
            if byteQueInput>1000:
                ser.reset_input_buffer()
        else:
            #Sensor data size is 3 byte. If not evenly divideable by three, python didn't catch all packages. CLEAR IT!
            baddataCounter +=1
            print('INFO: Que out of sync! - Buy faster CPU!!\n Out of sync count: ' +str(baddataCounter)+'\n')
            ser.reset_input_buffer()
        
            
     
