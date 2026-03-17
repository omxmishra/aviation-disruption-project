import pandas as pd

def load_master_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    df = df.copy()

    df["event_type"] = df["event_type"].fillna("No Event")
    df["severity"] = df["severity"].fillna("None")

    return df