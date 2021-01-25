#!/usr/bin/env python
# coding: utf-8

from App import App
from DataManager import DataManager

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json"
    pokemons = []
    app = App("Pokedex", pokemons)
    dataManager = DataManager(app, pokemons)
    #dataManager.handleData(url)
    app.start()
