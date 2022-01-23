import random, math
from classes.magic import Spell
from classes.inventory import Item

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'         #Red
    ENDC = '\033[0m'          #(probably)(yeah its true) to end formating
    BOLD = '\033[1m'          #Bold
    UNDERLINE = '\033[4m'     #underline
    #Refer here: https://ozzmaker.com/add-colour-to-text-in-python/

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk-10
        self.atkh = atk+10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    '''def generate_spell_damage(self, i):
        mgl =  self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)'''

    def take_damage(self, dmg):
        self.hp -= dmg
        if(self.hp<0):
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if(self.hp > self.maxhp):
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    '''def get_spell_name(self, i):
        return self.magic[i]['name']'''

    '''def get_spell_mp_cost(self, i):
        return self.magic[i]['cost']'''

    def choose_action(self):
        print("\n" + "    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print("    " + bcolors.OKBLUE + bcolors.BOLD + "ACTIONS:" + bcolors.ENDC)
        i = 1
        for item in self.actions:
            print("      " + str(i) + ".", item)
            i+=1

    def choose_magic(self):
        i = 1
        print('\n' + "    " + bcolors.OKBLUE + bcolors.BOLD + "MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("          " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i+=1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "INVENTORY:" + bcolors.ENDC)
        for item in self.items:
            print("  " + str(i) + ".", item["item"].name + ":", item["item"].description, " (x" + str(item["quantity"]) + ")")
            i+=1

    def choose_target(self,  enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    Target:" + bcolors.ENDC)
        for enemy in enemies:
            print("        " + str(i) + ".", enemy.name)
            i+=1
        target = int(input("    Choose target: ")) - 1
        return target



    def get_enemy_stats(self):
        hp_bar = math.ceil(self.hp / self.maxhp * 50) * '█' + (50 - math.ceil(self.hp / self.maxhp * 50)) * ' '
        hp_blank_bar = ""
        if len(str(self.hp)) < 5:
            hp_blank_bar = (5 - len(str(self.hp))) * " "
        print("                      __________________________________________________")
        print(bcolors.BOLD + self.name + "   " + hp_blank_bar + str(self.hp) + "/" + str(
            self.maxhp) + " |" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|")

    def get_stats(self):
        hp_bar = math.ceil(self.hp/self.maxhp*25)*'█' + (25-math.ceil(self.hp/self.maxhp*25))*' '
        mp_bar = math.ceil(self.mp/self.maxmp*10)*'█' + (10-math.ceil(self.mp/self.maxmp*10))*' '
        hp_blank_bar = ""
        mp_blank_bar = ""
        if len(str(self.hp))<4:
            hp_blank_bar = (4-len(str(self.hp)))*" "
        if len(str(self.mp))<3:
            mp_blank_bar = (3-len(str(self.mp)))*" "
        print("                      _________________________                __________")
        print(bcolors.BOLD + self.name + "     " + hp_blank_bar + str(self.hp) + "/" + str(self.maxhp) + " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + "|      " + mp_blank_bar + str(self.mp) + "/" + str(self.maxmp) + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "| ")
        # "███████████████         "

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        magic = self.magic[magic_choice]
        magic_cost = magic.cost
        magic_name = magic.name
        magic_dmg = magic.dmg

        if self.mp < magic.cost or (magic.type=="White" and (self.hp/self.maxhp)>0.5):
            return self.choose_enemy_spell(self)
        else:
            return magic








#Problems:
'''
3 turns are completed even if enemy get killed in first one
If valos's mp is low and he uses mp then error is thrown and turn is passed in to nick
'''