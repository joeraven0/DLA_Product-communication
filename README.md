# DLA_Finished

## #1_Node-Red_S85-binary.json
> **Node-Red**
>
> Full Node-Red script for collecting and sorting data from S85-sensor over RS232 (dongle converter from RS485). Uses Node-Red Dashboard.

## #1_Node-Red_S85_binaryFunction.js
> **Javascript**
>
> Javascript function file - Same code as running inside function block in .json above.

## #2_PY38_tcp2ascii_char_client.py
> **Python 3.8**
>
> Reads hex over TCP and prints non readable chars from standard ASCII-table, i.e. \<STX\>\<CR\>. No need to use HyperTerminal or other old RS232 softwares anymore!

## #3_PY27_SendCFG_N-Series
> **Python 2.7**
>
> Send config file to Matrix N-series by using HMP SEND_CFG command and x-modem.
>
> Procedure
> 1. Initialize communication
> 2. Enter HMP mode
> 3. Build package
> 4. Send package
> 5. Exit HMP mode
