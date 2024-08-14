import shutil
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

class CodeModelAccess:

    def save_ckp(state, is_best, checkpoint_dir, best_model_dir):
        f_path = checkpoint_dir / 'checkpoint.pt'
        torch.save(state, f_path)
        if is_best:
            best_fpath = best_model_dir / 'best_model.pt'
            shutil.copyfile(f_path, best_fpath)