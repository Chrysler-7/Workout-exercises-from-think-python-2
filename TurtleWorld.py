
import turtle
t = turtle.Turtle()
def square(t): # t here is a parameter
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(t) # t here is an argument
# NOTE: WHEN YOU CALL A FUNCTION, THE ARGUMENTS ARE ASSIGNED TO THE PARAMETERS
