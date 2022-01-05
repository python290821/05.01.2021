from calc import total
import typing
import pytest

def test_total_empty() -> None:
    assert total([]) == 0

def test_total_empty() -> None:
    assert total([110.0]) == 110.0

def test_total_empty() -> None:
    assert total([1.0, 2.0, 3.0]) == 6.0

@pytest.mark.parametrize(('xs', 'expected'),(
        ([], 0.0),
        ([110.0], 110),
        ([1.0, 2.0, 3.0], 6.0)))
def test_total_various_inputs(xs, expected):
    assert total(xs) == expected