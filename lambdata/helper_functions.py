"""lambdata - helper functions for cleaning dataframes"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def null_count(df):

    nulls = df.isnull().sum()

    return nulls

def train_test_split_func(df, frac):

    train, test = train_test_split(df, train_size=frac, random_state=42)

    return train, test
