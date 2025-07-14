import faiss
import pickle
from sentence_transformers import SentenceTransformer

class DocumentRetriever:
    def __init__(self, index_path, id2doc_path, model_name='all-MiniLM-L6-v2'):
        self.index = faiss.read_index(index_path)
        with open(id2doc_path, "rb") as f:
            self.id2doc = pickle.load(f)
        
        self.model = SentenceTransformer(model_name)

    def retrieve(self, query, top_k=3):
        # Generating embedding for the user query
        query_embedding = self.model.encode([query])
        
        # Performing similarity search
        distances, indices = self.index.search(query_embedding, top_k)

        # Collecting matched docs and scores
        results = []
        for idx, dist in zip(indices[0], distances[0]):
            doc = self.id2doc[idx]
            results.append((doc, dist))
        
        return results
