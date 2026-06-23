from langchain_ollama import ChatOllama
from retriever.vector_store import load_vector_store
from retriever.reranker import rerank
from tools.web_search import web_search
from tools.calculator import calculate
import os
# Load local LLM
llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0.3
)


def ask_agent(query):

    print("Reloading vector database...")

    vector_db = load_vector_store()

    docs_with_scores = vector_db.similarity_search_with_score(
        query,
        k=5
    )

    docs = []
    scores = []

    for doc, score in docs_with_scores:

        print(
            "Retrieved:",
            os.path.basename(
                doc.metadata.get("source", "Unknown")
            ),
            "Score:",
            score
        )

        docs.append(doc)
        scores.append(score)

    # Best similarity score
    best_score = scores[0] if scores else 1

    # If score is too bad → web search
    if best_score > 1.2:

        web_results = web_search(query)

        web_context = "\n".join([r["content"] for r in web_results[:3]])

        prompt = f"""
You are an AI assistant.

Answer the question using the web search results.

Web Results:
{web_context}

Question:
{query}
"""

        response = llm.invoke(prompt)

        return f"{response.content}\n\n🌐 Source: Web Search"

    # Otherwise use document context
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI research assistant.

Use the provided document context to answer the question.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    sources = set()

    for doc in docs:
        source = os.path.basename(doc.metadata.get("source", "Unknown"))
        page = doc.metadata.get("page", 0) + 1
        sources.add(f"{source} (Page {page})")

    sources_text = "\n".join(sources)

    return f"{response.content}\n\n📚 Sources:\n{sources_text}"