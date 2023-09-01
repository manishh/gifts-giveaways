import unittest
import requests
import requests_mock

"""
The code here integrates two public APIs: 
- For currency conversion: https://github.com/fawazahmed0/currency-api#readme 
- For US zipcode information: https://api.zippopotam.us/

The class `TestAPIIntegrations` tests these API integration using `requests_mock`. 
"""


def get_converted_price(product_price: int, conversion_currency: str) -> float:
    converted_price = None
    base_currency = "usd"
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{base_currency}/{conversion_currency.lower()}.json"

    try:
        resp = requests.get(api_url)
        if resp.ok:     # HTTP OK
            currency_data = resp.json()
            converted_price = product_price * currency_data[conversion_currency]
            print(f"Converted price for the product: {round(converted_price, 2)} {conversion_currency.upper()}")
        else:
            print(f"Response: {resp.text} (HTTP-{resp.status_code})")
    except Exception as ex:
        print(f"Error: {ex}")    # show error
    finally:
        return converted_price


def get_product_availability(zipcode: int) -> bool:
    availability = None
    skip_states = ["Idaho", "Indiana", "Kansas", "Kentucky", "Mississippi", "Nebraska", "North Carolina",
                   "Oklahoma", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Wyoming"]
    api_url = f"https://api.zippopotam.us/us/{zipcode}"

    try:
        resp = requests.get(api_url)
        if resp.ok:     # HTTP OK
            zip_data = resp.json()
            state = zip_data["places"][0]["state"]
            availability = False if state in skip_states else True
            print(f"The product is available in: {state} - {availability}")
        else:
            print(f"Response: {resp.text} (HTTP-{resp.status_code})")
    except Exception as ex:
        print(f"Error: {ex}")    # show error
    finally:
        return availability


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
