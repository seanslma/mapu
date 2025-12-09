import string
import numpy as np
import pandas as pd
from collections.abc import Iterable


def gen_rand_strs(
    rng: np.random.Generator,
    str_cnt: int,
    str_len: tuple[int, int],
    str_chars: list[str],
) -> list[str]:
    str_lens = rng.integers(
        low=str_len[0], high=str_len[1], size=str_cnt, endpoint=True
    )
    rand_strs = [''.join(rng.choice(str_chars, size=str_len)) for str_len in str_lens]
    return rand_strs


def gen_str_vals(
    size: int,
    rng: np.random.Generator,
    str_cnt: int = None,
    str_len: int | tuple[int, int] = None,
    str_chars: list[str] = None,
    col_strs: list[str] = None,
) -> np.ndarray:
    if str_cnt is None:
        str_cnt = 10
    if str_len is None:
        str_len = (5, 5)
    elif isinstance(str_len, int):
        str_len = (str_len, str_len)
    if col_strs is None:
        if str_chars is None:
            str_chars = [c for c in string.ascii_letters + string.digits]
        col_strs = gen_rand_strs(rng, str_cnt, str_len, str_chars)
    val = rng.choice(col_strs, size=size)
    return val


def gen_ts_vals(
    size: int,
    rng: np.random.Generator,
    start_date: str = None,
    end_date: str = None,
    freq: str = None,
    random: bool = False,
) -> np.ndarray:
    if start_date is None:
        start_date = '2024-01-01'
    if end_date is None:
        end_date = '2025-01-01'
    if freq is None:
        freq = 'D'
    if random is None:
        random = False
    val = pd.date_range(start_date, end_date, freq=freq, inclusive='left')[:size]
    if random:
        val = rng.choice(val, size=size)
    return val


def gen_num_vals(
    size: int,
    rng: np.random.Generator,
    low: int | float = None,
    high: int | float = None,
    dtype: str = None,
) -> np.ndarray:
    if low is None:
        low = 0
    if high is None:
        high = 2
    func = rng.integers if dtype[0] == 'i' else rng.uniform
    vals = func(low=low, high=high, size=size)
    return vals


def gen_missing_vals(
    vals: np.ndarray,
    rng: np.random._generator.Generator,
    dtype: str,
    missing_pct: float = None,
) -> np.ndarray:
    if missing_pct is None or missing_pct <= 0 or missing_pct >= 1:
        return vals
    if dtype == 's':
        missing_val = None
    elif dtype == 't':
        missing_val = np.datetime64('NaT')
    else:
        missing_val = np.nan
    if dtype == 'i':
        vals = vals.astype(np.float64)
    mask = rng.uniform(size=len(vals)) <= missing_pct
    vals[mask] = missing_val
    return vals


def sanitize_parameters(
    name_prefix: str,
    params: dict,
    par_names: list[str],
):
    if isinstance(params, int):
        cnt = params
        par = {}
    else:
        cnt = params['count']
        par = {
            k: (
                list(v) + [None] * (cnt - len(v))
                if isinstance(v, Iterable)
                else [v] * cnt
            )
            for k, v in params.items()
        }
    if name_prefix in ('i', 'f'):
        par_names += ['dtype']
        par['dtype'] = [name_prefix] * cnt
    default_val = [None] * cnt
    parameters = [
        {key: par.get(key, default_val)[i] for key in par_names} for i in range(cnt)
    ]
    col_names = par.get('name')
    if col_names is None or col_names.count(None) > 1 or col_names.count('') > 1:
        col_names = [f'{name_prefix}{i}' for i in range(1, cnt + 1)]
    col_missing_pcts = par.get('missing_pct', default_val)
    return col_names, parameters, col_missing_pcts


def gen_rand_df(
    nrow: int,
    str_cols: dict = None,
    ts_cols: dict = None,
    int_cols: dict = None,
    float_cols: dict = None,
    rand_seed: int = 11,
) -> pd.DataFrame:
    col_types = ['s', 't', 'i', 'f']
    inputs = [str_cols, ts_cols, int_cols, float_cols]
    funcs = [gen_str_vals, gen_ts_vals, gen_num_vals, gen_num_vals]
    par_names = [
        ['str_cnt', 'str_len', 'str_chars', 'col_strs'],
        ['start_date', 'end_date', 'freq', 'random'],
        ['low', 'high'],
        ['low', 'high'],
    ]
    df = pd.DataFrame()
    rng = np.random.default_rng(seed=rand_seed)
    for i, params in enumerate(inputs):
        if params is not None:
            col_names, col_params, col_missing_pcts = sanitize_parameters(
                col_types[i], params, par_names[i]
            )
            df = pd.concat(
                [
                    df,
                    pd.DataFrame(
                        {
                            col: gen_missing_vals(
                                funcs[i](nrow, rng, **col_params[j]),
                                rng,
                                col_types[i],
                                col_missing_pcts[j],
                            )
                            for j, col in enumerate(col_names)
                        }
                    ),
                ],
                axis=1,
            )
    return df


if __name__ == '__main__':
    # example 1
    df = gen_rand_df(
        nrow=365 * 24 * 60,
        str_cols=1,
        ts_cols=2,
        int_cols=1,
        float_cols=2,
    )
    print(df[:2])

    # example 2
    d2 = gen_rand_df(
        nrow=10,
        str_cols={
            'count': 2,
            'name': ['country', 'color'],
            'str_len': [3, (3, 9)],
            'str_cnt': [2, 5],
            'col_strs': [['UK', 'US', 'AU'], ['blue', 'black', 'red']],
        },
        ts_cols={
            'count': 2,
            'name': ['start_date', 'end_date'],
            'start_date': ['2020-01-01', '2024-01-01'],
            'end_date': ['2021-01-01', '2025-01-01'],
            'freq': 'QS',
            'random': False,
        },
        int_cols={
            'count': 1,
            'name': ['quantity'],
            'low': [0],
            'high': [100],
            'missing_pct': [0.3],
        },
        float_cols={
            'count': 2,
            'name': ['price', 'charge'],
            'low': [1, 0.1],
            'high': [100, 0.9],
            'missing_pct': [0.3, 0.2],
        },
    )
    print(d2[:3])
