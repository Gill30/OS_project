
#connected=0
import socket               
from thread import *

#connected_user =[0,0,0,0,0,0,0,0,0,0]

s = socket.socket()         
host = socket.gethostname()
port = 8887                
s.connect((host, port))

x=s.recv(29)

print x
x=s.recv(2)


onlin_user=int(x)



for index in range(onlin_user):
     x=s.recv(15)
     print x


x=raw_input("enter your name : ")
s.send(x)

def func(s):
	while 1:
		x=s.recv(1024)
                print x
               

start_new_thread(func,(s,))

def enter_user(s):
   other_person=raw_input('Enter no of person to  chat with: ')
   s.send('!New chat')
   print '   '
   s.send(str(other_person))
 


#enter_user(s)


while 1:
	x=raw_input()
         
	if x=='Q' or  x=='q':
		break
	elif x=='N' or x=='n':
                enter_user(s)
        else :
		s.send(x)
s.close()             
