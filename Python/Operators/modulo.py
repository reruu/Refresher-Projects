#The modulo operator % returns the remainder of a division:
'''
Common use: checking if a number is even or odd

Even number: number % 2 == 0
Odd number: number % 2 == 1 '''

a,b,c = 9,2,11
d = a % 2
e = b % 3
f = c % 10

x,y,z = 15,4,23
w = x % y
v = z % x
u = z % y
 
g = 10
g %= 3  # stores 1 as remainder

h = 10
h -= 4
# h now holds 6
