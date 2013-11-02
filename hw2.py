# Name: Joseph Barnes
# Evergreen Login: barjos05
# Computer Science Foundations
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

#Name: Joseph Barnes
# Evergreen Login: barjos05
# Computer Science Foundations

###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"


import hw2_test

n = hw2_test.n
sum = 0
i = 0

while i <= n : 
    sum = sum + i
    print sum
    i = i + 1

##I added 1 to n in order for the program to print all the numbers
##up to 100.



### Problem 2


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"


n=10

for i in range(n+1):
    if i > 0:
        print 1.0/i






###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0

for i in range(n):
    triangular = n * (n+1) / 2
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n * (n+1) / 2




###
### Problem 4
###


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"



n = 10
product = 1

for i in range(n):
    product = product * (i + 1)
print "factorial=",product


###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

n = 10
numlines = n

for i in range(n):
    print 'factorial of', n, '='
    n = n-1
    product = 1
    for i in range(n+1):
        product = product * (i + 1)
    print product

###
### Problem 6
###


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

n = 10
recip = 0

for i in range(n):
    if i > 0:
        recip = (1.0/i) + recip
        print recip

###
### Collaboration
###

# For this assignment I did not use any collaborators. However I did use the text
# a good deal in order to complete this assignment.


###
### Reflection
###

# This assignment has taken me some time because I thought I had submitted an updated copy to my git hub repository.
# I have made the corrections a second time. Initially I was having trouble with figuring out how to get parts two and six to output decimal reciprocals.
# I thought that this was a good assignment and that it contained everything that was necessary to complete the assignment.
