#!/usr/bin/env python3

from filesystems.filepaths import FilePaths

def test_initial():
    assert True

def test_filepath_exists():
    fp = FilePaths()
    result = fp.path 
    # expected = 'usr/bin/spam'
    expected = '/home/gwalters/Workspace'
    fp.print_path()
    assert result == expected

def test_for_drive_attached():
    fp = FilePaths()
    result = fp.drive_attached()
    assert result

def test_for_is_file():
    fp = FilePaths()
    result = fp.is_file('/home/gwalters/test.txt')
    assert result

def test_is_directory():
    fp = FilePaths()
    result = fp.is_directory('/home')
    assert result

def test_write_to_file():
    fp = FilePaths()
    file_path = '/home/gwalters/test.txt'
    message = 'hello!'
    fp.write_to_file(file_path, message)
    expected = fp.find_in_file(file_path, message)
    assert expected