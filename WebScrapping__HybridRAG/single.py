
import asyncio
import os
import aiofiles
import logging
import urllib.parse
from crawl4ai import AsyncWebCrawler

# Folder to store all markdown files
OUTPUT_FOLDER = "extracted_pages"

# Ensure the folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="crawler_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Rate limiting: Maximum requests per second
MAX_REQUESTS_PER_SECOND = 2
REQUEST_DELAY = 1 / MAX_REQUESTS_PER_SECOND

# Custom User-Agent header
CUSTOM_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

async def fetch_and_save_page(url, index):
    """Fetch page content and save to a markdown file."""
    try:
        async with AsyncWebCrawler(headers=CUSTOM_HEADERS) as crawler:
            result = await crawler.arun(url=url, screenshot=False)
            
            if not result:
                logging.error(f"Failed to fetch: {url}")
                print(f"Failed to fetch: {url}")
                return

            # # Ensure correct method is used to access links
            # links_data = result.links  # Use the correct attribute or method
            
            text = result.links.get('text', 'No text')
            print(text)
            content = result.markdown
            filename = os.path.join(OUTPUT_FOLDER, f"page_{index}.md")

            async with aiofiles.open(filename, "w", encoding="utf-8") as f:
                await f.write(f"# Extracted Content from {url}\n\n{text}\n\n{content}")

            # print(result)
            print(f"Saved: {filename}")

        await asyncio.sleep(REQUEST_DELAY)  # Rate limiting inside function
    except Exception as e:
        logging.error(f"Error fetching {url}: {e}", exc_info=True)
        print(f"Error fetching {url}: {e}")





async def main():
    start_url = "https://us.pg.com/annualreport2024/"

    try:
        async with AsyncWebCrawler(headers=CUSTOM_HEADERS) as crawler:
            result = await crawler.arun(url=start_url, screenshot=True)

        if not result or not hasattr(result, "links"):
            logging.error("Failed to fetch the start URL or no links found.")
            print("Failed to fetch the start URL or no links found.")
            return
        
        links = result.links.get("internal", [])
        
        if not links:
            logging.warning("No internal links found.")
            print("No internal links found.")
            return

        tasks = []
        for index, link in enumerate(links):
            href = link.get("href", "").strip()
            
            if not href:
                continue

            full_url = urllib.parse.urljoin(start_url, href)  # Safer URL handling
            tasks.append(fetch_and_save_page(full_url, index))

        await asyncio.gather(*tasks)  # Run all requests asynchronously

    except Exception as e:
        logging.error(f"Error in main function: {e}", exc_info=True)
        print(f"Error in main function: {e}")

if __name__ == "__main__":
    asyncio.run(main())











# Performing hybrid rag




from langchain_community.retrievers import PineconeHybridSearchRetriever
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

api_key = os.getenv('pc_api_key')

from pinecone import Pinecone, ServerlessSpec

index_name="hybrid-search-langchain-pinecone-1" # in small caps only

## initialize the Pinecone client
pc=Pinecone (api_key=api_key)

#create the index
if index_name not in pc.list_indexes().names():
    pc.create_index(
                    name=index_name,
                    dimension=768, #dimension of dense vector by default dimension
                    metric='dotproduct', ## sparse values supportted only for dotproduct
                    spec=ServerlessSpec(cloud='aws', region="us-east-1")
                    )

index = pc.Index(index_name)
index

from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
)

# Example text to generate embeddings
sample_text = "This is a test for embeddings."

# Generate the embedding
vector = embeddings.embed_query(sample_text)

# Get the dimension of the embedding
print("Embedding Dimension:", len(vector))

##  sparse matrix
from pinecone_text.sparse import BM25Encoder
bm25_encoder = BM25Encoder().default()
bm25_encoder

# Import necessary modules for getting chunked text
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter



directory_path = r"E:\craw4ai1\extracted_pages"
loader = DirectoryLoader(directory_path, glob="*.md")  # adjust glob pattern for different file types
# Load documents from the directory
documents = loader.load()

# Set up text splitter for chunking
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

#Split documents into chunks
chunked_docs = text_splitter.split_documents(documents)

chunked_docs

# Extract the page_content from each document and store it in a list
contents = [doc.page_content for doc in chunked_docs]
contents



import nltk
nltk.download('punkt_tab', download_dir='E:\craw4ai1\.venv/nltk_data')

nltk.data.path.append('E:\craw4ai1\.venv/nltk_data')

# tfidf values on these sentence
bm25_encoder.fit (contents)

# store the values to a json file 
bm25_encoder.dump("bm25_values.json")

# load to your BM25Encoder object 
bm25_encoder = BM25Encoder().load("bm25_values.json")

# making hybrid retriever
retriever = PineconeHybridSearchRetriever(embeddings=embeddings, sparse_encoder=bm25_encoder, index=index)
retriever

retriever.add_texts(contents)

User_Query = '''
what was the operating cash flow in 2020?'''

retrieved_chunks = retriever.invoke(User_Query, k=5)
retrieved_chunks

# from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

from langchain_ollama import ChatOllama

# Initialize the LLM
llm = ChatOllama(
                            model="deepseek-r1",
                            streaming=True,
                        )

# 4. Create the Prompt Template for document processing
document_prompt = PromptTemplate(input_variables=["context"], template="Given the following context:\n{context}\nPlease answer the query: {User_Query} concisely:")

# 5. Set up the StuffDocumentsChain
chain = create_stuff_documents_chain( llm=llm, prompt=document_prompt,)



# 7. Run the chain with the formatted documents
response = chain.invoke({"context": retrieved_chunks, 'User_Query': User_Query})

# 8. Output the result
print(response)



