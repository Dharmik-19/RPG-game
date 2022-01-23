import random
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

'''
print("\n\n")
print("NAME                HP                                     MP")
print("                    _________________________              __________")
print(bcolors.BOLD + "Valos:     460/460 |" + bcolors.OKGREEN + "███████████████         " + bcolors.ENDC + bcolors.BOLD + " |      65/65 |" + bcolors.OKBLUE + "██████████" + bcolors.ENDC + "| ")

print("                    _________________________              __________")
print("Valos:     460/460 |                         |      65/65 |          | ")

print("                    _________________________              __________")
print("Valos:     460/460 |                         |      65/65 |          | ")
print("\n\n")'''







# Create black magic
fire = Spell("Fire", 25, 600, "Black")
thunder = Spell("Thunder", 25, 600, "Black")
blizzard = Spell("Blizzard", 25, 600, "Black")
meteor = Spell("Meteor", 40, 1200, "Black")
quake = Spell("Quake", 14, 140, "Black")

# Create white magic
cure = Spell("Cure", 25, 650, "White")
cura = Spell("Cura", 32, 1500, "White")
curaga = Spell("Curaga", 50, 6000, "white")

#Create inventory
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("super potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully resrores HP/MP of any one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)





'''magic= [{"name": "Fire", "cost": 10, "dmg": 100},
        {"name": "Thunder", "cost": 12, "dmg": 124},
        {"name": "Blizzard", "cost": 10, "dmg": 100}]'''

# Instantioting people
player_magic = [fire, thunder, blizzard, meteor, cure, cura]
enemy_magic = [fire, meteor, curaga]

player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}]

player1 = Person("Valos ", 3260, 132, 300, 34, player_magic, player_items)
player2 = Person("Nick  ", 4160, 188, 311, 34, player_magic, player_items)
player3 = Person("Robot ", 3089, 174, 288, 34, player_magic, player_items)
players = [player1, player2, player3]

enemy1 = Person("Imp    ", 1250, 130, 560, 325, enemy_magic, [])
enemy2 = Person("Magus ", 18200, 701, 525, 25, enemy_magic, [])
enemy3 = Person("Imp    ", 1250, 130, 560, 325, enemy_magic, [])
enemies = [enemy1, enemy2, enemy3]

defeated_enemies = 0
defeated_players = 0

running = True
while running:
    print("\n\n    ======================================================================")

    print("\n")
    print("NAME                 HP                                     MP")
    for player in players:
        player.get_stats()
    for enemy in enemies:
        enemy.get_enemy_stats()
    print("\n")

    for player in players:
        player.choose_action()
        player_choice1 = int(input("    Enter your choice: ")) - 1

        if player_choice1 == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("    " + player.name.replace(' ','') + " attacked " + enemies[enemy].name.replace(" ", "") + " dealing", int(dmg), "points of damage")

            if enemies[enemy].hp == 0:
                print("\n" + "    " + bcolors.FAIL + bcolors.BOLD + enemies[enemy].name.replace(" ", "") + " has died!" + bcolors.ENDC)
                del enemies[enemy]
                defeated_enemies += 1

            if defeated_enemies == 3:
                print("\n" + bcolors.OKGREEN + "    You are victorious!" + bcolors.ENDC)
                running = False
                break

        elif player_choice1 == 1:
            player.choose_magic()
            player_choice2 = int(input("    Enter your choice: ")) - 1

            if player_choice2 == -1:
                continue

            spell = player.magic[player_choice2]

            '''spell_cost = player.get_spell_mp_cost(player_choice2)
                spell = player.get_spell_name(player_choice2)'''

            spell_cost = spell.cost
            spell_name = spell.name

            if player.get_mp() < spell_cost:
                print(bcolors.FAIL + "\nNot enough MP" + bcolors.ENDC)
                continue

            player.reduce_mp(spell_cost)

            '''dmg = player.generate_spell_damage(player_choice2)'''

            dmg = spell.generate_damage()

            if spell.type == "White":
                player.heal(dmg)
                print(bcolors.OKBLUE + "    " + spell_name, "Increased", str(dmg), "points of", player.name.replace(' ','') +'`s' +  " health" + bcolors.ENDC)

            elif spell.type == "Black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(dmg)
                print(bcolors.OKBLUE + "    " + player.name.replace(' ',''), "deals", str(dmg), "points of damage to " + enemies[enemy].name.replace(" ", ""), "using", spell_name, "spell" + bcolors.ENDC)

                if enemies[enemy].hp == 0:
                    print(bcolors.FAIL + "    " + bcolors.BOLD + "Enemy Team`s " + enemies[enemy].name.replace(' ', '') + " has died!" + bcolors.ENDC)
                    del enemies[enemy]
                    defeated_enemies += 1

            if defeated_enemies == 3:
                print("\n" + bcolors.OKGREEN + "    You are victorious!" + bcolors.ENDC)
                running = False
                break

        elif player_choice1 == 2:
            player.choose_item()
            player_choice3 = int(input("    Enter your choice: ")) - 1

            if player_choice3 == -1:
                continue

            item = player.items[player_choice3]["item"]

            if player.items[player_choice3]["quantity"] == 0:
                print("\n" + "    " + bcolors.FAIL + item.name + "`s supplies exhausted!" + bcolors.ENDC)
                continue

            player.items[player_choice3]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print("    " + bcolors.OKGREEN + item.name + " heals for", str(item.prop), bcolors.ENDC)

            elif item.type == "elixer":
                if item.name == "MegaElixer":
                    for homie in players:
                        homie.hp = homie.maxhp
                        homie.mp = homie.maxmp
                    print("    " + bcolors.OKGREEN + item.name + " fully restored HP/MP of our team" + bcolors.ENDC)

                elif item.name == "Elixer":
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print("    " + bcolors.OKGREEN + item.name + " fully restord HP/MP of " + player.name.replace(" ", "") + bcolors.ENDC)

            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print("    " + bcolors.FAIL + player.name.replace(' ','') + " deal " + str(item.prop) + " points of damage to " + enemies[enemy].name.replace(' ', ''), "using", item.name + bcolors.ENDC)

                if enemies[enemy].hp == 0:
                    print(bcolors.FAIL + "\n    " + bcolors.BOLD + "Enemy Team`s " + enemies[enemy].name.replace(' ', '') + " has died!" + bcolors.ENDC)
                    del enemies[enemy]
                    defeated_enemies+=1

                if defeated_enemies == 3:
                    print("\n" + bcolors.OKGREEN + "    You are victorious!" + bcolors.ENDC)
                    running = False
                    break
        else:
            continue


    if defeated_enemies == 3:
        #print(bcolors.OKGREEN + "    You are victorious!" + bcolors.ENDC)
        #running = False
        break




    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        a = 0
        for i in enemy.magic:
            if i.cost > enemy.mp:
                a+=1
        if a == 3:
            enemy_choice = 0
        print(enemy_choice, enemy.mp)
        target = random.randrange(0, len(players))


        if enemy_choice == 0:
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print(bcolors.FAIL + "    " + enemy.name.replace(" ", "") +  " attacks " + players[target].name.replace(" ", "") + " dealing " +  str(enemy_dmg), " points of damage" + bcolors.ENDC)
            if players[target].hp == 0:
                print("\n    " + bcolors.FAIL + bcolors.BOLD + "Your teamate " + players[target].name.replace(" ","") + " has died!" + bcolors.ENDC)
                del players[target]
                defeated_players+=1
            if defeated_players == 3:
                print("\n" + bcolors.FAIL + "    You have been defeated!" + bcolors.ENDC)
                running = False
                break

        elif enemy_choice == 1:
            #name, cost, damage, type
            magic = enemy.choose_enemy_spell()
            magic_dmg = magic.generate_damage()
            enemy.reduce_mp(magic.cost)

            if magic.type == "White":
                enemy.heal(magic_dmg)
                print(bcolors.FAIL + "    " + enemy.name.replace(' ', ''), " Increases", str(magic_dmg),
                      "points of health using " + magic.name, "spell" + bcolors.ENDC)
            elif magic.type == "Black":
                players[target].take_damage(magic_dmg)
                print(bcolors.FAIL + "    " + enemy.name.replace(" ",""), "deals", str(magic_dmg), "points of damage to " + players[target].name.replace(" ", ""), "using", magic.name, "spell" + bcolors.ENDC)
            if players[target].hp == 0:
                print("\n    " + bcolors.FAIL + bcolors.BOLD + "Your teamate " + players[target].name.replace(" ","") + " has died!" + bcolors.ENDC)
                del players[target]
                defeated_players+=1
            if defeated_players == 3:
                print("\n" + bcolors.FAIL + "    You have been defeated!" + bcolors.ENDC)
                running = False
                break













    if defeated_players == 3:
        #print(bcolors.FAIL + "    You have been defeated!" + bcolors.ENDC)
        #running = False
        break

    '''print('---------------------------------')
    print(bcolors.FAIL + "Enemy HP:", str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print(bcolors.OKGREEN + "Your HP:", str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print(bcolors.OKBLUE + "Your MP:", str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")'''







#https://www.geeksforgeeks.org/inheritance-in-python/
#use it for inheritance
