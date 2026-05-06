from random import random, randint, choice




class living:
    def __init__(self, name, health, attack, speed, moves=None):
        self.name = name
        self.health = health
        self.mp = 100 #mana points
        self.attack = attack
        self.speed = speed
        self.moves = moves if moves else []

    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage): 
        self.health -= damage
        print(f"{self.name} takes {damage} damage! HP left: {max(0, self.health)}")
    
    def deal_damage(self, target, mult):
        damage = int(self.attack * mult) + randint(-2, 5)
        target.take_damage(damage)

all_moves = [
    ["Agi", True, 10, 1, 1.3, True, False, "Burn", 0.75],
    ["Zio", True, 20, 1, 1.25, True, False, "Stun", 0.25],
    ["Bufu", True, 30, 1, 1.5, True, False, "Freeze", 0.25],
    ["Dia", False, 15, 1,  2, False, False, "Heal", 0.95] # Name, is_offensive, mp/hp cost, mp(1)/hp(2) damage_mult, hit all, effect, effect chance
]

def battle(player, enemy1, enemy2):
    print(f"\n=== {player.name} vs {enemy1.name} & {enemy2.name} ===\n")
    
    while player.is_alive() and (enemy1.is_alive() or enemy2.is_alive()):
        print(f"\n{player.name} HP: {player.health} MP: {player.mp}")
        print(f"{enemy1.name} HP: {enemy1.health} | {enemy2.name} HP: {enemy2.health}")
        print("1. Attack  2. Special  3. Run")
        action = input("Choose: ")
        
        if action == "1":
            print(f"Attack 1. {enemy1.name}  2. {enemy2.name}")
            target = input("Choose target: ")
            if target == "1" and enemy1.is_alive():
                player.deal_damage(enemy1, 1.0)
            elif target == "2" and enemy2.is_alive():
                player.deal_damage(enemy2, 1.0)
            else:
                print("Invalid target!")
                continue
        elif action == "2":
            if not player.moves:
                print("No special moves available!")
                continue
            print("Available moves:")
            for i, move in enumerate(player.moves):
                print(f"{i + 1}. {move[0]} (MP Cost: {move[2]}, Damage Mult: {move[3]})")
            move_choice = input("Choose a move: ")
            if not move_choice.isdigit() or int(move_choice) < 1 or int(move_choice) > len(player.moves):
                print("Invalid move choice!")
                continue
            player.mp -= player.moves[int(move_choice) - 1][2]
            move = player.moves[int(move_choice) - 1]
            print(f"Attack 1. {enemy1.name}  2. {enemy2.name}")
            target = input("Choose target: ")
            if target == "1" and enemy1.is_alive():
                print(f"{player.name} uses {move[0]}!")
                player.deal_damage(enemy1, move[3])
            elif target == "2" and enemy2.is_alive():
                print(f"{player.name} uses {move[0]}!")
                player.deal_damage(enemy2, move[3])
            else:
                print("Invalid target!")
                continue
        elif action == "3":
            print(f"{player.name} ran away!")
            return False
        else:
            print("Invalid choice!")
            continue
        
        if enemy1.is_alive():
            enemy1.deal_damage(player, 1.0)
        if enemy2.is_alive():
            enemy2.deal_damage(player, 1.0)
    
    if player.is_alive():
        print(f"\n{player.name} wins!\n")
        return True
    else:
        print(f"\nYou were defeated!\n")
        return False


def main():
    player = living("Hero", 100, 15, 10, [all_moves[0], all_moves[1]])
    enemy1 = living("Goblin", 60, 10, 8)
    enemy2 = living("Orc", 50, 12, 7)
    
    # TODO: Add map system here later
    battle(player, enemy1, enemy2)


if __name__ == "__main__":
    main()
