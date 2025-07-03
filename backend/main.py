from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ingest import load_files
from embed import embed_chunks
from graph import build_graph

app = FastAPI()

# ✅ Allow Vite dev server (5173) to talk to FastAPI (8000)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/build-graph")
def build_graph_endpoint():
    chunks = load_files("sample_data/notes", "sample_data/bookmarks.json")
    embeddings = embed_chunks(chunks)
    G = build_graph(chunks, embeddings)
    nodes = [{"data": {"id": str(i), "label": chunk[:40]}} for i, chunk in enumerate(chunks)]
    edges = [{"data": {"source": str(e[0]), "target": str(e[1])}} for e in G.edges()]
    return {"nodes": nodes, "edges": edges}

@app.post("/ask")
def ask_copilot(query: Query):
    return {"answer": f"You asked: {query.question} — Here’s a stub answer."}