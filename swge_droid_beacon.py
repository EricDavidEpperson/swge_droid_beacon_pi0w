import os
import random
import time

def beacon_function():
    payload = ['01', '02', '03', '04', '05', '06', '07']
    os.system("sudo hciconfig hci0 noleadv")
    os.system("sudo hcitool -i hci0 cmd 0x08 0x0008 0C 02 01 1A 10 FF 83 01 0A 04 " + random.choice(payload) + " 02 A6 01")
    os.system("sudo hciconfig hci0 leadv 3")    

def rnd_delay():
     delay = random.randrange (60, 300)
     time.sleep(delay)

while True:
    beacon_function()
    rnd_delay()

