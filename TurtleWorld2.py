import turtle
t = turtle.Turtle()
def square(t,length):
    for i in range(4):
        t.fd (length)
        t.lt (90)
square(t,100)

#GENERALIZATION - IN THIS VERSION THE SQUARE CAN BE ANY SIZE.
#. Add another parameter, named length, to square. 
# Modify the body so length of the sides is length, and then modify the function call to provide a second argument. 
# Run the program again. Test your program with a range of values for length.