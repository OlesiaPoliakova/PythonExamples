
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        return f"{self.name}: start the engine and turn the steering wheel"

    @abstractmethod
    def stop(self):
        pass

    @property
    def movement_type(self):
        if self.name == "Auto":
            return '4 tires are spinning'
        elif self.name == "Ship":
            return 'it is sailing on water'
        elif self.name == "Airplane":
            return 'is in the air most of the time'
        elif self.name == "BMP":
            return '4 tires are spinning or it is sailing on water'
        elif self.name == "Automotive":
            return '4 tires are spinning or it is in the air most of the time'

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def turn(self):
        print(f"{self.name}:rapidly turn the steering wheel and make turn in the right direction")

class Auto(Vehicle):
    def __init__(self,
                 name: str,
                 speed: int,
                 tire = 4,
                 steering_wheel=1):
        Vehicle.__init__(self, name)
        self.speed = speed
        self.tire = tire
        self.steering_wheel = steering_wheel

    def start(self):
       pass

    def stop(self):
        return f"{self.name}: pulls the break and stop"

    def move(self, distance):
        print(f"{self.name}:{self.movement_type}")
        return distance / self.speed

    def turn(self):
        pass


class Ship(Vehicle):
    def __init__(self,
                 name: str,
                 speed: int,
                 steering_wheel=1,
                 anchor=1):
        Vehicle.__init__(self, name)
        self.speed = speed
        self.steering_wheel = steering_wheel
        self.anchor = anchor

    def start(self):
        pass

    def stop(self):
        return f"{self.name}: drop the anchor and stop"

    def move(self, distance):
        print(f"{self.name}:{self.movement_type}")
        return distance / self.speed

    def turn(self):
        pass

class Airplane(Vehicle):
    def __init__(self,
                 name: str,
                 speed: int,
                 steering_wheel=2,
                 wings=2):
        Vehicle.__init__(self, name)
        self.speed = speed
        self.steering_wheel = steering_wheel
        self.wings = wings

    def start(self):
        return f"{self.name}:start the engine, turn the steering wheel and take off"

    def stop(self):
        return f"{self.name}: make landing and stop"

    def move(self, distance):
        print(f"{self.name}:{self.movement_type}")
        return distance / self.speed

    def turn(self):
        pass


class BMP(Auto, Ship):
    def __init__(self,
                 name: str,
                 speed: int,
                 tire=4,
                 steering_wheel=1,
                 anchor=1):
        Auto.__init__(self, name, speed, tire, steering_wheel)
        Ship.__init__(self, name, speed, steering_wheel, anchor)

    def start(self):
        pass

    def stop(self):
        return f"{self.name}: pulls the break and stop"

    def move(self, distance):
        print(f"{self.name}:{self.movement_type}")
        return distance / self.speed

    def turn(self):
        pass

class Automotive(Auto, Airplane):
    def __init__(self,
                 name: str,
                 speed: int,
                 tire=4,
                 steering_wheel=1,
                 wings = 2):
        Auto.__init__(self, name, speed, tire, steering_wheel)
        Airplane.__init__(self, name, speed, steering_wheel, wings)

    def start(self):
        pass

    def stop(self):
        return f"{self.name}: pulls the break and stop"

    def move(self, distance):
        print(f"{self.name}:{self.movement_type}")
        return distance / self.speed

    def turn(self):
        pass

# racer1 = Auto("Auto", 50)
# racer1.move(100)
transport_park = [Auto("Auto", 50), Ship("Ship", 150), Airplane("Airplane", 900), BMP("BMP", 60), Automotive("Automotive", 200)]
racers = sorted((racer.move(100), racer.name) for racer in transport_park)
print(f"Race results (time in seconds)")
for time, name in racers:
    print(f"{name}: {time}")
