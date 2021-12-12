import unittest
import requests
import time
from SentimentAnalyser import SentimentAnalyserText

class TestApp(unittest.TestCase):
    
    def testmodel(self):
        prog = SentimentAnalyserText
        texts = ["I am a potato","I am the best","You are the worst","The rain is made of water.","That chicken is clever, like you.","I hate you with all my heart, go die in a ditch.","That camel think, so he is.","What glorious weather we have today.","The baker is a stupid ugly man, I hope the gestapo will get him.","I hope you get yourself a great family, who you love with all your heart, so that one day you lose everything but live a long life after that. "]
        labels =["neutral","positif","negatif","neutral","positif","negatif","neutral","positif","negatif","negatif"]
        count = 0
        
        for i in range (9):
            if (prog(texts[i])==labels[i]):
                count +=1
        print(count)
        if (count >= 8):
            re= True
        else:
            re = False
        self.assertEqual(re,True)
        



if (__name__ == '__main__'):
    unittest.main()