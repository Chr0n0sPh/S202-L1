from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()

# #1 - Pokemon por Tipo
# def getPokemonsByType(types: list):
# return db.collection.find({"type": {"$in": types}})
# types = ["Ice"]
# pokemons = getPokemonsByType(types)
# writeAJson(pokemons, "pokemons_by_type")

# #2 - Pokémons tipo Pedra OU Gelo que não tem evolução
# tipos = ["Rock", "Ice"]
# pokemons = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": False} })
# writeAJson(pokemons, "pokemons tipo Pedra e Gelo que não tem evolução")

# #3 - Pokemons com duas Fraquezas
# pokemons = db.collection.find({"weaknesses": {"$size": 2}})
# writeAJson(pokemons, "pokemons com duas fraquezas")

# #4 - Pokemons que são de grama ou fraco contra grama
# pokemons = db.collection.find({"$or": [{"type":"Grass"},{"weaknesses": "Grass"}]})
# writeAJson(pokemons, "Pokemons que são de grama ou fraco contra grama")

#5 - Pokemon por nome
def getPokemonByName(name: str):
    return db.collection.find({"name": name})

pikachu = getPokemonByName("Nidoking")
writeAJson(pikachu, "nidoking")