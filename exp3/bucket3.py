print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
# Shape classes
class Circle:
    def draw(self):
        print("Drawing Circle")

class Square:
    def draw(self):
        print("Drawing Square")

# Factory class
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type.lower() == "circle":
            return Circle()
        elif shape_type.lower() == "square":
            return Square()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Demonstration
if __name__ == "__main__":
    factory = ShapeFactory()

    shape1 = factory.create_shape("circle")
    shape1.draw()  # Output: Drawing Circle

    shape2 = factory.create_shape("square")
    shape2.draw()  # Output: Drawing Square
