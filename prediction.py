from flair.models import TextClassifier
from flair.data import Sentence
import math

classifier = TextClassifier.load('en-sentiment')
string = 'im a bit sad'
def preprocess(raw):
    return raw.strip()

def predict_raw(input_text):
    text = preprocess(input_text)
    sentence = Sentence(text)
    classifier.predict(sentence)
    sign = 1 if sentence.tag == "POSITIVE" else -1
    return sign * sentence.score

def predict_depression(raw):
    return round(max(0, min(10, 1.5 * math.atanh(-raw) + 5)))

if __name__ == "__main__":
    print(predict_raw(string))