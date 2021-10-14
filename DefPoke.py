from Pokemon import Poke
from Attacks import CreateAttack

########################################################################
#Attaques
ice_beam = CreateAttack("Ice Beam","Ice", 50)
psychic = CreateAttack("Psychic","Psy",60)
confusion = CreateAttack("Confusion","Psy",40)
tri_attack = CreateAttack("Tri Attack","Normal",40)


flamethrower = CreateAttack("Flamethrower", "Fire",40)
fire_blast = CreateAttack("Fire Blast", "Fire",50)
waterfall = CreateAttack("Waterfall", "Water",40)
hydro_pump = CreateAttack("Hydro Pump", "Water",50)
giga_drain = CreateAttack("Giga Drain", "Grass",40)
solar_beam = CreateAttack("Solar Beam", "Grass",50)
wing_attack = CreateAttack("Wing CreateAttacks","Fly", 35)
drill_peck = CreateAttack("Drill Peck","Fly", 40)
fly = CreateAttack("Fly","Fly", 50)
tackle = CreateAttack("Tackle","Normal", 30)
scratch = CreateAttack("Scratch","Normal", 35)
rapid_spin = CreateAttack("Rapid Spin","Normal", 35)
slash = CreateAttack("Slash","Normal", 35)
mega_punch = CreateAttack("Mega Punch","Normal", 35)
tri_CreateAttacks = CreateAttack("Tri CreateAttacks","Normal", 40)
hyperbeam = CreateAttack("Hyperbeam","Normal", 55)
feint_CreateAttacks = CreateAttack("Feint CreateAttacks","Dark", 35)
pay_back = CreateAttack("Pay Back","Dark", 40)
crunch = CreateAttack("Crunch","Dark", 40)
thunder_bolt = CreateAttack("Thunder Bolt","Electric", 35)
thunder = CreateAttack("Thunder","Electric", 50)
high_jump_kick = CreateAttack("High Jump Kick","Combat", 50)
psybeam = CreateAttack("Psybeam","Psy", 50)
sludge_bomb = CreateAttack("Sludge Bomb","Poison", 40)
acid = CreateAttack("Acid","Poison", 40)
ice_punch = CreateAttack("Ice Punch","Ice", 35)


#######################################################################
#POKEMON :
mewtwo_attacks = [psychic, confusion, tri_attack, ice_beam]
mewtwo = Poke("Mewtwo", 60, "Psy",150, mewtwo_attacks)

charizard_attacks = [flamethrower, wing_attack, slash, fire_blast]
charizard = Poke("Charizard", 110,"Fire", 110, charizard_attacks)
