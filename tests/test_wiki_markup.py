#!/usr/bin/env python3 

import pytest
import pyperclip
from wiki_markup.bullet_point_adder import BulletPointAdder

def test_initial():
    pass

def test_get_clipboard_contents():
    bpa = BulletPointAdder()
    pyperclip.copy('test')
    result = bpa.get_clipboard_text()
    assert result is not None

def test_lines_of_text_separated():
    bpa = BulletPointAdder()
    pyperclip.copy('item1\nitem2\nitem3\nitem4\nitem5')
    bpa.get_clipboard_text()
    result = bpa.separate_text_lines()
    assert result != 0 

def test_add_bullet_to_lines():
    bpa = BulletPointAdder()
    pyperclip.copy('item1\nitem2\nitem3\nitem4\nitem5')
    bpa.get_clipboard_text()
    bpa.separate_text_lines()
    bpa.add_bullets_to_lines()
    result = bpa.lines
    expected_result = ['* item1', '* item2', '* item3', '* item4', '* item5']
    assert expected_result == result

def test_lines_back_into_single_string():
    bpa = BulletPointAdder()
    pyperclip.copy('item1\nitem2\nitem3\nitem4\nitem5')
    bpa.get_clipboard_text()
    bpa.separate_text_lines()
    bpa.add_bullets_to_lines()
    bpa.lines_back_to_single_string()
    result = bpa.text 
    expected_result = "* item1\n* item2\n* item3\n* item4\n* item5"
    assert expected_result == result