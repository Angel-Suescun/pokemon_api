# Pokemon API

API REST construida con Flask para simular encuentros de Pokemon, capturarlos y administrar un equipo en memoria.

## Caracteristicas

- Encuentra un Pokemon aleatorio usando la PokeAPI.
- Captura el ultimo Pokemon encontrado.
- Consulta el equipo actual.
- Busca un Pokemon del equipo por id o nombre.
- Libera un Pokemon del equipo por id o nombre.

## Estructura del proyecto

```text
pokemon_api/
|-- app.py
|-- controllers/
|   |-- pokemon_controller.py
|-- services/
|   |-- pokemon_service.py
|-- repositories/
|   |-- pokemon_repository.py
|-- README.md
```

## Arquitectura

- Controller: expone endpoints HTTP y devuelve codigos de estado.
- Service: contiene la logica de negocio y llamadas a la PokeAPI.
- Repository: maneja almacenamiento en memoria del cache y del equipo.

## Requisitos

- Python 3.10 o superior
- pip

## Instalacion

1. Crear y activar entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
pip install flask requests
```

## Ejecutar la aplicacion

```powershell
python app.py
```

Servidor por defecto:

- http://127.0.0.1:5000

## Endpoints

### 1) Encontrar Pokemon

- Metodo: GET
- Ruta: /pokemon/encounter

Ejemplo:

```powershell
curl http://127.0.0.1:5000/pokemon/encounter
```

Respuesta esperada:

```json
{
	"id": 25,
	"name": "pikachu"
}
```

### 2) Capturar Pokemon en cache

- Metodo: POST
- Ruta: /pokemon/capture

Ejemplo:

```powershell
curl -X POST http://127.0.0.1:5000/pokemon/capture
```

Respuesta esperada:

```json
{
	"captured": {
		"id": 25,
		"name": "pikachu"
	},
	"team": ["pikachu"]
}
```

Si no hay Pokemon en cache:

```json
{
	"error": "No hay ningun Pokemon en cache para capturar."
}
```

### 3) Ver equipo

- Metodo: GET
- Ruta: /pokemon/team

Ejemplo:

```powershell
curl http://127.0.0.1:5000/pokemon/team
```

Respuesta esperada:

```json
["pikachu", "bulbasaur"]
```

### 4) Obtener Pokemon del equipo por id o nombre

- Metodo: GET
- Ruta: /pokemon/team/<identifier>

Ejemplos:

```powershell
curl http://127.0.0.1:5000/pokemon/team/25
curl http://127.0.0.1:5000/pokemon/team/pikachu
```

Respuesta esperada:

```json
{
	"id": 25,
	"name": "pikachu"
}
```

### 5) Liberar Pokemon del equipo por id o nombre

- Metodo: DELETE
- Ruta: /pokemon/team/<identifier>

Ejemplos:

```powershell
curl -X DELETE http://127.0.0.1:5000/pokemon/team/25
curl -X DELETE http://127.0.0.1:5000/pokemon/team/pikachu
```

Respuesta esperada:

```json
{
	"released": {
		"id": 25,
		"name": "pikachu"
	},
	"team": []
}
```

## Notas importantes

- El equipo se guarda en memoria. Al reiniciar el servidor, se pierde el estado.
- El endpoint de captura usa el ultimo Pokemon generado por encounter.
- La API depende de https://pokeapi.co para obtener datos de Pokemon.


