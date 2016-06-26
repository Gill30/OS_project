import socket
import sys

j=0
conn=[0,0,0,0,0,0,0,0,0,0]

list0=[];
list1=[];
list2=[];
list3=[];
list4=[];
list5=[];
list6=[];
list7=[];
list8=[];
list9=[];
connected_user=[list0,list1,list2,list3,list4,list5, list6, list7,list8,list9]

name =['','','','','','','','','','']
user_data=['','','','','','','','','','']

from thread import * 
HOST = ''
PORT = 8887
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((HOST, PORT))
except socket.error as msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()     
s.listen(10)
print 'Socket now listening'

#Server established
 
                


def newperson(c):
   
    user=0
    while 1:
       
      data=conn[c].recv(124)
     
      if data =='!New chat':
        
         user=int(conn[c].recv(4))
        
         if user<i and (user not in connected_user): 
             
                 #connected[c]=connected[c]+1
                 connected_user[c].append(user)
                 connected_user[user].append(c)
                 conn[user].send('You are connected with '+str(c))

      elif len(connected_user[c])>0:
      
         k=len(connected_user[c])-1   
         while k >=0:
            conn[connected_user[c][k]].send(user_data[c]+' said =  \"  '+data+' \"')
            k=k-1
         

i=0
while 1:
        conn[i], add = s.accept()
        j=j+1
        
        conn[i].send('***Welcome to the server*** \n')
        conn[i].send(str(i))
        
        for index in range(i):
            
            conn[i].send('\n'+str(index)+'    : '+name[index])
        

       
        name[i]=conn[i].recv(1024)
        
        
        user_data[i]='\n\n'+str(i)+'    : '+name[i]
        
        for index in range(i):
               conn[index].send(user_data[i])

      
        print 'Connected with ' + str(add[0]) + ':' + str(add[1])
        start_new_thread(newperson ,(i,))
        i=i+1 
s.close()
