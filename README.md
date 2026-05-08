# CiscoNet Expert — Asistente IA para Redes Cisco

CiscoNet Expert es un asistente basado en Retrieval-Augmented Generation (RAG) especializado en redes Cisco y troubleshooting de nivel CCNA.

El sistema combina Gemini, ChromaDB y LangGraph para proporcionar respuestas técnicas contextualizadas utilizando documentación Cisco.

---

## Características

- Sistema RAG (Retrieval-Augmented Generation)
- Búsqueda semántica sobre documentación Cisco
- Asistencia técnica para Cisco IOS
- Memoria conversacional
- Orquestación mediante LangGraph
- Base vectorial con ChromaDB
- Integración con Gemini 2.5 Flash
- Prompt engineering especializado en redes

---

## Temas soportados

- VLANs
- Switching
- Routing
- OSPF
- ACLs
- NAT / PAT
- DHCP
- Comandos Cisco IOS
- Troubleshooting de red

---

## Stack tecnológico

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| Gemini 2.5 Flash | Modelo LLM |
| Gemini Embeddings | Embeddings vectoriales |
| ChromaDB | Base de datos vectorial |
| LangChain | Pipeline RAG |
| LangGraph | Orquestación del agente |
| Jupyter Notebook | Entorno de desarrollo |

---

## Arquitectura del proyecto

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

## Estructura del repositorio

```text
cisconet-expert-rag/
│
├── Proyecto_CiscoNet_Expert.ipynb
├── README.md
├── requirements.txt
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
├── src/
│
└── examples/
```

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/cisconet-expert-rag.git
cd cisconet-expert-rag
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Variables de entorno

Crear un archivo `.env`:

```env
GOOGLE_API_KEY=tu_api_key
```

---

## Ejecución del proyecto

Abrir Jupyter Notebook:

```bash
jupyter notebook
```

Ejecutar:

```text
Proyecto_CiscoNet_Expert.ipynb
```

---

## Ejemplos de consultas

```text
¿Cómo configuro una VLAN en un switch Cisco?

¿Cómo puedo bloquear la comunicación entre VLAN 10 y VLAN 20 utilizando ACLs?

¿Cómo soluciono problemas de adyacencia OSPF?

¿Cómo configuro NAT overload en un router Cisco?

¿Qué comandos Cisco IOS son útiles para troubleshooting de routing?
```

---

## Ejemplo de respuesta

```text
Switch(config)# vlan 10
Switch(config-vlan)# name Marketing

Switch(config)# interface fa0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
```

---

## Mejoras futuras

- Aplicación web con Streamlit
- Arquitectura multiagente
- Búsqueda híbrida
- Integración con Packet Tracer
- Validación automática de configuraciones Cisco
- Persistencia avanzada de conversaciones

---

## Contexto académico

Este proyecto ha sido desarrollado como trabajo final de un curso de IA Generativa enfocado en:

- Integración de LLMs
- Prompt engineering
- Sistemas RAG
- Bases de datos vectoriales
- Agentes IA
- Workflows con LangGraph

---

## Autor

Jose Torres Sanchez