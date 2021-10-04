"""
The tests in this file involves test doubles (namely mocking the return
results of functions).

As always, note that mocking allows us to have isolated and consistent tests,
but it abtracts away the actual behaviour of our software.

python has a standard mocking feature (unittest.mock). The tests in this file
use pytest-mock a wrapper around unittest.mock to make writing mocks a bit
clearer.

Of course, one is free to use unittest.mock directly or any other packages to,
mock stuff, as long as they help you achieve your end results.

Each language does things a little bit differently, but the core concept around
how to work with test doubles remains the same.
"""


import pytest
from doggo.get_random_doggo import get_random_doggo


class TestGetRandomDoggo:
  def test_get_random_doggo_success_case(self, mocker):
    """It should return the URL to a random doggo photo
    """

    # ##### Arrange ##### #
    
    # Create a mock value for the requests.get() function. We want
    # it to not do its usual thing (making a /GET HTTP request) and
    # always return the object below.
    mock_get_return_value = mocker.Mock()
    mock_get_return_value.json.return_value = {
      'message': 'https://my-doggo.com', 
      'status': 200
    }

    # Tell the requests.get() function inside the doggo.get_random_doggo
    # module to always return mock_get_return_value. Don't worry too
    # much about mocker syntax as each language does things a little bit
    # differently.
    # Docs: github.com/pytest-dev/pytest-mock/#usage.
    mock_get = mocker.patch(
      'doggo.get_random_doggo.requests.get',
      return_value=mock_get_return_value, autospec=True
    )

    # We expect the returned value from get_random_doggo to be this URL
    # string. Note that it's also the 'message' field of our mock return
    # value.
    expected = 'https://my-doggo.com'

    # Act

    actual = get_random_doggo()

    # Assert

    assert expected == actual

    mock_get.assert_called()
    mock_get.assert_called_with('https://dog.ceo/api/breeds/image/random')

  def test_get_random_doggo_failure_case(self, mocker):
    """It should raise SystemExit exception
    """

    # Arrange
    
    mock_get_return_value = mocker.Mock()
    mock_get_return_value.raise_for_status.side_effect = SystemExit()

    # Tell the requests.get() function inside the doggo.get_random_doggo
    # module to always raise a SystemExit() error.
    mock_get = mocker.patch(
      'doggo.get_random_doggo.requests.get',
      return_value=mock_get_return_value,
      autospec=True
    )
    
    # Act & Assert

    with pytest.raises(SystemExit):
        get_random_doggo()
        mock_get.assert_called()
        mock_get.assert_called_with(
          'https://dog.ceo/api/breeds/image/random'
        )
