from flask import Blueprint, jsonify, request

from services.pokemon_service import PokemonService

pokemon_bp=Blueprint("pokemon", __name__)
service= PokemonService


@pokemon_bp.route("pokemon/encounter", methods=["GET"])
def encounter() -> dict:
    result = service.encounter_pokemon()
    return jsonify(result), 200

@pokemon_bp.route("pokemon/capture", methods=["POST"])
def capture() -> dict:
    try:
        result = service.capture_pokemon()
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@pokemon_bp.route("pokemon/team", methods=["GET"])
def get_team()-> dict:
    team = service.get_team()
    return jsonify(team), 200


@pokemon_bp.route("pokemon/team/<identifer>", methods=["GET"])
def get_team(identifier: int | str)-> dict:
    try:
        pokemon = service.get_pokemon(identifier)
        return jsonify(pokemon), 200
    except LookupError as e:
        return jsonify({"error": str(e)}), 404


@pokemon_bp.route("pokemon/team/<identifer>", methods=["DELETE"])
def release_pokemon(identifier: int | str)-> dict:
    try:
        result = service.release_pokemon(identifier)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except LookupError as e:
        return jsonify({"error": str(e)}), 404



