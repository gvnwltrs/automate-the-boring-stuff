#!/usr/bin/env python3 

from is_phone_number.is_phone_number import PhoneNumber

def test_init():
    pass 

def test_phone_number_given():
    input = "888-555-7777"
    number = PhoneNumber(input)
    assert number.number is not None

def test_is_phone_number():
    input = "888-555-7777"
    number = PhoneNumber(input)
    result = number.isPhoneNumber(number.number)
    expected_result = True
    assert result == expected_result