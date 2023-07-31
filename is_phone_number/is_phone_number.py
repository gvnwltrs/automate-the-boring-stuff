#!/usr/bin/env python3 

import re

class PhoneNumber:
    def __init__(self, number=None):
        self.number = number

    def isPhoneNumber(self, number):
        phoneNumberRegex = re.compile(r'''(
                                      (\d{3}|\(\d{3}\))? # area code
                                      (\s|-|\.)?        # separator
                                      \d{3}            # first 3 digits
                                      (\s|-|\.)         # separator
                                      \d{4}             # last 4 digits 
                                      (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
                                      )''', re.VERBOSE)
        mo = phoneNumberRegex.search(number)
        print('Phone number found: {0}'.format(mo.group())) # where group() returns the match 
        print('{0} is a phone number:'.format(number))
        return False if mo is None else True