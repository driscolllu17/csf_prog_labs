# Name: Joseph  Barnes
# Evergreen Login:barjos05  
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"
#quadratic equation = x2-5.86 x+ 8.5408
a = 1
b = 5.86
c = 8.5408

#Use the quadratic formula to solve the equation above.

rootadd = (- b + math.sqrt(b ** 2 - 4 * a * c)/(2 * a))
rootsubt = (-b - math.sqrt(b ** 2 - 4 * a * c)/(2 * a))
print "Root addition=",rootadd, "and","Root subtraction=",rootsubt

###
### Problem 2
###

print "Problem 2 solution follows:"
import hw1_test
print "a =",hw1_test.a
print "b =",hw1_test.b
print "c =",hw1_test.c
print "d =",hw1_test.d
print "e =",hw1_test.e
print "f =",hw1_test.f


###
### Problem 3
###
a = hw1_test.a
b = hw1_test.b
c = hw1_test.c
d = hw1_test.d
e = hw1_test.e
f = hw1_test.f

print "Problem 3 solution follows:"
print ((a and b) or (not c) and not (d or e or f)) 
#
##
###
### Reflection
###

# This assignment took me quite a bit of time because of troubles I had with 
#github. This is a new re-draft of my homework that I thought I had saved to my github repository.
#Hopefully this time I am able to properly submitt my work for evaluation.
#For this assignment I used the asigned tutorials associated with the lab as well as the course texts.
#Initially I spent longer on this assingnment because I thought we were supposed to write a program that is more complicated.
