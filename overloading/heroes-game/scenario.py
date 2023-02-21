class NotPrintableObjectError(Exception):
    
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class Scenario:

    def __init__(self):
        self.printable_objects = list()

    def add_printable_obj(self, printable_obj):
        self.printable_objects.append(printable_obj)

    def clear(self):
        print("Clearing the Printable Objects List")
        self.printable_objects.clear()

    def render(self):
        for printable in self.printable_objects:
            if isinstance(printable, PrintableObject):
                printable.print()
            else:
                raise NotPrintableObjectError('Fatal Error: A not printable object was found in the list!')


class PositionableObject:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 1


class PrintableObject(PositionableObject):

    def __init__(self):
        super().__init__()

    def print(self, _3d=False):
        if _3d is False:
            # Behavior 1
            print(f"--- I'm a printable object. ({self.x}, {self.y})")
        else:
            # Behavior 2
            print(f"--- I'm a printable object. ({self.x}, {self.y}), {self.z}")


class Obstacle(PrintableObject):
    
    def __init__(self, type="Rock"):
        super().__init__()
        self.type = type

    def print(self, _3d=False):
        super().print()
        print(f"\tI'm a {self.type}!")

# PositionableObject <--- Obstacle
# PositionableObject <--- Character <----- Hero
#                                    |
#                                    +---- Monster

# PositionableObject <--- PrintableObject <-------- Obstacle
#                                          +------- Character <----- Hero
#                                                              +---- Monster