import pandas as pd
from typing import Callable, Dict, Any


def apply_standard_filters(df: pd.DataFrame, filters: Dict[str, Any]) -> pd.DataFrame:
    """Apply simple equality or range filters."""
    for column, condition in filters.items():
        if isinstance(condition, tuple) and len(condition) == 2:
            low, high = condition
            df = df[(df[column] >= low) & (df[column] <= high)]
        else:
            df = df[df[column] == condition]
    return df


def apply_custom_filter(df: pd.DataFrame, func: Callable[[pd.DataFrame], pd.DataFrame]) -> pd.DataFrame:
    """Apply a user-defined filter function."""
    try:
        return func(df)
    except Exception as exc:
        raise ValueError(f"Error in custom filter: {exc}")
