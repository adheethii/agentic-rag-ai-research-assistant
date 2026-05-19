import os
from utils.pdf_loader import load_documents
from retriever.vector_store import create_vector_store

DOC_FOLDER = "data/documents"

all_docs = []

for file in os.listdir(DOC_FOLDER):
    if file.endswith(".pdf"):
        path = os.path.join(DOC_FOLDER, file)
        docs = load_documents(path)
        all_docs.extend(docs)

print(f"Loaded {len(all_docs)} document chunks")

create_vector_store(all_docs)

print("Vector database created successfully")