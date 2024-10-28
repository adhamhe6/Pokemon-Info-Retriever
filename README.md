# Pokémon Info Retrieval

A versatile Pokémon information retrieval application featuring a FastAPI backend, a Python desktop GUI, and an HTML web interface for accessing data from PokeAPI.

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
    - [FastAPI Backend Setup](#fastapi-backend-setup)
    - [Python Desktop GUI Setup](#python-desktop-gui-setup)
    - [HTML Web Interface](#html-web-interface)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Features
- Retrieve detailed information about Pokémon, including their abilities, height, weight, and base experience.
- User-friendly desktop application for quick access to Pokémon data.
- HTML web interface for easy access through a browser.

## Technologies Used
- Python 3.10
- FastAPI
- Requests
- Tkinter (for the desktop GUI)
- HTML/CSS (for the web interface)

## Setup Instructions

### FastAPI Backend Setup
1. Make sure you have Python 3.10 or higher installed.
2. Install the required dependencies:

    ```bash
    pip install fastapi uvicorn requests
    ```

3. Start the FastAPI server:

    ```bash
    uvicorn pokemon_api_backend:app --reload
    ```

4. The server will be running on [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Python Desktop GUI Setup
- Run the desktop GUI application with:

    ```bash
    python pokemon_app_gui.py
    ```

### HTML Web Interface
- Open `pokemon_frontend.html` in a web browser to access the web interface.

## Usage
1. Enter a Pokémon name in the GUI or web interface to retrieve its information.
2. View details such as ID, height, weight, base experience, and abilities.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to add.

## Acknowledgments
- Thanks to the [PokeAPI](https://pokeapi.co/) for providing the Pokémon data.
- Inspired by the Pokémon games and community.

Happy coding! 😊