#!/usr/bin/python
# Black Eagle Analytics & Data LLC
# Written by Shane Bruce 28th of Aug 2019
# as a speed and capability comparison
# of Perl v Python :  test.perl and test.python

import time
x=int(input("Limit to Fibonacci:"))
count1 = 0
count2 = 0
a, b = 0, 1

start = time.time()
while a < x:
    count2 = count2 + 1
    prime = True
    for n in range(2,a):
        if a % n == 0:
            print(a,': equals', n, '*', a//n,)
            prime = False
            break
    if prime and a > 1:
        print(a,': Prime number',)
        count1+=1
    a, b = b, a+b

etime = (time.time()-start)*1000
print ("Elasped time:%8.3f" % etime,"MillSec")
print ('For', x, 'there are', count2, "values in the Fibonacci Sequence, of which")
print (count1, 'are Prime Numbers.')
