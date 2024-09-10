import random
import time

# Define player and enemy classes
class Player:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_enemy(self, enemy):
        enemy.health -= self.attack
        print(f"{self.name} attacked {enemy.name} for {self.attack} damage.")

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_player(self, player):
        player.health -= self.attack
        print(f"{self.name} attacked {player.name} for {self.attack} damage.")

# Create player and enemy instances
player = Player("Rendalith", 200, 20)
player2 = Player("Thalisean", 100, 20)
enemy = Enemy("Goblin", 50, 15)

# Game loop
while True:
    print("\nChoose an action:")
    print("1. Attack enemy")
    print("2. Check health")
    print("3. Quit")

    choice = int(input())

    if choice == 1:
        player.attack_enemy(enemy)
        if enemy.health <= 0:
            print("You defeated the Goblin!")
            break
        enemy.attack_player(player)
        if player.health <= 0:
            print("You were defeated by the Goblin!")
            break
    elif choice == 2:
        print(f"{player.name}'s health: {player.health}")
        print(f"{player2.name}'s health: {player2.health}")
        print(f"{enemy.name}'s health: {enemy.health}")
    elif choice == 3:
        print("Quitting the game...")
        break
    else:
        print("Invalid choice. Please try again.")