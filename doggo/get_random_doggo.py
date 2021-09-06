import requests


def get_random_doggo() -> str:
    """Return a URL to a random photo of a doggo!
    """

    try:
        url = 'https://dog.ceo/api/breeds/image/random'
        response = requests.get(url)
        response.raise_for_status()

        return (response.json())['message']

    except requests.exceptions.RequestException as e:
        raise SystemExit(e) from None
