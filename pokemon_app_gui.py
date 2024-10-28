import tkinter as tk
from tkinter import messagebox
import requests

# Define the URL for the FastAPI backend
API_URL = "http://127.0.0.1:8000/pokemon/"

def get_pokemon_info():
    pokemon_name = entry.get().strip()
    if not pokemon_name:
        messagebox.showwarning("Input Error", "Please enter the Pokémon name.")
        return

    try:
        response = requests.get(f"{API_URL}{pokemon_name}")
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        display_pokemon_info(data)
    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "Pokémon not found!")
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "An error occurred while retrieving data.")

def display_pokemon_info(data):
    result_text = (
        f"{data['name'].capitalize()}\n"
        f"ID: {data['id']}\n"
        f"Height: {data['height']}\n"
        f"Weight: {data['weight']}\n"
        f"Base Experience: {data['base_experience']}\n"
        f"Abilities: {', '.join(data['abilities'])}"
    )
    result_label.config(text=result_text)

# Create the main window
root = tk.Tk()
root.title("Pokémon Info Application")
root.geometry("400x400")
root.resizable(False, False)

# Set fonts and colors
font_large = ("Arial", 16)
font_medium = ("Arial", 12)
bg_color = "#f8f9fa"
fg_color = "#343a40"
btn_color = "#007bff"
btn_hover_color = "#0056b3"

# Set background color
root.configure(bg=bg_color)

# Create UI elements
label_title = tk.Label(root, text="Pokémon Info Application", font=font_large, bg=bg_color, fg=fg_color)
label_input = tk.Label(root, text="Enter Pokémon Name:", font=font_medium, bg=bg_color, fg=fg_color)
entry = tk.Entry(root, font=font_medium)
result_label = tk.Label(root, text="Enter a Pokémon name above to get its information!", font=font_medium, bg="#e9ecef", fg=fg_color, wraplength=350, justify="center", padx=10, pady=10)

# Function to change button color on hover
def on_enter(e):
    btn_get_info['background'] = btn_hover_color

def on_leave(e):
    btn_get_info['background'] = btn_color

btn_get_info = tk.Button(root, text="Get Info", font=font_medium, bg=btn_color, fg="white", command=get_pokemon_info)
btn_get_info.bind("<Enter>", on_enter)
btn_get_info.bind("<Leave>", on_leave)

# Place elements in the window
label_title.pack(pady=20)
label_input.pack()
entry.pack(pady=5)
btn_get_info.pack(pady=20)
result_label.pack(pady=10)

# Start the application
root.mainloop()
