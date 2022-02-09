# Importing re package (used for regular expression)
import re
from nltk import tokenize
# Constructing Pattern for words with only capital letters
pattern = re.compile(r"\b[A-Z][A-Z]+\b")

# Turning the file into a string
with open('hamlet_act1.txt', 'r') as f:
    contents = f.read()

# Act 1 without the names of the character
content_no_names = re.sub(pattern, '', contents)

# Removing White Space (This was copied from stack overflow post)
content = "".join([s for s in content_no_names.strip().splitlines(True) if s.strip()])

# Creating a RegEx Pattern to mine Sentences:
'''
    1. Sentences can end in the following character set: ?, !, .
    2. The end character of a sentence is followed by a space (' ') then a capital letter    
'''

pattern = re.compile(r'([A-Z][^\.!?]+[\.!?])')
list_of_sentences = re.findall(pattern, content)

print(list_of_sentences)
# To se





