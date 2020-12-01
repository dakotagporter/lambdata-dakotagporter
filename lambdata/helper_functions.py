"""lambdata - helper functions for cleaning dataframes"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def null_count(df):
    """
    Returns total amount of null values in the DataFrame.
    """
    nulls = df.isnull().sum()

    return nulls


def train_test_split_func(df, frac):
    """
    Does a train-test-split using sklearn.
    """
    train, test = train_test_split(
                    df, train_size=frac, test_size=(1-frac), random_state=42)

    return train, test


class ColAvg(pd.DataFrame):
    """
    Returns average of each int columns in a given DataFrame.
    """
    def calculate(self):
        avgs = []

        for col in self.columns:
            if self[col].dtype == 'int64':
                avg = self[col].sum() / len(self[col])
                avgs.append(avg)
            else:
                avgs.append(None)

        return avgs


if __name__ == "__main__":
    pass
