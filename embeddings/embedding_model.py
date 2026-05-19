from langchain_community.embeddings import HuggingFaceEmbeddings

def load_embedding():

    model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-base-en-v1.5"
    )

    return model
#sentence-transformers/all-MiniLM-L6-v2