import json
from pprint import pprint
import random
import string
import hmac
import base64
import hashlib
import time
import requests
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


base_url = 'https://sandboxapi.rapyd.net'   # Replace with actual
# secret_key = '(your-secret-key)' # Never transmit the secret key by itself.
# access_key = '(your-access-key)' # The access key received from Rapyd.

access_key = os.getenv("RAPYD_ACCESS_KEY")
secret_key = os.getenv("RAPYD_SECRET_KEY") 

# salt: randomly generated for each request.
def generate_salt(length=12):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))

  # Current Unix time (seconds).
def get_unix_time(days=0, hours=0, minutes=0, seconds=0):
    return int(time.time())

def update_timestamp_salt_sig(http_method, path, body):
    if path.startswith('http'):
        path = path[path.find(f'/v1'):]
    salt = generate_salt()
    timestamp = get_unix_time()
    to_sign = (http_method, path, salt, str(timestamp), access_key, secret_key, body)
    
    h = hmac.new(secret_key.encode('utf-8'), ''.join(to_sign).encode('utf-8'), hashlib.sha256)
    signature = base64.urlsafe_b64encode(str.encode(h.hexdigest()))
    return salt, timestamp, signature

def current_sig_headers(salt, timestamp, signature):
    sig_headers = {'access_key': access_key, 
                   'salt': salt,
                   'timestamp': str(timestamp),
                   'signature': signature,
                   'idempotency': str(get_unix_time()) + salt}
    return sig_headers

# http_method = get|put|post|delete - must be lowercase
# path = Portion after the base URL.
# body = JSON body with no whitespace except in strings.
def pre_call(http_method, path, body=None):
    str_body = json.dumps(body, separators=(',', ':'), ensure_ascii=False) if body else ''
    salt, timestamp, signature = update_timestamp_salt_sig(http_method=http_method, path=path, body=str_body)
    return str_body.encode('utf-8'), salt, timestamp, signature

def create_headers(http_method, url,  body=None):
    body, salt, timestamp, signature = pre_call(http_method=http_method, path=url, body=body)
    return body, current_sig_headers(salt, timestamp, signature)

def make_request(method,path,body=''):
    body, headers = create_headers(method, base_url + path, body) # JSON body goes here. Always empty string for GET; 
    # pprint(f"Request Headers: {headers}\n\n\Body: {body}")
    headers['content-type'] = 'application/json'
    
    if method == 'get':
        response = requests.get(base_url + path,headers=headers)
    elif method == 'put':
        response = requests.put(base_url + path, data=body, headers=headers)
    elif method == 'delete':
        response = requests.delete(base_url + path, data=body, headers=headers)
    else:
        response = requests.post(base_url + path, data=body, headers=headers)

    if response.status_code != 200:
        pprint(response.content)
        raise TypeError(response, method,base_url + path)
    return json.loads(response.content)
              