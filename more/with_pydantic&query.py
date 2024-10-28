import requests
import logging
from functools import lru_cache
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="Pokémon Info API", description="Retrieve Pokémon information using PokeAPI", version="1.0")

base_url = "https://pokeapi.co/api/v2/"

# Define Pydantic models for response data
class PokemonInfo(BaseModel):
    name: str
    id: int
    height: int
    weight: int
    base_experience: int
    abilities: List[str]

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

@app.get("/pokemon/{name}", response_model=PokemonInfo, summary="Get Pokémon Information")
def read_pokemon_info(
    name: str,
    min_height: Optional[int] = Query(None, ge=1, description="Minimum height of the Pokémon"),
    max_height: Optional[int] = Query(None, ge=1, description="Maximum height of the Pokémon"),
):
    """API endpoint to get Pokémon information with optional height filtering."""
    pokemon_data = get_pokemon_info(name)
    if not pokemon_data:
        raise HTTPException(status_code=404, detail="Pokémon not found")

    # Apply filtering based on height if specified
    if min_height is not None and pokemon_data['height'] < min_height:
        raise HTTPException(status_code=400, detail=f"Pokémon height is less than {min_height}")
    if max_height is not None and pokemon_data['height'] > max_height:
        raise HTTPException(status_code=400, detail=f"Pokémon height is more than {max_height}")

    # Transform data to fit the Pydantic model
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    return PokemonInfo(
        name=pokemon_data['name'].capitalize(),
        id=pokemon_data['id'],
        height=pokemon_data['height'],
        weight=pokemon_data['weight'],
        base_experience=pokemon_data['base_experience'],
        abilities=abilities
    )

# Optional: Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
