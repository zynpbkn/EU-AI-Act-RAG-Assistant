__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from uuid import uuid4
from dotenv import load_dotenv

load_dotenv()

# --- AB Yapay Zeka Yasası kaynakları ---
urls = [
    "https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng",
    "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai",
    "https://commission.europa.eu/news-and-media/news/ai-act-enters-force-2024-08-01_en",
    "https://digital-strategy.ec.europa.eu/en/faqs/general-purpose-ai-models-ai-act-questions-answers"
]

# --- Web sayfalarını yükle ---
raw_documents = WebBaseLoader(urls).load()

# --- Metinleri parçalara ayır ---
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=200
)
split_documents = text_splitter.split_documents(raw_documents)

# --- Embedding modeli ---
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

# --- Chroma vektör veritabanı ---
vector_store = Chroma(
    collection_name="eu-ai-act",
    embedding_function=embeddings,
    persist_directory="/home/train/week_05_08/hw6_rag/chromadb",
)

# --- Belgeleri ekle ---
uuids = [str(uuid4()) for _ in range(len(split_documents))]
vector_store.add_documents(documents=split_documents, ids=uuids)

print("✅ Web sayfaları başarıyla yüklendi ve Chroma veritabanına eklendi!")
