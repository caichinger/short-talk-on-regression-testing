"""
Regression tests.
"""
from functools import singledispatch

import pandas as pd
from approvaltests.approvals import verify


@singledispatch
def ourverfiy(obj):
    verify(obj)


@ourverfiy.register(pd.DataFrame)
def _(obj):
    return verify(obj.to_json(orient="split", indent=4))


def test_thing():
    # prepare
    # act
    result = "Very important! =)"
    # assert
    ourverfiy(result)


def test_with_dataframe():
    result = pd.DataFrame({"foo": [1, 2], "bar": [10, 20]})
    ourverfiy(result)
