import polars as pl
import polars.selectors as cs


def pl_ht(self, n=2):
    if self.shape[0] < 2 * n:
        df = self
    else:
        df = pl.concat([self[:n], self[-n:]])
    with pl.Config(tbl_hide_dataframe_shape=True):
        print(f'shape: {self.shape}')
        print(df)


def pl_print(self, n=0, d=2):
    df = self if n == 0 else self[:n]
    df = df.with_columns((cs.float() | cs.decimal()).round(d))
    with pl.Config(tbl_hide_dataframe_shape=True):
        print(f'shape: {self.shape}')
        print(df)


def parquet_to_csv(filepath: str):
    """
    Read parquet and save as csv
    """
    filepath_csv = f'{filepath[:-7]}csv'
    pl.read_parquet(filepath).write_csv(filepath_csv)


def lowercase_polars_df(df: pl.DataFrame) -> pl.DataFrame:
    """
    Converts all column headers and string columns in a Polars DataFrame to lowercase
    """
    # Lowercase column headers
    df = df.rename({col: col.lower() for col in df.columns})
    # Lowercase string columns
    df = df.with_columns([
        cs.string().str.to_lowercase()
    ])
    return df


def to_float32_polars_df(df: pl.DataFrame) -> pl.DataFrame:
    """
    Convert all numerical columns type to float32
    """
    df = df.with_columns(
        (cs.float() | cs.decimal()).cast(pl.Float32)
    )
    return df


def inf_count(df: pl.DataFrame) -> pl.DataFrame:
    df_inf = (
        df.select([
            (pl.col(col).is_infinite().sum().alias(col))
            for col in df.columns
        ])
        .unpivot(variable_name='col', value_name='inf_cnt')
        .filter(pl.col('inf_cnt') > 0)
        .sort('inf_cnt', descending=True)
    )
    return df_inf


def nan_count(df: pl.DataFrame) -> pl.DataFrame:
    df_nan = (
        df.select([
            (pl.col(col).is_nan().sum().alias(col))
            for col in df.columns
        ])
        .unpivot(variable_name='col', value_name='nan_cnt')
        .filter(pl.col('nan_cnt') > 0)
        .sort('nan_cnt', descending=True)
    )
    return df_nan


def nul_count(df: pl.DataFrame) -> pl.DataFrame:
    df_nul = (
        df.select([
            (pl.col(col).is_null().sum().alias(col))
            for col in df.columns
        ])
        .unpivot(variable_name='col', value_name='nul_cnt')
        .filter(pl.col('nul_cnt') > 0)
        .sort('nul_cnt', descending=True)
    )
    return df_nul
