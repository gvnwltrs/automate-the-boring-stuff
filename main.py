#!/usr/bin/env python3 

from password_locker.pw import PWLocker

if __name__ == '__main__':
    print('starting now')

    PL = PWLocker()

    PL.set_account_name()
    PL.is_account_authorized()