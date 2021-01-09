#!/usr/bin/python
import time
print("Hello")
x=int(input("Limit to Fibonacci:"))
count1 = 0
count2 = 0
a, b = 0, 1

start = time.time()
while a < x:
	count2 +=1
    	print a,
    	prime = True
    	for n in range (2,a):
        		if a % n == 0:
            		print ': equals', n, '*', a//n,
            			prime = False
            			Break
    	if prime and a > 1:
      		 print ': Prime number',
       		count1+=1
    	a, b = b, a+b
    	Print

Print
etime = (time.time()-start)*1000
print "Elasped time:%8.3f" % etime,
print "MillSec"
print 'For', x, 'there are', count2, "values"
print 'in the Fibonacci Sequence,'
print 'of which', count1, 'are Prime Numbers.'
Print
