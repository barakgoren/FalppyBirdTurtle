import turtle


class Cloud:
    def __init__(self, x, y):
        self.new_cloud = turtle.Turtle()
        self.new_cloud2 = turtle.Turtle()
        self.new_cloud3 = turtle.Turtle()
        self.bottom = turtle.Turtle()

        self.new_cloud.color("white")
        self.new_cloud.shape("circle")
        self.new_cloud.penup()
        self.new_cloud.goto(0 + x, -0.7 + y)
        self.new_cloud2.color("white")
        self.new_cloud2.shape("circle")
        self.new_cloud2.shapesize(1.3)
        self.new_cloud2.penup()
        self.new_cloud2.goto(-20 + x, 2 + y)
        self.new_cloud3.penup()
        self.new_cloud3.color("white")
        self.new_cloud3.shape("circle")
        self.new_cloud3.goto(-40 + x, -0.7 + y)
        self.bottom.penup()
        self.bottom.shape("square")
        self.bottom.shapesize(stretch_len=2, stretch_wid=0.2)
        self.bottom.color("white")
        self.bottom.goto(-19 + x, -9 + y)

    def back(self):
        self.new_cloud.back(1)
        self.new_cloud2.back(1)
        self.new_cloud3.back(1)
        self.bottom.back(1)
