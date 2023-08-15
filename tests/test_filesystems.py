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