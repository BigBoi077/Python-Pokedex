class Pokemon():
    def __init__(self, json):
        self.id = json['id']
        self.names = json['name']
        self.stats = json['base']
        self.types = json['type']
        self.imageUrl = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{self.id}.png"