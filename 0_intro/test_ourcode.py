"""
(Regression) tests.
"""
from conftest import assert_that_it_does_not_change
from ourcode import thing


def test_thing():
    # prepare
    # act
    result = thing()
    # assert
    assert result == "Very important!"


def test_thing_as_regression_test():
    # prepare
    # act
    result = thing()
    # assert
    assert_that_it_does_not_change(result)
