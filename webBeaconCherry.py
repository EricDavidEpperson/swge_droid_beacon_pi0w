#!/usr/bin/python3

import bluetooth._bluetooth as bluez
import cherrypy
import os
import random
import struct
import subprocess
import time

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

def func(cmd_pkt):
  sock = bluez.hci_open_dev(0)
  bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Enable, dis_adv)
  bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Data, cmd_pkt)
  bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Enable, enb_adv)

class swgeBeacon(object):

  @cherrypy.expose
  def index(self):
    html = \
"""
<head><script src="https://code.jquery.com/jquery-3.4.1.min.js"></script></head>
<body>
  <h3>SW:GE Droid BLE Beacon Generaor</h3>
  <form method="post" action="set_beacon">
    <input type="radio" name="data" id="slct1" value=data01> 01  Mrktplace/Depot<br>
    <input type="radio" name="data" id="slct2" value=data02> 02  Droids<br>
    <input type="radio" name="data" id="slct3" value=data03> 03  Resistance<br>
    <input type="radio" name="data" id="slct4" value=data04> 04  ?????<br>
    <input type="radio" name="data" id="slct5" value=data05> 05  Mrktplace/Depot<br>
    <input type="radio" name="data" id="slct6" value=data06> 06  Dok Ondar's<br>
    <input type="radio" name="data" id="slct7" value=data07> 07  First Order<br>
    <input type="radio" name="data" id="slctRnd" checked value=data00> Random<br>
    <br>
    <input type="Submit" value="Submit" style="background-color:green">
  </form>
  <form method="post" action="disa_BLE">
    <input type="Submit" value="Disable" style="background-color:crimson">
  </form>
  <form method="post" action="timed_rnd_beacon" id="StartFrm">
    <input type="radio" id="slctTmr">
    <label for="time_slct">Time in minutes (1-10) </label>
    <input type="number" name="time_value" id="time_slct" min="1" max="10" style="text-align: right;" disabled value="5">
    <input type="Submit" value="Start" style="background-color:green" disabled>
  </form>
  <form method="post" action="timed_rnd_beacon" id="StopFrm">
    <input type="hidden" name="time_value" id="time_stop" value="0">
    <input type="Submit" value="Stop" style="background-color:crimson" id="StopBtn" disabled>
  </form>
<script>
$('#slctTmr').click(function()
{
  $('#time_slct').prop("disabled", false);
  $("input:Submit[value=Start]").prop("disabled", false);
  $("input:radio[name=data]").prop("checked", false);
  $("input:Submit[value=Submit]").prop("disabled", true);
  $("input:Submit[value=Disable]").prop("disabled", true);
});

$("input:radio[name=data]").click(function()
{
  $('#slctTmr').prop("checked", false);
  $('#time_slct').prop("disabled", true);
  $("input:Submit[value=Start]").prop("disabled", true);
  $("input:Submit[value=Submit]").prop("disabled", false);
  $("input:Submit[value=Disable]").prop("disabled", false);
});

$("input:Submit[value=Start]").click(function()
{
  $('#StartFrm').submit();
  $('#StopBtn').prop("disabled", false);
  $(":input").not('#StopBtn').prop("disabled", true);
});

$('#StopBtn').click(function()
{
  $('#time_stop').prop("disabled", false);
  $('#StopFrm').submit();
  $('#StopBtn').prop("disabled", true);
  $("input:Submit[value=Start]").prop("disabled", false);
  $('#time_slct').prop("disabled", false);
  $("input:Radio[name=data]").prop("disabled", false);
  $('#slctTmr').prop("disabled", false);
});
</script>
</body>
"""
    return html

  @cherrypy.expose
  def set_beacon(self, data):
    if data == "data00":
      cmd_pkt = random.choice(dd)
    else: cmd_pkt = eval(data)#I know, security risk and shoud be sanitized
    func(cmd_pkt)
    html = "<h1>Setting Beacon</h1>"
    return return_header + html

  @cherrypy.expose
  def disa_BLE(self):
    sock = bluez.hci_open_dev(0)
    bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_HCI_LE_Set_Advertising_Enable, dis_adv)
    html = "<h1>Disabling BLE Advertisement</h1>"
    return return_header + html

  @cherrypy.expose
  def timed_rnd_beacon(self, time_value):
    cherrypy.response.status = 204
    subprocess.Popen(["sudo", "/opt/swgedbr.py", time_value])

if __name__ == '__main__':
  cherrypy.config.update({'server.socket_host': '0.0.0.0'})
  cherrypy.quickstart(swgeBeacon())
