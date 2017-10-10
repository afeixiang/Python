'''
Exercise for ThinkPython chapter 15
'''
import math

class Point:
    """
    Represents a Point

    attributes:x, y
    """
class Rectangle:
    """
    Represents a Rectangle.

    attributes:width, height, corner.
    """
class Circle:
    """
    Represents a circle.

    attributes: center, radius
    """

def point_in_circle(tpoint, circle):
    '''
    Return True if tpoint is in tcircle, False if not.
    '''
    distance = math.sqrt((circle.center.x - tpoint.x)**2 + (circle.center.y - tpoint.y)**2)
    print(distance)
    return distance < circle.radius

myCircle = Circle()
myCircle.center = Point()
myCircle.center.x = 150
myCircle.center.y = 100
myCircle.radius = 75
point = Point()
point.x = 100
point.y = 90
print(point_in_circle(point, myCircle))