import pandas as pd
from sklearn.model_selection import train_test_split

import columns
import paths

SEED = 42

def split_train_test(X, y, test_size=0.2, stratify=None):
    return train_test_split(
        X, y,
        test_size=test_size,
        random_state=SEED,
        stratify=stratify
    )

def downsample_data(df):
    df_pos = df[df[columns.fire_occurrence_column] == 1]
    df_neg = df[df[columns.fire_occurrence_column] == 0]
    df_neg_sample = df_neg.sample(n=len(df_pos), random_state=42)
    return pd.concat([df_pos, df_neg_sample])