from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
def create_freq_table(text):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    #ps = PorterStemmer()

    freqtable = {}
    for word in words:
        #word = ps.stem(word)
        if word  in stopWords:
            continue
        else:
            if word in freqtable:
                freqtable[word]+=1
            else:
                freqtable[word] = 1

    return freqtable

def score_sentences(sentences,freqtable):
    sentvalue = {}
    for sentence in sentences:
        for word in freqtable:
            if word in sentence.lower():
                if sentence[0:10] in sentvalue:
                    sentvalue[sentence[0:10]] += freqtable[word]
                else:
                    sentvalue[sentence[0:10]] = freqtable[word]
        sentvalue[sentence[0:10]] = sentvalue[sentence[0:10]]//len(word_tokenize(sentence))

    return sentvalue

def get_threshold(sentvalue):
    s = 0
    for entry in sentvalue:
        s += sentvalue[entry]
    return int(s//len(sentvalue))

def summarize(sentences,sentvalue,threshold):
    summary = ''
    for sentence in sentences:
        if sentvalue[sentence[0:10]]>=threshold:
            summary += ' ' + sentence
    return summary


f = open('file.txt',encoding='utf8')
text = f.read().replace('\n',' ')
f.close()
sentences = sent_tokenize(text)
freqtable = create_freq_table(text)
sentvalue = score_sentences(sentences,freqtable)
threshold = get_threshold(sentvalue)
op = summarize(sentences,sentvalue,threshold)
print(op)