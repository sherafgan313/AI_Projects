import numpy as np
import pandas as pd

def normalize_column(data, column_name):
    """
    Normalize a column in a DataFrame to the 0-1 range.
    Args:
        data (pd.DataFrame): The DataFrame containing the column.
        column_name (str): The name of the column to normalize.
    Returns:
        pd.DataFrame: DataFrame with a new column for normalized values.
    """
    col_values = data[column_name].values
    normalized = (col_values - col_values.min()) / (col_values.max() - col_values.min())
    data[f"{column_name}_normalized"] = normalized
    return data

def encode_categorical(data, column_name):
    """
    Encode a categorical column in a DataFrame into integers.
    Args:
        data (pd.DataFrame): The DataFrame containing the column.
        column_name (str): The name of the column to encode.
    Returns:
        pd.DataFrame: DataFrame with a new column for encoded values.
        dict: Mapping of categories to integers.
    """
    categories = data[column_name].unique()
    mapping = {cat: idx for idx, cat in enumerate(categories)}
    data[f"{column_name}_encoded"] = data[column_name].map(mapping)
    return data, mapping

def remove_duplicates(data, column_name):
    """
    Remove duplicate rows based on a specific column.
    Args:
        data (pd.DataFrame): The DataFrame to process.
        column_name (str): The column to check for duplicates.
    Returns:
        pd.DataFrame: DataFrame with duplicates removed.
    """
    return data.drop_duplicates(subset=[column_name])

def remove_duplicates2(data, exclude_column=None, subset=None):
    """
    Remove duplicate rows based on a subset of columns.
    Args:
        data (pd.DataFrame): The DataFrame to process.
        exclude_column (str, optional): Column to exclude from duplicate check (e.g., 'id').
        subset (list, optional): List of columns to check for duplicates. If None, use all columns except exclude_column.
    Returns:
        pd.DataFrame: DataFrame with duplicates removed.
    """
    if subset is None:
        # Use all columns except the exclude_column (if specified)
        columns_to_check = [col for col in data.columns if col != exclude_column]
    else:
        columns_to_check = subset
    return data.drop_duplicates(subset=columns_to_check)