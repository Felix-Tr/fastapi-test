import unittest
import json
import requests


class TestRequests(unittest.TestCase):
    """
    Test some basic functionalities of the api
    """
    def setUp(self):
        self.strings = {0: "Zero",
                        1: "One",
                        12: "Twelve",
                        25: "Twenty-five",
                        103: "One hundred and three",
                        814: "Eight hundred and fourteen",
                        1201: "One thousand two hundred and one",
                        201410: "Two hundred and one thousand four hundred and ten"}

    def test_int2str(self):
        for n, n_string in self.strings.items():
            response = requests.post(url="http://127.0.0.1/convert/", json={"number": n})
            response = json.loads(response.text)
            self.assertEqual(response['number_string'], n_string)

    def test_Exception(self):
        response = requests.post(url="http://127.0.0.1/convert/", json={"number": 1000001})
        response = json.loads(response.text)
        self.assertEqual(response['detail'], "Number is of order greater 6")

if __name__ == '__main__':
    unittest.main()
