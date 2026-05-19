from rank_bm25 import BM25Okapi

class HybridRetriever:

    def __init__(self, docs, vector_db):

        self.docs = docs
        self.vector_db = vector_db

        corpus = [doc.page_content.split() for doc in docs]
        self.bm25 = BM25Okapi(corpus)

    def search(self, query):

        vector_results = self.vector_db.similarity_search(query, k=5)

        tokenized = query.split()
        bm25_scores = self.bm25.get_scores(tokenized)

        top_bm25 = sorted(
            range(len(bm25_scores)),
            key=lambda i: bm25_scores[i],
            reverse=True
        )[:5]

        keyword_docs = [self.docs[i] for i in top_bm25]

        return vector_results + keyword_docs