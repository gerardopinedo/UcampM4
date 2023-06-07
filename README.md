# UcampM4

Primero, asegúrate de tener la biblioteca Requests instalada. Puedes instalarla utilizando el siguiente comando:

pip install requests

Una vez que hayas instalado la biblioteca, se puede ejecutar el programa. 

El programa es una Pokédex virtual construida en Python utilizando la biblioteca Requests y la API de PokéAPI (https://pokeapi.co/). La Pokédex permite al usuario buscar información sobre los Pokémon ingresando sus nombres. Cuando el programa se ejecuta, el usuario introduce el nombre de un Pokémon. A continuación, el programa utiliza la biblioteca Requests para realizar una solicitud GET a la API de PokéAPI, obteniendo los datos correspondientes al Pokémon especificado. Si el Pokémon existe, el programa extrae la imagen frontal del Pokémon, su peso, altura, movimientos, habilidades y tipos desde la respuesta JSON de la API. Luego, el programa muestra la información obtenida, incluyendo la imagen, peso, altura, movimientos, habilidades y tipos del Pokémon al usuario. Además de mostrar la información al usuario, el programa guarda todos los datos del Pokémon, incluyendo el enlace a la imagen frontal del Pokémon, en un archivo JSON dentro de una carpeta llamada "pokedex" Si el Pokémon especificado no existe, el programa muestra un mensaje de error correspondiente. En resumen, el programa utiliza la biblioteca Requests para realizar solicitudes a la API de PokéAPI, extrae los datos necesarios del JSON de respuesta, muestra la información al usuario y guarda los datos en un archivo JSON en la carpeta "pokedex".
