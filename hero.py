from random import randint

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
        
        actualDmg = randint(self.dmg - self.dmg * rateMin, self.dmg + self.dmg * rateMax)
        print(f'🔥 STRIKE! {self.name} attacked {enemy.name} - 🥊 DMG:{actualDmg}')
        

hero1 = Hero("Arthur", 3000, 5000, 1000, 200, "tanker")
hero2 = Hero("Valhein", 1000, 1000, 150, 800, "marksman")
hero1.introduce()