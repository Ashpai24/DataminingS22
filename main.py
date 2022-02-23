# Importing re package (used for regular expression)
import os
import re
import nltk
from os.path import exists

FILE_NAME = "Bigrams_Occurrence.txt"
if exists(FILE_NAME):
    os.remove(FILE_NAME)

# Constructing Pattern for Parsing Sentences
pattern = re.compile(r"('?[A-Z],?'?\s?[a-z][^\d.!?]*-?[-\".!?])")

# Turning the file into a string
with open('hamlet_act1.txt', 'r') as f:
    contents = f.read()

# Current Regex does not end on the "--" & includes the stage directions
sentences = pattern.findall(contents)
print("Number of Sentences Mined: ", len(sentences))

# Pattern for Getting Noun and Verb Pairs
pattern1 = re.compile(r"\('[A-Z]?[a-z]+',\s'NN[A-Z]?[A-Z]?'\),\s\('[A-Z]?[a-z]+',\s'VB[A-Z]?'\)")

# Pattern for Getting Pronoun Verb Pairs
pattern2 = re.compile(r"\('[A-Z]?[a-z]+',\s'PRP'\),\s\('[A-Z]?[a-z]+',\s'VB[A-Z]?'\)")

noun_verb_pairs = []
pronoun_verb_pairs = []

# Tokenizing each Sentence to see POS (Part of Speech)
for word in sentences:
    sentence_with_tagset = nltk.pos_tag(nltk.word_tokenize(word))
    matches_n_v = pattern1.findall(str(sentence_with_tagset))
    matches_pn_v = pattern2.findall(str(sentence_with_tagset))

    # Adding each Regex Match to A list
    for match1 in matches_n_v:
        noun_verb_pairs.append(match1.lower())
    for match2 in matches_pn_v:
        pronoun_verb_pairs.append(match2.lower())

# Printing the Len of each Calculated List
print("Number of Noun Verb Pairs: " + str(len(noun_verb_pairs)))
print("Number of Pronoun Verb Pairs: " + str(len(pronoun_verb_pairs)))

combined_list = noun_verb_pairs + pronoun_verb_pairs
print("Number of Noun Verb and Pronoun Verb Pairs: " + str(len(combined_list)))

# '(w, POS), (w2, POS)' Structure --> (w1, w2, w3, ... wN)
pattern_parse = re.compile(r"([a-z]+)(?=',)")
wordlist = []
for element in combined_list:
    word_pair_matches = pattern_parse.findall(str(element))
    for match in word_pair_matches:
        wordlist.append(match)

# Converting (w1, w2, w3, ... wN) --> [(w1, w2), (w3, w4), ... (wN-1, wN)]
paired_list = [wordlist[i] + ' ' + wordlist[i + 1] for i in range(0, len(wordlist) - 1, 2)]
print(paired_list)

# Using Dictionary to Count Number of Pair Occurrences
dictionary = {}
for item in paired_list:
    if item in dictionary:
        dictionary[item] = dictionary[item] + 1;
    else:
        dictionary[item] = 1

# Printing top 10 K, V Pairs of Dictionary - Unless there is Tie
f = open(FILE_NAME, "a")
sorted_keys = sorted(dictionary, key=dictionary.get, reverse=True)
for r in sorted_keys:
    if dictionary[r] >= 3:
        f.write("Word Pair: " + r + " --> Number Occurrences: " + str(dictionary[r]) + "\n")

f.close()
