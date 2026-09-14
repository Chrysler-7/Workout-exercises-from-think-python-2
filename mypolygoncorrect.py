import turtle
bob = turtle.Turtle()
bob.fd(100)
bob.lt(90)

bob.fd(100)
bob.lt(90)

bob.fd(100)
bob.lt(90)

bob.fd(100)

print(bob)
turtle.mainloop()

#Whether forward and left or forward and right or instead of forward it's backward all that changes is the direction the square starts to be drawn from.

#FROM THINK PYTHON 2
#The argument of fd is a distance in pixels, so the actual size depends on your display.
#Other methods you can call on a Turtle are bk to move backward, lt for left turn, and rt right turn. The argument for lt and rt is an angle in degrees.
#Also, each Turtle is holding a pen, which is either down or up; if the pen is down, theTurtle leaves a trail when it moves. The methods pu and pd stand for “pen up” and “pen down”.
#To draw a right angle, add these lines to the program (after creating bob and before calling mainloop):
 #bob.fd(100)
 #bob.lt(90)
 #bob.fd(100)
#When you run this program, you should see bob move east and then north, leavingtwo line segments behind.