from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Qdrant
from qdrant_client.http.models import Distance, VectorParams
from langchain_community.vectorstores import qdrant
from langchain_openai import OpenAIEmbeddings
from qdrant_client.http.models import Distance, VectorParams
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from qdrant_client.http import models
from qdrant_client import QdrantClient
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import qdrant_client
import getpass
import os

load_dotenv()

url = os.getenv('Qdrant_URL')
qrdant_api_key=os.getenv('Qdrant_API_KEY')
qdrant_client = QdrantClient(url=url, api_key= qrdant_api_key)
api_key = os.getenv('OpenAI_API_Key')
embeddings = OpenAIEmbeddings(api_key=api_key)
print("Success in importing modules")



file_names = ['story1.txt', 'story2.txt', 'story3.txt']

# Create collections for each file
collections = []
for file_name in file_names:
    try:
        collection_name = f"{os.path.splitext(file_name)[0]}-collection"
        qdrant_client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
        )
        collections.append(collection_name)
        print(f"Collection has been append{collections}")
    except Exception as e:
        print(f'Failed to create the collection for {file_name}: {e}')



def get_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size=1000, 
        chunk_overlap= 200,
        length_function=len
        )
    chunks = text_splitter.split_text(text)
    return chunks

for file_name, collection_name in zip(file_names, collections):
    with open(file_name) as f:
        raw_text = f.read()
    texts = get_chunks(raw_text)
    vector_store = Qdrant(
        client=qdrant_client, collection_name=collection_name,
        embeddings=embeddings,
    )
    vector_store.add_texts(texts)
print("i think code works correct till here")


qas = []
try: 
    for collection_name in collections:
        vector_store = Qdrant(
            client=qdrant_client, collection_name=collection_name,
            embeddings=embeddings,
        )
        qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type = "stuff",
                                 retriever= vector_store.as_retriever()
                )          

        qas.append(qa)
except Exception as e:
    print(f"Error: {e}")




collection_name = 'story3-collection'    # SIMPLY CHANGE THE COLLECTION TO DO THE QUERY 
if collection_name in collections:
    collection_index = collections.index(collection_name)
    
    # Use the corresponding RetrievalQA object for the query
    qa = qas[collection_index]
    query = "What is the wifi password?"
    response = qa.invoke(query)
    print("Query:", query)
    print("Response:", response)
else:
    print(f"Collection {collection_name} not found.")
