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

    def is_directory(self, path):
        return os.path.isdir(path)


    def write_to_file(self, path, msg): 
        with open(path, "w") as file:
            file.write(msg)

    def find_in_file(self, file, search_term):
        with open(file, "r") as file:
            for line in file:
                if search_term in line:
                    return True
        return False 
