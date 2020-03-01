# swge_droid_beacon_pi0w
Project to create a BLE beacon to interact with SW:GE Droid using Raspberry Pi Zero W and python

Based on work done by Ruthsarian, Spork|Dead Bothans, Cowkitty|Dead Bothans, Vince Parker, holapenguin, YohanUM, and others at the Disney Star Wars Galaxy's Edge #makers discord.

The droids built in SWGE Droid Depot at Disney Land and Disney World Hollywood Studios respond randomly to BLE beacons placed thourghout the park's land.
There has already been work to recreate this with Micro:bit SBC's. I have a spare Raspberry Pi Zero W, which is capable of BLE advertising, so I decided to use it and some python to make our droid do the same at home (or anywhere I take the Pi). I have also tested it using a Raspberry Pi 4.

To get the latest version of this to work, it is necessary to install PyBLuez. To do this, run the following commands:

  > sudo apt-get install bluetooth libbluetooth-dev
  
  > sudo pip install pybluez
