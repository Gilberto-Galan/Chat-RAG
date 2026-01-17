from transformers import pipeline
from langchain_classic.llms import HuggingFacePipeline
from langchain_classic.embeddings import HuggingFaceEmbeddings
from langchain_classic.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA
from langchain_classic.prompts import PromptTemplate

# 1. Cargar Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 2. Cargar FAISS
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# REDUCIMOS k a 2 para no pasarnos del límite de 512 tokens
retriever = db.as_retriever(search_kwargs={"k": 2})

# 3. Configurar el LLM
# Añadimos truncation=True para que no explote si se pasa del límite
pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=100,
    truncation=True, 
    model_kwargs={"max_length": 512}
)
llm = HuggingFacePipeline(pipeline=pipe)

# 4. PROMPT OBLIGATORIO (Para que no de respuestas aleatorias)
template = """Usa el siguiente contexto para responder la pregunta al final. 
Si no sabes la respuesta, di que no lo sabes, no intentes inventar.
Contexto: {context}
Pregunta: {question}
Respuesta corta:"""

PROMPT = PromptTemplate(template=template, input_variables=["context", "question"])

# 5. Cadena RAG
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": PROMPT}
)

print("Chat listo. Probando con contexto optimizado...")

while True:
    user_input = input("\nTu: ")
    if user_input.lower() in ["salir", "exit"]: break
    
    # Usamos invoke en lugar de run para evitar el Warning
    resultado = qa.invoke({"query": user_input})
    print(f"IA: {resultado['result']}")