from flask import jsonify
from services.pokemon_service import PokemonService


service = PokemonService()

def register_routes(app) -> None:

    @app.route("/pokemon/encounter", methods=["GET"])
    def encounter()-> tuple[dict, int]:
        result = service.encounter_pokemon()
        return jsonify(result), 200
    
    @app.route("/pokemon/capture", methods=["POST"])
    def capture()-> tuple[dict, int]:
        try:
            result = service.capture_pokemon()
            return jsonify(result), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        
    @app.route("/pokemon/team", methods=["GET"])
    def get_team()-> tuple[dict, int]:
        team = service.get_team()
        return jsonify(team), 200
    
    @app.route("/pokemon/team/<identifier>", methods=["GET"])
    def get_pokemon(identifier)-> tuple[dict, int]:
        try:
            pokemon = service.get_pokemon(identifier)
            return jsonify(pokemon), 200
        except LookupError as e:
            return jsonify({"error": str(e)}), 404
        
    @app.route("/pokemon/team/<identifier>", methods=["DELETE"])
    def release_pokemon(identifier)-> tuple[dict, int]:
        try:
            result = service.release_pokemon(identifier)
            return jsonify(result), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except LookupError as e:
            return jsonify({"error": str(e)}), 404