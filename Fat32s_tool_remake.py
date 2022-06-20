import imp
import subprocess
from turtle import setx
import webbrowser
import os,sys
from matplotlib.colors import get_named_colors_mapping
from termcolor import colored as cl
from colorama import init

init()

print(cl("Welcome to FAT32S Tool Remake","yellow")) # Welcome message to the user and instructions on how to use the tool and how to exit the program if the user wishes to. The user can also view the source code of the tool if they wish.
print(cl("This tool is designed to help you. with the following tasks:","yellow")) # This is the intro to the tool and what it can do. It is also a list of what the tool can do. 
print(cl("It will help you to create a FAT32S file.","yellow"))
print(cl("this tool is made by:","yellow")) # This is the name of the author of the tool. It is also a list of the author's name.  
print(cl("-Sebastian","yellow")) # This is the name of the author of the tool. It is also a list of the author's ni-name. 
print(cl("-Create a FAT32S file","yellow"))  # siril siklar pe                          SA                                 TÜRRRRRRRRRRRRKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK

while True:
  get_input = input("command: ")
  if get_input == "browser":
      webbrowser.open_new_tab("https://search.brave.com/")
  elif get_input == "cmd":
      os.system("start")
  elif get_input == "notepad":
       os.system("notepad")
  elif get_input == "dxdiag":
      os.system("dxdiag")
  elif get_input == "regedit":
      os.system("regedit")
  elif get_input == "explorer":
      os.system("explorer")
  elif get_input == "eudcedit":
      os.system("eudcedit")
  elif get_input == "msinfo32":
      os.system("msinfo32")
  elif get_input == "eventvwr":
      os.system("eventvwr")
  elif get_input == "charmap":
      os.system("charmap")
  elif get_input == "colorcpl":
      os.system("colorcpl")
  elif get_input == "taskschd":
      os.system("taskschd")
  elif get_input == "taskmgr":
      os.system("taskmgr")
  elif get_input == "sndvol":
      os.system("sndvol")
  elif get_input == "Color Management":
      os.system("colorcpl")
  elif get_input == "ColorMan":
      os.system("colorcpl")
  elif get_input == "TaskMan":
      os.system("taskmgr")
  elif get_input == "Volume Mixer":
      os.system("sndvol")
  elif get_input == "rstrui":
      os.system("rstrui")
  elif get_input == "psr":
      os.system("psr")
  elif get_input == "certlm":
      os.system("certlm")
  elif get_input == "certmgr":
      os.system("certmgr")
  elif get_input == "cliconfg":
      os.system("cliconfg")
  elif get_input == "comexp":
      os.system("comexp")
  elif get_input == "compmgmt":
      os.system("compmgmt")
  elif get_input == "credwiz":
      os.system("credwiz")
  elif get_input == "cttune":
      os.system("cttune")
  elif get_input == "dialer":
      os.system("dialer")
  elif get_input == "dvdplay":
      os.system("dvdplay")
  elif get_input == "fsmgmt":
      os.system("fsmgmt")
  elif get_input == "fsquirt":
      os.system("fsquirt")
  elif get_input == "hdwwiz":
      os.system("hdwwiz")
  elif get_input == "iscsicpl":
      os.system("iscsicpl")
  elif get_input == "mobsync":
      os.system("mobsync")
  elif get_input == "msdt":
      os.system("msdt")


  elif get_input == "U2X -download -7zip -2107 -win -x64":
     webbrowser.open_new_tab("https://www.7-zip.org/a/7z2107-x64.exe")
  elif get_input == "osk":
      os.system("osk")
  elif get_input == "U2X -download -steam -all":
      webbrowser.open_new_tab("https://store.steampowered.com/about/")
  elif get_input == "netplwiz":
      os.system("netplwiz")
  elif get_input == "msconfig":
      os.system("msconfig")
  elif get_input == "magnify":
      os.system("magnify")
  elif get_input == "filehistory":
      os.system("filehistory")
  elif get_input == "eventvwr":
      os.system("eventvwr")
  elif get_input == "dpiscaling":
      os.system("dpiscaling")
  elif get_input == "diskmgmt":
      os.system("diskmgmt")
  elif get_input == "dccw":
      os.system("dccw")
  elif get_input == "control":
      os.system("control")
  elif get_input == "cleanmgr":
      os.system("cleanmgr")
  elif get_input == "certmgr":
      os.system("certmgr")
  elif get_input == "calc":
      os.system("calc")
  elif get_input == "tpm":
      os.system("tpm")
  elif get_input == "msra":
      os.system("msra")
  elif get_input == "nslookup":
      os.system("nslookup")
  elif get_input == "perfmon":
      os.system("perfmon")
  elif get_input == "quickassist":
      os.system("quickassist")
  elif get_input == "services":
      os.system("services")
  elif get_input == "changepk":
      os.system("changepk")
  elif get_input == "conhost":
    os.system("conhost")
  elif get_input == "dfrgui":
    os.system("dfrgui")
  elif get_input == "dpiscaling":
    os.system("DpiScaling")
  elif get_input == "filehistory":
    os.system("FileHistory")
  elif get_input == "fxscover":
    os.system("FXSCOVER")
  elif get_input == "gpedit":
    os.system("gpedit")
  elif get_input == "workfolders":
    os.system("WorkFolders")
  elif get_input == "write":
    os.system("write")
  elif get_input == "wf":
    os.system("WF")
  elif get_input == "powershell":
    os.system("powershell")
  elif get_input == "certreq":
    os.system("certreq")
  elif get_input == "ipksetup":
    os.system("lpksetup")
  elif get_input == "calculator":
    os.system("calc")
  elif get_input == "fondue":
    os.system("Fondue")
  elif get_input == "cmstp":
    os.system("cmstp")
  elif get_input == "bdechangepin":
    os.system("bdechangepin")
  elif get_input == "displayswitch":
    os.system("DisplaySwitch")
  elif get_input == "dpapimig":
    os.system("dpapimig")
  elif get_input == "esentutl":
    os.system("esentutl")
  elif get_input == "fodhelper":
    os.system("fodhelper")
  elif get_input == "useraccountcontrolsettings":
    os.system("UserAccountControlSettings")
  elif get_input == "verifiergui":
    os.system("verifiergui")
  elif get_input == "wfs":
    os.system("WFS")
  elif get_input =="wiaacmgr":
    os.system("wiaacmgr")
  elif get_input == "winver":
    os.system("winver")
  elif get_input == "wscollect":
    os.system("WSCollect")
  elif get_input == "wscript":
    os.system("wscript")
  elif get_input == "wsreset":
    os.system("WSReset")
  elif get_input == "wusa":
    os.system("wusa")
  elif get_input == "vulkaninfo":
    os.system("vulkaninfo")
  elif get_input == "utilman":
    os.system("Utilman")
  elif get_input == "userinit":
    os.system("userinit")
  elif get_input == "tpmtool":
    os.system("TpmTool")
  elif get_input == "tpminit":
    os.system("TpmInit")
  elif get_input == "tabcal":
    os.system("tabcal")
  elif get_input == "systempropertiesadvanced":
    os.system("SystemPropertiesAdvanced")
  elif get_input == "systempropertiescomputername":
    os.system("SystemPropertiesComputerName")
  elif get_input == "systempropertiesdataexecutionprevention":
    os.system("SystemPropertiesDataExecutionPrevention")
  elif get_input == "systempropertieshardware":
    os.system("SystemPropertiesHardware")
  elif get_input == "systempropertiesperformance":
    os.system("SystemPropertiesPerformance")
  elif get_input == "systempropertiesprotection":
    os.system("SystemPropertiesProtection")
  elif get_input == "systempropertiesremote":
    os.system("SystemPropertiesRemote")
  elif get_input == "systeminfo":
    os.system("systeminfo")
  elif get_input == "slui":
    os.system("slui")
  elif get_input == "sigverif":
    os.system("sigverif")
  elif get_input == "shrpubw":
    os.system("shrpubw")
  elif get_input == "mblctr":
    os.system("mblctr")
  elif get_input == "iexpress":
    os.system("iexpress")
  elif get_input == "devicepairingwizard":
    os.system("DevicePairingWizard")
  else:
     print("not found")
