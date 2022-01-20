
from datetime import date


class Human:
    population = 0

    def __init__(self,
                 name: str,
                 surname: str,
                 birth_date: date,
                 gender: str,
                 weight: float,
                 height: float,
                 speed: int,
                 smile: bool,
                 emotion: str,):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender
        self.weight = weight
        self.height = height
        self.speed = speed
        self.smile = smile
        self.emotion = emotion

        if self.__class__.population < 10:
            self.__class__.population += 1
        else:
            raise RuntimeError("You could not create instance. Limit 10 reached")

    @property
    def movement_type(self):
        if self.speed <= 4:
            return 'walking'
        elif self.speed > 4:
            return 'running'
        elif self.speed > 30:
            return 'driving by vehicle'
        else:
            return 'not moving'

    @property
    def mood(self):
        if self.smile:
            return 'good mood'
        elif not self.smile:
            if self.emotion in ["joyful", "exiting", "calm", "dreaming", "passionate", "enthusiastic"]:
                return 'good mood'
            else:
                return 'bad mood'

    @property
    def age(self):
        return (date.today() - self.birth_date).days // 365

    def life_energy(self):
        if self.movement_type == 'not moving':
            print(f"I'm {self.name} and I'm quarantined and depressed")
        elif self.movement_type == 'walking' or 'running':
            print(f"I'm {self.name} and I moves every day and I'm full of energy")
        elif self.movement_type == 'driving by vehicle':
            print(f"I'm {self.name} and I have a vehicle")

    def stand(self, location):
        print(f"I'm {self.name} and I'm standing at the {location}")

    def sleep(self, snore_sound):
        print(f"I'm {self.name} and I'm sleeping in my bed and snoring {snore_sound}")

    def say(self, phrase: str):
        if self.mood == 'good mood':
            print(f"I'm {self.name} and I'm saying: - {phrase} because I'm in good mood")
        elif self.mood == 'bad mood':
            print(f"I'm {self.name} and I'm don't wonna talk because I'm in bad mood")

    def eat(self, dish):
        print(f"{self.name} eats {dish}")

    def lie(self, bed):
        print(f"I'm {self.name} and I'm laying on the {bed}")

person1 = Human("Serg", "Penkov", date(1998, 5, 25), "mail", 80, 1.75, 50, True, 'upset')
person2 = Human("Victor", "Kurkin", date(1995, 5, 25), "mail", 75, 1.80, 30, False, 'joyful')
person3 = Human("Ivan", "Tetcher", date(1989, 5, 25), "mail", 90, 1.95, 10, True, 'passionate')

person1.eat("onion")
person3.say(f"Life is amazing")
person2.life_energy()
