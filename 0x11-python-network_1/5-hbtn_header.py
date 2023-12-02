import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id:
        print("X-Request-Id:", x_request_id)
    else:
        print("X-Request-Id not found in the response headers.")

except requests.exceptions.RequestException as e:
    print("Error:", e)

