import requests
import json as JSON
from PIL import Image
from Pokemon import Pokemon
from ProgressBar import ProgressBar

class DataManager():
    def __init__(self, app, pokemons):
        self.app = app
        self.pokemons = pokemons
        self.progressBar = None

    def initProgressBar(self, json):
        self.progressBar = ProgressBar(len(json), 50, "cls", self.app)
        self.app.setNbrPokemons(len(json))

    def handleData(self, url):
        response = requests.get(url)
        jsonContent = response.json()
        self.initProgressBar(jsonContent)
        self.createPokemons(jsonContent)
        self.progressBar.end()

    def createPokemons(self, json):
        for singlePokemon in json:
            self.createPokemon(singlePokemon)
            self.progressBar.update_bar(singlePokemon['id'])

    def downloadImage(self, imageUrl, pokemonFileName):
        img = Image.open(requests.get(imageUrl, stream = True).raw)
        img.save(f"./Pokemon-Images/{pokemonFileName}.png")
            
    def createPokemon(self, json):
        pokemon = Pokemon(json)
        self.pokemons.append(pokemon)
        if self.app.downloadEnabled:
            print(pokemon.names['english'])
            self.downloadImage(pokemon.imageUrl, f"{pokemon.id}")

    def prettyPrintJSON(self, json):
        print(JSON.dumps(json, indent=4, sort_keys=True))

    def getImage(self, pokemon):
        return requests.get(pokemon.imageUrl)