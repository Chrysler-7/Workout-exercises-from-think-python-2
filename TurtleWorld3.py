import math

import turtle
t = turtle.Turtle
def circle(t,r):
    circumference = 2*math.pi*r
    n =50
    length = circumference/n
    circle(t,n,length)
print(circle)

#TO RE-DO WITH WI-FI