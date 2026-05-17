import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from mapu.pandas import explode_date_range


def test_basic():
    df = pd.DataFrame(
        {
            'start_date': ['2023-01-01', '2023-01-02'],
            'end_date': ['2023-01-01 01:00:00', '2023-01-02 02:00:00'],
        }
    )
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['end_date'] = pd.to_datetime(df['end_date'])

    result = explode_date_range(df, 'start_date', 'end_date', freq='1h')
    expected = pd.DataFrame(
        {
            'ts': pd.to_datetime(
                [
                    '2023-01-01 00:00:00',
                    '2023-01-01 01:00:00',
                    '2023-01-02 00:00:00',
                    '2023-01-02 01:00:00',
                    '2023-01-02 02:00:00',
                ]
            )
        }
    )

    assert_frame_equal(result[['ts']], expected)


def test_with_offsets():
    df = pd.DataFrame(
        {
            'start_date': ['2023-01-01', '2023-01-02'],
            'end_date': ['2023-01-01 01:00:00', '2023-01-02 02:00:00'],
        }
    )
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['end_date'] = pd.to_datetime(df['end_date'])

    result = explode_date_range(
        df,
        'start_date',
        'end_date',
        freq='1h',
        start_date_offset=pd.DateOffset(hours=1),
        end_date_offset=pd.DateOffset(hours=-1),
    )
    expected = pd.DataFrame({'ts': pd.to_datetime(['2023-01-02 01:00:00'])})

    assert_frame_equal(result[['ts']], expected)


def test_with_roll():
    df = pd.DataFrame(
        {
            'start_date': ['2023-01-01 00:30:00', '2023-01-02 00:30:00'],
            'end_date': ['2023-01-01 01:30:00', '2023-01-02 02:30:00'],
        }
    )
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['end_date'] = pd.to_datetime(df['end_date'])

    result = explode_date_range(
        df,
        'start_date',
        'end_date',
        freq='1h',
        start_date_roll='forward',
        end_date_roll='back',
    )
    expected = pd.DataFrame(
        {
            'ts': pd.to_datetime(
                ['2023-01-01 01:00:00', '2023-01-02 01:00:00', '2023-01-02 02:00:00']
            )
        }
    )

    assert_frame_equal(result[['ts']], expected)


def test_empty_dataframe():
    df = pd.DataFrame(columns=['start_date', 'end_date'])
    result = explode_date_range(df, 'start_date', 'end_date', freq='1h')
    expected = pd.DataFrame(columns=['ts'], dtype='datetime64[ns]')

    assert_frame_equal(result, expected)


def test_invalid_column_names():
    df = pd.DataFrame(
        {'start_date': ['2023-01-01'], 'end_date': ['2023-01-01 01:00:00']}
    )
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['end_date'] = pd.to_datetime(df['end_date'])

    with pytest.raises(KeyError):
        explode_date_range(df, 'invalid_start', 'end_date', freq='1h')
