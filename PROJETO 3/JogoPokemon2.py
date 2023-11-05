import random
from random import randint

# Classes


class Pokemon:
    def __init__(self, name, type, hp, attack, defense, move1, move2):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.move1 = move1
        self.move2 = move2

    def attack(self, other_pokemon):
        # Calculate the damage done by this Pokemon's attack.
        damage = self.attack * (1 - other_pokemon.defense / 100)
        # Apply the damage to the other Pokemon.
        other_pokemon.hp -= damage

    def defend(self, other_pokemon):
        # Calculate the damage done to this Pokemon by the other Pokemon's attack.
        damage = other_pokemon.attack * (1 - self.defense / 100)
        # Apply the damage to this Pokemon.
        self.hp -= damage


class GrassPokemon(Pokemon):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, "Grass", hp, attack, defense)

    def attack(self, other_pokemon):
        # Grass Pokemon are strong against Water Pokemon.
        if other_pokemon.type == "Water":
            damage = self.attack * 1.5
        else:
            damage = self.attack
        # Apply the damage to the other Pokemon.
        other_pokemon.hp -= damage


class FirePokemon(Pokemon):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, "Fire", hp, attack, defense)

    def attack(self, other_pokemon):
        # Fire Pokemon are strong against Grass Pokemon.
        if other_pokemon.type == "Grass":
            damage = self.attack * 1.5
        else:
            damage = self.attack
        # Apply the damage to the other Pokemon.
        other_pokemon.hp -= damage


class WaterPokemon(Pokemon):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, "Water", hp, attack, defense)

    def attack(self, other_pokemon):
        # Water Pokemon are strong against Fire Pokemon.
        if other_pokemon.type == "Fire":
            damage = self.attack * 1.5
        else:
            damage = self.attack
        other_pokemon.hp -= damage


# Iniciais
charmander = Pokemon('charmander', 'Fire', 50, 15, 20, 'scratch', 'growl')
bulbasaur = Pokemon('bulbasaur', 'Grass', 50, 15, 20, 'tackle', 'growl')
squirtle = Pokemon('squirtle', 'Water', 50, 15, 20, 'tackle', 'tail whip')
iniciais = {0: bulbasaur, 1: charmander, 2: squirtle}
rival = {0: bulbasaur, 1: charmander, 2: squirtle}

# Escolha
while True:
    starter = int(
        input('Choose a pokémon.\n0 - Bulbasaur\n1 - Charmander\n2 - Squirtle\n'))
    if starter > 2 or starter < 0:
        print('Please, try again')
    else:
        break

# Definir o inicial
for i in range(0, 3):
    if starter == i:
        self_pokemon = iniciais[i]

rival_pokemon = random.choice(rival)

# Inicio da batalha
print('Prepare-se para a batalha!')
print(f'Go, {self_pokemon.name}!')
print(f'Rival send out {rival_pokemon.name}!')

# Batalha
while self_pokemon.hp > 0 and rival_pokemon.hp > 0:
    atack = int(input(
        f'What atack should be used?\n1 is {self_pokemon.move1} \n2 is {self_pokemon.move2}.\n'))
    while True:
        if atack > 2 or atack < 1:
            print('Please try again.')
        else:
            break
    if atack == 1:
        # Charmander Vs Bulbasaur
        if self_pokemon.type == 'Fire' and rival_pokemon == 'Grass':
            print(
                f'{self_pokemon.name} used {self_pokemon.move1}! {rival_pokemon.name} lost {damage} hp!')
            rival_pokemon.hp -= FirePokemon.attack
        # Charmander Vs Squirtle
        elif self_pokemon == iniciais[1] and rival_pokemon == iniciais[2]:
            damage = randint(10, 15)
            print(
                f'{self_pokemon.name} used {self_pokemon.move1}! {rival_pokemon.name} lost {damage} hp!')
            rival_pokemon.hp -= damage
        # Bulbasaur Vs Charmander
        elif self_pokemon == iniciais[0] and rival_pokemon == iniciais[1]:
            damage = randint(10, 15)
            print(
                f'{self_pokemon.name} used {self_pokemon.move1}! {rival_pokemon.name} lost {damage} hp!')
            rival_pokemon.hp -= damage
        # Bulbasaur Vs Squirtle
        elif self_pokemon == iniciais[0] and rival_pokemon == iniciais[2]:
            damage = randint(10, 20)
            print(
                f'{self_pokemon.name} used {self_pokemon.move1}! {rival_pokemon.name} lost {damage} hp!')
            rival_pokemon.hp -= damage
        # Squirtle Vs Bulbasaur
        elif self_pokemon == iniciais[2] and rival_pokemon == iniciais[0]:
            damage = randint(10, 15)
            print(
                f'{self_pokemon.name} used {self_pokemon.move1}! {rival_pokemon.name} lost {damage} hp!')
            rival_pokemon.hp -= damage
        # Squirtle Vs Charmander
        elif self_pokemon == iniciais[2] and rival_pokemon == iniciais[1]:
            damage = randint(10, 20)
            print(
                f'{self_pokemon.name} used {self_pokemon.move1}! {rival_pokemon.name} lost {damage} hp!')
            rival_pokemon.hp -= damage
    else:
        print(
            f'{self_pokemon.name} used {self_pokemon.move2}! For instance, it do nothing!')

    rival_atack = randint(1, 2)
    if rival_atack == 1:
        if self_pokemon == iniciais[1] and rival_pokemon == iniciais[0]:
            damage = randint(10, 20)
            print(
                f'{self_pokemon.name} used {self_pokemon.move1}! {rival_pokemon.name} lost {damage} hp!')
            rival_pokemon.hp -= damage
        # Charmander Vs Squirtle
        elif self_pokemon == iniciais[1] and rival_pokemon == iniciais[2]:
            damage = randint(10, 15)
            print(
                f'{self_pokemon.name} used {self_pokemon.move1}! {rival_pokemon.name} lost {damage} hp!')
            rival_pokemon.hp -= damage
        # Bulbasaur Vs Charmander
        elif self_pokemon == iniciais[0] and rival_pokemon == iniciais[1]:
            damage = randint(10, 15)
            print(
                f'{self_pokemon.name} used {self_pokemon.move1}! {rival_pokemon.name} lost {damage} hp!')
            rival_pokemon.hp -= damage
        # Bulbasaur Vs Squirtle
        elif self_pokemon == iniciais[0] and rival_pokemon == iniciais[2]:
            damage = randint(10, 20)
            print(
                f'{self_pokemon.name} used {self_pokemon.move1}! {rival_pokemon.name} lost {damage} hp!')
            rival_pokemon.hp -= damage
        # Squirtle Vs Bulbasaur
        elif self_pokemon == iniciais[2] and rival_pokemon == iniciais[0]:
            damage = randint(10, 15)
            print(
                f'{self_pokemon.name} used {self_pokemon.move1}! {rival_pokemon.name} lost {damage} hp!')
            rival_pokemon.hp -= damage
        # Squirtle Vs Charmander
        elif self_pokemon == iniciais[2] and rival_pokemon == iniciais[1]:
            damage = randint(10, 20)
            print(
                f'{self_pokemon.name} used {self_pokemon.move1}! {rival_pokemon.name} lost {damage} hp!')
            rival_pokemon.hp -= damage
    else:
        print(
            f'{rival_pokemon.name} use {rival_pokemon.move2} For instance, it do nothing!')

# Final da batalha
if rival_pokemon.hp <= 0:
    print('Congratulations! You won!')
    print(f'{self_pokemon.name} still have {self_pokemon.hp} hp.')
elif self_pokemon.hp <= 0:
    print('Oh man, you lost!')
    print(f'{rival_pokemon.name} still have {rival_pokemon.hp} hp.')
