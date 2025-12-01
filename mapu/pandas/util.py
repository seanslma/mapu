import pandas as pd


def df_diffs(df1, df2):
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
    d1_joined = (
        df_joined
        .filter(like='_df1')
        .rename(columns=lambda x: x.rsplit('_', 1)[0])
    )
    d2_joined = (
        df_joined
        .filter(like='_df2')
        .rename(columns=lambda x: x.rsplit('_', 1)[0])
    )

    # Compare two dfs with `ne`, col names must be the same
    diffs = df_joined[d1_joined.ne(d2_joined).any(axis=1)]

    return diffs

if __name__ == '__main__':
  # Create two example DataFrames with string columns
  df1 = pd.DataFrame({
      'fruit': ['apple', 'banana'],
      'id': [1, 2],
      'price': [4, 3.1],
      'store': ['us', 'uk'],
  }).set_index(['fruit', 'id'])
  
  df2 = pd.DataFrame({
      'fruit': ['apple', 'banana'],
      'id': [1, 3],
      'price': [4, 3.2],
      'store': ['us', 'uk'],
  }).set_index(['fruit', 'id'])
  
  df = pandas_diffs(df1, df2)
  
  # Show the resulting differences
  print(df)
