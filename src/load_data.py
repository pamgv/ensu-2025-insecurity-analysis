from pathlib import Path
import zipfile
import pandas as pd


def find_main_csv(zip_obj: zipfile.ZipFile) -> str:
    
    csv_files = [name for name in zip_obj.namelist() if name.lower().endswith(".csv")]

    preferred = [
        name for name in csv_files
        if "conjunto_de_datos_ensu_cb" in name.lower()
        and "conjunto_de_datos/" in name.lower()
    ]

    if not preferred:
        raise ValueError("Main ENSU CB CSV not found inside ZIP.")

    return preferred[0]


def load_ensu_zip(zip_path: Path, quarter_label: str) -> pd.DataFrame:
    
    with zipfile.ZipFile(zip_path, "r") as z:
        csv_name = find_main_csv(z)
        with z.open(csv_name) as f:
            df = pd.read_csv(f, encoding="utf-8", low_memory=False)

    df["quarter"] = quarter_label
    return df


def load_all_quarters(raw_dir: Path, file_map: dict) -> dict:
    
    dfs = {}
    for quarter, filename in file_map.items():
        zip_path = raw_dir / filename
        dfs[quarter] = load_ensu_zip(zip_path, quarter)
    return dfs


def concat_quarters(dfs: dict) -> pd.DataFrame:
    
    return pd.concat(dfs.values(), ignore_index=True)


def get_common_columns(dfs: dict) -> list:
    
    common_cols = set.intersection(*(set(df.columns) for df in dfs.values()))
    return sorted(common_cols)
