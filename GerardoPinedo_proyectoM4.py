import requests
import os
import json

def obtener_datos_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    response = requests.get(url)

    if response.status_code == 404:
        print("¡Error! No se encontró el Pokémon especificado.")
        return None

    data = response.json()
    imagen_url = data['sprites']['front_default']
    peso = data['weight']
    altura = data['height']
    movimientos = [move['move']['name'] for move in data['moves']]
    habilidades = [ability['ability']['name'] for ability in data['abilities']]
    tipos = [tipo['type']['name'] for tipo in data['types']]

    pokemon_info = {
        'nombre': nombre_pokemon,
        'imagen_url': imagen_url,
        'peso': peso,
        'altura': altura,
        'movimientos': movimientos,
        'habilidades': habilidades,
        'tipos': tipos
    }

    return pokemon_info

def guardar_en_archivo(pokemon_info):
    carpeta_pokedex = 'pokedex'
    if not os.path.exists(carpeta_pokedex):
        os.makedirs(carpeta_pokedex)

    nombre_archivo = f"{carpeta_pokedex}/{pokemon_info['nombre']}.json"

    with open(nombre_archivo, 'w') as archivo:
        json.dump(pokemon_info, archivo)

def mostrar_info_pokemon(pokemon_info):
    print("Nombre:", pokemon_info['nombre'])
    print("Imagen:", pokemon_info['imagen_url'])
    print("Peso:", pokemon_info['peso'])
    print("Altura:", pokemon_info['altura'])
    print("Movimientos:", ", ".join(pokemon_info['movimientos']))
    print("Habilidades:", ", ".join(pokemon_info['habilidades']))
    print("Tipos:", ", ".join(pokemon_info['tipos']))

# Obtener el nombre del Pokémon desde el usuario
nombre_pokemon = input("Introduce el nombre de un Pokémon: ")

# Obtener los datos del Pokémon desde la API
pokemon_info = obtener_datos_pokemon(nombre_pokemon)

if pokemon_info:
    # Guardar la información del Pokémon en un archivo .json
    guardar_en_archivo(pokemon_info)

    # Mostrar la información del Pokémon al usuario
    mostrar_info_pokemon(pokemon_info)
