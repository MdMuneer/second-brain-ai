import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def build_graph(chunks, embeddings, threshold=0.75):
    G = nx.Graph()
    for i, chunk in enumerate(chunks):
        G.add_node(i, text=chunk)

    emb_matrix = np.array(embeddings)
    sim_matrix = cosine_similarity(emb_matrix)

    for i in range(len(chunks)):
        for j in range(i + 1, len(chunks)):
            if sim_matrix[i][j] >= threshold:
                G.add_edge(i, j, weight=sim_matrix[i][j])

    return G