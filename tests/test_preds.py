import unittest
import requests
import json

class TestPredictions(unittest.TestCase):
    def setUp(self):
        self.url = "http://serve-sentiment-env.eba-9bz3mptm.ca-central-1.elasticbeanstalk.com/predict"
        self.headers = {'Content-Type': 'application/json'}

    def test_valid_predictions(self):
        test_cases = [
            {"text": "ice cream is not taefdbet5sty", "expected": 'REAL'},
            {"text": "iphone is not euroiewruiowe", "expected": 'REAL'},
            {"text": "The sky is not jfsdkl;afjklsdafj", "expected": 'FAKE'},
            {"text": "The computer is a form of technology", "expected": 'FAKE'}
        ]

        for i, case in enumerate(test_cases):
            with self.subTest(i=i):
                response = requests.post(self.url, json={"text": case["text"]}, headers=self.headers)
                self.assertEqual(response.status_code, 200)
                data = response.json()
                self.assertIn('prediction', data)
                self.assertEqual(data['prediction'], case['expected'])

    def test_empty_input(self):
        response = requests.post(self.url, json={"text": ""}, headers=self.headers)
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Invalid input. "text" cannot be empty')

    def test_missing_text_field(self):
        response = requests.post(self.url, json={}, headers=self.headers)
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Invalid input. "text" field is required')

    def test_non_string_input(self):
        response = requests.post(self.url, json={"text": 123}, headers=self.headers)
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Invalid input. "text" must be a string')

    def test_invalid_json(self):
        response = requests.post(self.url, data="invalid json", headers=self.headers)
        self.assertEqual(response.status_code, 500)
        data = response.json()
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()