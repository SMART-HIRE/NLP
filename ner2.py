import spacy
import json
#import pandas as pd
import os
from tqdm import tqdm
from spacy.tokens import DocBin
with open('data11.json') as fp:
    train_data= json.load(fp)
nlp=spacy.blank("en")
db=DocBin()
for text, annot in zip(tqdm(train_data)): # data in previous format
    doc = nlp.make_doc(text) # create doc object from text
    ents = []
    for start, end, label in annot["entities"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # label the text with the ents
    db.add(doc)
print(len(train_data))
os.chdir(r'C:\Users\Anusree\Desktop\NLP3\env')
db.to_disk("./train.spacy")