from openai import OpenAI

client = OpenAI()

def embed_chunks(chunks):
    embeddings = []
    for chunk in chunks:
        emb = client.embeddings.create(
            model="text-embedding-3-large",
            input=chunk
        )
        embeddings.append(emb.data[0].embedding)
    return embeddings