def run(startup):
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
     print (red+'Welcome to PGhost Console')
     print ('Please wait...')
     sleep(3)
     os.system('clear')
     jump=yellow+'Starting in '
     os.system('clear')
     print (jump,5)
     sleep(1)
     os.system('clear')
     print (jump,4)
     sleep(1)
     os.system('clear')
     print (jump,3)
     sleep(1)
     os.system('clear')
     print (jump,2)
     sleep(1)
     os.system('clear')
     print (jump,1)
     sleep(1)
     os.system('clear')
     print (jump,0)
     sleep(1)
     print (green+'Console are Initiallized waiting system to run it....')
     sleep(3)
     os.system('clear')
     for i in range (0,50):
        print (blue+'Running PGhost console... \ ')
        sleep(0.03)
        os.system('clear')
        print (red+'Running PGhost console... | ')
        sleep(0.03)
        os.system('clear')
        print (green+'Running PGhost console... / ')
        sleep(0.03)
        os.system('clear')
        print (white+'Running PGhost console... - ')
        sleep(0.03)
        os.system('clear')

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
| Fix & repair your system problems......7   |..........|
| Exit..................................99   |__________|
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
run('')
from menumodule import stm
stm('')















