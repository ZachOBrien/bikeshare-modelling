"""
Utilities for preprocessing the data

"""

import pandas as pd


def one_hot_encode_columns(df, column_names):
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
    return pd.concat([df_copy] + dummies, axis=1)
