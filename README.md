# 📚 Personal RAG Chatbot (Local AI)

Este proyecto permite chatear con cualquier documento PDF de forma local utilizando técnicas de **Retrieval-Augmented Generation (RAG)**.

## 🚀 Características
- **100% Local:** No requiere API Keys de OpenAI.
- **Eficiente:** Optimizado para correr en CPU.
- **Arquitectura:** Basado en LangChain-Classic y Hugging Face.

## 🛠️ Instalación
1. Clona el repositorio.
2. Crea un entorno virtual: `python -m venv venv`.
3. Instala dependencias: `pip install -r requirements.txt`.
4. Coloca tu PDF en la carpeta `/data`.
5. Ejecuta `python ingest.py` para indexar.
6. Ejecuta `python chat.py` para hablar con tus documentos.

## 🧠 Modelos utilizados
- **Embeddings:** `all-MiniLM-L6-v2`
- **LLM:** `google/flan-t5-base`
