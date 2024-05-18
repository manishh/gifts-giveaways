import asyncio

import grequests
import httpx
import requests
import uplink
import urllib3
import aiohttp


# demonstrates `requests` library
def demo_requests():
    print("Testing `requests` library...")
    resp = requests.get('https://httpbin.org/get', params={"foo": "bar"})
    if resp.status_code == 200:     # success
        print(f"Response Text: {resp.text} (HTTP-{resp.status_code})")
    else:   # error
        print(f"Error: HTTP-{resp.status_code}")


# demonstrates `requests` library with streaming
def demo_requests_streaming():
    print("Testing `requests` library with streaming...")
    resp = requests.get('https://httpbin.org/stream/10', stream=True)
    for chunk in resp.iter_content(chunk_size=1024):
        print(chunk.decode('utf-8'))


# demonstrates `urllib3` library
def demo_urllib3():
    print("Testing `urllib3` library...")
    http = urllib3.PoolManager()    # PoolManager for connection pooling
    resp = http.request('GET', 'https://httpbin.org/get', fields={"foo": "bar"})

    if resp.status == 200:     # success
        print(f"Response: {resp.data.decode('utf-8')} (HTTP-{resp.status})")
    else:   # error
        print(f"Error: HTTP-{resp.status}")


# demonstrates `urllib3` library's stream rsponse
def demo_urllib3_streaming():
    print("Testing `urllib3` library's streaming response...")
    http = urllib3.PoolManager()    # PoolManager for connection pooling

    # Streaming response
    with http.request('GET', 'https://httpbin.org/stream/10', preload_content=False) as streaming_resp:
        for chunk in streaming_resp.stream():
            print(chunk.decode('utf-8'))


# demonstrates `uplink`
@uplink.json
class JSONPlaceholderAPI(uplink.Consumer):
    @uplink.get("/posts/{post_id}")
    def get_post(self, post_id):
        pass


def demo_uplink():
    print("Testing `uplink` library...")
    api = JSONPlaceholderAPI(base_url="https://jsonplaceholder.typicode.com")
    resp = api.get_post(post_id=1)
    if resp.status_code == 200:     # success
        print(f"Response: {resp.json()} (HTTP-{resp.status_code})")
    else:   # error
        print(f"Error:HTTP-{resp.status_code}")


# demonstrates `grequests`
def demo_grequests():
    print("Testing `grequests` library...")
    # Fetching data from multiple endpoints concurrently
    urls = [
        'https://www.python.org/',
        'http://httpbin.org/get',
        'http://httpbin.org/ip',
    ]

    responses = grequests.map((grequests.get(url) for url in urls))
    for resp in responses:
        print(f"Response for: {resp.url} ==> HTTP-{resp.status_code}")


# demonstrates `grequests`
def demo_grequests_long():
    print("Testing `grequests` library (long)...")
    # Fetching data from multiple endpoints concurrently
    endpoints = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/todos',
    ]

    responses = grequests.map((grequests.get(url) for url in endpoints))
    for response in responses:
        if response.status_code == 200:     # success
            data = response.json()
            print(f"Endpoint: {response.url}")
            print(f"Number of items: {len(data)}")
            # You can process the data further as needed
        else:       # error
            print(f"Error fetching data from {response.url}: {response.status_code}")


# demonstrates `httpx`
async def fetch_posts():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://jsonplaceholder.typicode.com/posts')
        return response.json()


async def demo_httpx():
    print("Testing `httpx` library...")
    posts = await fetch_posts()
    for idx, post in enumerate(posts):
        print(f"Post #{idx+1}: {post['title']}")


def demo_httpx_misc():
    print("Testing `httpx` library for HTTP/2...")
    client = httpx.Client(http2=True)
    resp = client.get("https://http2.github.io/")
    print(resp.headers)

    print("Testing `httpx` library for streaming...")
    with httpx.stream("GET", "https://httpbin.org/stream/10") as resp:
        for text in resp.iter_text():
            print(text)


# demonstrate `aiohttp`
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def demo_aiohttp():
    print("Testing `aiohttp` library...")
    urls = [
        'https://www.python.org/',
        'http://httpbin.org/get',
        'http://httpbin.org/ip',
    ]
    tasks = [fetch_data(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    for resp_text in responses:
        print(f"Response code: {resp_text}")


if __name__ == "__main__":
    # uncomment the function that you want to test

    # demo_requests()
    # demo_requests_streaming()
    # demo_urllib3()
    # demo_urllib3_streaming()
    # demo_uplink()
    # demo_grequests()
    # demo_requests_http2()
    # asyncio.run(demo_httpx())
    # demo_httpx_misc()
    asyncio.run(demo_aiohttp())
