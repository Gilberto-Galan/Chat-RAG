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

## 🛠️ Tecnologías y Herramientas

Este proyecto fue construido utilizando un stack de IA moderna optimizado para ejecución local:

* **[LangChain / LangChain-Classic](https://github.com/langchain-ai/langchain):** Framework principal utilizado para orquestar la lógica del RAG, gestionar los prompts y conectar el recuperador con el modelo de lenguaje.
* **[Hugging Face Transformers](https://huggingface.co/docs/transformers/index):** Proporciona la infraestructura para cargar y ejecutar el modelo **Flan-T5-Base** (LLM) y el modelo de embeddings **all-MiniLM-L6-v2**.
* **[FAISS (Facebook AI Similarity Search)](https://github.com/facebookresearch/faiss):** Biblioteca de alto rendimiento para la búsqueda de similitudes en espacios vectoriales, utilizada para almacenar e indexar los fragmentos del libro.
* **[PyTorch](https://pytorch.org/):** Backend de computación tensorial necesario para ejecutar los modelos de Deep Learning en la CPU/GPU.
* **[PyPDF](https://pypdf.readthedocs.io/):** Librería encargada de la extracción y procesamiento de texto desde los archivos PDF originales.
* **[Sentence-Transformers](https://sbert.net/):** Utilizada para generar representaciones vectoriales (embeddings) de alta calidad que permiten a la IA "entender" el contexto de las preguntas.
