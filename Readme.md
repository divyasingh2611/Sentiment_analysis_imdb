# Sentiment Analysis API

A FastAPI-based REST API for sentiment analysis of text using machine learning.

## Description

This API provides sentiment analysis capabilities using a pre-trained machine learning model. It processes text input and returns sentiment classification as either "Positive" or "Negative".

## Features

- Text preprocessing and cleaning
- NLTK-based tokenization and lemmatization
- Removal of HTML tags, special characters, and stopwords
- FastAPI-powered REST endpoint
- Pydantic model validation

## Prerequisites

- Python 3.x
- Required packages (listed in requirements.txt)

## Installation

1. Clone the repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```
3. Ensure you have the model file (`model.pkl`) in the root directory

## Required Files

- `main.py`: Main application file containing the API implementation
- `requirements.txt`: List of Python dependencies
- `model.pkl`: Pre-trained machine learning model (not included in repository)

## API Endpoints

### POST /predict

Analyzes the sentiment of provided text.

**Request Body:**
```json
{
    "text": "Your text for analysis"
}
```

**Response:**
```json
{
    "sentiment": "Positive"
}
```

## Running the Application

To start the API server:

```bash
python main.py
```

The server will start at `http://127.0.0.1:8000`

## Usage Example

Using curl:
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text":"This is a great product!"}'
```

## Dependencies

- fastapi
- uvicorn
- scikit-learn
- nltk
- beautifulsoup4
- pydantic

## NLTK Downloads

The application automatically downloads the following NLTK data:
- punkt_tab
- wordnet
- stopwords

## IMDB Sentiment Analysis Database
Overview
This repository contains a SQLite database of 50,000 IMDB movie reviews with their associated sentiment labels (positive/negative). The dataset is structured to support sentiment analysis tasks and natural language processing projects.
Dataset Details

Total Reviews: 50,000
Features:

Review text (full movie reviews)
Sentiment (binary classification: positive/negative)


Format: SQLite database (.db file)
Table Name: imdb_movies

Database Structure
The database contains a single table 'imdb_movies' with two columns:

review: TEXT - Contains the full text of movie reviews
sentiment: TEXT - Contains the sentiment label ('positive' or 'negative')

Usage
To use this database in your Python project:
pythonCopyimport sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('imdb_data.db')

# Query the database
df = pd.read_sql_query("SELECT * FROM imdb_movies", conn)

# Don't forget to close the connection
conn.close()
# Purpose

This database is ideal for:
- Developing sentiment analysis models
- Training text classification algorithms
- Natural Language Processing (NLP) research
- Educational purposes in machine learning

Data Source
The dataset is sourced from IMDB movie reviews and has been processed and stored in a SQLite database format for easier access and manipulation.

## Requirements

Python 3.x
sqlite3
pandas (for easy data manipulation)

## Notes

- The API uses NLTK for text preprocessing
- Text cleaning includes HTML tag removal, special character removal, and lemmatization
- The model file must be present in the root directory for the application to work
