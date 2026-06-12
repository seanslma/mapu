import pandas as pd


def pd_ht(self, n=2, c=None, r=None):
    if n < 0 or self.shape[0] <= 2 * n:
        df = self
    else:
        df = pd.concat([self[:n], self[-n:]])
    with pd.option_context(
        'display.show_dimensions',
        False,
        'display.max_rows',
        None if (n is None or n < 0) else 2 * n,
        'display.max_columns',
        None if (c is None or c < 0) else c,
    ):
        print(f'shape: {self.shape}')
        print(df)


def remove_cols_utc(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts datetime columns in UTC to timezone-naive (tz=None)
    """
    for col in df.select_dtypes(include=['datetimetz']).columns:
        tz = df[col].dt.tz
        if tz is not None and 'utc' in str(tz).lower():
            df[col] = df[col].dt.tz_localize(None)
    return df


def df_diffs(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Get rows in two dfs that are different to each other.
    Comparison is based on df MultiIndex
    """
    # Perform an outer join
    df_joined = pd.merge(
        df1,
        df2,
        how='outer',
        left_index=True,
        right_index=True,
        suffixes=('_df1', '_df2'),
    )

    # Compare the columns to find differences
    d1_joined = df_joined.filter(like='_df1').rename(
        columns=lambda x: x.rsplit('_', 1)[0]
    )
    d2_joined = df_joined.filter(like='_df2').rename(
        columns=lambda x: x.rsplit('_', 1)[0]
    )

    # Compare two dfs with `ne`, col names must be the same
    diffs = df_joined[d1_joined.ne(d2_joined).any(axis=1)]

    return diffs


if __name__ == '__main__':
    # Create two example DataFrames with string columns
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

    df = df_diffs(df1, df2)

    # Show the resulting differences
    print(df)
