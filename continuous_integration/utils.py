import pandas as pd
import numpy as np

def label_diff(y_train, y_test, verbose=False):
    train = y_train.value_counts() / len(y_train)
    test = y_test.value_counts() / len(y_test)
    if verbose:
        print("Categories in the training set:")
        print(train)
        print("Categories in the test set:")
        print(test)
    return np.absolute(train-test)

def sample_and_complement(df, sample_frac=0.33, random_state=None):
    """
    Random dataframe split.
    
    Parameters
    ----------
    
    df : provide a pandas DataFrame as input
    
    sample_frac : fraction of the sample
    
    random_state : int or RandomState instance, default=None
        Controls the shuffling applied to the data before applying the split.
    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame([['female',54,1],['male',45,0],['male',32,1],['female',24,1],['female',40,0],['female',39,1]], columns=['gender','age','label'])
    >>> part1, part2 = sample_and_complement(df, sample_frac=0.33, random_state=42)
    >>> print(part1)
       gender  age  label
    2    male   32      1
    3  female   24      1
    4  female   40      0
    5  female   39      1
    >>> print(part2)
       gender  age  label
    0  female   54      1
    1    male   45      0
    """
    test_part = df.sample(frac=sample_frac, random_state=random_state)
    train_part = df[~df.index.isin(test_part.index)]
    return train_part, test_part

def process_parts(parts, label_col, shuffle=True, random_state=None):
    df = pd.concat(parts)
    if shuffle:
        df = df.sample(frac=1.0, random_state=random_state)
    return df.drop(label_col, axis=1).copy(), df[label_col]

def train_test_split_wrt_col(X, y, test_size=0.33, col=None, shuffle=True, random_state=None, label_col="LABEL"):
    df = X.copy()
    df[label_col] = y
    if col == None:
        col = label_col
    categories = list(df[col].unique())
    train_parts, test_parts = [], []
    for val in categories:
        train_part, test_part = sample_and_complement(df[df[col]==val], test_size, random_state)
        train_parts.append(train_part)
        test_parts.append(test_part)
    X_train, y_train = process_parts(train_parts, label_col, shuffle, random_state)
    X_test, y_test = process_parts(test_parts, label_col, shuffle, random_state)
    return X_train, X_test, y_train, y_test