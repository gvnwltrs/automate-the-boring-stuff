#!/usr/bin/env python3

import unittest

class TestThis(unittest.TestCase):

    def test_this(self):
        result = True
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()