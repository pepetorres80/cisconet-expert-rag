import os
from dotenv import load_dotenv

import streamlit as st

from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)

from langchain_chroma import Chroma

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential
)


# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

load_dotenv()

st.set_page_config(
    page_title="CiscoNet Expert",
    page_icon="🖧",
    layout="centered"
)

st.title("CiscoNet Expert")
st.caption(
    "Asistente RAG especializado en redes Cisco y troubleshooting CCNA"
)

st.success("Aplicación cargada correctamente")


# ============================================================
# SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = """
Eres CiscoNet Expert, un asistente de IA especializado en redes Cisco.

Tu función es ayudar a resolver dudas técnicas sobre:
- VLANs
- Switching
- Routing
- OSPF
- ACLs
- NAT
- DHCP
- Cisco IOS
- Troubleshooting de red

Reglas:
1. Responde usando el contexto recuperado.
2. Si no hay información suficiente en el contexto, dilo claramente.
3. Sé técnico, claro y estructurado.
4. Incluye comandos Cisco IOS cuando sea útil.
5. Explica paso a paso.
"""


# ============================================================
# CARGA DE MODELOS Y VECTORSTORE
# ============================================================

@st.cache_resource
def load_models_and_vectorstore():

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        st.error(
            "No se encontró GOOGLE_API_KEY en el archivo .env"
        )
        st.stop()

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2
    )

    vectorstore = Chroma(
        persist_directory="data/chromadb_cisco",
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )

    return llm, retriever


# ============================================================
# RETRIES
# ============================================================

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=2, min=2, max=12)
)
def safe_llm_invoke(llm, prompt):

    return llm.invoke(prompt)


# ============================================================
# GENERACIÓN RESPUESTA
# ============================================================

def generate_response(question, history, llm, retriever):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    formatted_history = "\n".join(
        [
            (
                f"Usuario: {m['content']}"
                if m["role"] == "user"
                else f"Asistente: {m['content']}"
            )
            for m in history
        ]
    )

    prompt = f"""
{SYSTEM_PROMPT}

Historial de conversación:
{formatted_history}

Contexto recuperado:
{context}

Pregunta del usuario:
{question}

Respuesta:
"""

    response = safe_llm_invoke(llm, prompt)

    return response.content


# ============================================================
# MEMORIA STREAMLIT
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# HISTORIAL CHAT
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ============================================================
# INPUT USUARIO
# ============================================================

question = st.chat_input(
    "Pregunta algo sobre redes Cisco..."
)


# ============================================================
# RESPUESTA
# ============================================================

if question:

    llm, retriever = load_models_and_vectorstore()

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner(
            "Consultando documentación Cisco..."
        ):

            answer = generate_response(
                question,
                st.session_state.messages,
                llm,
                retriever
            )

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("CiscoNet Expert")

    st.write(
        "Sistema RAG con Gemini, ChromaDB y LangGraph."
    )

    if st.button("Limpiar conversación"):

        st.session_state.messages = []

        st.rerun()

    st.divider()

    st.write("Ejemplos:")

    st.code(
        "How do I configure a VLAN on a Cisco switch?"
    )

    st.code(
        "How do I troubleshoot OSPF neighbor adjacency?"
    )

    st.code(
        "How can I block VLAN 20 from accessing VLAN 10?"
    )