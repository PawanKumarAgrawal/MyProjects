Developed a web-based knowledge base that implements a Hybrid Retrieval-Augmented Generation (RAG) pipeline! 🔥
🌐 Project Overview

This project focuses on creating an intelligent knowledge base by leveraging a Hybrid RAG approach. The system is designed to scrape data from specified websites, process and store the information efficiently, and provide insightful responses to user queries.
🔍 User Query Example

User Query:
"Analyze P&G's sustainability with key metrics in a summarized way."
✨ How It Works

    Data Extraction:
        Input a website URL into the system.
        The system scrapes all data from the provided URL, including one level of hyperlink drill-down.

    Data Storage:
        The extracted data is stored in Pinecone, facilitating efficient retrieval.

    Response Generation:
        Upon receiving a user query, the system retrieves relevant information from the stored data.
        Generates a coherent and informative response based on the retrieved data.

🔍 Tech Stack

    Data Storage:
        Pinecone (Note: This is the only non-open-source component)

    Models:
        Private embedding model
        Private text generation Large Language Model (LLM)

🎯 Next Steps

    Transition to an open-source hybrid vector database to enhance efficiency and control over the data storage and retrieval process.