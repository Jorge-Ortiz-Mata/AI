import chromadb

chroma_client = chromadb.HttpClient(host='localhost', port=8000)

# ================================== Access to the collection ============================

collection = chroma_client.get_collection(name="car_collection")

result = collection.query(
  query_texts="Que es un coche?",
  n_results=4,
  include=["documents"]
)

print(result)
