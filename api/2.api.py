import requests

base_url = "https://pokeapi.co/api/v2/" # Base url of PokeAPI

def get_pokemon_info(name):
  url = f"{base_url}/pokemon/{name}" # This is full url that i need here
  response = requests.get(url) #.get here use to get the response status 
  print(response)

  if response.status_code == 200: #.status_code use for decode the status of response of an api
    pokemon_data = response.json() #.json() use to convert response status to readable data
    return pokemon_data
  else:
    print(f"Failed to retrive data {response.status_code}")

pokemon_name = input("Type Pokemon Name: ")
pokemon_info = get_pokemon_info(pokemon_name) # Now this is dictionary we can sort to use

if pokemon_info:
  print(f"Name: {pokemon_info["name"]}")
  print(f"Id: {pokemon_info["id"]}")
  print(f"Height: {pokemon_info["height"]}")
  print(f"Weight: {pokemon_info["weight"]}")
# Response code 200 means okay