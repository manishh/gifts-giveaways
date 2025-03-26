from utilities import make_request
from pprint import pprint

def show_supported_countries():
    resp = make_request(method='get',
                        path='/v1/data/countries')
    pprint(resp)

def list_payment_methods_for_country(country_code: str):
    resp = make_request(method='get', path=f'/v1/payment_methods/countries/{country_code}')
    pprint(resp)

def get_payment_method_fields(pay_method: str):
    resp = make_request(method='get', path=f'/v1/payment_methods/{pay_method}/required_fields')
    pprint(resp)    


# Error
# {"status":{"error_code":"INVALID_CURRENCY","status":"ERROR","message":"The request attempted an operation that requires a currency, but the value was missing or not recognized. The request was rejected. Corrective action: Use the correct 3-letter ISO 4217 code for the currency in uppercase letters.", "response_code":"INVALID_CURRENCY","operation_id":"2f5ab71e-cab2-4b5c-8199-5cd71c94fe5c"}
#  }
#ref: https://docs.rapyd.net/en/create-a-payment-in-python.html
def make_payment(amount: float):
    data = {
        "amount": f"{amount}",
        "currency": "EUR",
        "payment_method": {
            "type": "gb_visa_card",
            "fields": {
                "number": "4111111111111111",
                "expiration_month": "12",
                "expiration_year": "27",
                "cvv": "567",
                "name": "John Doe"
            }
        }
    }
    
    resp =  make_request(method='post', path='/v1/payments', body=data)
    print(f"Status --> {resp.get('status', {}).get('status', "")}")
    pprint(resp)


if __name__ == '__main__':
    # show_supported_countries()    # works fine
    # list_payment_methods_for_country('GB') # works fine
    # get_payment_method_fields('gb_zapp_bank')    # works fine

    # was working until 6 March 2025
    make_payment(555.0)    # invalid currency error???


