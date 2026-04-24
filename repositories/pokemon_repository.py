

class PokemonRepository:
    def __init__(self) -> None:
        self.team = []
        self.cache = None

    def set_cache(self, pokemon: dict) -> None:
        self.cache = pokemon

    def get_cache(self) -> dict | None:
        return self.cache
    
    def clear_cache(self) -> None:
        self.cache = None

    def get_team(self) -> list:
        return self.team
    
    def add_to_team(self, pokemon: dict) -> None:
        self.team.append(pokemon)

    def find_in_team(self, identifier: int | str) -> dict | None:
        for pokemon in self.team:
            if (str(pokemon["id"]) == str(identifier) or pokemon["name"].lower() == str(identifier).lower()):
                return pokemon
        return None
    
    def remove_from_team(self, pokemon: dict) -> None:
        self.team = [p for p in self.team if p["id"] != pokemon["id"]]