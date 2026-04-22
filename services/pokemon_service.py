import random
import requests
from repositories.pokemon_repository import PokemonRepository

class PokemonService:
    def __init__(self) -> None:
        self.repo = PokemonRepository()

    def encounter_pokemon(self) -> None:
        
