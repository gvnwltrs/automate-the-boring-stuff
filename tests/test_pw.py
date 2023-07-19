#!/usr/bin/env python3 

import pytest
from password_locker.pw import PWLocker

def test_initial():
    pass

def test_for_password_dict():
    pw_locker = PWLocker()
    result = pw_locker.PASSWORDS
    expected_result = {
        'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
        'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
        'luggage': '12345'}
    assert expected_result == result

def test_for_account_name():
    pw_locker = PWLocker()
    result = pw_locker.account 
    assert result is not None

