import requests

"""
The code here integrates two public APIs: 
    - For currency conversion: https://github.com/fawazahmed0/currency-api#readme 
    - For US zipcode information: https://api.zippopotam.us/
    
    These functions can be tested with `TestAPIIntegrations` class (from: api_integration_tests.py)
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