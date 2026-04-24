import random
import requests
from repositories.pokemon_repository import PokemonRepository

class PokemonService:
    def __init__(self) -> None:
        self.repo = PokemonRepository()

    def get_total_pokemon(self) -> int: 
        url = "https://pokeapi.co/api/v2/pokemon" 
        response = requests.get(url) 
        data = response.json() 
        return data["count"]

    def encounter_pokemon(self) -> dict:
        pokemon_id = random.randint(1, self.get_total_pokemon())
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}" 
        response = requests.get(url) 
        if response.status_code != 200:
            raise ValueError("Error al obtener el Pokémon de la API.")
        data = response.json() 
        pokemon = { 
            "id": data["id"], 
            "name": data["name"] 
            } 
        self.repo.set_cache(pokemon) 
        return pokemon
    
    def capture_pokemon(self) -> dict: 
        pokemon = self.repo.get_cache() 
        if not pokemon: 
            raise ValueError("No hay ningún Pokémon en caché para capturar.")
        self.repo.add_to_team(pokemon) 
        team = self.get_team() 
        self.repo.clear_cache()
        return { "captured": pokemon, "team": team }
        
    def get_team(self) -> list:
        team = self.repo.get_team()
        return [pokemon["name"] for pokemon in team]
    
    def get_pokemon(self, identifier: int | str) -> dict:
        team = self.repo.get_team()
        for pokemon in team:
            if str(pokemon["id"]) == str(identifier) or pokemon["name"].lower() == str(identifier).lower():
                return pokemon
        raise LookupError("Pokémon no encontrado en el equipo.")
    
    def release_pokemon(self, identifier: int | str) -> dict:
        team = self.repo.get_team()
        if not team:
            raise ValueError("El equipo está vacío. No hay Pokémon para liberar.")
        for pokemon in team:
            if str(pokemon["id"]) == str(identifier) or pokemon["name"].lower() == str(identifier).lower():
                self.repo.remove_from_team(pokemon)
                team = self.get_team()
                return {"released": pokemon, "team": team}
        raise LookupError("Pokémon no encontrado en el equipo.")
