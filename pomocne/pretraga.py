import time
from pomocne.embedding import embeduj

def pretrazi(pitanje, indeks, lista, k=5):
    start = time.perf_counter()

    query = embeduj([pitanje]).astype("float32")

    distances, indices = indeks.search(query,k) #5 najblizih indeksa

    print(f"vreme za pretragu: {time.perf_counter()-start:.4f}s")

    # relevantne recenice za dati upit
    retrieved_sentences = [lista[i] for i in indices[0]]

    # for i, fragment in enumerate(retrieved_sentences):
    #     slicnost = (1 - distances[0][i] / 2) * 100
    #     print(f"Relevantna recenica {i+1}, slicnost {slicnost:.1f}%, distanca {distances[0][i]:.4f}\n{fragment}")
    #     print("-"*60)

    return retrieved_sentences