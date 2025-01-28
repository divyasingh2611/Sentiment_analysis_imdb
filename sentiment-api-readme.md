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

## Notes

- The API uses NLTK for text preprocessing
- Text cleaning includes HTML tag removal, special character removal, and lemmatization
- The model file must be present in the root directory for the application to work
