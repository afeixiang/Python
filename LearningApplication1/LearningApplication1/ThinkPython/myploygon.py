'''
Make a turtle program
'''
import turtle

bob = turtle.Turtle()

#bob.fd(100)
def square(t,length):
    '''
    Draw a square
    t is turtle
    length is the side's length
    '''
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t,length,n):
    '''
    Draw a ploygon
    t is turtle
    length is the sides' length
    n is the number of the side
    '''
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t,r):
    '''
    Draw a circle
    t is turtle
    r is radias
    '''
    #polygon(t,6.28*r/10000,10000)
    t.circle(r)

circle(bob,80)
turtle.mainloop()
