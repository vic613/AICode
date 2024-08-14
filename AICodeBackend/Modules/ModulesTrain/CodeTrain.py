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
from Modules.ModulesDataAccess.CodeDataAccess import CodeDataAccess
from Modules.ModulesModelAccess.CodeModelAccess import CodeModelAccess
from sklearn.model_selection import train_test_split

class CodeTrain:
   
    def tokenize(text):
        tok = spacy.load('en_core_web_sm')
        text = re.sub(r"[^\x00-\x7F]+", " ", text)
        regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]') # remove punctuation and numbers
        nopunct = regex.sub(" ", text.lower())
        return [token.text for token in tok.tokenizer(nopunct)]
    
    def encode_sentence(text, vocab2index, N=70):
        tokenized = CodeTrain.tokenize(text)
        encoded = np.zeros(N, dtype=int)
        enc1 = np.array([vocab2index.get(word, vocab2index["UNK"]) for word in tokenized])
        length = min(N, len(enc1))
        encoded[:length] = enc1[:length]
        return encoded, length


    def train_model(model, epochs=10, lr=0.001):
        batch_size = 5000
        reviews = CodeDataAccess.LoadData();
        counts = Counter()
        for index, row in reviews.iterrows():
            counts.update(CodeTrain.tokenize(row['review']))
        print("num_words before:",len(counts.keys()))
        for word in list(counts):
            if counts[word] < 2:
                del counts[word]
        # print("num_words after:",len(counts.keys()))
        vocab2index = {"":0, "UNK":1}
        words = ["", "UNK"]
        for word in counts:
            vocab2index[word] = len(words)
            words.append(word)
        reviews['encoded'] = reviews['review'].apply(lambda x: np.array(CodeTrain.encode_sentence(x,vocab2index )))
        X = list(reviews['encoded'])
        y = list(reviews['rating'])
        X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2)
        train_ds = CodeDataAccess(X_train, y_train)
        valid_ds = CodeDataAccess(X_valid, y_valid)
        train_dl = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
        val_dl = DataLoader(valid_ds, batch_size=batch_size)
        parameters = filter(lambda p: p.requires_grad, model.parameters())
        optimizer = torch.optim.Adam(parameters, lr=lr)
        for i in range(epochs):
            model.train()
            sum_loss = 0.0
            total = 0
            for x, y, l in train_dl:
                x = x.long()
                y = y.long()
                y_pred = model(x, l)
                optimizer.zero_grad()
                loss = F.cross_entropy(y_pred, y)
                loss.backward()
                optimizer.step()
                sum_loss += loss.item()*y.shape[0]
                total += y.shape[0]
            val_loss, val_acc, val_rmse = CodeTrain.validation_metrics(model, val_dl)
            if i % 5 == 1:
                print("train loss %.3f, val loss %.3f, val accuracy %.3f, and val rmse %.3f" % (sum_loss/total, val_loss, val_acc, val_rmse))

        checkpoint = {
            'epoch': epochs + 1,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict()
            }
        checkpoint_dir = os.path.abspath(os.curdir)+"\\Modules\\ModulesModel"
        model_dir = os.path.abspath(os.curdir)+"\\Modules\\ModulesModel"
        is_best = 1
        CodeModelAccess.save_ckp(checkpoint, is_best, checkpoint_dir, model_dir)
       

    def validation_metrics (model, valid_dl):
        model.eval()
        correct = 0
        total = 0
        sum_loss = 0.0
        sum_rmse = 0.0
        for x, y, l in valid_dl:
            x = x.long()
            y = y.long()
            y_hat = model(x, l)
            loss = F.cross_entropy(y_hat, y)
            pred = torch.max(y_hat, 1)[1]
            correct += (pred == y).float().sum()
            total += y.shape[0]
            sum_loss += loss.item()*y.shape[0]
            sum_rmse += np.sqrt(mean_squared_error(pred, y.unsqueeze(-1)))*y.shape[0]
        return sum_loss/total, correct/total, sum_rmse/total
            
    # def load_model():
    #     model = Net()
    #     optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

    #     checkpoint = torch.load(PATH)
    #     model.load_state_dict(checkpoint['model_state_dict'])
    #     optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    #     epoch = checkpoint['epoch']
    #     loss = checkpoint['loss']

    #     model.eval()
    #     # - or -
    #     model.train()

  