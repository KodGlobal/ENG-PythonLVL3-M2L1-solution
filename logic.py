import aiohttp
import random
from random import randint

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.img = None
        self.power = random.randint(30, 60)
        self.hp = random.randint(200, 400)
        if pokemon_trainer not in self.pokemons:
            self.pokemons[pokemon_trainer] = self

    async def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['forms'][0]['name']
                else:
                    return "Pikachu"

    async def info(self):
        if not self.name:
            self.name = await self.get_name()
        return f"""The name of your Pokémon: {self.name}
                : {self.power}
                Здоровье покемона: {self.hp}"""

    async def show_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    img_url = data['sprites']['front_default']
                    return img_url 
                else:
                    return None

    async def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1, 5)
            if chance == 1:
                return "The Wizard Pokémon used a shield during the battle!"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"The Pokémon trainer @{self.pokemon_trainer} attacks @{enemy.pokemon_trainer}\nThe health of @{enemy.pokemon_trainer} now equals {enemy.hp}"
        else:
            enemy.hp = 0
            return f"The Pokémon trainer @{self.pokemon_trainer} defeated @{enemy.pokemon_trainer}!"

class Wizard(Pokemon):
    # Wizard specific methods and properties can be added to this class
    pass

class Fighter(Pokemon):
    async def attack(self, enemy):
        super_power = randint(5, 15)
        self.power += super_power
        result = await super().attack(enemy)
        self.power -= super_power
        return result + f""

class Wizard(Pokemon):
    # In this class, we can add methods and properties unique to the Wizard class
    pass

class Fighter(Pokemon):
    async def attack(self, enemy):
        super_power = randint(5, 15)
        self.power += super_power
        result = await super().attack(enemy)
        self.power -= super_power
        return result + f"\nThe Fighter Pokémon used a super-attack. The added power is:{super_power}"
