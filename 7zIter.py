#!/usr/bin/env python
import os
import sys
import itertools
import string

print 'USAGE: python 7zIter.py <7z file>\n'

chars = string.ascii_letters + string.digits
for length in range(1,6):
    for iteration in itertools.product(chars, repeat=length):
        iteration = ''.join(iteration)            
        crackAttempt = os.system('7z e {} -aoa -p{} '.format(sys.argv[1],iteration))
        if crackAttempt == 0:
            print " The password was: " + iteration
            exit(1)
print 'Sorry, Password not found'
