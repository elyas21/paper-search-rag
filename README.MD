# Paper search

---

## Overview

---

This project is a web application that utilizes natural language processing (NLP) to summarize and analyze research papers. The application is built using Flask, a micro web framework for Python, and leverages the Ollama library for LLM (Large Language Model) functionality. The application employs a Retrieval-Augmented Generator (RAG) design to retrieve relevant papers from PubMed and generate summaries.

### Features

---

- Search and summarize research papers using a user-provided query
- Generate vector embeddings for papers
- Utilize a database to store and retrieve paper information
- Implement a RAG design to retrieve relevant papers from PubMed

## Retrieval-Augmented Generator (RAG) Design

---

The RAG design is a type of NLP architecture that combines the strengths of both retrieval and generation models. In this project, the RAG design is used to retrieve relevant papers from PubMed and generate summaries. The RAG design consists of two main components:

### 1. Retriever

---

The retriever is responsible for searching PubMed and retrieving a set of relevant papers based on the user-provided query. In this project, the retriever is implemented using the PubMed API.

### 2. Generator

---

The generator is responsible for generating a summary of the retrieved papers. In this project, the generator is implemented using the Ollama library, which is a LLM that can generate human-like text.

## PubMed Implementation

---

This project uses the PubMed API to retrieve relevant papers based on the user-provided query. PubMed is a free database of biomedical literature that is maintained by the National Library of Medicine (NLM). The PubMed API provides access to the PubMed database and allows developers to retrieve paper metadata, abstracts, and full-text articles.

In this project, the PubMed API is used to retrieve paper metadata and abstracts. The retrieved papers are then passed to the generator, which generates a summary of the papers.

## Requirements

---

- Python 3.x
- Flask 3.1.0
- Ollama 0.4.2
- NumPy 2.1.3
- BeautifulSoup4 4.12.0
- Langchain-community 0.3.10
- PubMed API credentials (obtained by registering for a PubMed API key)

## Installation

---

pip install -r requirement.txt

## Run the web

python app.py
