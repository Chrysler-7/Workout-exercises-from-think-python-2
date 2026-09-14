import turtle
bob = turtle.Turtle()

#Below is a simpler way to draw the square.

for i in range(4):
    bob.fd(100)
    bob.lt(90)

print(bob)
turtle.mainloop()