'''
Practice of function return value
'''
import math

def area(radius):
    '''
    Calculate the area for input radius
    radius:int
    '''
    aa1 = math.pi * radius**2
    return aa1

def absolute_value(value):
    '''
    Return the absolute value of the input value

    value:number
    '''
    if value < 0:
        return -value
    else:
        return value

def distance(x1, y1, x2, y2):
    '''
    Calculate distance from (x1,y1) to (x2,y2)

    x1: int
    y1: int
    x2: int
    y2: int
    '''
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def circle_area(xc, yc, xp, yp):
    '''
    Calculate the area of the circle from center point(xc,yc) to perimeter point(xp,yp)

    xc:int
    yc:int
    xp:int
    yp:int
    '''
    result = area( distance(xc,yc,xp,yp))
    return result

def factorial(n):
    '''
    Calculate factorial result of n

    n:int
    '''
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative intergers.')
        return None
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)

def ackermann(m,n):
    '''
    Calculate Ackermann result of m,n

    m:int
    n:int
    '''
    if m == 0:
        return n+1
    if m > 0 and n > 0:
       return ackermann(m-1, ackermann(m, n-1))
    if m > 0 and n == 0:
        return ackermann(m-1, 1)


#print(absolute_value(-7))
#print(absolute_value(17))
#print(distance(1,2,4,6))
#print(circle_area(1,2,4,6))
#print(factorial(('fred')))
#print(factorial((-25)))
#print(factorial((33)))
print(ackermann(3, 5))
