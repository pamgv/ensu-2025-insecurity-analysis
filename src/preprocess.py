import pandas as pd


SELECTED_COLUMNS = [
    "NOM_ENT", "NOM_MUN", "NOM_CD", "SEXO", "EDAD", "quarter",
    "BP1_1",
    "BP1_2_01", "BP1_2_02", "BP1_2_03", "BP1_2_04", "BP1_2_05",
    "BP1_2_06", "BP1_2_07", "BP1_2_08", "BP1_2_09", "BP1_2_10",
    "BP1_2_11", "BP1_2_12",
    "BP1_4_1", "BP1_4_2", "BP1_4_3", "BP1_4_4", "BP1_4_5", "BP1_4_6", "BP1_4_7",
    "BP1_8_1", "BP1_8_2", "BP1_8_3", "BP1_8_4", "BP1_8_5",
]

PERCEPTION_COLUMNS = [
    "BP1_1",
    "BP1_2_01", "BP1_2_02", "BP1_2_03", "BP1_2_04", "BP1_2_05",
    "BP1_2_06", "BP1_2_07", "BP1_2_08", "BP1_2_09", "BP1_2_10",
    "BP1_2_11", "BP1_2_12",
]

INCIVILITY_COLUMNS = [
    "BP1_4_1", "BP1_4_2", "BP1_4_3", "BP1_4_4", "BP1_4_5", "BP1_4_6", "BP1_4_7",
]

TRUST_COLUMNS = [
    "BP1_8_1", "BP1_8_2", "BP1_8_3", "BP1_8_4", "BP1_8_5",
]


def validate_selected_columns(df: pd.DataFrame, selected_cols: list) -> None:
    missing = [col for col in selected_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def select_analysis_columns(df: pd.DataFrame, selected_cols: list = None) -> pd.DataFrame:
    selected_cols = selected_cols or SELECTED_COLUMNS
    validate_selected_columns(df, selected_cols)
    return df[selected_cols].copy()


def replace_special_codes(df: pd.DataFrame, columns: list, codes=(9, 99)) -> pd.DataFrame:
    df = df.copy()
    replace_map = {code: pd.NA for code in codes}
    df[columns] = df[columns].replace(replace_map)
    return df


def convert_to_numeric(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    df = df.copy()
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def clean_analysis_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = select_analysis_columns(df)

    numeric_cols = PERCEPTION_COLUMNS + INCIVILITY_COLUMNS + TRUST_COLUMNS + ["SEXO", "EDAD"]
    df = convert_to_numeric(df, numeric_cols)

    # percepción: 3 = No aplica, 9/99 = missing
    df = replace_special_codes(df, PERCEPTION_COLUMNS, codes=(3, 9, 97, 98, 99))

    # otros bloques
    df = replace_special_codes(df, INCIVILITY_COLUMNS, codes=(9, 97, 98, 99))
    df = replace_special_codes(df, TRUST_COLUMNS, codes=(9, 97, 98, 99))

    return df