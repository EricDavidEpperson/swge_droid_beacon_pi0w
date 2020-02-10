# swge_droid_beacon_pi0w
Project to create a BLE beacon to interact with SW:GE Droid using Raspberry Pi Zero W and python

***Update as of February 2020. While working to make this proof of concept code into a proper program with validations and options, I discovered that Python is "supposed to" have their sockets() method work with Bluetooth BLE. In practice there are problematic functions that do not work as advertised in the inadequate documentation of this family.

I'm attempting to test after buildning Python 3.8 on the Pi Zero since there are some Bug reports that might be related that appear to have been addressed. At this point it would be recommended to anyone interested in using a Raspberry Pi with Python as a SWGE Beacon to use Pybluez.***

Based on work done by Ruthsarian, Spork|Dead Bothans, Cowkitty|Dead Bothans, Vince Parker, holapenguin, and others at the Disney Star Wars Galaxy's Edge #makers discord.
The droids built in SWGE Droid Depot at Disney Land and Disney World Hollywood Studios respond randomly to BLE beacons placed thourghout the park's land.
There has already been work to recreate this with Micro:bit SBC's.
I have a spare Raspberry Pi Zero W, which is capable of BLE advertising, so I decided to use it and some python to make our droid do the same at home (or anywhere I take the Pi).

Right now, for testing purposes, this is just a Proof of concept Python script that generates a BLE beacon signal and changes it at random intervals between 2-5 minutes.

Eventually it should:
- detect if SWGE droids are in range 
- determine the presence and type of personality chip
- and broadcast appropriately

The end goal is to create a Raspian image that will allow simple plug and play with a Raspberry Pi Zero W.
