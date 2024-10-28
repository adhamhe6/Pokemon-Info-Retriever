# import requests

# base_url = "https://pokeapi.co/api/v2/"

# def get_pokemon_info(name):
#     url = f"{base_url}/pokemon/{name}"
#     response = requests.get(url)
#     # print(response)
#     if response.status_code == 200:
#         # print("Data retrieved!")
#         pokemon_data = response.json()
#         # print(pokemon_data)
#         return pokemon_data
#     else:
#         print(f"Failed to retrieve data {response.status_code}")

# pokemon_name = "pikachu"
# pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info:
#     print(f"Name: {pokemon_info['name'].capitalize()}")
#     print(f"Id: {pokemon_info['id']}")
#     print(f"Height: {pokemon_info['height']}")
#     print(f"Weight: {pokemon_info['weight']}")


import requests
import logging
from functools import lru_cache

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

base_url = "https://pokeapi.co/api/v2/"

@lru_cache(maxsize=128)
def get_pokemon_info(name):
    """Retrieve Pokemon information from the API."""
    url = f"{base_url}pokemon/{name.lower()}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        logging.info(f"Data successfully retrieved for {name.capitalize()}")
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error occurred: {req_err}")
    return None

def display_pokemon_info(pokemon_data):
    """Display Pokemon information."""
    if not pokemon_data:
        print("No data available to display.")
        return

    print(f"\nName: {pokemon_data['name'].capitalize()}")
    print(f"Id: {pokemon_data['id']}")
    print(f"Height: {pokemon_data['height']}")
    print(f"Weight: {pokemon_data['weight']}")
    print(f"Base Experience: {pokemon_data['base_experience']}")
    print(f"Abilities: {', '.join([ability['ability']['name'] for ability in pokemon_data['abilities']])}")

def main():
    pokemon_name = input("Enter the name of the Pokémon: ").strip()
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        display_pokemon_info(pokemon_info)
    else:
        print("Failed to retrieve Pokémon data. Please try again.")

if __name__ == "__main__":
    main()
