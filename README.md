# CiscoNet Expert — Asistente IA para Redes Cisco

CiscoNet Expert es un asistente basado en Retrieval-Augmented Generation (RAG) especializado en redes Cisco y troubleshooting de nivel CCNA.

El sistema combina Gemini, ChromaDB y LangGraph para proporcionar respuestas técnicas contextualizadas utilizando documentación Cisco real.

---

# Descripción del proyecto

El objetivo del proyecto es construir un asistente especializado capaz de:

- Consultar documentación técnica Cisco.
- Recuperar información relevante mediante búsqueda semántica.
- Generar respuestas contextualizadas utilizando Gemini.
- Mantener memoria conversacional entre preguntas.
- Ayudar en tareas de configuración y troubleshooting de redes.

El sistema implementa una arquitectura RAG completa utilizando embeddings, base vectorial y un workflow basado en LangGraph.

---

# Dominio del proyecto

El asistente está especializado en tecnologías Cisco y contenidos CCNA:

- Configuración de VLANs
- Switching y Routing
- OSPF
- ACLs
- NAT / PAT
- DHCP
- Troubleshooting Cisco IOS

---

# Características principales

- Sistema RAG (Retrieval-Augmented Generation)
- Búsqueda semántica sobre documentación Cisco
- Memoria conversacional
- Integración con Gemini 2.5 Flash
- Base vectorial ChromaDB
- Workflow mediante LangGraph
- Interfaz Streamlit
- Prompt engineering especializado

---

# Stack tecnológico

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| Gemini 2.5 Flash | Modelo LLM |
| Gemini Embeddings | Embeddings vectoriales |
| ChromaDB | Base de datos vectorial |
| LangChain | Pipeline RAG |
| LangGraph | Orquestación del agente |
| Streamlit | Interfaz web |
| Jupyter Notebook | Desarrollo y experimentación |

---

# Arquitectura general del sistema

```text
Documentos PDF
      ↓
Carga de documentos
      ↓
Chunking y limpieza
      ↓
Gemini Embeddings
      ↓
Base vectorial ChromaDB
      ↓
Retriever semántico
      ↓
Workflow LangGraph
      ↓
Generación de respuestas con Gemini
```

---

# Arquitectura LangGraph

El flujo conversacional del agente se implementa mediante LangGraph utilizando dos nodos principales:

## 1. Retrieve Node

Responsable de:
- Recibir la pregunta del usuario.
- Buscar información relevante en ChromaDB.
- Recuperar contexto mediante búsqueda semántica.

## 2. Generate Node

Responsable de:
- Construir el prompt final.
- Combinar historial + contexto recuperado.
- Generar respuestas usando Gemini.

## Flujo del grafo

```text
Usuario
   ↓
Retrieve Node
   ↓
Generate Node
   ↓
Respuesta final
```

El sistema mantiene memoria conversacional entre turnos para mejorar la coherencia del diálogo.

---

# Justificación del System Prompt

El system prompt fue diseñado para especializar el comportamiento del modelo en el dominio Cisco Networking.

Objetivos principales:

- Restringir el dominio técnico.
- Reducir alucinaciones.
- Obligar al modelo a utilizar el contexto recuperado.
- Generar respuestas estructuradas y orientadas a troubleshooting.
- Incluir comandos Cisco IOS cuando sea necesario.

Este enfoque mejora la precisión y coherencia del sistema RAG.

---

# Estructura del repositorio

```text
cisconet-expert-rag/
│
├── Proyecto_CiscoNet_Expert.ipynb
├── streamlit_app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── docs/
│   ├── ccna_official_guide.pdf
│   ├── cisco_warrior.pdf
│   └── ...
│
├── data/
│   └── chromadb_cisco/
│
└── examples/
```

---

# Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/cisconet-expert-rag.git
cd cisconet-expert-rag
```

---

## 2. Crear entorno virtual

```bash
python -m venv venv
```

---

## 3. Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Variables de entorno

Crear un archivo `.env`:

```env
GOOGLE_API_KEY=tu_api_key
```

---

# Guía de ejecución

## Ejecutar Notebook

```bash
jupyter notebook
```

Abrir:

```text
Proyecto_CiscoNet_Expert.ipynb
```

---

## Ejecutar aplicación Streamlit

```bash
streamlit run streamlit_app.py
```

---

# Dependencias principales

- langchain
- langgraph
- chromadb
- langchain-google-genai
- streamlit
- pypdf
- python-dotenv
- tenacity

---

# Ejemplos de consultas

```text
¿Cómo configuro una VLAN en un switch Cisco?

¿Cómo puedo bloquear la comunicación entre VLAN 10 y VLAN 20 utilizando ACLs?

¿Cómo soluciono problemas de adyacencia OSPF?

¿Cómo configuro NAT overload en un router Cisco?

¿Qué comandos Cisco IOS son útiles para troubleshooting de routing?
```

---

# Ejemplo de respuesta

```text
Switch(config)# vlan 10
Switch(config-vlan)# name Marketing

Switch(config)# interface fa0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
```

---

# Mejoras futuras

- Despliegue público en Streamlit Cloud
- Arquitectura multiagente
- Búsqueda híbrida
- Integración con Packet Tracer
- Validación automática de configuraciones Cisco
- Persistencia avanzada de conversaciones

---

# Contexto académico

Este proyecto ha sido desarrollado como trabajo final del módulo de IA Generativa enfocado en:

- Integración de LLMs
- Prompt engineering
- Sistemas RAG
- Bases de datos vectoriales
- Agentes IA
- LangGraph workflows

---

# Autor

Jose Torres Sanchez