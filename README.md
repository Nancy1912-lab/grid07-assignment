# Grid07 AI Assignment

This project is a simple AI workflow system built using Python, LangGraph, FAISS, and sentence-transformers.

## Features

- Persona routing using vector similarity
- LangGraph workflow pipeline
- Prompt safety filtering
- Dynamic content generation

## Technologies Used

- Python
- LangGraph
- FAISS
- Sentence Transformers

## Project Structure

- main.py
- router.py
- graph_flow.py
- rag_engine.py
- personas.py

## Run Project

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run project:

```bash
python main.py
```

## Example Query

Input:
bitcoin trends

Output:
crypto persona selected