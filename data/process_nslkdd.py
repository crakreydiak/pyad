import pandas as pd
import numpy as np
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.process_ids2017 import parse_args, save_stats

TRAIN_FILENAME = 'KDDTrain+.txt'
TEST_FILENAME = 'KDDTest+.txt'

NORMAL_LABEL = 0
ANORMAL_LABEL = 1
NORMAL_CAT = "normal"


def df_stats(df: pd.DataFrame):
    num_cols = df.select_dtypes(include=[np.number]).columns
    cat_cols = df.select_dtypes(include=['category', 'object']).columns
    return {
        'in_features': df.shape[1],
        'n_instances': df.shape[0],
        'Numerical Columns': len(num_cols),
        'Categorical Columns': len(cat_cols)
    }


def import_data(base_path: str):
    base_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/kddcup99-mld"
    url_info = f"{base_url}/kddcup.names"
    df_info = pd.read_csv(url_info, sep=":", skiprows=1, index_col=False, names=["colname", "type"])
    colnames = df_info.colname.values
    coltypes = np.where(df_info["type"].str.contains("continuous"), "float", "str")
    colnames = np.append(colnames, ["label"])
    coltypes = np.append(coltypes, ["str"])
    df_train = pd.read_csv(
        os.path.join(base_path, TRAIN_FILENAME), names=colnames, index_col=False, dtype=dict(zip(colnames, coltypes))
    )
    df_test = pd.read_csv(
        os.path.join(base_path, TEST_FILENAME), names=colnames, index_col=False, dtype=dict(zip(colnames, coltypes))
    )
    # UBN added an extra `difficulty_level` columns which we ignore here
    return pd.concat([df_train, df_test], ignore_index=True, sort=False)


def uniq_step(df: pd.DataFrame):
    # Dropping columns with unique values
    cols_uniq_vals = df.columns[df.nunique() <= 1]
    print("Dropped {} columns: {} (unique values)".format(len(cols_uniq_vals), cols_uniq_vals))
    df = df.drop(cols_uniq_vals, axis=1)
    return df, cols_uniq_vals


def preprocess(df: pd.DataFrame, stats: dict):
    # Dropping columns with unique values
    df, dropped_cols = uniq_step(df)
    stats["uniq_cols"] = list(dropped_cols)

    # keep labels aside to avoid one-hot encoding them
    labels = df.label
    # One-hot encode the seven categorical attributes (except labels)
    # Assumes dtypes were previously assigned
    df = pd.get_dummies(df.iloc[:, :-1])
    df["label"] = labels
    # Keep the full labels aside before "binarizing" them
    df["Category"] = labels
    # Convert labels to binary labels
    df.loc[df["label"] == NORMAL_CAT, "label"] = 0
    df.loc[df["label"] != 0, "label"] = 1

    # We know the anomaly ration should be around 20%
    assert np.isclose(
        (df["label"] == ANORMAL_LABEL).sum() / len(df), .48,
        rtol=1.
    )

    assert df.isna().any(1).sum() == 0, "found nan values, aborting"

    return df, stats


def process_nslkdd(path: str, export_path: str):
    df = import_data(path)
    stats = df_stats(df)

    df, stats = preprocess(df, stats)

    stats['Normal Instances'] = (df['label'] == NORMAL_LABEL).sum()
    stats['Anormal Instances'] = (df['label'] == ANORMAL_LABEL).sum()
    stats['Anomaly Ratio'] = stats['Anormal Instances'] / len(df)
    stats['Final n_instances'] = len(df)
    stats['Final n_features'] = df.shape[1] - 2
    stats['NaN values'] = int(df.isna().any(1).sum())

    path = os.path.join(export_path, "nsl-kdd.csv")
    save_stats(
        os.path.join(export_path, "nslkdd_infos.csv"),
        stats
    )
    df.to_csv(path)


def main():
    args = parse_args()
    process_nslkdd(path=args.path, export_path=args.export_path)


if __name__ == '__main__':
    main()
