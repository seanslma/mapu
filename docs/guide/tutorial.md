# Quick Tutorial: Using explode_date_range

This tutorial shows you how to use the `mapu.pandas.explode_date_range` function.

## 1. Setup

First, ensure you have the `mapu` package installed:
```sh
pip install mapu
```

## 2. Basic Usage

The `gen_rand_df` can be used to create random data in a pandas DataFrame for testing.
```py
from mapu.pandas import gen_rand_df

# Example 1: create a dataframe with one string column, two timestamp columns, one integer column, and two float columns, for one year with a resolution of one minute.
df = gen_rand_df(
    nrow=365 * 24 * 60,
    str_cols=1,
    ts_cols={
        'count': 2,
        'name': ['start_date', 'end_date'],
        'start_date': ['2020-01-01', '2023-01-01'],
        'end_date': ['2023-01-01', '2025-01-01'],
        'freq': 'MS',
        'random': True,
    },
    int_cols=1,
    float_cols=2,
)
print(df[:2])
# Output: xxx
```

## 3. Using the `explode_date_range` function

This function can be used to explode two datetime columns in a pandas DataFrame to a list of datetime values as a new column. It's about `30x` faster than using the pandas `df.explode` function.
```py
from mapu.pandas import explode_date_range

# assume we already created the df in the previous section
df_exploded = explode_date_range(
    df=df,
    start_date_col='start_date',
    end_date_col='end_date',
    date_col='ts',
    freq='30min',
    inclusive='left',
    drop_date_cols=True,
)

print(df_exploded[:2])
# Output: xxx
```
