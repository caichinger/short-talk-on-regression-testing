"""
Regression tests.
"""
import pandas as pd
from pytest_regressions import dataframe_regression, file_regression


def test_thing(file_regression):
    # prepare
    # act
    result = "Very important! =)"
    # assert
    file_regression.check(result)


def test_with_dataframe(dataframe_regression):
    result = pd.DataFrame({"foo": [1, 2], "bar": [10, 20]})
    dataframe_regression.check(result)
