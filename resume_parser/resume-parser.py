from pyresparser import ResumeParser

import en_core_web_sm
nlp = en_core_web_sm.load()

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

data = ResumeParser('deedy-cv.pdf').get_extracted_data()


# Print out data
for k, v in data.items():
    # Since value may contain non-ascii character. We need to encode it. 
    # In this case, all non-ascii characters will return blank
    v_str = str(v).encode('ascii', 'ignore').decode()
    print(f"{k}:\n{v_str}\n")


















# # Iterate over each experience
# for experience in experiences:
#     try:
#         print(experience)
#     except UnicodeEncodeError:
#         print(experience.encode('utf-8'))


# for experience in experiences:
#     doc = nlp(experience)
#     # Perform any NLP task on 'doc'. For example, print the tokens:
#     for token in doc:
#         if token.is_alpha:
#             print(token.text)

#             # # The text
#             # print('Text:', token.text)
#             # # The base form of the word
#             # print('Lemma:', token.lemma_)
#             # # The simple UPOS part-of-speech tag
#             # print('POS:', token.pos_)
#             # # The detailed part-of-speech tag
#             # print('Tag:', token.tag_)
#             # # Syntactic dependency, i.e. the relation between tokens
#             # print('Dep:', token.dep_)
#             # # The word shape - Capitalization, punctuation, digits
#             # print('Shape:', token.shape_)
#             # # Is the ftoken an alpha character?
#             # print('Is alpha:', token.is_alpha)
#             # # Is the token part of a stop list, i.e. the most common words of the language?
#             # print('Is stop:', token.is_stop)
#             # # gives you the token’s text with its original trailing whitespace if it had any
#             # print('Text with trailing space:', token.text_with_ws)
#             # # returns the trailing whitespace on the token (empty string if there was no whitespace)
#             # print('Trailing whitespace:', token.whitespace_)

# list = [data["experience"]]

# print(list)

# # print("Experience:", data["experience"])