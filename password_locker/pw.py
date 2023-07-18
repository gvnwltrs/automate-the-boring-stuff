#!/usr/bin/env python3
# pw.py - An insecure password locker program. 

import sys
import pyperclip

class PWLocker:
    
    def __init__(self):
        self.PASSWORDS = {
            'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'}
        
        self.account = self.set_account_name()

    def set_account_name(self):
        if len(sys.argv) < 2: 
            print('Usage: python pw.py [account] - copy account password')
            sys.exit()
    
        return sys.argv[1]
    
    def is_account_authorized(self):
        if self.account in self.PASSWORDS:
            pyperclip.copy(self.PASSWORDS[self.account])
            print('Password for {0} copied to clipboard'.format(self.account))
            return True
    
        print('There is no account named {0}'.format(self.account))
        return False