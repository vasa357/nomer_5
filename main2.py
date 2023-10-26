from turtle import Turtle
a = Turtle()
sid = int(input("яка довжина багатокутника:"))
def square(sid1):
    print(sid1)
    for i in range(10):
        a.forward(sid1)
        a.left(40)
square(sid)
a.screen.mainloop()