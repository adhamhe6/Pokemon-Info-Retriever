import requests
import logging
from functools import lru_cache
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="Pokémon Info API", description="Retrieve Pokémon information using PokeAPI", version="1.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

base_url = "https://pokeapi.co/api/v2/"

@lru_cache(maxsize=128)
def get_pokemon_info(name: str):
    """Retrieve Pokémon information from the API."""
    url = f"{base_url}pokemon/{name.lower()}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        logging.info(f"Data successfully retrieved for {name.capitalize()}")
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        raise HTTPException(status_code=response.status_code, detail="Pokémon not found")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error occurred: {req_err}")
        raise HTTPException(status_code=500, detail="An error occurred while retrieving data")
    return None

@app.get("/pokemon/{name}", summary="Get Pokémon Information")
def read_pokemon_info(name: str):
    """API endpoint to get Pokémon information."""
    pokemon_data = get_pokemon_info(name)
    if not pokemon_data:
        raise HTTPException(status_code=404, detail="Pokémon not found")
    return {
        "name": pokemon_data['name'].capitalize(),
        "id": pokemon_data['id'],
        "height": pokemon_data['height'],
        "weight": pokemon_data['weight'],
        "base_experience": pokemon_data['base_experience'],
        "abilities": [ability['ability']['name'] for ability in pokemon_data['abilities']],
    }

# Optional: Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
