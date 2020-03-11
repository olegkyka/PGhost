red='\033[1;91m'
blue='\033[1;94m'
green='\033[1;92m'
yellow='\033[1;93m'
blue='\033[1;94m'
white='\033[1;97m'


imenu=red+'''
----------------------------------------------__________
| Go to Payloads.........................1   |..........|
| Go to Port Scanner.....................2   |.MAIN.....|
| Go to Viruses..........................3   |..........|
| Go to msfconsole.......................4   |....MENU..|
| ifconfig...............................5   |..........|
| Update PGhost..........................6   |..........|
| Fix & repair your system problems......7   |__________|
----------------------------------------------
'''
ipayloads=yellow+'''
---------------------PAYLOADS-----------------------

Create android Payload..........................1
Create Windows Payload..........................2
Create encrypted windows Payload and AV_bypass..3
Create linux payload............................4
Create python Payload...........................5
Create PHP Payload..............................6
Create java Payload.............................7
-------------Main Menu..........................8

'''

iports=yellow+'''
-----------------------PORT--SCANNER----------------

Automatically Scan IP Ports....................1
Manually Scan IP Ports.........................2
Get service by port............................3
Show IP of any HOST............................4
-------------Main Menu.........................5
'''
iviruses=yellow+'''
Create Python virus |ACTION:--> Crash System.......................1
Create Python virus |ACTION:--> Delete all files...................2
Create Python virus |ACTION:--> Delete all files and Crash System..3
-------------Main Menu.............................................4


'''
ifixes=yellow+'''
Fix Updates Problems:--> cannot update kali linux.....1
Fix Install Problem :--> Unable to locate packages....2
Update to the lasted version of Kali linux............3
-------------Main Menu................................4
'''

def stm(console):
    red='\033[1;91m'
    blue='\033[1;94m'
    green='\033[1;92m'
    yellow='\033[1;93m'
    blue='\033[1;94m'
    white='\033[1;97m'
    import os
    import socket
    import subprocess
    from time import sleep
    os.system('clear')
    print (imenu)
    print (green+'Menu|---choose : ')
    num1=input()
    num=int(num1)
    if num==1:
      os.system('clear')
      print (ipayloads)
      from Pghost_modules import Payloads
      Payloads('')
    elif num==2:
      os.system('clear')
      print (iports)
      from Pghost_modules import portscanner
      portscanner('')
    elif num==3:
      os.system('clear')
      print (iviruses)
      from Pghost_modules import viruses
      viruses('')
    elif num==4:
      os.system('msfconsole')
    elif num==5:
      os.system('ifconfig')
    elif num==6:
      os.system('clear')
      q=input ('Do you want to update PGhost? [Y/n] ')
      if q=='y':
         print ('Checking for updates........')
         os.system('cd ..&& rm -r PGhost')
         os.system('git clone https://www.github.com/Mahmoud7Osman/PGhost.git')
         os.system('clear')
         print ('Please restart PGconsole')
         print (blue+'Updated. Press Enter to exit ')
         input()
      else:
         print ('Aborting...')
    elif num==7:
      os.system('clear')
      print (ifixes)
      from Pghost_modules import fixes
      fixes('')
    elif num==99:
      print ('shutting down PGhost__console....')
      sleep(1)
      print ('\033[0;97m')
      os.system('clear')
      exit()
    else:
      print (red+'Number not found error',num)
      sleep(1)
      return stm(console)
############################

