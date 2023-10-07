import unittest 
import requests
from unittest.mock import patch, MagicMock
from joke import len_joke , get_joke, get_joke_with_exception
from requests.exceptions import Timeout, HTTPError


class TestJoke(unittest.TestCase):


    @patch('joke.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one'

        self.assertEqual(len_joke(), 3)



    def test_get_joke(self):

        with patch('joke.requests') as mock_requests:

            mock_response = MagicMock()

            mock_response.status_code = 200 
            mock_response.json.return_value = {'value': 'hello'}

            mock_requests.get.return_value = mock_response

            self.assertEqual(get_joke(), 'hello')
            self.assertEqual(get_joke_with_exception(), 'hello')


    def test_get_joke_fail(self):

        with patch('joke.requests') as mock_requests:

            mock_response = MagicMock(status_code=400)
            mock_response.json.return_value = {'value': 'hello'}

            mock_requests.get.return_value = mock_response

            self.assertEqual(get_joke(), 'no joke')
            self.assertEqual(get_joke_with_exception(), 'no joke')


    @patch('joke.requests')
    def test_get_joke_exception(self, mock_requests):

        mock_requests.exceptions = requests.exceptions

        mock_requests.get.side_effect = Timeout('Seems that the server is down')

        self.assertEqual(get_joke_with_exception(), 'no joke')


    @patch('joke.requests')
    def test_get_joke_raise_for_status(self, mock_requests):

        mock_requests.exceptions = requests.exceptions

        mock_response = MagicMock(status_code=403)

        mock_response.raise_for_status.side_effect = HTTPError('something goes wrong')

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke_with_exception(), 'HTTPError was raised')
           

        

           


if __name__ == '__main__':
    unittest.main()