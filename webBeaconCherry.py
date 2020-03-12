#!/usr/bin/python3

import bluetooth._bluetooth as bluez
import struct
import os
import cherrypy

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

html_header = \
"""
<meta http-equiv = "refresh" content = "1; url = ./" />
"""
class swgeBeacon(object):

  @cherrypy.expose
  def index(self):
    html_body = \
"""
    <form method="post" action="web_input">
      <input type="radio" name="data" id="slct1" value=data01>01<br>
      <input type="radio" name="data" id="slct2" value=data02>02<br>
      <input type="radio" name="data" id="slct3" value=data03>03<br>
      <input type="radio" name="data" id="slct4" value=data04>04<br>
      <input type="radio" name="data" id="slct5" value=data05>05<br>
      <input type="radio" name="data" id="slct6" value=data06>06<br>
      <input type="radio" name="data" id="slct7" value=data7>07<br><br>
      <input type="Submit">
    </form>
"""
    return html_body

  @cherrypy.expose
  def web_input(self, data):
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
    cmd_pkt = eval(data)
    sock = bluez.hci_open_dev(0)
    bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Enable, dis_adv)
    bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Data, cmd_pkt)
    bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Enable, enb_adv)
    html_body = "<h1>Setting Beacon</h1>"
    return html_header + html_body

if __name__ == '__main__':
  cherrypy.config.update({'server.socket_host': '0.0.0.0'})
  cherrypy.quickstart(swgeBeacon())