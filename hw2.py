# Name: Joseph Barnes
# Evergreen Login: barjos05
# Computer Science Foundations
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

 Name: Joseph Barnes
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


n = hw2_test.n
sum = 0
x = n + 1 

for i in range(n+1): 
    sum = sum + i
    print sum


# ... write your code and comments here (and remove this line)


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



# ... write your code and comments here (and remove this line)

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

# ... write your code and comments here (and remove this line)

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

# ... write your code and comments here (and remove this line)

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
