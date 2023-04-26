import spacy
nlp = spacy.load(r"output/model-best")
text = "Govardhan K is a javascript ,python,java."
doc = nlp(text)
print(doc.ents)
for ent in doc.ents:
    print (ent.text,">>>", ent.label_)