#!/usr/bin/perl
# Black Eagle Analytics & Data LLC
# Written by Shane Bruce 28th of Aug 2019
# as a speed and capability comparison
# of Perl v Python :  test.perl and test.python
#
use strict;
use warnings;
use Time::HiRes qw[gettimeofday tv_interval];
print "Hello \nLimit to Fibonacci:";
my $x = <STDIN>;
chomp $x;
print "\n";
my $prime;
my $count1 = 0;
my $count2 = 0;
my $a = 0;
my $b = 1;
my $c;

my $time1=[gettimeofday()];
while ($a < $x){
    $count2++;
    print $a;
    $prime = 1;
    for (my $n=2; $n<=$a; $n++){
        if ($a%$n==0 && $a>2 && $a!=$n){
            print " : equals ",$n, "*", $a/$n;
            $prime = 0;
            last;
        }
    }
    if ($prime==1 && $a>1){
        print ": Prime number";
        $count1++;
    }
    $c = $a;
    $a = $b;
    $b = $b+$c;
    print "\n";
}
my $time2=[gettimeofday()];
my $msec1 = tv_interval($time1)*1000;
my $msec2 = tv_interval($time2)*1000;
print "\nElapsed time: ", $msec1-$msec2, " MillSec.\n";
print "For ", $x;
print " there are ", $count2, " values";
print "\nin the Fibonacci Sequence;";
print "\nof which ", $count1, " are Prime Numbers. \n\n\n";
