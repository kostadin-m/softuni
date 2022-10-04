from pokemon import Pokemon


class Trainer:
    def __init__(self, name=None):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon.guild_name in [x.guild_name for x in self.pokemons]:
            return f'This pokemon is already caught'
        self.pokemons.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon):
        for index, value in enumerate(self.pokemons):
            if value.guild_name == pokemon:
                self.pokemons.pop(index)
            return f'You have released {pokemon}'
        return 'Pokemon is not caught'

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}' + '\n' + f'Pokemon count {len(self.pokemons)}' + '\n'
        for pokemon1 in self.pokemons:
            result += f'- {pokemon1.pokemon_details()}' + '\n'
        return result

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())