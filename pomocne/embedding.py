from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embeduj(fragmenti):
    return model.encode(fragmenti, show_progress_bar=True)