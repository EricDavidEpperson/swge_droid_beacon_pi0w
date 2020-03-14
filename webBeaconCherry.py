#!/usr/bin/python3

import bluetooth._bluetooth as bluez
import cherrypy
import os
import random
import struct
#import thread
#import time

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

return_header = \
"""
    <meta http-equiv = "refresh" content = "1; url = ./" />
"""

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

def func(cmd_pkt):
  bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Enable, dis_adv)
  bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Data, cmd_pkt)
  bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Enable, enb_adv)

class swgeBeacon(object):

  @cherrypy.expose
  def index(self):
    index_header = \
"""
    <head/>
"""
    html_body = \
"""
    <h3>SW:GE Droid BLE Beacon Generaor</h3>
    <form method="post" action="set_beacon">
      <input type="radio" name="data" id="slct1" value=data01> 01  Mrktplace/Depot<br>
      <input type="radio" name="data" id="slct2" value=data02> 02  Droids<br>
      <input type="radio" name="data" id="slct3" value=data03> 03  Resistance<br>
      <input type="radio" name="data" id="slct4" value=data04> 04  ?????<br>
      <input type="radio" name="data" id="slct5" value=data05> 05  Mrktplace/Depot<br>
      <input type="radio" name="data" id="slct6" value=data06> 06  Dok Ondar's<br>
      <input type="radio" name="data" id="slct7" value=data07> 07  First Order<br>
      <input type="radio" name="data" id="rnd_slct" checked value=data00> Random<br>
      <br>
      <input type="checkbox" name="" id="ff" value="" disabled><label for="ff"> FF <i> for future use</i>></label>
      <br><br>
      <input type="Submit" style="background-color:green">
    </form>
    <form method="post" action="disa_BLE">
      <input type="Submit" value="Disable" style="background-color:crimson">
    </form>
    Click <i> here </i> to set a timer for rotating random beacon changes <i> for future use</i>
"""
    return index_header + html_body

  @cherrypy.expose
  def set_beacon(self, data):
    if data == "data00":
      cmd_pkt = random.choice(dd)
    else: cmd_pkt = eval(data)#I know, security risk and shoud be sanitized
    func(cmd_pkt)
    html_body = "<h1>Setting Beacon</h1>"
    return return_header + html_body

  @cherrypy.expose
  def disa_BLE(self):
    bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Enable, dis_adv)
    html_body = "<h1>Disabling BLE Advertisement</h1>"
    return return_header + html_body

  @cherrypy.expose
  def set_timer(self):
    html_body = \
"""
    Note: Use the STOP button to stop the random beacon change timer. It will continue to operate until the button is pushed<br><br>
    <form method="post" action="countdown_timer">
    <label for="time">Time in minutes (1-10) </label>
    <input type="number" name="time_value" id="time" min="1" max="10" style="text-align: right;" value="5">
    <input type="Submit" style="background-color:green">
    </form>
"""
    return html_body

  @cherrypy.expose
  def countdown_timer(self, time_value):
    html_body = \
"""
    <h1> time_value goes here with a Cancel button </h1>
"""
    return html_body

if __name__ == '__main__':
  cherrypy.config.update({'server.socket_host': '0.0.0.0'})
  cherrypy.quickstart(swgeBeacon())
