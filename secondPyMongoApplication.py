from pprint import pprint

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

for post in posts.find():  # Mostrando todos os documentos
    pprint(post)
    print()

print(posts.count_documents({}))  # Contando a quantidade de documentos inseridos
print(posts.count_documents({"author": "mike"}))  # Contando a quantidade de documentos inseridos especificados
print(posts.count_documents({"tags": "insert"}))

