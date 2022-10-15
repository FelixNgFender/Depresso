from flair.models import TextClassifier
from flair.data import Sentence

classifier = TextClassifier.load('en-sentiment')
string = 'im a bit sad'
def preprocess(raw):
    return raw.strip()
def predict(input_text):
    text = preprocess(input_text)
    sentence = Sentence(text)
    classifier.predict(sentence)
    return sentence.score

print(predict(string))
