class PlayerStats:
  def __init__(self, name, classs, level, attack):
    self.name = name
    self.classs = classs
    self.level = level 
    self.attack = attack 


def display_player_stats(player):
  print("Your name is " + player.name)
  print("Your class is " + player.classs)
  print("Your level is %f" % (player.level))
  print("Your attack is %d" % (player.attack))
  print("")

