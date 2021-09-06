from fibonacci.fibonacci_from_zero import fibonacci_from_zero
import pytest


class TestFibonacciFromZero:

    @pytest.mark.parametrize("how_many, expected", [
        (0, []),
        (5, [0, 1, 1, 2, 3]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ])
    def test_fibonacci_from_zero(self, how_many, expected):
        actual = fibonacci_from_zero(how_many)

        assert len(expected) == len(actual)
        assert expected == actual
