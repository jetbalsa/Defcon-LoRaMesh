THIS FILE IS IN PROGRESS
##

Using a RFM95, RA-01. or RA-02 LoRA <strong>900Mhz Radio</strong>

You MUST use a 900Mhz radio in the USA, 433Mhz LoRa is not allowed!

If you use 433Mhz LoRa, All the Ham Radio nerds will hunt you down and shoot you :P

The basics is to broadcast a message out of the status display or some message. For HatChan I plan on broadcasting latest posts, GPS Coords, GPS Time, 

For things like the guy who does the Wifi APs, you can publish a list of APs currently.

I'm working on the protocol now once I get my radios in (7/16/2019)


So, I'm thinking something like

CALLSIGN|MSGTYPE|MSGID|MSGLEN|MESSAGE

Lengths

8|2|4|4|65535

thats 8 Letters max for Callsign, One int for msgtype, a unsigned int in unprefixed hex for msgid and msglen(so its max size is FFFF, loop once overflow) then message is 65535 ASCII letters long.

Example Message
Type 1 Messages are Replace, Ment for status panels and things

HATCHAN|01|64|A8|HatChan - The Hat Mounted Image Board\r\nGPS Lat:-77.123 Lon:34.2993\r\nGPS Time:1563195409\r\nLatest Posts:\r\n* Posting for Hatchan for the first....\r\n* First Post!

For Chat Messages, Use Proto 2 (ment for a appended log of messages)

JRWR|02|64|35|Cool Story Bro, I hope it works out

====================================

RADIO SETTINGS

915Mhz SF7 (Using the RadioHead Libs)
