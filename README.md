# DLA_Product-communication

Some final working scripts used when I worked as a field technician at Datalogic, just for testing, troubleshooting and "getting things up and running" on customers site. These are top layer scripts, only communicating and reading data from some Datalogic products.

## #1_Node-Red_S85-binary.json
> **Node-Red**
> **Sensor - S85**<br>
>
> Full Node-Red script for collecting and sorting data from S85-sensor over RS232 (dongle converter from RS485). Uses Node-Red Dashboard.
>
> Setup guide
> 1. Install node.js (linux, mac, windows)
> 2. Install Node-Red from node.js command promt
> 3. Start Node-Red server by typing node-red
> 4. Enter 'localhost:1880' in browser
> 5. Import json flow

> *Known bug: Packages might get out of sync caused by slow CPU and bad package handling.*
> *Output: Wrong distance data*

## #1_Node-Red_S85_binaryFunction.js
> **Javascript**
> **Sensor - S85**
>
> Javascript function file - Same code as running inside function block in .json above.
> INFO: Intended to be used inside Node-Red flow (#1_Node-Red_S85-binary.json)

> *Known bug: Packages might get out of sync caused by slow CPU and bad package handling.*
> *Output: Wrong distance data*

## #2_PY38_tcp2ascii_char_client.py
> **Python 3.8**
> **Non specified**
>
> Reads hex over TCP and prints non readable chars from standard ASCII-table, i.e. \<STX\>\<CR\>. No need to use HyperTerminal or other old RS232 softwares anymore!
>
> Connecting guide
> 1. Connect TCP-device
> 2. Set ip and port
> 3. Begin to send data, output will be hex!

## #3_PY27_SendCFG_N-Series.py
> **Python 2.7**
> **Matrix N**
> Send config file to Matrix N-series by using HMP SEND_CFG command and x-modem.
>
> Script steps
> 1. Initialize communication
> 2. Enter HMP mode
> 3. Build package
> 4. Send package
> 5. Exit HMP mode

## #4_PY38_S85_RS232.py
> **Python 3.8**
> **Sensor - S85**
> Read binary byte data from S85 RS232 (External converter from RS485 to RS232) and convert to decimal. Does same as #1 but bugfixed (and Python instead of Javascript)
>
> Script steps
> 1. Read byte package (3 bytes)
> 2. Convert to binary string
> 3. Remove bits according to S85 serial com guide
> 4. Convert output bitstring to int
> 5. Print the int (measured distance)!
