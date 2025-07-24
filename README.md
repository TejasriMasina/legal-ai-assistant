# 🧠 Legal AI Assistant

A lightweight AI-powered assistant to search and summarize legal case documents using only open-source tools.

## Features

- Web scrapes real legal case data
- Cleans and processes legal texts
- Removes duplicate case entries
- Summarizes each case using transformer models
- Builds semantic embeddings and FAISS index
- Searches and retrieves relevant cases based on user queries
- Interactive Streamlit interface for legal professionals

## Tech Stack

- **BeautifulSoup** – Web scraping
- **Transformers** – `facebook/bart-large-cnn` for summarization
- **Sentence Transformers** – `all-MiniLM-L6-v2` for semantic embeddings
- **FAISS** – Efficient vector search
- **Streamlit** – Frontend web app

## Project Workflow

1. **`legal_doc.py`** – Scrape and save raw case data
2. **`clean_text.py`** – Clean unnecessary formatting from case text
3. **`deduplicate.py`** – Identify and remove duplicate cases
4. **`summarizer.py`** – Generate summaries using a transformer model
5. **`embedder.py`** – Create embeddings and save them in a FAISS index
6. **`search_engine.py`** – Search similar cases via semantic similarity
7. **`app.py`** – Run the Streamlit app to interact with the system

## JSON Data Files

- `legal_cases_dataset.json` – Raw scraped cases
- `cleaned_legal_cases.json` – After cleaning
- `cleaned_legal_cases_deduplicate.json` – After removing duplicates
- `summaries.json` – Summarized content

## 🔍 What Happens When You Enter a Legal Query?

When a user types a query like _"termination of parental rights due to abuse"_, the system:

1. Converts the query into a vector using `all-MiniLM-L6-v2`
2. Searches the FAISS index for the **top 5 most semantically similar cases**
3. Displays each result with:
   - **Case Name**
   - **Court**
   - **Date**
   - **Summary** (generated using `facebook/bart-large-cnn`)

This enables fast discovery of **relevant precedents**, improving research efficiency.
