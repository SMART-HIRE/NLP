import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_name(resume_text):
    word_tokens = word_tokenize(resume_text)
    tagged_tokens = pos_tag(word_tokens)
    chunk_grammar = "NP: {<NNP>+}"
    parser = nltk.RegexpParser(chunk_grammar)
    parsed_text = parser.parse(tagged_tokens)
    names = []
    for subtree in parsed_text.subtrees():
        if subtree.label() == 'NP':
            name = ""
            for leaf in subtree.leaves():
                name += leaf[0] + ' '
            names.append(name.strip())
    return names

resume_text = "John Doe is a software engineer with 5 years of experience."
names = extract_name(resume_text)
print(names)  # ['John Doe']
