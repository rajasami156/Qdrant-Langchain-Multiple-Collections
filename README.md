

# Multi-Collection Chatbot with LangChain, OpenAI, and Qdrant 🚀 
### Welcome to our Multi-Collection Chatbot project! 

This project utilizes the power of LangChain, OpenAI embeddings, and Qdrant to manage multiple collections of text data, enabling specific querying across distinct datasets. Whether you're looking for advice, information, or answers within different contexts, our setup allows for efficient retrieval from segregated data collections. 📚

## Features
Multiple Collections Management: Create and manage multiple Qdrant collections to store varied datasets. 🗂️
Custom Queries: Send queries to specific collections to get relevant responses based on the dataset's context. 🔍
Integration with OpenAI: Leverage OpenAI embeddings for advanced understanding and matching of queries to the text data. 🧠
Efficient Data Handling: Utilize LangChain and Qdrant for optimized text data storage and retrieval. ⚡

## Getting Started
Prerequisites
Python 3.8+
OpenAI API Key
Qdrant running locally or hosted
Installation
Clone the Repository


How It Works
Collections Creation: The script first creates separate Qdrant collections for each text file, enabling isolated data management.
Data Ingestion: Texts are split into chunks and ingested into their respective collections, with OpenAI embeddings used for vector representation.
Querying: Leveraging LangChain's RetrievalQA, the setup allows for querying specific collections, using OpenAI embeddings to match queries to the most relevant texts.


Contributions
We welcome contributions and suggestions! Please create an issue or pull request to help improve the project. 🤝
