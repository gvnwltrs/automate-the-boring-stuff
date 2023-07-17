#!/usr/bin/env python3
# pw.py - An insecure password locker program. 

import sys

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