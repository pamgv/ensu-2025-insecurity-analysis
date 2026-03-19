import pandas as pd
from .preprocess import PERCEPTION_COLUMNS, INCIVILITY_COLUMNS, TRUST_COLUMNS

def categorize_insecurity(score: float) -> str:
    """
    Categorize perceived insecurity score into three interpretable levels.

    Scale assumptions:
    - Lower values indicate lower perceived insecurity
    - Higher values indicate higher perceived insecurity
    """
    if pd.isna(score):
        return "Unknown"
    if score < 1.50:
        return "Low"
    if score < 1.75:
        return "Medium"
    return "High"


def build_insecurity_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create insecurity score and insecurity level.
    """
    df = df.copy()
    df["insecurity_score"] = df[PERCEPTION_COLUMNS].mean(axis=1)
    df["insecurity_level"] = df["insecurity_score"].apply(categorize_insecurity)
    return df


def build_incivility_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create incivility score from BP1_4_* columns.
    Assumes higher values indicate more reported incivility.
    """
    df = df.copy()
    df["incivility_score"] = df[INCIVILITY_COLUMNS].mean(axis=1)
    return df


def build_trust_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create trust score from BP1_8_* columns.
    Keep in mind these variables contain many missing values.
    """
    df = df.copy()
    df["trust_score"] = df[TRUST_COLUMNS].mean(axis=1)
    return df


def build_all_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full feature engineering pipeline.
    """
    df = build_insecurity_features(df)
    df = build_incivility_score(df)
    df = build_trust_score(df)
    return df