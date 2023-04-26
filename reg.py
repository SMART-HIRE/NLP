
import json
import sys,fitz
import spacy
#nlp = spacy.load(r"output/model-best")
fname="sruthy.pdf"
doc=fitz.open(fname)
text=" "
for page in doc:
    text=text + str(page.get_text())
textinput=' '.join(text.split())

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop = stopwords.words('english')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
import en_core_web_sm
from spacy.matcher import Matcher
nlp = en_core_web_sm.load()
matcher = Matcher(nlp.vocab)
def extract_name(resume_text):
    nlp_text = nlp(resume_text)
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]#proper noun
    #matcher.add('NAME', None, pattern)
    matcher.add('NAME', [pattern], on_match=None)
    matches = matcher(nlp_text)
    for match_id, start, end in matches:
        span = nlp_text[start:end]
        return span.text
#print('Name:',extract_name(textinput))
name=extract_name(textinput)
import re
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))#stopword 
EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S', 
            'ME', 'M.E', 'M.E.', 'M.B.A', 'MBA', 'MS', 'M.S', 
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH', 
            'SSLC', 'SSC' 'HSC', 'CBSE', 'ICSE', 'X', 'XII','Diploma in Electronics and Communication','Diploma in Computer Science','Computer science Engineering','Electronics and Electrical Engineering','Electronics and Communication engineering'
        ]
def extract_education(resume_text):
    nlp_text = nlp(resume_text)
    #nlp_text = [sent.string.strip() for sent in nlp_text.sents]
    nlp_text = [sent.text.strip() for sent in nlp_text.sents]
    edu = {}
    for index, text in enumerate(nlp_text):
        for tex in text.split():
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex.upper() in EDUCATION and tex not in STOPWORDS:
                edu[tex] = text + nlp_text[index + 1]
    education = []
    for key in edu.keys():
        year = re.search(re.compile(r'(((20|19)(\d{})))'), edu[key])
        if year:
            education.append((key, ''.join(year[0])))
        else:
            education.append(key)
    return education
qualif= extract_education(textinput)
import pandas as pd
import spacy
nlp = spacy.load('en_core_web_sm')
nlp_text = nlp(textinput)
noun_chunks = nlp_text.noun_chunks
STOPWORDS = set(stopwords.words('english'))#stopword 
SKILLS = [
            'Python','Java', 'C++', 'C', 'ANDROID STUDIO', 
            'HTML', 'SQL', 'FIREBASE','CSS',
        ]
def extract_qualification(resume_text):
    nlp_text = nlp(resume_text)
    #nlp_text = [sent.string.strip() for sent in nlp_text.sents]
    nlp_text = [sent.text.strip() for sent in nlp_text.sents]
    edu = {}
    for index, text in enumerate(nlp_text):
        for tex in text.split():
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex.upper() in SKILLS and tex not in STOPWORDS:
                edu[tex] = text + nlp_text[index + 1]
    education = []
    for key in edu.keys():
        year = re.search(re.compile(r'(((20|19)(\d{})))'), edu[key])
        if year:
            education.append((key, ''.join(year[0])))
        else:
            education.append(key)
    return education
#print('Skills: ',extract_qualification(textinput))
skill= extract_qualification(textinput)


def extract_mobile_number(resume_text):
    phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), resume_text)
    
    if phone:
        number = ''.join(phone[0])
        if len(number) > 10:
            return number
        else:
            return number 
#print('Mobile Number: ',extract_mobile_number(textinput))
mob=extract_mobile_number(textinput)


def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)
#print('Mail id: ',extract_email_addresses(textinput))
mail=extract_email_addresses(textinput)
def extract_linkedin(string):
    linkedin_pattern = r"linkedin\.com\/in\/\w+[0-9-_a-zA-Z]+\/?"
    linkedin_url = re.findall(linkedin_pattern,string)
    return linkedin_url
l=extract_linkedin(textinput)
def extract_github(string):
    #github_pattern = r"github\.com\/\w+[0-9-_a-zA-Z]+\/?"
    github_pattern = r"^w+[0-9-_a-zA-Z]+\(github\.com\)$"
    # ^name02\(github\.com\)$"
    github_url = re.findall(github_pattern,string)
    return github_url
g=extract_github(textinput)
data = {
    "Name": name,
    "Qualification": qualif,
    "Skills":skill,
    "Mobile Number": mob,
    "Mail id":mail,
    "LinkedIn Url":l,
    "Github URL":g
}

# Open a new file in write mode and write the data to it in JSON format
with open('example.json', 'w') as f:
    json.dump(data, f)

# Print a message to confirm that the data has been written to the file
print("Data written to JSON file successfully!")