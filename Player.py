"""
name => string asked at begining of name
Pokedex => list, add to list every pokemon it meet
"""

from map import Map, Objects
from Pokemon import Poke
import random
import tool
import pygame

pygame.init()


class Player:
    PokeInventory = []
    name = ""
    pokedex = []
    position = [9, 39]
    Inventory = ["pokebowl", 0, "Potion de Soin", 0]
    forbidden = ["█"]

    def __init__(self, name, pokedex):
        self.name = name
        self.pokedex = pokedex

    def selectPokemon(self):
        print("Select a pokemon in your pokedex, number (1 -> 3)")
        for i in range(3):
            print(i, self.pokedex[i].name)
        userinput = input()
        return self.pokedex[userinput - 1]

    def ChoiceUser(self):
        print("Que voulez-vous faire ?\n")
        print("1 : Combattre")
        print("2 : Capturer")
        print("3 : Fuir")
        useript = input()
        if (ord(useript) > 51 or ord(useript) < 49):
            print("Entrez un chifre entre 1 et 3")
            self.ChoiceUser(self)
        else:
            return useript

    def UserChoiceInFight(self):
        print("Vous êtes maintenant en combat.")
        print("Que voulez vous faire ?")
        print("1 : Attaquer")
        print("2 : Vous soigner")
        print("3 : Capturer")
        useript = input()
        if (ord(useript) > 51 or ord(useript) < 49):
            print("Entrez un chifre entre 1 et 3")
            self.UserChoiceInFight(self)
        else:
            return useript

    def Combat(self, p):
        if (self.ChoiceUser(self) == '2'):
            if (self.Capture(p) == 0):
                return
        elif (self.ChoiceUser(self) == '3'):
            print("Vous prenez la fuite...")
            return
        elif (self.ChoiceUser(self) == '1'):
            fighter = self.selectPokemon(self)
            while (fighter.pv != 0 and p.pv != 0):
                info = self.UserChoiceInFight(self)
                if (info == '1'):
                    self.Attacks(self, fighter, p)
                    if (p.pv <= 0):
                        return
                elif (info == '2'):
                    if (self.Heal(self, fighter) != -1):
                        self.Heal(self, fighter)
                    else:
                        continue
                elif (info == '3'):
                    if (self.Capture(p) == 0):
                        print("Le Combat est donc terminé")
                        return
                self.AttackIA(self, p, fighter)
            a = fighter if fighter.pv > 0 else p

    # pok1 = pokémon attaquant
    # pok2 = pokémon attaqué
    def Attacks(self, pok1, pok2):
        print("Vous avez choisi d'attaquer !")
        print("Choisissez une des attaque de votre pokemon")
        for i in range(len(pok1.attacks)):
            print(i + 1, pok1.attacks[i])
        userSelect = tool.CheckedInput(1, len(pok1))
        print("Votre pokemon utilise " + pok1.attacks[userSelect])
        if (pok1.attacks[userSelect] != None):
            pok2.pv -= pok1.attacks[userSelect].damage
            print("Votre pokemon à enlevé " +
                  str(pok1.attacks[userSelect].damage) + " au pokémon adverse")
        else:
            self.AttackIA(pok1, pok2)

    # pok1 -> pokemon sauvage
    # pok2 -> pokemon apprivoisé
    def AttackIA(self, pok1, pok2):
        rdm = random.randint(0, len(pok1.attacks) - 1)
        if (pok1.attacks[rdm] != None):
            print("Votre pokemon utilise " + pok1.attacks[rdm])
            pok2.pv -= pok1.attacks[rdm].damage
            print("Le pokemon adverse à enlevé " +
                  str(pok1.attacks[rdm].damage) + " a votre pokemon")

    def Heal(self, pok):
        soin = 30
        if (self.Inventory[3] > 0):
            print("Vous soignez votre pokemon de " + soin + "pv")
            pok.pv += soin
            self.Inventory[3] -= 1
        else:
            print("Vous n'avez plus de potion de soin !")
            return -1

    def Capture(self, pok):
        prctpbol = 10
        prctPv = (1 - (pok.pv / pok.basepv)) * 100
        prctXp = (1 - (pok.xp / 60)) * 100
        if (prctPv + prctXp + prctpbol >= 105):
            self.PokeInventory.append(pok)
            print("Bravo ! vous venez de capturer un " + pok.name)
            return 0
        else:
            print("Ah mince, " + pok.name + " s'est échappé ! retente au prochain tour")
            return -1

    def AddToPokedex(self, *arg):
        for elem in arg:
            self.pokedex.append(elem)

    def AddToPokeInventory(self, *arg):

        for elem in arg:
            self.pokedex.append(elem)

    def SelectStarter(self):
        Ouisticram = Poke("Ouisticram", 0, "fire", 20)
        Tortipouss = Poke("Tortipouss", 0, "grass", 20)
        Tiplouf = Poke("Tiplouf", 0, "water", 20)
        self.AddToPokedex(Ouisticram, Tortipouss, Tiplouf)
        print(
            "Bonjour je me présente je suis le professeur DumbleDargent, Enchanté "
            + self.name +
            ", bienvenue dans ce monde pokemon, pret pour l'aventure ?")
        print(
            "Tu dois d'abord choisir ton premier pokemon. Tu as le choix entre 3 de mes meilleures recrues \n"
        )
        print("Lequel choisis-tu ?\n")
        print("1 : Tortipouss")
        print("2 : Ouisticram")
        print("3 : Tiplouf\n")
        print("Entre un nombre entre 1 et 3")
        ans = tool.CheckedInput(1, 3)
        if (ans == 1):
            self.PokeInventory.append(Ouisticram)
        elif (ans == 2):
            self.PokeInventory.append(Tortipouss)
        elif (ans == 3):
            self.PokeInventory.append(Tiplouf)

        print(
            "Ah, je vois que tu as choisis " + self.PokeInventory[0].name +
            ", c'est un très bon choix, beaucoup de puissance en lui, je le sens.\nVous êtes fait pour etre de bons amis. Maintenant, pars a l'exploration de kanto et complète ce pokedex pour moi."
        )
        return

    # █

    def Move(self):
        while True:
            key_input = pygame.key.get_pressed()
            if key_input[pygame.K_RIGHT]:
                if map.Map.decorpix[self.position[0]][self.position[1] + 1].asci not in self.forbidden:
                    self.position[1] += 1
            elif key_input[pygame.K_LEFT]:
                if map.Map.decorpix[self.position[0]][self.position[1] - 1].asci not in self.forbidden:
                    self.position[1] -= 1
            elif key_input[pygame.K_DOWN]:
                if map.Map.decorpix[self.position[0] - 1][self.position[1]].asci not in self.forbidden:
                    self.position[0] -= 1
            elif key_input[pygame.K_UP]:
                if map.Map.decorpix[self.position[0] + 1][self.position[1]].asci not in self.forbidden:
                    self.position[0] += 1