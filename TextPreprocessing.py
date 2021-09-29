from nltk.stem import LancasterStemmer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
#import spacy
import nltk
import string
import re
from wordfreq import zipf_frequency
from textblob import TextBlob


stemmer = LancasterStemmer()
#stemmer = PorterStemmer()

def stemSentence(sentence):
    """
    Apply stemming on a given ``sentence`` (see ``nltk.stem.lancaster``).

    """
    return stemmer.stem(sentence)

def removeStopwords(sentence):
    """
    Tokenizes a given ``sentence`` (see ``nltk.tokenize``) and removes stopwords from it (see ``nltk.corpus.stopwords``).

    We also remove custom selected stopwords: ["‘", "’","-",".","”","“",'.',"new","said",'—'].

    """
    tokens = word_tokenize(sentence)
    customStopwords = ["‘", "’","-",".","”","“",'.',"new","said",'—']
    allStopwords = stopwords.words() + word_tokenize(string.punctuation) + customStopwords
    return [w for w in tokens if w not in allStopwords]

def removeNumbers(sentence):
    """
    Removes numbers from a given ``sentence``.

    """
    return re.sub(r'\d+', '', sentence)

def parseSentence(sentence):
    """
    Applys ``removeNumbers``, ``stemSentence`` and ``removeStopwords`` on a given ``sentence``.

    """
    return removeStopwords(stemSentence(removeNumbers(sentence)))

def wordfreq(word):
    """
    Returns the frequency of a word in the English language, based on many sources of data (see https://pypi.org/project/wordfreq/).

    """
    return zipf_frequency(word,'en')

def getNames(word):
    """
    Returns and filters the entity type of a word in the English language (see https://pypi.org/project/spacy/).

    """
    names = []
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(word)
    for token in doc:
        if token.ent_type_ == "PERSON" or token.pos_ == "PROPN":
            names.append(token.text)
    return names
    '''
    Possible tags according to https://medium.com/@gianpaul.r/tokenization-and-parts-of-speech-pos-tagging-in-pythons-nltk-library-2d30f70af13b
    CC coordinating conjunction
    CD cardinal digit
    DT determiner
    EX existential there (like: “there is” … think of it like “there exists”)
    FW foreign word
    IN preposition/subordinating conjunction
    JJ adjective ‘big’
    JJR adjective, comparative ‘bigger’
    JJS adjective, superlative ‘biggest’
    LS list marker 1)
    MD modal could, will
    NN noun, singular ‘desk’
    NNS noun plural ‘desks’
    NNP proper noun, singular ‘Harrison’
    NNPS proper noun, plural ‘Americans’
    PDT predeterminer ‘all the kids’
    POS possessive ending parent’s
    PRP personal pronoun I, he, she
    PRP$ possessive pronoun my, his, hers
    RB adverb very, silently,
    RBR adverb, comparative better
    RBS adverb, superlative best
    RP particle give up
    TO, to go ‘to’ the store.
    UH interjection, errrrrrrrm
    VB verb, base form take
    VBD verb, past tense took
    VBG verb, gerund/present participle taking
    VBN verb, past participle taken
    VBP verb, sing. present, non-3d take
    VBZ verb, 3rd person sing. present takes
    WDT wh-determiner which
    WP wh-pronoun who, what
    WP$ possessive wh-pronoun whose
    WRB wh-abverb where, when
    '''

def getNouns(words):
    """
    Returns all nouns of the list ``words``.

    """
    nounTags = ["NN","NNS","NNP","NNPS","FW"]
    return tagWords(words, nounTags)

def getVerbs(words):
    """
    Returns all verbs of the list ``words``.

    """
    verbTags = ["VBD","VBG","VBN","VBP","VBZ"]
    return tagWords(words,verbTags)

def tagWords(words, tags):
    """
    Computes tags for all ``words`` and optionally applies a filter which is a list of tags.

    """
    txt = " ".join(words)
    tagged = nltk.pos_tag(nltk.word_tokenize(txt))
    if len(tags) == 0:
        #No filters given as input, return all words
        return tagged
    else:
        return [x[0] for x in tagged if x[1] in tags]