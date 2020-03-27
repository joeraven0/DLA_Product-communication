//Function 1 to be send to Function 2
var binary0 = msg.payload[0].toString(2);
var binary1 = msg.payload[1].toString(2);
var binary2 = msg.payload[2].toString(2);
var binaryString = binary0+binary1+binary2;
msg.payload = '0'+binary0+binary1+binary2;
return msg;
//--------------END----------------


//Function 2 receives output from Function 1
var c = msg.payload;
var binaryArray=[];
var i = 0;
var binaryString=0;
var binaryValue=0;
//Arrange binary string due to rules for Datalogic S85 sensor
for(var i=4;i<8;i++){
    binaryArray.push(c[i]);
}
for(var i=10;i<=15;i++){
    binaryArray.push(c[i]);
}
for(var i=18;i<=23;i++){
    binaryArray.push(c[i]);
}
//MAKE BINARY TO DECIMAL BY USING 2^i BITSHIFT RULE! (not used in this)
//Invert array values, end element to beginning
var invertbinaryArray=[];
for(var i=0;i<16;i++){
    invertbinaryArray[i]=binaryArray[15-i];
}
//Binary to decimal
for(var i=0;i<16;i=i+1){
    binaryValue += (Math.pow(2,i))*Number(invertbinaryArray[i]);
}
msg.payload  = binaryValue;
return msg;
//--------------END-----------------------
