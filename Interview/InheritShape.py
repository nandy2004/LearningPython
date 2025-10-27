class Shape():
    def Values(self):
        print("This is the base class")
        self.PI=3.14
        self.r=5.0
        self.l=10
        self.b=15
class Circle(Shape):
    def Area(self):
        area=self.PI*self.r*self.r
        print("Area of a Circle is ",area)
class Rectangle(Shape):
    def Area(self):
        area=self.l*self.b
        print("Area of a Rectangle is",area)

shape=Circle()
shape.Values()
shape.Area()
shapes=Rectangle()
shapes.Values()
shapes.Area()