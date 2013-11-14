# Joseph Barnes
# barjos05
# Lab 3

n = 10 #Enter an integer value.

series = 'sum'
series = 'fibonacci'
fib = 0 

a = 1 #set a to 1 to start at 1
b = 0 #set b to zero to begin adding the numbers from zero on
i = 0 #initialize i to zero

if series == 'fibonacci':
    while i < n:
        fib = a + b
        a = b
        b = fib
        i = i + 1
    print fib
   
elif series == 'sum':
    while i < n:
        b = b + 3 #keep adding 3 to b each time for each value i until i reaches n
        i = i + 1 
    print b
            
else: 
    print 'invalid string'
