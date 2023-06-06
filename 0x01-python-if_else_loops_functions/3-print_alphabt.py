#!/usr/bin/python3
for l in range(ord('a'), ord('z')+1):
    if l is not (ord('q')) and l is not (ord('e')):
        print('{}'.format(chr(l)), end='')
