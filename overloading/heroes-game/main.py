from scenario import Scenario, Obstacle, NotPrintableObjectError
from characters import Hero, Monster, Statistics

if __name__ == '__main__':
    scenario = Scenario()

    hero = Hero("Mathias")
    monster1 = Monster("Bad Wolf")
    monster2 = Monster("Alien X")
    tree = Obstacle(type="Tree")
    rock1 = Obstacle(type="Big Rock")
    rock2 = Obstacle(type="Small Rock")

    # statistics = Statistics()

    scenario.add_printable_obj(hero)
    scenario.add_printable_obj(monster1)
    scenario.add_printable_obj(monster2)

    # scenario.add_printable_obj(statistics)

    scenario.add_printable_obj(tree)
    scenario.add_printable_obj(rock1)
    scenario.add_printable_obj(rock2)


    try:
        scenario.render()
    except NotPrintableObjectError as error:
        # To see this error happening uncomment lines 14 and 20
        print(f"Not Printable Object Detected... ({error.msg})")
        scenario.clear()


