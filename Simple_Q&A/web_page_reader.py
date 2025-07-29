# Import the OpenAI LLM integration from llama_index
from llama_index.llms.openai import OpenAI
# Import the SimpleWebPageReader for loading web page content
from llama_index.readers.web import SimpleWebPageReader
# Import the VectorStoreIndex for indexing and querying documents
from llama_index.core import VectorStoreIndex
import llama_index
import os
# Import dotenv for loading environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables (such as API keys) from .env file
load_dotenv()

def main(url: str) -> None:
    # Load and parse the web page content from the given URL
    document = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    # Create a vector index from the loaded document
    index = VectorStoreIndex.from_documents(documents=document)
    # Create a query engine from the index
    query_engine = index.as_query_engine()
    # Query the index for information about the history of Generative AI
    response = query_engine.query("What is the history og Generative AI")
    # Print the response from the query
    print(response)

# Entry point: run the main function with a sample URL if this script is executed directly
if __name__=="__main__":
    main(url="https://medium.com/@raja.gupta20/generative-ai-for-beginners-part-1-introduction-to-ai-eadb5a71f07d")

