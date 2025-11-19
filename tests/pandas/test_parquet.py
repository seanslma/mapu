from mapu.pandas.parquet import pa_mod

if __name__ == '__main__':
    import pandas as pd

    d = pd.DataFrame({'x': [-2, -8, 3]}, dtype='int64[pyarrow]')
    print(pa_mod(d.iat[1, 0], 3))
