#Assignment Operator


a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", c)

c += a
print ("Line 2 - Value of c is ", c )

c *= a
print ("Line 3 - Value of c is ", c )

c /= a 
print ("Line 4 - Value of c is ", c )

c  = 2
c %= a
print ("Line 5 - Value of c is ", c)

c **= a
print ("Line 6 - Value of c is ", c)

c //= a
print ("Line 7 - Value of c is ", c)

#Arithmetic Operator
x = 15
y = 4


print('x + y =',x+y)


print('x - y =',x-y)


print('x * y =',x*y)


print('x / y =',x/y)


print('x // y =',x//y)


print('x ** y =',x**y)

#comparision Operator
x = 10
y = 12


print('x > y is',x>y)

print('x < y is',x<y)


print('x == y is',x==y)

print('x != y is',x!=y)

print('x >= y is',x>=y)


print('x <= y is',x<=y)

# Logical Operators in Python
x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)



#Identity operators in Python
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]


print(x1 is not y1)


print(x2 is y2)


print(x3 is y3)


# Membership operators in Python
x = 'Hello world'
y = {1:'a',2:'b'}


print('H' in x)


print('hello' not in x)


print(1 in y)


print('a' in y)