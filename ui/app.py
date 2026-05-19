import sys
import os
import streamlit as st
import base64

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rag_pipeline.rag_agent import ask_agent
from retriever.vector_store import load_vector_store
from langchain_ollama import ChatOllama

st.set_page_config(page_title="Hybrid RAG AI Assistant")

st.markdown("""
<style>

/* ---------------- MAIN BACKGROUND ---------------- */

.stApp{
background: radial-gradient(circle at top,
#0f172a 0%,
#020617 60%,
#000000 100%);
color:white;
font-family:'Inter',sans-serif;
}

/* OPTIONAL GLOW EFFECT */
.stApp::before{
content:"";
position:fixed;
top:-200px;
left:-200px;
width:600px;
height:600px;
background:radial-gradient(circle,
rgba(59,130,246,0.2),
transparent 70%);
filter:blur(120px);
z-index:-1;
}

/* ---------------- HEADINGS ---------------- */

h1,h2,h3{
color:#ffffff !important;
font-weight:600;
letter-spacing:-0.5px;
}

/* Target Streamlit buttons */
div.stButton > button {

    background: rgba(18, 21, 33, 0.7) !important;
    color: #e0e0e0 !important;

    border: 1px solid rgba(59, 130, 246, 0.3) !important;
    border-radius: 10px !important;

    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);

    /* Smaller size */
    padding: 0.4rem 1rem !important;
    min-height: auto !important;
    width: auto !important;

    font-size: 14px !important;
    font-weight: 500 !important;

    transition: all 0.25s ease;

    box-shadow: 0 4px 10px rgba(0,0,0,0.4);
}

/* Hover effect */
div.stButton > button:hover {

    border: 1px solid rgba(59,130,246,0.8) !important;
    background: rgba(28,34,56,0.8) !important;

    transform: translateY(-2px);

    box-shadow: 0 0 15px rgba(37,99,235,0.4);

    color: #ffffff !important;
}

/* Click effect */
div.stButton > button:active {

    transform: translateY(0px) scale(0.96);

}

/* INPUT BOX */

div[data-baseweb="input"]{
background:rgba(255,255,255,0.03) !important;
border:1px solid rgba(255,255,255,0.1) !important;
border-radius:10px !important;
}

/* SIDEBAR */

section[data-testid="stSidebar"]{
background:#020617;
border-right:1px solid rgba(255,255,255,0.05);
}

.summary-card{
background: linear-gradient(
135deg,
rgba(255,255,255,0.05),
rgba(255,255,255,0.02)
);

backdrop-filter: blur(16px);

border:1px solid rgba(255,255,255,0.08);

border-radius:16px;

padding:22px;

box-shadow:
0 10px 40px rgba(0,0,0,0.45);

line-height:1.6;
}            

</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div style='text-align:center; padding:40px 0;'>
    <h1 style='font-size:42px;'>✨ Hybrid RAG AI Assistant</h1>
    <p>
    Ask questions, summarize documents, and explore knowledge instantly.
    </p>
</div>
""", unsafe_allow_html=True)


# -------------------------
# SEARCH MODE
# -------------------------

mode = st.radio(
    "Search Mode",
    ["Document Assistant", "Web Search"],
)

# refresh when mode changes
if "last_mode" not in st.session_state:
    st.session_state.last_mode = mode

if mode != st.session_state.last_mode:
    st.session_state.last_mode = mode
    st.rerun()


vector_db = load_vector_store()

if "history" not in st.session_state:
    st.session_state.history = []

if "last_uploaded" not in st.session_state:
    st.session_state.last_uploaded = None
# -------------------------
# SIDEBAR
# -------------------------
uploaded_file = st.sidebar.file_uploader("📂 Document Workspace", type="pdf")

if uploaded_file:

    save_path = f"data/documents/{uploaded_file.name}"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.session_state.last_uploaded = uploaded_file.name

    st.sidebar.success("Uploaded successfully!")
st.sidebar.write("📌 Your Documents")

docs_folder = "data/documents"

files = os.listdir(docs_folder)

for file in files:
    st.sidebar.write("📄", file)
# -------------------------
# HISTORY BUTTON
# -------------------------

show_history = st.sidebar.button("💬 Conversation History")

if show_history:
    for q, r in st.session_state.history:
        st.sidebar.write("•", q)
# -----------------------------
# Question Input
# -----------------------------
if mode == "Document Assistant":
    query = st.text_input("Ask anything about your document... ")
    col1, col2 = st.columns([1,1])

    with col2:
      summarize_btn = st.button("📑 Summarize ")

    with col1:
      ask_btn = st.button("🔎 Ask")
    if summarize_btn:
       if st.session_state.last_uploaded is None:

          st.warning("Upload a document first")

       else:
          docs = vector_db.similarity_search(
            st.session_state.last_uploaded,
            k=10
        )

          context = "\n\n".join([doc.page_content for doc in docs])
          llm = ChatOllama(model="llama3.2:1b")

          prompt = f"""
You are an AI research assistant.

Read the last uploaded document context and give a clear summary.

Context:
{context}

Provide a concise summary of the document.
"""

          from langchain_ollama import ChatOllama

          llm = ChatOllama(model="llama3.2:1b")
          with st.spinner("Summarizing document ...."):
           response = llm.invoke(prompt)

          st.markdown("### 📑 Document Summary")
          st.markdown(
    f"""
    <div class="summary-card">
    {response.content}
    </div>
    """,
    unsafe_allow_html=True
)

    if ask_btn:

     if query:

        with st.spinner("Thinking....."):
           response = ask_agent(query)

        st.session_state.history.append((query, response))
        
        st.markdown(f"**🤖 AI Answer:**")
        st.write(response)
# -------------------------
# WEB SEARCH MODE
# -------------------------

if mode == "Web Search":

    query = st.text_input("Ask anything from the web")

    if st.button("🌐 Search"):

        if query:

            with st.spinner("Searching the web..."):

                response = ask_agent(query)

            st.session_state.history.append((query, response))

            st.markdown("**Answer:**")

            st.write(response)