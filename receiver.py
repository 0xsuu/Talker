#!/usr/bin/env python

import os
import sys
import dbm

from socket import *
from time import ctime

os.system('clear')

db = dbm.open('userData','c')

if not 'nickname' in db.keys():
    db['nickname'] = ''

if not db['nickname']:
    print 'Please set a Receiver nickname first'
    sys.exit()

nickname = db['nickname']

HOST = ''
PORT = 2700
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

gotNickname = False

while 1:
  os.system('clear')
  if gotNickname==True:
    print 'Lost connection from: %s (IP:%s)' % (guestNickname, ADDR[0])
  print 'waiting for message...'
  tcpCliSock, ADDR = tcpSerSock.accept()
  
  tcpCliSock.send('Connected to %s\nPress Enter to end the talk' % nickname)
  
  while 1:
    data = tcpCliSock.recv(BUFSIZ)
    
    if not data:
      break
    
    if data[0]=='\x10':
      if gotNickname==False:
        guestNickname = data
        gotNickname = True
        print '...connected from: %s (IP:%s)' % (guestNickname, ADDR[0])
          
    else:
      print '[%s]%s: %s' % (ctime(),guestNickname, data)
      data =  raw_input('> ')
      tcpCliSock.send('[%s]%s: %s' % (ctime(), nickname, data))

tcpCliSock.close()
tcpSerSock.close()