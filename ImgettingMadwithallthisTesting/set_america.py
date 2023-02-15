import Base
Locations = ["Radar"]
class Radar:
    def __init__(self, name, owner, workers, xCords, yCords, length, width): # in the future create a AddWorker or Do math to add workers 
        self.name = name
        self.xCords = xCords
        self.yCords = yCords
        self.length = length
        self.width = width
        self.owner = owner
        self.workers = workers


# class Industry:
#     def __init__(self, name, owner, workers ,xCords, yCords, length, width): # in the future create a AddWorker or Do math to add workers 
#         self.name = name
#         self.xCords = xCords
#         self.yCords = yCords
#         self.length = length
#         self.width = width
#         self.owner = owner
#         self.workers = workers

def set_america(name,owner,workers,xCords,yCords,length,width):        
    for x in range(0, 1, 1):
        # Xcords = int(input("\nset_america\nEnter X Cords For %s: " % Locations[x]))
        # # while Xcords > 500:
        #     # Xcords = int(input("X Cords Cannot be greater than 500, Enter X Cords Again: "))
        # Ycords = int(input("Enter Y Cords For %s: " % Locations[x]))
        # # while Ycords > 500:
        #     # Ycords = int(input("Y Cords Cannot be greater than 500, Enter Y Cords Again: "))


        if Locations[x] == "Radar":
            radar = Radar("Radar", owner, workers, xCords, yCords,length,width )
            
        return radar.name, radar.owner ,radar.workers, radar.xCords, radar.yCords, radar.length, radar.width


def test_set_america():
    test_cases =  [
                  ('Radar','Test',4000,200,300,400,500, ('Radar','Test',4000,200,300,400,500)),
                  ('Radar','Test',7500,375,450,800,230, ('Radar','Test',7500,375,450,800,230)),
                  ('Radar','player_Two',500,950,870,450,200, ('Radar','player_Two',500,950,870,450,200))

                  ]
    for i, (name, owner, workers, xCords, yCords, length, width, expected) in enumerate(test_cases):
            result = set_america(name,owner,workers,xCords,yCords,length,width)
            passed = result == expected
            status = "PASSED" if passed else "FAILED"
            print(f"\nTest {i}: {status}\nInput:    {result}\nExpected: {expected}\nGot:      {result}\n")

test_set_america()