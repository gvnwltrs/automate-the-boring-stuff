#!/usr/bin/env python3 

import pyperclip

class BulletPointAdder:
    
    def __init__(self):
        self.text = None
        self.lines = None

    def get_clipboard_text(self):
        self.text = pyperclip.paste()

        return self.text
    
    def separate_text_lines(self):
        self.lines = self.text.split('\n')

        return len(self.lines)
    
    def add_bullets_to_lines(self):
        for i in range(len(self.lines)):
            self.lines[i] = '* ' + self.lines[i]

    def lines_back_to_single_string(self):
        self.text = '\n'.join(self.lines)
        print(self.text)