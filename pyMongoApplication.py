import datetime
import pprint

import pymongo as pyM
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://kaiquefreiresantos05:kaique2005@cluster0.0kml1yf.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Verificando se foi conectado com sucesso
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test  # Criando o banco de dados

"""
collection = db.test_collection
print(db.test_collection)
print(db.list_collection_names())
"""

# Definição de informações para compor o doc

post = {
    "author": "mike",
    "text": "My first MongoDB application based on Python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# Preparando para submeter as info

posts = db.posts  # Definindo o banco de dados que vai receber as informações

# post_id = posts.insert_one(post).inserted_id  # Inserindo o 'post' no database usando o 'insert_one'


# print(post_id)  # Printando a variável
print(db.posts)  # Printando os itens do banco 'posts'
print(db.list_collection_names())  # Printando as collections que tenho na nuvem

# pprint.pprint(db.posts.find_one())  # Mostrando como se fosse o própio documento

# Bulk insert

new_posts = [{
    "author": "mike",
    "text": "Another post from test database",
    "tags": ["bulk", "post", "insert"],
    "date": datetime.datetime.utcnow()

}, {
    "author": "kaique",
    "text": "Post from Kaique. New post available!",
    "title": "Mongo test title",
    "date": datetime.datetime(2009, 11, 10, 10, 45)
}]

# result = posts.insert_many(new_posts)  # Inserindo arquivos no database posts
# print(result.inserted_ids)

print("\nRecuperação final")
pprint.pprint(db.posts.find_one({"author": "kaique"}))  # Pegando a primeira ocorrência do database

print("\nDocumentos presentes na coleção post")
for post in posts.find():  # Recuperando todos as info
    pprint.pprint(post)



