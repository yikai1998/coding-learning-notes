# coding=gbk
# string function
import re

s = 'Arthur: three! Arthur'.lstrip('Arthur: ')  # from left begin to start mapping, stop when the first char found is out of scope list
# ee! Arthur

s = 'Arthur: three! Arthur'.removeprefix('Arthur')
# : three! Arthur

s = 'Arthur: three! Arthur'.removesuffix('Arthur')
# Arthur: three!

s = 'string    methods in python.'
s2 = re.sub('\\s+', '=', s)  # s2 = re.sub(r' ', '=', s)  string====methods=in=python.
# string=methods=in=python.

s = 'Python is awsome! Yes, is true!'
s = s.partition('is')
# ('Python ', 'is', ' awsome! Yes, is true!')

s = 'Python is awsome! Yes, is true!'
s = s.partition('was')
# ('Python is awsome! Yes, is true!', '', '')

s = 'Python'
s = s.center(40, '=')
# =================Python=================

s = 'Python'
s = s.rjust(30, '=')
# ========================Python

s = 'Java'
s = s.swapcase()
# jAVA

s = '-185.2'
s = s.zfill(8)
# -00185.2
