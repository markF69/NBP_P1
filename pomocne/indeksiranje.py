import faiss
import numpy as np

def indeksiraj(vektor):
    index = faiss.IndexFlatL2(vektor.shape[1])#384 | manji razmak slicniji fragm
    index.add(np.asarray(vektor,dtype="float32"))# imace redne brojeve u indx iste kao u listi
    return index