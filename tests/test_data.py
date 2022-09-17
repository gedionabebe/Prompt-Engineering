import pandas as pd
import unittest
import sys,os
sys.path.append(os.path.abspath(os.path.join("./scripts")))
from data_fetch import get_news_data,get_job_data
from preprocessor import input_preprocessor

data = get_job_data(path='data/relations_dev.txt',repo='C:/Users/User/Desktop/Prompt-Engineering',version='relations_dev.txt_v1')
class TestPromptGeneration(unittest.TestCase):

    def setUp(self):
        self.pre = input_preprocessor(data)
        self.get_news = get_news_data(path='data/Example_data.xlsx',repo='C:/Users/User/Desktop/Prompt-Engineering',version='Example_data_v1')
        self.get_jobs = get_job_data(path='data/relations_dev.txt',repo='C:/Users/User/Desktop/Prompt-Engineering',version='relations_dev.txt_v1')

    def test_get_news(self):
        self.assertEqual(
           self.get_news.shape[0] , 10)

    def test_get_jobs(self):
        self.assertEqual(
            self.get_jobs.shape[0], 22)
    def test_preprocessor(self):
        self.assertEqual(len(self.pre),22)


if __name__ == "__main__":
    unittest.main()