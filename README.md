# swge_droid_beacon_pi0w
Project to create a BLE beacon to interact with SW:GE Droid using Raspberry Pi Zero W and python

Based on work done by Ruthsarian, Spork|Dead Bothans, Cowkitty|Dead Bothans, Vince Parker, holapenguin, YohanUM, and others at the Disney Star Wars Galaxy's Edge #makerspace discord.

The droids built in SWGE Droid Depot at Disney Land and Disney World Hollywood Studios respond randomly to BLE beacons placed thourghout the park's land.

There has already been work to recreate this with Micro:bit SBC's. I have a spare Raspberry Pi Zero W, which is capable of BLE advertising, so I decided to use it and some python to make our droid do the same at home (or anywhere I take the Pi). I have also tested it using a Raspberry Pi 4.

It is necessary to install PyBLuez and CherryPy. To do this, run the following commands:

  > sudo apt-get install bluetooth libbluetooth-dev
  
  > sudo pip3 install pybluez cherrypy

Management is done through a web page served by CherryPy. I would recommend to copy webBeaconCherry.py and swgedbr.py to your /opt directory. You can start the webserver with the following command:

  sudo webBeaconCherry.py &

The web server is configured to listen on port 8080. To access the web page you can point a web browser at the IP address or hostname of the Raspberry Pi, similar to the following examples:

  http://raspberrypi:8080
or
  http://192.168.0.xxx:8080
  
I'll leave it to you to find what the hostname or IP address of your Pi is. Google is your friend ;D
  
If you decide to name the files differently or place them in different location, keep in mind that /opt/swgedbr.py is hardcoded on line 133 of webBeaconCherry.py and will need to be updated. The swgedbr.py file can be used from the command line; usage is:

  sudo swgedbr.py {0|X} &

X is minutes you want to the beacon to run before changing to a different randomly selected beacon. Use 0 to stop the beacon. You can't run the command with X > 0 consecutively. This causes errors that I am still tryign to resolve. You'll need to run it with 0 before changing to a new timer value. Sometimes running the command with 0 also throws errors, but they can be ignored since those happen when no beacon is running. If there are any issues starting the beacon, go to /var and delete swgedbr.pid and try it again.

Using the web UI minimizes these issues since buttons are disabled depending upon choices, but once you hit the "Start" button, it's not advised to reload or use the back button. Most issues can be resolved by running "sudo /opt/swgedbr.py" and/or removing /var/swgedbr.py
