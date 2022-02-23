# Importing re package (used for regular expression)
import re
import nltk

nltk.help.upenn_tagset()
# Constructing Pattern for words with only capital letters
pattern = re.compile(r"('?[A-Z],?'?\s?[a-z][^\d.!?]*-?[-\".!?])")

# Turning the file into a string
with open('hamlet_act1.txt', 'r') as f:
    contents = f.read()

# Current Regex does not end on the "--" & includes the stage directions
sentences = pattern.findall(contents)
print("Number of Sentences Mined: ", len(sentences))

pattern1 = re.compile(r"\('[A-Z]?[a-z]+',\s'NN[A-Z]?[A-Z]?'\),\s\('[A-Z]?[a-z]+',\s'VB[A-Z]?'\)")
pattern2 = re.compile(r"\('[A-Z]?[a-z]+',\s'PRP'\),\s\('[A-Z]?[a-z]+',\s'VB[A-Z]?'\)")

noun_verb_pairs = []
pronoun_verb_pairs = []
for word in sentences:
    sentence_with_tagset = nltk.pos_tag(nltk.word_tokenize(word))
    print(str(sentence_with_tagset))
    matches_n_v = pattern1.findall(str(sentence_with_tagset))
    matches_pn_v = pattern2.findall(str(sentence_with_tagset))
    for match1 in matches_n_v:
        noun_verb_pairs.append(match1.lower())
    for match2 in matches_pn_v:
        pronoun_verb_pairs.append(match2.lower())

print(len(noun_verb_pairs))
print(len(pronoun_verb_pairs))

combined_list = noun_verb_pairs + pronoun_verb_pairs
print(combined_list)
pattern_parse = re.compile(r"([a-z]+)(?=',)")
wordlist = []

for element in combined_list:
    word_pair_matches = pattern_parse.findall(str(element))
    for match in word_pair_matches:
        wordlist.append(match)

paired_list = [wordlist[i] + ' ' + wordlist[i + 1] for i in range(0, len(wordlist) - 1, 2)]

dictionary = {}
for item in paired_list:
    if item in dictionary:
        dictionary[item] = dictionary[item] + 1;
    else:
        dictionary[item] = 1

'''for k, v in dictionary.items():
    print(k, v)'''