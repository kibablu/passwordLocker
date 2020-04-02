#!/usr/bin/env python3 
# pw.py - An insecure password locker program
import sys, pyperclip

PASSWORDS = {
    'email': 'example@gmail.com',
    'blog': 'wordpress.org',
    'luggage': '12345'
}

if len(sys.argv) < 2: # checks if sys.argv is less that 2 from a command 
    print('Usage: python password.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name -- sys.argv is a list argument from a command

if account in PASSWORDS: # check if the arguments are in PASSWORDS Dictionary
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

'''
This new code looks in the PASSWORDS dictionary for the account name.
If the account name is a key in the dictionary, we get the value corresponding
to that key, copy it to the clipboard, and print a message saying that we
copied the value. Otherwise, we print a message saying there’s no account
with that name.
'''

# output after running python password.py email -- example@gmail.com