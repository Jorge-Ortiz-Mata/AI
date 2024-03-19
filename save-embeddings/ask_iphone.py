import chromadb

chroma_client = chromadb.HttpClient(host='localhost', port=8000)

# ================================== Access to the collection ============================

collection = chroma_client.get_collection(name="iphone_collection")

result = collection.query(
  query_texts=["Cual sera el tamaño de la pantalla?"],
  n_results=4,
  include=["documents"]
)

print(result)
