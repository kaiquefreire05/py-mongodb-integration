from pprint import pprint

import pymongo
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://kaiquefreiresantos05:kaique2005@cluster0.0kml1yf.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

# Verificando se foi conectado com sucesso
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test  # Acessando a collection
posts = db.posts  # Acessando a tabela de string 'posts'

print("\nMostrando todas info da collection post: ")
for post in posts.find():  # Mostrando todos os documentos
    pprint(post)
    print()

print(posts.count_documents({}))  # Contando a quantidade de documentos inseridos
print(posts.count_documents({"author": "mike"}))  # Contando a quantidade de documentos inseridos especificados
print(posts.count_documents({"tags": "insert"}))

print("\nRecuperando info da collection post de maneira ordenada: ")
for post in posts.find({}).sort("date"):
    pprint(post)

result = db.profiles.create_index([('author', pymongo.ASCENDING)], unique=True)
print(sorted(list(db.profiles.index_information())))

user_profile_user = [
    {'user_id': 211, 'name': 'Kaique'},
    {'user_id': 212, 'name': 'Luke'},
    {'user_id': 213, 'name': 'Maria'}
]

print("\nCollections armazenadas no MongoDB: ")
# result = db.profile_user.insert_many(user_profile_user)  # Adicionando os docs na collection

collections = db.list_collection_names()  # Pegando apenas os nomes das collections existentes

for collection in collections:
    print(collection)

# db['posts'].drop()  # Excluindo a collection 'posts'

for collection in collections:
    db[collection].drop()  # Método para excluir todas as collections

print(posts.delete_one({"author": "mike"}))
print(db.profile_user.drop())
