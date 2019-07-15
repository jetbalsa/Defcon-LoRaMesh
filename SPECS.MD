THIS FILE IS IN PROGRESS
##

Using a RFM95, RA-01. or RA-02 LoRA 900Mhz Radio

The basics is to broadcast a message out of the status display or some message. For HatChan I plan on broadcasting latest posts, GPS Coords, GPS Time, 

For things like the guy who does the Wifi APs, you can publish a list of APs currently.

I'm working on the protocol now once I get my radios in (7/16/2019)


So, I'm thinking something like

CALLSIGN|PROTOVERSION|MSGID|MSGLEN||MESSAGE

Lengths

8|1|5|5|65535

thats 8 Letters max for Callsign, One int for proto, a unsigned int for msgid and msglen(so its max size is 65535, loop once overflow) then message is 65535 ASCII letters long.


Trasmitted every min time of once a minute, use Wait for TX (To make sure line is clear) Store Messages as you see fit, no store and forward.


Example Message


HATCHAN|1|00001|00168|HatChan - The Hat Mounted Image Board\r\nGPS Lat:-77.123 Lon:34.2993\r\nGPS Time:1563195409\r\nLatest Posts:\r\n* Posting for Hatchan for the first....\r\n* First Post!
