import turtle 
bob = turtle.Turtle()
bob.fd(100)
bob.lt(90)
bob.fd(100)

bob.fd(100)
bob.rt(90)
bob.bk(100)

bob.bk(100)
bob.lt(90)
bob.bk(100)

bob.bk(100)
bob.lt(90)
bob.bk(100)
#Results in a square when run
#The turtle module (with a lowercase t) provides a function called Turtle (with an uppercase T) that creates a Turtle object, which we assign to a variable named bob.
#This is self done,correct way is in mypolygoncorrect.py

print(bob)
turtle.mainloop()

for i in range(4):
    print("Hello!")


