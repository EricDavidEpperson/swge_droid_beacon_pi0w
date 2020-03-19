# swge_droid_beacon_pi0w
Project to create a BLE beacon to interact with SW:GE Droid using Raspberry Pi Zero W and python

Based on work done by Ruthsarian, Spork|Dead Bothans, Cowkitty|Dead Bothans, Vince Parker, holapenguin, YohanUM, and others at the Disney Star Wars Galaxy's Edge #makers discord.

The droids built in SWGE Droid Depot at Disney Land and Disney World Hollywood Studios respond randomly to BLE beacons placed thourghout the park's land.
There has already been work to recreate this with Micro:bit SBC's. I have a spare Raspberry Pi Zero W, which is capable of BLE advertising, so I decided to use it and some python to make our droid do the same at home (or anywhere I take the Pi). I have also tested it using a Raspberry Pi 4.

I have decided to change directions for UI/management and am adding a Web UI utilizing CherryPy. The first version only allows for selecting beacon 01-07, but I do plan to add more functionality shortly. The scripts I am posting here are also meant to run with Python3 since 2 has been EoL'd. 

To get the latest version of this to work, it is necessary to install PyBLuez and CherryPy. To do this, run the following commands:

  > sudo apt-get install bluetooth libbluetooth-dev
  
  > sudo pip3 install pybluez cherrypy

The web server is configured to listen on port 8080. To access the web page you can point a web browser at the IP address or hostname of the Raspberry Pi, similar to the following examples:

  http://raspberrypi:8080
or
  http://192.168.0.xxx:8080
  
  I'll leave it to you to find what the hostname or IP address of your Pi is. Google is your friend ;D
  
Testing revealed that threading (or using cherrypy.process.plugins.BackgroundTask) would cause the application to freeze and need to stop the full python task to stop. Work will continue on this feature and I willl update further when available.
