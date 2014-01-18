#!/usr/bin/env/python

import os
import sys
import dbm

def main():
    while 1:
        os.system('clear')
        print '\t==================[Talker 1.0]=================='
        print
        print '\t                     [Menu]'
        print
        print '\t[1]Set your nickname for Receiver'
        print '\t[2]Set your nickname for Sender'
        print '\t[3]Set your target IP'
        print
        print '\t[4]Launch Receiver'
        print '\t[5]Launch Sender'
        print
        print '\t[6]Scan IPs'
        print '\t[7]Show my info'
        print '\t[8]About & Help'
        print
        print '\t[0]Exit'
        print
        print
        print
    
        choiceDict = {
        '1': setReceiverNickname,
        '2': setSenderNickname,
        '3': setTargetIP,
        '4': launchReceiver,
        '5': launchSender,
        '6': searchIP,
        '7': showInfo,
        '8': talkerHelp,

        '0': exit
        }
        choice = raw_input(':')
        
        #check for input
        if not choice.isdigit():
            print 'Invalid Input'
            continue
        if int(choice) > 8 or int(choice) < 0:
            print 'Invalid Input'
            continue
        
        os.system('clear')
        choiceDict[choice]()


def setReceiverNickname():
    db = dbm.open('userData','c')
    
    if not 'nickname' in db.keys():
        db['nickname'] = ''
    
    if db['nickname'] == '':
        nickname = raw_input('There\'s no nickname for Receiver, Please input one: \n')
        db['nickname'] = nickname
    else:
        nickname = raw_input('Current nickname for Receiver is %s\ninput a new nickname or press Enter to return to menu:\n' % db['nickname'])
        if not nickname == '':
            db['nickname'] = nickname

    return

def setSenderNickname():
    db = dbm.open('userData','c')
    
    if not 'guestNickname' in db.keys():
        db['guestNickname'] = ''
    
    if db['guestNickname'] == '':
        guestNickname = raw_input('There\'s no nickname for Sender, Please input one: \n')
        db['guestNickname'] = guestNickname
    else:
        guestNickname = raw_input('Current nickname for Sender is %s\ninput a new nickname or press Enter to return to menu:\n' % db['guestNickname'])
        if not guestNickname == '':
            db['guestNickname'] = guestNickname

    return

def setTargetIP():
    db = dbm.open('userData','c')
    
    if not 'targetIP' in db.keys():
        db['targetIP'] = ''
    
    if db['targetIP'] == '':
        targetIP = raw_input('There\'s no target IP, Please input one: \n')
        db['targetIP'] = targetIP
    else:
        targetIP = raw_input('Current target IP is %s\ninput a new target IP or press Enter to return to menu:\n' % db['targetIP'])
        if not targetIP == '':
            db['targetIP'] = targetIP

    return

def launchReceiver():
    os.system('python receiver.py')
    print
    print
    print
    print
    raw_input('Press Enter to return')
    
    return

def launchSender():
    os.system('python sender.py')
    print
    print
    print
    print
    raw_input('Press Enter to return')
    
    return

def searchIP():
    ip = raw_input('Input 3 digit of your IP(example: 192.168.1): ')
    os.system('nmap -sn %s.*' % ip)
    print
    print
    print
    print
    raw_input('Press Enter to return')
    return

def showInfo():
    db = dbm.open('userData','c')
    
    if not 'nickname' in db.keys():
        db['nickname'] = ''
    
    if not 'guestNickname' in db.keys():
        db['guestNickname'] = ''

    if not 'targetIP' in db.keys():
        db['targetIP'] = ''

    print 'Receiver nickname: '
    if not db['nickname']:
        print 'NOT GIVEN'
    else:
        print db['nickname']

    print

    print 'Sender nickname: '
    if not db['guestNickname']:
        print 'NOT GIVEN'
    else:
        print db['guestNickname']

    print

    print 'Target ip(for Sender): '
    if not db['targetIP']:
        print 'NOT GIVEN'
    else:
        print db['targetIP']

    print
    print
    print
    print
    raw_input('Press Enter to return')

    return

def talkerHelp():
    print '\t==================[Talker 1.0]=================='
    print
    print '\t                     [Help]'
    print '\tFirst, set all the infomation before launch something'
    print '\tThen, launch Receiver to receive messages \n\tand launch Sender to send messages'
    print
    print
    print
    print '\tFor more information, send Email to: sun.me.0207@gmail.com'
    print '\tTwitter: @0xSuu'
    print
    print
    print
    print
    raw_input('Press Enter to return')
    
    return

def exit():
    os.system('clear')
    sys.exit(0);

if __name__ == '__main__':
    main()