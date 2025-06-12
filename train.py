#!/usr/bin/env python3
import numpy as np
from torch.utils.data import Dataset

class ChessValueDataset(Dataset):
    def __init__(self):
        dat=np.loadz("processed/dataset_1k.npz")
        self.X=dat['X']
        self.Y=dat['Y']

    def __len__(self):
        return self.X.shape[0]

    def __getitem__(self,idx):
        return {'X':self.X.shape[idx],'Y': self.Y.shape[idx]}
    
chess_dataset
