#!/usr/bin/env python3 

import os  
 

class FilePaths:
    def __init__(self):
        self.path = os.path.join('/', 'home', 'gwalters', 'Workspace')

    def print_path(self):
        print(self.path)
    
    def print_contents_of_dir(self):
        print(os.listdir(self.path))

    def print_size_of_dir(self):
        print('{0}MB'.format(os.path.getsize(self.path)))
        print('{0}GB'.format(os.path.getsize(self.path)/1024))
    
    def drive_attached(self):
        return os.path.exists('/media/gwalters')
    
    def is_file(self, path):
        return os.path.isfile(path)