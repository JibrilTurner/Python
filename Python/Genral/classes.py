##
## Created by Jibril on 01/18/2023.
##
class PlayerStats:
  def __init__(self, name, classs, level, attack):
    self.name = name
    self.classs = classs
    self.level = level 
    self.attack = attack 

p2 = PlayerStats("Jibril","mage",17.5,10)

print("Your name is " + p2.name)
print("Your class is " + p2.classs)
print("your level is %f" % (p2.level))
print("your attack is %d" % (p2.attack))
print("")
