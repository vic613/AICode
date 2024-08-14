import torch
import torch.nn as nn
import pandas as pd
import numpy as np
import re
import spacy
import jovian
from collections import Counter
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F
import string
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
from sklearn.metrics import mean_squared_error
import os

class CodeDataAccess:

    def LoadData():
     #loading the data
        filename = os.path.abspath(os.curdir)+"\\Modules\\ModulesData\\reviews.csv"
        reviews = pd.read_csv(filename)
        reviews['Title'] = reviews['Title'].fillna('')
        reviews['Review Text'] = reviews['Review Text'].fillna('')
        reviews['review'] = reviews['Title'] + ' ' + reviews['Review Text']
        
        reviews = reviews[['review', 'Rating']]
        reviews.columns = ['review', 'rating']
        reviews['review_length'] = reviews['review'].apply(lambda x: len(x.split()))
        reviews.head()

        #changing ratings to 0-numbering
        zero_numbering = {1:0, 2:1, 3:2, 4:3, 5:4}
        reviews['rating'] = reviews['rating'].apply(lambda x: zero_numbering[x])
        #mean sentence length
        np.mean(reviews['review_length'])
        return reviews
    
    def __init__(self, X, Y):
        self.X = X
        self.y = Y
        
    def __len__(self):
        return len(self.y)
    
    def __getitem__(self, idx):
        return torch.from_numpy(self.X[idx][0].astype(np.int32)), self.y[idx], self.X[idx][1]