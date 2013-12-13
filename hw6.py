# Name:Joseph Barnes
# Evergreen Login: barjos05
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

x = 22
print x
result = (33 == x)
print result
print type(result)

y = "This is a string"
print y
result_string = ("String" == y) 
print result_string
print type(result_string)

another_string = "This is another string"
print another_string
result_string = ("String" == another_string) 
print result_string
print type(result_string)

#The answers are not the same when comparing numbers as comparing strings.
#They wold be the same for other types such as type float.

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

def retrn_number( int ):
   "This prints a number into this function"
   print int
   return
a = retrn_number
d = (a == retrn_number)
print d

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

x = 22
y = (x == 22)
print y

z = (x == 'This is a string')
print x
# The values of an assignments y and z are boolean. 
#These values change depending on the original assignment.

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"
w = (1 == 2)
print w
w = (3 == 3)
print w
#    Write code that assigns value of an equality comparison between two integers to a variable called w, like this: w = (1 == 2).
#    Print the value of w. Is this what you expected?
#    In a separate line of code, after the ones above, write another assignment to w using two different values in order to get a different value for w than you got above. Print out this new value of w.
#    Answer in English in the comments the difference between


###
### Problem 7
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"

#  Explain what happens in English when you execute the following. Put these in comments in your hw6.py.

   # "Assert True" asserts that a statment condition is true and will continue if so. If not an error will show up.
   # "Assert False" asserts that a statment condition is false and will continue if so. If not an error will show up.
practice_assert = 33
test_assert = (practice_assert == int)
x = 22
   
print x
result = (33 == x)
print result
print type(result)
#    Write Python code that calls assert with a boolean expression that you expect to be true.
#    Write Python code that calls assert with a boolean expression that you expect to be false.
#    Write Python code that calls assert with a boolean expression that uses the return value of a function call, like you did above in Problem 3.
#    Explain in English, in the comments of your code, the detailed behavior of an assert statement in the different circumstances you observed above.

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").