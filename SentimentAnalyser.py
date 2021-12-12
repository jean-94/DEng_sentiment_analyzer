import numpy as np
import nltk
from statistics import mean
from nltk.sentiment import SentimentIntensityAnalyzer

def lst2str(lst):
    string =""
    for word in lst:
        string += " " + word.lower()
    return string


def SentimentAnalyserSentences(text, sia, unwanted):
    tab_sent_ntk = []
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        sentence = [word for word in words if word.lower() not in unwanted]
        tab_sent_ntk.append(sia.polarity_scores(lst2str(sentence)))
    return tab_sent_ntk

def NNP(sent):
    if sent["neg"] > sent["neu"]:
        if sent["neg"] > sent["pos"]:
            return 0
        else:
            return 2
    else:
        if sent["neu"] > sent["pos"]:
            return 1
        else:
            return 2

def NNP_text(tab):
    tab_re = []
    for sent in tab:
        tab_re.append(NNP(sent))
    return np.round(mean(tab_re))

def SentimentAnalyserText(text):
    nltk.download(["stopwords","averaged_perceptron_tagger","vader_lexicon","punkt",])

    unwanted = nltk.corpus.stopwords.words("english")
    sia = SentimentIntensityAnalyzer()

    sent_text = [word for word in nltk.word_tokenize(text) if word.lower() not in unwanted]
    sent_wtext = NNP(sia.polarity_scores(lst2str(sent_text)))

    sent_stext = NNP_text(SentimentAnalyserSentences(text, sia, unwanted))

    resultat = np.round((sent_stext * 0.5) + (sent_wtext * 0.5))

    if resultat == 0:
        return "negatif"
    if resultat == 1:
        return "neutral"
    if resultat == 2:
        return "positif"

if (__name__ == "__main__"):
    print(
        SentimentAnalyserText("You're terrible."),
        SentimentAnalyserText("You're a potato."),
        SentimentAnalyserText("You're great.")
        )