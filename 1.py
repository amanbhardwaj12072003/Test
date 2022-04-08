import gensim
import os
from gensim.utils import simple_preprocess

doc = open('/home/garvit/Desktop/Toipc Modelling' , encoding='utf-8')

tokenized = []

for sentence in doc.read().split('.'):
    tokenized.appen(simple_preprocess(sentence , deacc = True))

print(tokenized)