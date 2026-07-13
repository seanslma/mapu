import numpy as np
import pandas as pd
from mspu.pandas import df_diffs


def test_df_diffs_basic():
    df1 = pd.DataFrame(
        {
            'fruit': ['apple', 'banana', 'apple'],
            'id': [1, 2, 4],
            'store': ['us', 'uk', 'cn'],
            'price': [4, 3.1, 2.5],
        }
    ).set_index(['fruit', 'id'])

    df2 = pd.DataFrame(
        {
            'fruit': ['apple', 'banana', 'apple'],
            'id': [1, 3, 4],
            'store': ['us', 'uk', 'cn'],
            'price': [4, 3.2, 2.5],
        }
    ).set_index(['fruit', 'id'])

    result = df_diffs(df1, df2)

    # Expected output with suffixes for each dataframe
    expected = pd.DataFrame(
        {
            'store_df1': ['uk', np.nan],
            'price_df1': [3.1, np.nan],
            'store_df2': [np.nan, 'uk'],
            'price_df2': [np.nan, 3.2],
        },
        index=pd.MultiIndex.from_tuples(
            [('banana', 2), ('banana', 3)], names=['fruit', 'id']
        ),
    )

    pd.testing.assert_frame_equal(result, expected)


def test_df_diffs_identical():
    """Test df_diffs with identical dataframes"""
    df1 = pd.DataFrame(
        {
            'fruit': ['apple', 'banana'],
            'id': [1, 2],
            'price': [4, 3.1],
        }
    ).set_index(['fruit', 'id'])

    df2 = df1.copy()

    result = df_diffs(df1, df2)

    # Should return empty dataframe when dfs are identical
    assert result.empty


def test_df_diffs_different_indices():
    """Test df_diffs with different indices"""
    df1 = pd.DataFrame(
        {
            'fruit': ['apple', 'banana'],
            'id': [1, 2],
            'price': [4, 3.1],
        }
    ).set_index(['fruit', 'id'])

    df2 = pd.DataFrame(
        {
            'fruit': ['orange', 'grape'],
            'id': [5, 6],
            'price': [2, 1.5],
        }
    ).set_index(['fruit', 'id'])

    result = df_diffs(df1, df2)

    # Should return rows with all differences
    assert len(result) > 0
