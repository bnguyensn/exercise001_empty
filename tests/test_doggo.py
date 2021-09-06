import pytest
from doggo.get_random_doggo import get_random_doggo


class TestGetRandomDoggo:
    def test_get_random_doggo_success_case(self, mocker):
        """It should return the URL to a random doggo photo
        """

        # Arrange

        mock_get_return_value = mocker.Mock()
        mock_get_return_value.json.return_value = {
            'message': 'https://my-doggo.com', 'status': 200}

        mock_get = mocker.patch('doggo.get_random_doggo.requests.get',
                                return_value=mock_get_return_value, autospec=True)

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

        mock_get = mocker.patch('doggo.get_random_doggo.requests.get',
                                return_value=mock_get_return_value, autospec=True)

        # Act & Assert

        with pytest.raises(SystemExit):
            get_random_doggo()
            mock_get.assert_called()
            mock_get.assert_called_with(
                'https://dog.ceo/api/breeds/image/random')
