import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

    content = response.text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)

except requests.exceptions.HTTPError as e:
    print(f"Error code: {e.response.status_code}")
except requests.exceptions.RequestException as e:
    print("Error:", e)

