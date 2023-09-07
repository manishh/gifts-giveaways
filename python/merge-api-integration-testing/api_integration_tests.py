import unittest
import requests_mock
from api_integration import get_converted_price, get_product_availability

"""
The code here integrates two public APIs: 
- For currency conversion: https://github.com/fawazahmed0/currency-api#readme 
- For US zipcode information: https://api.zippopotam.us/

The class `TestAPIIntegrations` tests these API integration using `requests_mock`. 
"""


class TestAPIIntegrations(unittest.TestCase):

    def test_get_converted_price(self):
        test_data = {"date": "2023-09-01", "inr": 82.6}
        expected_price = 8260
        with requests_mock.Mocker() as mock:
            mock.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/inr.json", json=test_data)
            calculated_price = get_converted_price(100, "inr")
            self.assertEqual(calculated_price, expected_price, f"Price calculation is incorrect.")

    def test_get_converted_price_failure(self):
        with requests_mock.Mocker() as mock:
            mock.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/inr.json", status_code=404)
            calculated_price = get_converted_price(100, "inr")
            self.assertIsNone(calculated_price, "Price is _not_ None.")

    def test_get_product_availability_true(self):
        test_data = {"post code": "90210", "places": [{"place name": "Beverly Hills", "state": "California"}]}
        with requests_mock.Mocker() as mock:
            mock.get("https://api.zippopotam.us/us/90210", json=test_data)
            product_availability = get_product_availability(90210)
            self.assertTrue(product_availability, f"Product availability is incorrect.")

    def test_get_product_availability_false(self):
        test_data = {"post code": "75001", "places": [{"place name": "Addison", "state": "Texas"}]}
        with requests_mock.Mocker() as mock:
            mock.get("https://api.zippopotam.us/us/75001", json=test_data)
            product_availability = get_product_availability(75001)
            self.assertFalse(product_availability, f"Product availability is incorrect.")

    def test_get_product_availability_failure(self):
        with requests_mock.Mocker() as mock:
            mock.get("https://api.zippopotam.us/us/75001", status_code=500)
            product_availability = get_product_availability(75001)
            self.assertIsNone(product_availability, f"Product availability is incorrect.")


if __name__ == '__main__':
    unittest.main(verbosity=2)
