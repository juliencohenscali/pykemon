from Attacks import CreateAttack

class Poke:
  xpCap = [10,30,60]
  element = { "fire":0,"water":1,"grass ":2}

  def __init__(self,name, xp, element, pv,attacks):
      self.attacks = attacks
      self.name = name
      self.xp = xp
      self.element = element
      self.pv = pv
      self.basepv = pv

  def Evolve(self):
      if(self.xp == self.xpCap[0]):
          self.name = "Super " + self.name
      elif(self.xp == self.xpCap[1]):
          l = self.name.split(' ')
          self.name = "Mega " + l[1]
      elif(self.xp == self.xpCap[2]):
          l = self.name.split(' ')
          self.name = "Giga " + l[1]

  def __print__(self):
    nextXpCap = 0
    for i in self.xpCap:
      if(self.xp <= i):
        nextXpCap = i
        break
    return ("Le pokémon " + self.name + " est de type " + self.element + " a " + str(self.pv) + " pv et a " + str(self.xp) + " point d'xp sur " + str(nextXpCap) + " avant sa prochaine évolution")



