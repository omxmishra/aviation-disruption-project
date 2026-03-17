import pandas as pd

def create_target(df):
    df = df.copy()

    df["target"] = df["disruption_category"].map({
        "Cancelled": 1,
        "Rerouted": 0
    })

    return df


def select_features(df):
    return df[[
        "airline",
        "origin",
        "destination",
        "severity",
        "severity_level",
        "disruption_type",
        "flights_affected",
        "disruption_category",
        "target"
    ]]