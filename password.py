#!/usr/bin/env python3 
# pw.py - An insecure password locker program
import sys, pyperclip

PASSWORDS = {
    'email': 'example@gmail.com',
    'blog': 'wordpress.org',
    'luggage': '12345'
}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name -- list argument from the PASSWORD Dictionary

if account in PASSWORDS: # check if the arguments are in PASSWORDS Dictionary
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)


# output after running python password.py email -- example@gmail.com