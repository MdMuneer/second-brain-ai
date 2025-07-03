from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def embed_chunks(chunks):
    embeddings = []
    for chunk in chunks:
        emb = client.embeddings.create(
            model="text-embedding-3-large",
            input=chunk
        )
        embeddings.append(emb.data[0].embedding)
    return embeddings