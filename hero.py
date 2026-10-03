from random import randint
from time import sleep
class Hero():
    # constructor
    def __init__(self, name, hp, mana, armor, dmg, hero_type):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.armor = armor
        self.dmg = dmg
        self.hero_type = hero_type
    # method print info
    def introduce(self):
        print(f"====> Hero: {self.name} <====")
        print(f"- Hero type: {self.hero_type}")
        print(f"- Health: {self.hp}")
        print(f"- Mana: {self.mana}")
        print(f"- Armor: {self.armor}")
        print(f"- Damage: {self.dmg}")
        print("======================")

    def strike(self, enemy):
        rateMin = 0.2
        rateMax = 0.2
        if (self.hero_type == "tanker"):
            rateMin = 0.1
            rateMax = 0.1
        if (self.hero_type == "marksman"):
            rateMin = 0.2
            rateMax = 0.6
        
        actualDmg = randint(round(self.dmg - self.dmg * rateMin), round(self.dmg + self.dmg * rateMax))
        print(f'🔥 STRIKE! {self.name} attacked {enemy.name} - 🥊 DMG:{actualDmg}')
        enemy.armor -= actualDmg
        if enemy.armor < 0:
            enemy.hp += enemy.armor
            enemy.armor = 0
        print("========================================")
        print(f'🤺 STRIKE! Hero {enemy.name} has been hit!')
        print(f'- 🎽 Armor: {enemy.armor}')
        print(f'- ❤️‍🩹 HP: {enemy.hp}')

    def fight(self, enemy):
        while self.hp > 0 and enemy.hp > 0:
            # Self attack enemy
            self.strike(enemy)
            if enemy.hp <= 0:
                print(f'☠️ Hero {enemy.name} has fallen!')
                break
            sleep(5)
            # enemy attack self
            enemy.strike(self)
            if self.hp <= 0:
                print(f'☠️ Hero {enemy.name} has fallen!')
                break
# main program
valhein = Hero("Valhein", 1000, 1000, 150, 800, "marksman")
arthur = Hero("Arthur", 3000, 5000, 1000, 200, "tanker")
tara = Hero("Tara", 2500, 6000, 800, 350, 'tanker')

print("Welcome to Arena of Valor")
sleep(2)
print('Please select the type of mission: ')
mission = int(input("0 - Exit the game \n1 - Introduce your self \n2 - Attack enemy\n"))
while mission != 0:
    if mission == 1:
        valhein.introduce()
    if mission == 2:
        print("What boss you want to fight?")
        type = int(input("1 - Arthur  2 - Tara \n"))
        if type == 1:
            valhein.fight(arthur)
            if valhein.hp > 0:
                print("You Win! 🥇")
    mission = int(input("0 - Exit the game \n1 - Introduce your self \n2 - Attack enemy\n"))
