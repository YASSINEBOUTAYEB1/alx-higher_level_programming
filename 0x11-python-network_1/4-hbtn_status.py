import requests

url = 'https://alx-intranet.hbtn.io/status'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

    content = response.text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)

except requests.exceptions.RequestException as e:
    print("Error:", e)

