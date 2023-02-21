from scenario import PrintableObject


class Character(PrintableObject):

    def __init__(self, name="Character"):
        super().__init__()
        self.name = name
        self.power = 10
        self.armor = 10


class Hero(Character):
    
    def __init__(self, name="Super Hero"):
        super().__init__(name)
        self.cape_color = "Red"

    def print(self, _3d=False):
        super().print()
        print(f"\tI'm the Super Hero {self.name}")

    def __str__(self):
        return "anything"

    def __add__(self, obj_to_be_added):
        return f"{self.name}+{obj_to_be_added.name}" 


class Monster(Character):
    
    def __init__(self, name="Monster XYZ"):
        super().__init__(name)

    def print(self, _3d=False):
        super().print()
        print(f"\tI'm the Monster {self.name}")


class Statistics:

    def print(self):
        print("Printing some statiscs...")