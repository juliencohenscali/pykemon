class CreateAttack:

    def __init__(self, nom, typeBase, damage):
        self.nom = nom
        self.typeBase = typeBase
        self.damage = damage

    def __print__(self):
      return self.nom

