

import os
import time
try:
 from tqdm import tqdm
except:
 os.system('pip install tqdm')
finally:
 from tqdm import tqdm


ifcookie = os.path.isfile('cookie.rock')

def reg(inpuser,inppassw):           
 u = open('user.rock','w')
 u.write(inpuser)
 u.close()
 p = open('passw.rock','w')
 p.write(inppassw)
 p.close()

os.system('pkg install figlet')
os.system('pkg install nano')
os.system('clear')


def clogo():
 print('''
\033[1;35m
 #####                                #
#     # ###### ##### #    # #####     #        ####   ####  #    #
#       #        #   #    # #    #    #       #    # #    # #   #
 #####  #####    #   #    # #    #    #       #    # #      ####
      # #        #   #    # #####     #       #    # #      #  #
#     # #        #   #    # #         #       #    # #    # #   #
 #####  ######   #    ####  #         #######  ####   ####  #    #

-------------------------------------------------------------------
                [ ] A ADVANCE TERMUX LOCKER  [ ]
                  [] CODED BY SHOAIB ISLAM []
                  ...........................
          [ [  shoaibmadeinbangladesh@gmail.com  ] ]
       [ [  https://www.github.com/thegteatestshoaib ] ]
        [ [  https://www.facebook.com/The.Et3rnity  ] ]
_____________________________________________________________________


''')

def call():
 os.system('clear')
 clogo()
 print('\033[1;31m [+]What do you want to do?[+]')
 print('\033[1;32m')
 print('[1]Change Password')
 print('[2]Change Theme')
 print()
 print()
 chose = input('Enter A Option: ')
 chose = int(chose)
 print()
 print()
 if chose == 1:
  Newuser = input('ENTER NEW USERNAME: ')
  Newpass = input('ENTER NEW PASSWORD :')
  u = open('user.rock','w')
  u.write(Newuser)
  u.close()
  p = open('passw.rock','w')
  p.write(Newpass)
  p.close()
  print()
  print('YOUR NEW USERNAME IS {} AND PASSWORD IS {}'.format(Newuser,Newpass))        
 else:
  print('\033[1;32m')
  print()
  sss = input('ENTER WHAT DO YOU WANT TO FIGLET: ')
  rock = open('locker.py','a')
  rock.write('\nos.system("clear  && figlet {}")'.format(sss))
                                                                                
  print('done')
if ifcookie:
 call()
else:
 os.system('clear')
 clogo()
 print('\033[1;32m')
 print('ENTER VALID INFORMATION FOR REGISTER:')
 print()
 print()
 user = input('Set Username: ')
 pssw = input('Set Password: ')
 print()
 reg(user,pssw)
 print('YOUR USER NAME IS {} AND PASSWORD IS {}'.format(user,pssw))
 os.mknod('cookie.rock')                                 
 n = open('/data/data/com.termux/files/usr/etc/bash.bashrc','a')
 n.write('\ncd Locker && python locker.py')
 n.write('\ncd ..')          
 n.close()
 print()
 print('SYSTEM INITIALIZING')
 print()
 for i in tqdm(range(0,100)):
  time.sleep(0.03)
 print('Done')




print('\033[1;37m')
