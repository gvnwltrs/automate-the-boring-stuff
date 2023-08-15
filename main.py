#!/usr/bin/env python3 

import filesystems.filepaths as F
# import password_locker.pw as pwl
# import is_phone_number.is_phone_number as ipn

if __name__ == '__main__':
    fp = F.FilePaths()

    fp.print_contents_of_dir()
    fp.print_size_of_dir()