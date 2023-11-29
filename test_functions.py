import pytest
from hypothesis import given, settings, Verbosity
from hypothesis.strategies import integers, text
from functions import addition, reverse_string


@pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (3, 4, 7)])
def test_addition_parametrize(x, y, expected):
    assert addition(x, y) == expected


@pytest.mark.parametrize("string, expected", [('hola','aloh'), ('a', 'a'), ('', '')])
def test_reverse_string_parametrize(string, expected):
    assert reverse_string(string) == expected


@given(x = integers(), y = integers())
@settings(max_examples = 20, verbosity = Verbosity.verbose)
def test_addition_hypothesis(x, y):
    expected_sum = x + y
    result = addition(x, y)
    assert result == expected_sum


@given(string = text())
@settings(max_examples = 20, verbosity = Verbosity.verbose)
def test_reverse_string_hypothesis(string):
    assert string == reverse_string(string[::-1])
