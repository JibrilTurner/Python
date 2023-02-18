import Base
import itertools

class Radar:

    def __init__(self, name, owner, workers, xCords, yCords, length, width, population=None, radiusOfPeople=None,):
        self.name = name
        self.xCords = xCords
        self.yCords = yCords
        self.length = length
        self.width = width
        self.owner = owner
        self.workers = workers
        self.population = population
        self.radiusOfPeople = radiusOfPeople

class Industry:
    def __init__(self, name, owner, workers, xCords, yCords, length, width, population=None, radiusOfPeople=None):
        self.name = name
        self.xCords = xCords
        self.yCords = yCords
        self.length = length
        self.width = width
        self.owner = owner
        self.workers = workers
        self.population = population
        self.radiusOfPeople = radiusOfPeople

class Capital:
    def __init__(self, name,owner, population, xCords, yCords, radiusOfPeople):
        self.name = name
        self.owner = owner
        self.population = population
        self.xCords = xCords
        self.yCords = yCords
        self.radiusOfPeople = radiusOfPeople

class MissleDefenseSystem:
    def __init__(self, name, owner, workers, xCords, yCords, length, width, population=None, radiusOfPeople=None ,radiusOfAffect = None):
        self.name = name
        self.xCords = xCords
        self.yCords = yCords
        self.length = length
        self.width = width
        self.owner = owner
        self.workers = workers
        self.population = population
        self.radiusOfPeople = radiusOfPeople
        self.radiusOfAffect = radiusOfAffect

def set_america(name, owner, workers, xCords, yCords, length, width, population=None, radiusOfPeople=None,radiusOfAffect=None):
    if name == "Radar":
        location = Radar(name, owner, workers, xCords, yCords, length, width, population, radiusOfPeople,radiusOfAffect)
    elif name == "Capital":
        location = Capital(name,owner, population, xCords, yCords, radiusOfPeople)
    elif name == "Industry":
        location = Industry(name, owner, workers, xCords, yCords, length, width, population, radiusOfPeople)
    elif name == "MissleDefenseSystem":
        location = MissleDefenseSystem(name, owner, workers, xCords, yCords, length, width, population, radiusOfPeople,radiusOfAffect)
    else:
        raise ValueError(f"Invalid location name: {name}")
    return location.name, location.owner, location.population, location.xCords, location.yCords, location.radiusOfPeople, location.radiusOfAffect




my_capital = Capital(name='Capital', owner='Me', population=10000, xCords=150, yCords=175, radiusOfPeople=10)

def test_set_america():
    test_cases = [

                      ('Radar', 'Test', 4000, 200, 300, 400, 500, None, ('Radar', 'Test', 4000, 200, 300, 400, 500, None, 5)),
                    # ('Capital', 'Test', None, 234, 123, None, None, 8000, 5, ('Capital', 'Test', 8000, 234, 123, 5)),
                    # ('Industry', 'Test', 8000, 700, 900, 600, 400, None, 5, ('Industry', 'Test', 8000, 700, 900, 600, 400, None, 5)),
                    # ('MissleDefenseSystem', 'Test', 4000, 200, 300, 400, 500, None, 5, 4, ('MissleDefenseSystem', 'Test', 4000, 200, 300, 400,))





                    # (my_capital.name, my_capital.owner, None, my_capital.xCords, my_capital.yCords, None, None, my_capital.population, my_capital.radiusOfPeople, (my_capital.name, my_capital.owner, my_capital.population, my_capital.xCords, my_capital.yCords, my_capital.radiusOfPeople)),
                 ]
                 
    for i, (name, owner, workers, xCords, yCords, length, width, population, radiusOfPeople,radiusOfAffect,expected) in enumerate(test_cases):
        result = set_america(name, owner, workers, xCords, yCords, length, width, population, radiusOfPeople,radiusOfAffect)
        passed = result == expected
        status = "PASSED" if passed else "FAILED"
        print(f"\nTest {i}: {status}\nInput:    {result}\nExpected: {expected}\nGot:      {result}\n")

test_set_america()
