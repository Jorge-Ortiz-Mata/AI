import chromadb
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

chroma_client = chromadb.HttpClient(host='localhost', port=8000)

# ================================== Create Car collection ============================
collection = chroma_client.create_collection(name="car_collection")

loader = TextLoader("car.txt")
documents = loader.load()

text_splitter_config = CharacterTextSplitter(chunk_size=600, chunk_overlap=0)
docs = text_splitter_config.split_documents(documents)

chunks_ids = []
chunks_texts = []

for index, chunk in enumerate(docs):
  chunks_ids.append(f'id{index + 1}')
  chunks_texts.append(chunk.page_content)

collection.add(
  documents=chunks_texts,
  ids=chunks_ids
)

# ================================== Create Iphone collection ============================
collection = chroma_client.create_collection(name="iphone_collection")

loader = TextLoader("iphone.txt")
documents = loader.load()

text_splitter_config = CharacterTextSplitter(chunk_size=600, chunk_overlap=0)
docs = text_splitter_config.split_documents(documents)

chunks_ids = []
chunks_texts = []

for index, chunk in enumerate(docs):
  chunks_ids.append(f'id{index + 1}')
  chunks_texts.append(chunk.page_content)

collection.add(
  documents=chunks_texts,
  ids=chunks_ids
)
