import unittest 
from unittest.mock import patch, MagicMock
from joke import len_joke , get_joke



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


    def test_get_joke_fail(self):

        with patch('joke.requests') as mock_requests:

            mock_response = MagicMock(status_code=400)
            mock_response.json.return_value = {'value': 'hello'}

            mock_requests.get.return_value = mock_response

            self.assertEqual(get_joke(), 'no joke')
        

           


if __name__ == '__main__':
    unittest.main()