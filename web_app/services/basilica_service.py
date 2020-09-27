import basilica 
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

def basilica_api_client():
    coonnection = basilica.Connection(API_KEY)
    print(type(connection)) 
    return coonnection
    
if __name__ == "__main__":
    print("-----")
    connection = basilica_api_client()

    print("-----")
    sentence = "Hello again"
    sent_embeddings = connection.embed_sentence(sentence)
    print(list(sent_embeddings))

    print("-----")
    sentences = ["Hello","Again"]
    print(sentences)
    embeddings = connection.embed_sentences(sentences)
    print(list(embeddings))