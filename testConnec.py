import unittest
import requests
import time
from statistics import mean
from bs4 import BeautifulSoup

class TestApp(unittest.TestCase):
    def testconnection(self):
        url = 'http://10.0.0.19:4000/'
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        text = "".join(soup.label.contents)
        self.assertEqual(text,"Type the speech")
    
    def testreports(self):
        nb_test = 2
        tab = []
        for i in range(nb_test):
            t_rstart = time.process_time()
            requests.get("http://10.0.0.19:4000/")
            t_rend = time.process_time()
            tab.append(t_rend - t_rstart)
        if mean(tab) <= 0.1:
            re = True
        else :
            re = False
        self.assertEqual(re,True)

if (__name__ == '__main__'):
    unittest.main()
