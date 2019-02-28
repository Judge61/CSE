class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name, mileage):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100
        self.mileage = mileage

    def start_engine(self):
        self.engine_status = True
        print("You turn the key and the car turns on")

    def move_forward(self):
        self.fuel -= 1
        print("The car moves forward")

    def turn_left(self):
        self.fuel -= 1
        print("HE IS MAKING A LEFT TURN!")

    def turn_off(self):
        self.engine_status = False
        print("You turned off the car")


class KeylessCar(Car):
    def __init__(self):
        super(KeylessCar, self).__init__(name, mileage)

    def start_engine(self):
        self.engine_status = True
        print("You push the button and the car turns on")

weibe_car = KeylessCar("Tesla", 25)

class Impala(Car):
    def __init__(self):
        super(Impala, self).__init__('Impala', 25)


aman_car = Impala()
aman_car.start_engine()
aman_car.move_forward()
aman_car.turn_left()
aman_car.move_forward()
aman_car.turn_off()


