class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.happylevel = 1
    def bark(self):
        print(f"{self.name} says Woof!")
    
    def pet(self):
        self.happylevel = self.happylevel + 1
        print(f"{self.name} is happy")
        print(f"happiness level = {self.happylevel}")
    

uinput = input("name your Tamagotchi")
my_dog = Tamagotchi(uinput)
opt = "1"
my_dog.bark() 
while opt != "3":
    opt = input("interact, 1 = pet, 2 = feed, 3 = quit")
    if opt == "1":
        my_dog.pet()
