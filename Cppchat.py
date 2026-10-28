import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="C++ RAG Chatbot")
st.title("C++ RAG Chatbot")


# Build the vector store once and reuse it across reruns
@st.cache_resource(show_spinner="Loading and indexing CPP.txt...")
def load_db():
    docs = TextLoader("CPP.txt", encoding="utf-8").load()
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=200, chunk_overlap=20
    ).split_documents(docs)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.from_documents(chunks, embeddings)


db = load_db()

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a C++ tutor. Answer using only the context below. "
     "If the answer is not in the context, say you don't know.\n\n"
     "Context:\n{context}"),
    ("user", "Question: {question}"),
])
llm = OllamaLLM(model="gemma2:2b")
chain = prompt | llm | StrOutputParser()

query = st.text_input("Enter your question for C++:")

if query:
    results = db.similarity_search(query, k=3)
    context = "\n\n".join(doc.page_content for doc in results)

    with st.spinner("Thinking..."):
        answer = chain.invoke({"context": context, "question": query})

    st.subheader("Answer")
    st.write(answer)

    with st.expander("Retrieved chunks"):
        for i, doc in enumerate(results, start=1):
            st.markdown(f"**Result {i}**")
            st.write(doc.page_content)
            st.divider()