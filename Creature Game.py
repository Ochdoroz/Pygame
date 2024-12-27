from random import randint
# create a class named "Monster" that has the following attributes:
# name, health, attack_damage, critical_hit_chance


# each monster should also have the following methods:
class Monster:  
    # __init__() method that takes in the
    # name, health, attack_damage, and critical_hit_chance
    def __init__(self, name, health, attack_damage, critical_hit_chance):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.critical_hit_chance = critical_hit_chance
        if critical_hit_chance < 0:
            raise Exception(f'Value is below 0 for Crit Chance on monster "{name}"')

# __str__() method that returns a string representation of the monster
    def __str__(self):
        return f"Name:{self.name},Health:{self.health}, Attack Damage:{self.attack_damage},Critical Hit Chance:{self.critical_hit_chance}"

# get_attack_damage() method that returns the attack damage to
# the monster for a single attack. if the monster lands a critical hit
# the damage will be doubled.
    
    def get_attack_damage(self):
        critical_hit = randint(1, 100)
        if critical_hit < self.critical_hit_chance:
            return self.attack_damage * 2
        return self.attack_damage
    
    def get_attack_stat(self):
        return self.attack_damage

# get_healthpoints() method that returns the health points of the monster
    def get_healthpoints(self):
        return self.health

# is_asleep() method that returns True if the monster has 0 health
    def is_asleep(self):
        return self.health == 0

    def get_name(self):
        return self.name
# take_damage() method that takes in an integer amount of damage and
# subtracts it from the monster's health. if the monster's health goes
# below 0, set the health to 0.

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0


# write another class named "FightSimulation" that has the following
# attributes:
# monster1, monster2, game_over
class FightSimulation:
    # you should have the following methods:

    # __init__() method that takes in two monsters
    def __init__(self, monster1, monster2):
        self.monster1 = monster1
        self.monster2 = monster2
        self.gameover = 0

# fight() method that simulates a fight between the two monsters as follows:
# randomly choose which monster attacks first. then, have the monsters
# take turns attacking each other until one of them is asleep. if the
# monster that is asleep is monster1, set game_over to 1. if the monster
# that is asleep is monster2, set game_over to 2.
# fight() should print details of damage dealt and health remaining for 
# each monster
    def fight(self):
        if self.gameover == 0:
            print(f"It a fight between {self.monster1} and {self.monster2}")
            turn = randint(1, 2)
            if turn == 1:
                attacking = self.monster1
                defending = self.monster2
            else:
                attacking = self.monster2
                defending = self.monster1
            while True:
                attack = attacking.get_attack_damage()
                print(f"{defending.get_name()} has {defending.get_healthpoints()} health")
                if attack > attacking.get_attack_stat():
                    print(f"{attacking.get_name()} dealt a critical {attack} damage!")
                else:
                    print(f"{attacking.get_name()} dealt {attack} damage!")
                defending.take_damage(attack)
                remaining_health = defending.get_healthpoints()
                print(f"{defending.get_name()} took {attack} damage they have {remaining_health} remaining health")
                if defending.is_asleep():
                    break
                tmp = attacking
                attacking = defending
                defending = tmp
            if defending == self.monster1:
                self.gameover = 1
            else:
                self.gameover = 2
        else:
            # either print that the game is over and cannot fight again
            # or raise an exception
            raise Exception(' you cannot fight a fight that has been finished')
    # __str__() method that returns a string representation of the fight.
    # it should be one of:
    # Dracula has won the fight against Balrog
    # Godzilla has won the fight against King Kong
    # The fight between Banshee and Ghost is to commence

    def __str__(self):
        if self.gameover == 1:
            return f'{self.monster2.get_name()} has won the fight against {self.monster1.get_name()}!'
        if self.gameover == 2:
            return f'{self.monster1.get_name()} has won the fight against {self.monster2.get_name()}!'
        else:
            return f"the fight between {self.monster2.get_name()} and {self.monster1.get_name()} is about to commence"


# write a main() function that creates 2 monsters and simulates a fight between them
# print the results of the fight
def creature_builder():
    creature_builder_lst = []
    print('Please follow instructions carefully, failure to do so could result in termination of your creature')
    print('please enter your creatures name (no longer then 20 characters)')
    name = str(input())
    if len(name) > 20:
        raise Exception('invalid name, creature terminated')
    creature_builder_lst.append(name)
    acceptable_characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    print('enter your creature health as a number')
    health = str(input())
    for char in health:
        if char != '0':
            break
        else:
            raise Exception('invalid health, creature terminated')
    for char in health:
        if char not in acceptable_characters:
            raise Exception('invalid health, creature terminated')
    creature_builder_lst.append(int(health))
    print('enter attack damage as a number')
    attack = str(input())
    for char in attack:
        if char not in acceptable_characters:
            raise Exception('invalid attack, creature terminated')
    creature_builder_lst.append(int(attack))
    print('enter critical hit chance as a number(the higher the number the more likely to land a critical hit)')
    critical_hit_chance = str((input()))
    for char in critical_hit_chance:
        if char not in acceptable_characters:
            raise Exception('invalid critical_hit_chance, creature terminated')
    creature_builder_lst.append(int(critical_hit_chance))
    return creature_builder_lst


def file_reader():
    """Reads the file and returns a dictionary of the creatures"""
    creatures = {

    }
    file = open('creatures.txt', 'r')
    while True:
        line = file.readline().strip()
        if line == '':
            break
        creature = line.split(' ')
        name = creature[0]
        creature.pop(0)
        creatures[name] = creature
    file.close()
    return creatures


def create_monster(player, creatures):
    """Creates a monster from the creatures dictionary"""
    name = player
    health, attack, critical_hit_chance = map(int, creatures.get(player))
    return Monster(name, health, attack, critical_hit_chance)


def build_creature(creatures):
    """Builds a creature and adds it to the creatures dictionary"""
    while True:
        try:
            creature = creature_builder()
            break
        except Exception as e:
            print(e)
    name = creature[0]
    creature.pop(0)
    creatures[name] = creature
    return creatures


def display_creatures(creatures):
    """Displays the creatures in the creatures dictionary"""
    print('Here are the creatures you can choose from:')
    for key in creatures:
        print(key.capitalize())


def display_stats(creatures):
    """Displays the stats of the creatures in the creatures dictionary"""
    print('Type in a creature\'s name to see its stats:')
    for key in creatures:
        print(key.capitalize())
    while True:
        ans = str(input()).lower()
        if creatures.get(ans) is None:
            print("That creature doesn't exist please try again")
        else:
            print(f"Health:{creatures.get(ans)[0]}, Attack Damage:{creatures.get(ans)[1]}, Critical Hit Chance:{creatures.get(ans)[2]}")
        print('Would you like to see another creature\'s stats?')
        ans = str(input()).lower()
        if ans != 'yes' and ans != 'y':
            break


def select_opponents_creature(creatures):
    """Selects a creature from the creatures dictionary"""
    print('Select a creature for your opponent:')
    for key in creatures:
        print(key.capitalize())
    while True:
        player = str(input()).lower()
        if creatures.get(player) is None:
            print("That creature doesn't exist please try again")
        else:
            break
    return player


def select_creature(creatures):
    """Selects a creature from the creatures dictionary"""
    print('Select which creature you want to use:')
    for key in creatures:
        print(key.capitalize())
    while True:
        player = str(input()).lower()
        if creatures.get(player) is None:
            print("That creature doesn't exist please try again")
        else:
            break
    return player


def selecting_creatures():
    """Selects the creatures to fight"""
    print('Do you want to build your own creature?')
    ans = str(input().lower())
    creatures = file_reader()
    if ans == 'yes' or ans == 'y':
        while True:
            creatures = build_creature(creatures)
            print('Would you like to create another creature?')
            ans = str(input()).lower()
            if ans != 'yes' and ans != 'y':
                break
    display_creatures(creatures)
    print('Would you like to see a creature\'s stats?')
    ans = str(input()).lower()
    if ans == 'yes' or ans == 'y':
        display_stats(creatures)
    print('Would you like to fight a creature?')
    ans = str(input()).lower()
    if ans != 'yes' and ans != 'y':
        return None
    player_one = select_creature(creatures)
    player_two = select_opponents_creature(creatures)
    monster1 = create_monster(player_one, creatures)
    monster2 = create_monster(player_two, creatures)
    return monster1, monster2, creatures


def main():
    competitors = selecting_creatures()
    if competitors is None:
        print('you have chosen not to fight, have a nice day')
    else:
        fight = FightSimulation(competitors[0], competitors[1])
        print (fight)
        fight.fight()
        print(fight)
        print('Would you like to save your creatures?')
        ans = str(input()).lower()
        if ans == 'yes' or ans == 'y':
            file_writer(competitors[2])






def file_writer(creatures):
    """Writes the creatures dictionary to a file"""
    file = open('creatures.txt', 'w')
    for key in creatures:
        file.write(key + ' ')
        for item in creatures.get(key):
            file.write(str(item) + ' ')
        file.write('\n')
    file.close()



if __name__ == "__main__":
    main()

