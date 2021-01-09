# Perl-V-Python-Latency
How fast can we find Fibonacci sequences of Primes in each? Who's the fastest? Who's the best? 

Output for a limit of 999999
 
python test.python
Hello
Limit to Fibonacci:999999
0
1
1
2 : Prime number

3 : Prime number

5 : Prime number

8 : equals 2 * 4
13 : Prime number

21 : equals 3 * 7
34 : equals 2 * 17
55 : equals 5 * 11
89 : Prime number

144 : equals 2 * 72
233 : Prime number

377 : equals 13 * 29
610 : equals 2 * 305
987 : equals 3 * 329
1597 : Prime number

2584 : equals 2 * 1292
4181 : equals 37 * 113
6765 : equals 3 * 2255
10946 : equals 2 * 5473
17711 : equals 89 * 199
28657 : Prime number

46368 : equals 2 * 23184
75025 : equals 5 * 15005
121393 : equals 233 * 521
196418 : equals 2 * 98209
317811 : equals 3 * 105937
514229 : Prime number

832040 : equals 2 * 416020

Elapsed time: 100.779 MillSec
For 999999 there are 31 values
in the Fibonacci Sequence,
of which 9 are Prime Numbers.

test.perl
Hello
Limit to Fibonacci:999999
0
1
1
2: Prime number

3: Prime number

5: Prime number

8 : equals 2*4
13: Prime number

21 : equals 3*7
34 : equals 2*17
55 : equals 5*11
89: Prime number

144 : equals 2*72
233: Prime number

377 : equals 13*29
610 : equals 2*305
987 : equals 3*329
1597: Prime number

2584 : equals 2*1292
4181 : equals 37*113
6765 : equals 3*2255
10946 : equals 2*5473
17711 : equals 89*199
28657: Prime number

46368 : equals 2*23184
75025 : equals 5*15005
121393 : equals 233*521
196418 : equals 2*98209
317811 : equals 3*105937
514229: Prime number

832040 : equals 2*416020

Elapsed time: 69.012 MillSec.
For 999999 there are 31 values
in the Fibonacci Sequence;
of which 9 are Prime Numbers. 




So, the Perl is OBVIOUSLY FASTER, and a more stable coding language.  Now this is to be expected.  It’s a mature language which has been refined and become faster and more stable with it’s of it’s 5th General Perl and subsequent 15 versions.   The hype from Python was mind-boggling, it’s not anywhere near the standard that a professional development language should be.  My only guess as to why it’s lauded, it’s cheap on keystrokes and easy to learn.   It should NOT be topping the lists of requisites by development companies.  But here is the closing argument: Python breaks in this simple program when the limit is 40,000,000 (Forty Million).  It’s lauded as a BIG DATA language; most programming languages handle the number 2,247,483,647 (BIG INT) around Two Billion.  Python simply is collage of quick steps to a weaker foundation backing the language.  Unless I’m missing some ‘switch’, but I’ve the impression that Python is supposed to be the language that doesn’t need the fine-tuning to write a program. 

But first Notice how much FASTER Perl is, which in BIG DATA where it counts most.

 
test.python

Elapsed time:1469.582 MillSec

For 35000000 there are 38 values
in the Fibonacci Sequence,
of which 9 are Prime Numbers.

test.perl

Elapsed time: 68.779 MillSec.

For 35000000 there are 38 values
in the Fibonacci Sequence;
of which 9 are Prime Numbers.
 
And finally, at 40,000,000 (Forty Million) Python Breaks

 
test.python  (40,000,000)

Traceback (most recent call last):

  File "test.python", line 26, in <module>
    for n in range (2,a):
MemoryError
  
test.perl

Elapsed time: 69.151 MillSec.

For 40000000 there are 39 values
in the Fibonacci Sequence;
of which 9 are Prime Numbers 

Now Perl I ran at a limit of 100,000,000,000 (One Hundred Billion).  It did finally start slowing down in the 2 Billion range on the prime number as it had to run a Modulus (division with no remainder) all 2 Billion times.  So, some seconds appear for the first time in Perl test. 

test.perl 

Elapsed time: 422191.347 MillSec.

For 1000000000000 there are 60 values
in the Fibonacci Sequence;
of which 11 are Prime Numbers.

It’s a good program because the size of the numbers rapidly geometrically increases but the output of the Fibonacci is only the a few dozen values.   Perl’s overwhelming Python in speed of numerical calculations and capacity.   But now I like Python, it’s some easy code, but I thought I’d be able to brag, but only to those who are programming language illiterate.  Perl gives a better shake, though once too thought so simple as to be lame by C++ or Assembly in turn. 
