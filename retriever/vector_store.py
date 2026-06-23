from langchain_community.vectorstores import FAISS
from embeddings.embedding_model import load_embedding

import shutil
import os

def create_vector_store(docs):

    if os.path.exists("data/vector_store"):
        shutil.rmtree("data/vector_store")

    embeddings = load_embedding()

    vector_db = FAISS.from_documents(docs, embeddings)

    vector_db.save_local("data/vector_store")

    return vector_db


def load_vector_store():

    embeddings = load_embedding()

    db = FAISS.load_local(
        "data/vector_store",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db