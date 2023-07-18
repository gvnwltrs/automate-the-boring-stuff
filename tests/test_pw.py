#!/usr/bin/env python3 

import unittest
from password_locker.pw import PWLocker

class TestPW(unittest.TestCase):

    def test_initial(self):
        pass

    def test_for_password_dict(self):
        pw_locker = PWLocker()
        result = pw_locker.PASSWORDS
        expected_result = {
            'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'}
        self.assertEqual(expected_result, result)

    def test_for_account_name(self):
        pw_locker = PWLocker()
        result = pw_locker.account 
        self.assertIsNotNone(result)

    def test_for_authorized_account(self):
        pw_locker = PWLocker()
        result = pw_locker.is_account_authorized()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()