import os

folders = [
"data/documents",
"data/database",
"embeddings",
"retriever",
"tools",
"rag_pipeline",
"utils",
"ui"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("Project folders created successfully")