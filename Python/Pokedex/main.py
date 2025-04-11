import requests
import os

pokemon = input("Search Pokemon:    ")


response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
data = response.json()


os.system('cls')

print(f"{pokemon.upper()}\n\n")

for s in data['stats']:
    print(f"{s['stat']['name'].upper()}: {s['base_stat']}")


print("\n\nTYPES:")

for t in data['types']:
    print(t['type']['name'].upper())

print("\nABILITIES:")

for a in data['abilities']:
    print(a['ability']['name'].upper())
