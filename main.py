import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import re
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')


with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_sentiment(text):
    def clean_text(text):
        text = BeautifulSoup(text, "html.parser").get_text()
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'http\S+', '', text)
        text = text.lower()
        text = ''.join([i for i in text if i.isalpha() or i.isspace()])
        tokens = nltk.word_tokenize(text)
        lemma = WordNetLemmatizer()
        tokens = [lemma.lemmatize(i) for i in tokens if i not in stopwords.words('english')]
        text = ' '.join(tokens)
        return text
    cleaned_text = clean_text(text)
    prediction = model.predict([cleaned_text])
    if prediction[0] == 1:
        return "Positive"
    else:
        return "Negative"

app = FastAPI()

class TextInput(BaseModel):
    text: str


@app.post("/predict")
async def predict(input: TextInput):
    result = predict_sentiment(input.text)

    return {"sentiment": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



