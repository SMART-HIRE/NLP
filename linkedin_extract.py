
# # import json
# # import sys,fitz
# # import spacy
# # #nlp = spacy.load(r"output/model-best")
# # fname="Profile.pdf"
# # doc=fitz.open(fname)
# # text=" "
# # for page in doc:
# #     text=text + str(page.get_text())
# # textinput=' '.join(text.split())
# # print(textinput)



# import fitz
# import re
# filename = 'Profile.pdf'
# heading = 'Top Skills'
# with fitz.open(filename) as doc:
#     for page in doc:
#         text = page.get_text()
#         if text:
#             match = re.search(rf'{heading}\s*(.+?)\n\n', text, re.DOTALL)
#             if match:
#                 details = match.group(1).strip()
#                 print(details)



import PyPDF2

pdfFileObj = open('Profile.pdf', 'rb') # replace example.pdf with the name of your PDF file
pdfReader = PyPDF2.PdfReader(pdfFileObj)
heading = 'Top Skills'
for pageNum in range(len(pdfReader.pages)):
    pageObj = pdfReader.pages[pageNum]
    text = pageObj.extract_text()
    if heading in text:
        startIndex = text.index(heading)
        endIndex = text.index('\n', startIndex)
        details = text[startIndex:endIndex]
        print(details)
pdfFileObj.close()

