"""
This file acts as a descriptive introduction to testing Python code with pytest.
It starts out by describing the simplest way of testing a function, to suggesting
a few noteworthy abstractions.
"""


from fibonacci.fibonacci_from_zero import fibonacci_from_zero
import pytest


"""
1. SIMPLE

A very simple test, not grouped in classes or anything, no abstractions.
"""


def test_fibonacci_from_zero_simple():
  # Arrange
  expected = [0, 1, 1, 2]
  
  # Act
  actual = fibonacci_from_zero(4)

  # Assert
  assert len(expected) == len(actual)
  assert expected == actual

 

"""
2. ABSTRACTED

As we add more test cases, things will start to get repetitive if we keep
adding test functions. We can abstract away bits of our test to alleviate
this.

pytest has the fixtures decorator, which is a great feature to leverage for
this purpose.
Docs: docs.pytest.org/en/6.2.x/fixture.html

Note that other language will do things differently, but the core concept
remains the same.
"""


@pytest.fixture
def test_fibonacci_from_zero_test_cases():
  return [
    [0, []],
    [5, [0, 1, 1, 2, 3]],
    [10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]]
  ]


def test_fibonacci_from_zero_abstracted_assert(test_fibonacci_from_zero_test_cases):
  for test_case in test_fibonacci_from_zero_test_cases:
    # Arrange
    how_many = test_case[0]
    expected = test_case[1]

    # Act
    actual = fibonacci_from_zero(how_many)

    # Assert
    assert len(expected) == len(actual)
    assert expected == actual


"""
3. PARAMETRIZED

pytest also has the parametrize decorator, which allows us to shorten
the code above even further.
Docs: docs.pytest.org/en/6.2.x/parametrize.html

We have also put the test function inside a class here, to nicely
isolate and organise our test.
"""


class TestFibonacciFromZeroParameterized:

    @pytest.mark.parametrize("how_many, expected", [
        (0, []),
        (5, [0, 1, 1, 2, 3]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ])
    def test_fibonacci_from_zero(self, how_many, expected):
        actual = fibonacci_from_zero(how_many)

        assert len(expected) == len(actual)
        assert expected == actual



"""
4. CONCLUSION

There are no "right" or "wrong" ways to write tests, only the most 
appropriate for the situation. There are conventions though, and 
following common convention will get you quite a long way (don't
have to fully stick to them if you have a reason why, of course).

In addition, every language does things differently, but the core
concept of how a test is structured (via Arrange / Act / Assert or
Given / When / Then) and abstracted (basically DRY - Don't Repeat
Yourself) remains the same.

Take a look at your favourite open source package on GitHub for 
inspirations! May be you can even suggest some improvements to them!

pandas: github.com/pandas-dev/pandas/tree/master/pandas/tests
numpy: github.com/numpy/numpy/tree/main/numpy (visit individual folders for their tests)
"""
