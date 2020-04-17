# DLA_Finished

## #1_Node-Red_S85-binary.json
> **Node-Red**
> **Sensor - S85**<br>
>
> Full Node-Red script for collecting and sorting data from S85-sensor over RS232 (dongle converter from RS485). Uses Node-Red Dashboard.
>
> *BUG: Packages might get out of sync caused by slow CPU and bad package handling.*

## #1_Node-Red_S85_binaryFunction.js
> **Javascript**
> **Sensor - S85**
>
> Javascript function file - Same code as running inside function block in .json above.
>
> *BUG: Packages might get out of sync caused by slow CPU and bad package handling.*

## #2_PY38_tcp2ascii_char_client.py
> **Python 3.8**
> **Non specified**
>
> Reads hex over TCP and prints non readable chars from standard ASCII-table, i.e. \<STX\>\<CR\>. No need to use HyperTerminal or other old RS232 softwares anymore!

## #3_PY27_SendCFG_N-Series
> **Python 2.7**
> **Matrix N**
> Send config file to Matrix N-series by using HMP SEND_CFG command and x-modem.
>
> Software steps
> 1. Initialize communication
> 2. Enter HMP mode
> 3. Build package
> 4. Send package
> 5. Exit HMP mode

## #4_PY38_S85_RS232.py
> **Python 3.8**
> **Sensor - S85**
> Read binary byte data from S85 RS232 (External converter from RS485 to RS232) and convert to decimal. Does same as #1 but bugfixed
>
> Software steps
> 1. Read byte package (3 bytes)
> 2. Convert to binary string
> 3. Remove bits according to S85 serial com guide
> 4. Convert output bitstring to int
> 5. Print int!
