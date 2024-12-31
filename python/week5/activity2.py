class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Example usage
if __name__ == "__main__":
    my_car = Car()
    my_plane = Plane()
    
    my_car.move()
    my_plane.move()
