
import os
import getpass
import time 
import sys
import hashlib
try:
 from tqdm import tqdm
except:
 os.system('pip install tqdm')
finally:
 from tqdm import tqdm


def jsprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5./100)
                     

os.system('clear')
print('''
\033[1;34m
 ____            _                     _               _            _ _
/ ___| _   _ ___| |_ ___ _ __ ___     | |    ___   ___| | _____  __| | |
\___ \| | | / __| __/ _ \ '_ ` _ \    | |   / _ \ / __| |/ / _ \/ _` | |
 ___) | |_| \__ \ ||  __/ | | | | |   | |__| (_) | (__|   <  __/ (_| |_|
|____/ \__, |___/\__\___|_| |_| |_|___|_____\___/ \___|_|\_\___|\__,_(_)
       |___/                     |_____|




''')

us = open('user.rock','r').readline()
ps = open('passw.rock','r').readline()
us = us
ps = ps


user = us
password = ps


while True:
 try:
   try:
    print('\033[1;32m')
    inpusr = input('UserName: ')
    inppsw = getpass.getpass(prompt='Password: ')
   except: 
    print('\033[1;32m')
    inpusr = input('UserName: ')
    inppsw = getpass.getpass(prompt='Password: ')
   if inpusr == user and inppsw == password:
    print()
    print('\033[1;31m')
    jsprint('Identity Confirmed!!Please wait a sec ...')
    print()
    print('\033[1;35m')
    for i in tqdm(range(0,100)):
     time.sleep(0.01)
    print('\033[1;37m')
    print()
    os.system('clear')
    break
   else:
    continue
 except:
  os.system('exit') 



