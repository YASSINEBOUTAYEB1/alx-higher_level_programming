import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Prepare data to be sent in the POST request
data = {'email': email}

try:
    # Send POST request
    response = requests.post(url, data=data)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

    content = response.text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)

except requests.exceptions.RequestException as e:
    print("Error:", e)

