#!/usr/bin/python3

import bluetooth._bluetooth as bluez
import os
import random
import signal
import struct
import sys
import time

pid = os.getpid()
time_value = sys.argv[1]

def pid_check():
  fileXst = os.path.isfile('/var/swgedbr.pid')
  if fileXst == False:
    f = open("/var/swgedbr.pid", "w+")
    f.write(str(pid))
    f.close()
  else:
    pass
  g = open("/var/swgedbr.pid", "r+")
  h = g.read()
  if h == str(pid):
    g.close()
    return
  else:#supposed to handle if a new swgebr.py x>0 command comes in. Script crashes bc somehow .pid gets written with binary @^(\x00) values in front of the pid str
#Also fails if previous swgebr.py process was not shut down properly. Manually remove /var/swgedbr.pid and try again "sudo rm -f /var/swgebr.pid"
    os.kill(int(h), signal.SIGTERM)
    g.truncate(0)
    g.write(str(pid))
    g.close()

def beacon():
  OGF_LE_CTL=0x08
  OCF_HCI_LE_Set_Advertising_Data=0x0008
  OCF_HCI_LE_Set_Advertising_Enable=0x000A
  dis_adv=struct.pack("<B", 0x00)
  enb_adv=struct.pack("<B", 0x01)
  data01=struct.pack("<BBBBBBBBBBBBBB", 0x0D, 0x02, 0x01, 0x06, 0x09, 0xFF, 0x83, 0x01, 0x0A, 0x04, 0x01, 0x02, 0xA6, 0x01)
  data02=struct.pack("<BBBBBBBBBBBBBB", 0x0D, 0x02, 0x01, 0x06, 0x09, 0xFF, 0x83, 0x01, 0x0A, 0x04, 0x02, 0x02, 0xA6, 0x01)
  data03=struct.pack("<BBBBBBBBBBBBBB", 0x0D, 0x02, 0x01, 0x06, 0x09, 0xFF, 0x83, 0x01, 0x0A, 0x04, 0x03, 0x02, 0xA6, 0x01)
  data04=struct.pack("<BBBBBBBBBBBBBB", 0x0D, 0x02, 0x01, 0x06, 0x09, 0xFF, 0x83, 0x01, 0x0A, 0x04, 0x04, 0x02, 0xA6, 0x01)
  data05=struct.pack("<BBBBBBBBBBBBBB", 0x0D, 0x02, 0x01, 0x06, 0x09, 0xFF, 0x83, 0x01, 0x0A, 0x04, 0x05, 0x02, 0xA6, 0x01)
  data06=struct.pack("<BBBBBBBBBBBBBB", 0x0D, 0x02, 0x01, 0x06, 0x09, 0xFF, 0x83, 0x01, 0x0A, 0x04, 0x06, 0x02, 0xA6, 0x01)
  data07=struct.pack("<BBBBBBBBBBBBBB", 0x0D, 0x02, 0x01, 0x06, 0x09, 0xFF, 0x83, 0x01, 0x0A, 0x04, 0x07, 0x02, 0xA6, 0x01)
  dd = [data01, data02, data03, data04, data05, data06, data07]
  sock = bluez.hci_open_dev(0)
  cmd_pkt = random.choice(dd)
  bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Enable, dis_adv)
  bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Data, cmd_pkt)
  bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Enable, enb_adv)

def timer(time_value):
  time_seconds = int(time_value)*60
  start_time = time.time()
  while time_seconds > 0:
    time.sleep(1)
    current_time = time.time()
    elapsed_time = current_time - start_time
    if time_seconds > elapsed_time:
      continue
    else:
      main(time_value)

def main(time_value):
  if int(time_value) > 0:
    pid_check()
    beacon()
    timer(time_value)
  else:
    f = open("/var/swgedbr.pid")
    g = f.read()
    f.close()
    os.kill(int(g), signal.SIGTERM)#Script fails if previous swgebr.py process was not shut down properly. Manually remove /var/swgedbr.pid and try again "sudo rm -f /var/swgebr.pid"
    os.remove("/var/swgedbr.pid")
    OGF_LE_CTL=0x08
    OCF_HCI_LE_Set_Advertising_Enable=0x000A
    dis_adv=struct.pack("<B", 0x00)
    sock = bluez.hci_open_dev(0)
    bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Enable, dis_adv)
    
if __name__ == '__main__':
  main(time_value)
