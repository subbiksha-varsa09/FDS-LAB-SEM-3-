import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import gutenberg

nltk.download('gutenberg')

nltk.download('punkt')
nltk.download('punkt_tab')

sample = gutenberg.raw("austen-emma.txt")

token = word_tokenize(sample)

wlist = []

for i in range(50):
    wlist.append(token[i])

wordfreq = [wlist.count(w) for w in wlist]

print("Pairs")
print(list(zip(wlist, wordfreq)))