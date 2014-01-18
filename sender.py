#!/usr/bin.env python

import os
import sys
import dbm

from socket import *

os.system('clear')

db = dbm.open('userData','c')

if not 'guestNickname' in db.keys():
    db['guestNickname'] = ''
        
if not 'targetIP' in db.keys():
    db['targetIP'] = ''

if not db['guestNickname']:
    print 'Please set a Sender nickname first'
    sys.exit()

if not db['targetIP']:
    print 'Please set a target IP first'
    sys.exit()

nickname = db['guestNickname']
HOST = db['targetIP']

PORT = 2700
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

firstConnect = True

while 1:
  while 1:
    if firstConnect!=True:
      print 'Waiting for message...'
    
    data = tcpCliSock.recv(BUFSIZ)
    print data
    if data:
      break
  
  if firstConnect==True:
    tcpCliSock.send('\x10%s' % nickname)
    firstConnect = False
  
  data = raw_input('> ')
  if not data:
    break
  tcpCliSock.send(data)
  if not data:
    break

tcpCliSock.close()