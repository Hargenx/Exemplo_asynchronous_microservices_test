import unittest
import requests

class TestMicroservice(unittest.TestCase):

    def test_oi_endpoint(self):
        response = requests.get('http://localhost:5000/oi')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Oi do Python microservice!')

if __name__ == '__main__':
    unittest.main()
