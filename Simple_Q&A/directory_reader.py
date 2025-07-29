from llama_index.readers.web import SimpleDirectoryReader
from llama_index import VectorStoreIndex
import os
from dotenv import load_dotenv
import logging
import sys

load_dotenv()

def main(url:str)-> None:
    """
    Loads all documents from the specified directory, creates a vector index,
    and queries the index to summarize the content of the articles.
    """
    documents = SimpleDirectoryReader(url).load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("What did the artical saying please sumamrize it")
    print(response)

    if __name__=='__main__':
        main(url='C:\\Users\\mitesh\\data')

