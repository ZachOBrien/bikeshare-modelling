"""
Utilities for preprocessing the data

"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def preprocess_bikeshare_data(df, categorical_cols, label_col):
    """Preprocess the Bikeshare Ridership Data
    
    One-hot encodes categorical columns, and applies MinMaxScaler to the
    label column "cnt" because it will be a feature as well as a label
    in the time series models.
    
    Args:
        df (pd.DataFrame):
            Data
        categorical_cols (list[str]):
            Names of columns to one-hot encode
        label_col (str):
            Name of the label column (column with label)
    
    Returns:
        pd.DataFrame, MinMaxScaler:
            Data with categorical values one-hot encoded and labels scaled,
            and the scaler fit to the original label range
    """
    new_df = one_hot_encode(df, column_names=categorical_cols)
    new_df, scaler = min_max_scale(new_df, col=label_col)
    return new_df, scaler


def min_max_scale(df, col):
    """Apply MinMax scaling to one column in a DataFrame
    
    Args:
        df (pd.DataFrame):
            Data with a column of real values named `col`
        col (str):
            Name of the column to scale
    
    Returns:
        (pd.Dataframe, MinMaxScaler):
            The Data with `col` scaled, as well as the fit MinMaxScaler so that
            data can be inverse transformed back into the original scale
    """
    scaler = MinMaxScaler()
    df_copy = df.copy()
    label_data = df_copy[col].to_numpy().reshape(-1, 1)
    scaler.fit(label_data)
    df_copy[col] = scaler.transform(label_data)
    return df_copy, scaler
    
    
def one_hot_encode(df, column_names):
    """One-hot encode columns in a DataFrame

    Args:
        df (pd.DataFrame): 
            Data
        column_names (list[str]): 
            Names of columns which should be converted to one-hot encoding

    Returns:
        pd.DataFrame:
            Data with the specified columns converted to one-hot encoding
    """
    df_copy = df.copy()
    dummies = [pd.get_dummies(df_copy[col], prefix=col) for col in column_names]
    df_copy.drop(column_names, axis=1, inplace=True)
    return pd.concat(dummies + [df_copy], axis=1)