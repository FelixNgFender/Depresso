from flair.models import TextClassifier
from flair.data import Sentence

classifier = TextClassifier.load('en-sentiment')
sentence = Sentence('Mai-san and Shouko-san both love me, but I love Tenshi-sama.')
classifier.predict(sentence)# print sentence with predicted labels
print('Sentence above is: ', sentence.labels)
