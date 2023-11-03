#!/usr/bin/python3
exec("from ctypes import CDLL\nCDLL('libc.so.6').printf('#pythoniscool\\n')")
