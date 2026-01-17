import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Definir rutas (opcional, para mantener orden)
pdf_path = "data/Saga Dune - Frank Herbert.pdf"
index_path = "faiss_index"

# 1. Cargar documento PDF
if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"El archivo no se encuentra en: {pdf_path}")

print("Cargando PDF...")
loader = PyPDFLoader(pdf_path)
documents = loader.load()
print(f"PDF cargado. Total de páginas: {len(documents)}")

# 2. Dividir texto
print("Dividiendo texto...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=80,
)
docs = splitter.split_documents(documents)
print(f"Texto dividido en {len(docs)} fragmentos (chunks).")

# 3. Embeddings
print("Generando embeddings (esto puede tardar un poco)...")
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4. Crear y guardar índice FAISS
print("Creando índice FAISS...")
db = FAISS.from_documents(docs, embeddings)
db.save_local(index_path)

print(f"¡Listo! Documentos indexados correctamente en la carpeta '{index_path}'.")