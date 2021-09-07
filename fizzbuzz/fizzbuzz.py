from typing import Union, List


Result = Union[int, str]


def fizzbuzz(how_many: int) -> List[Result]:
  """Given an an integer n, return a list of length n where:
  - Items at indices divisible by 3 should be "Fizz"
  - Items at indices divisible by 5 should be "Buzz"
  - Items at indices divisible by both 3 and 5 should be "FizzBuzz"
  - In all other cases, the item should be the index number itself

  Arguments:
  int - how_many: the length of the result list
  """

  result = []

  for i in range(1, how_many + 1):
    if i % 3 == 0 and i % 5 == 0:
      result.append('FizzBuzz')
    elif i % 3 == 0:
      result.append('Fizz')
    elif i % 5 == 0:
      result.append('Buzz')
    else:
      result.append(i)
  
  return result