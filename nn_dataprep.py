"""
Data preparation for PyTorch neural models

"""

import torch
from torch.utils.data import Dataset

class BikeshareDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.from_numpy(X).float()
        self.y = torch.from_numpy(y).float()
        self.dataset_size = len(self.y)
    
    def __len__(self):
        return self.dataset_size
        
    def __getitem__(self, idx):
        feature_vec = self.X[idx]
        label = self.y[idx]
        return feature_vec, label

"""
class BikeshareDataset(Dataset):
    def __init__(self, preprocessed_df, target_cols):
        self.X = torch.from_numpy(preprocessed_df.to_numpy()[:-1]).float()
        self.y = torch.from_numpy(preprocessed_df[target_cols].to_numpy()[1:]).float()
        self.dataset_size = len(self.y)
    
    def __len__(self):
        return self.dataset_size
        
    def __getitem__(self, idx):
        feature_vec = self.X[idx]
        label = self.y[idx]
        return feature_vec, label
"""