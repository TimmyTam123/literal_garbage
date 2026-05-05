from random import random


print("Hello, World!")

class living:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage): 
        self.health -= damage
        print(f"{self.name} takes {damage} damage! HP left: {max(0, self.health)}")
    
    def deal_damage(self, target):
        damage = self.attack + random.randint(-2, 5)  # Add some randomness to the attack
        target.take_damage(damage)
