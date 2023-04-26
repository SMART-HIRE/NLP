import sys,fitz
import spacy
nlp = spacy.load(r"output/model-best")
fname="alice.pdf"
doc=fitz.open(fname)
text=" "
for page in doc:
    text=text + str(page.get_text())
text=' '.join(text.split())
print(text)
doc = nlp(text)
print(doc.ents)
for ent in doc.ents:
    print (ent.text,">>>", ent.label_)