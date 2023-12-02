import requests
import sys

if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

url = 'http://0.0.0.0:5000/search_user'
data = {'q': q}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

    json_data = response.json()

    if json_data:
        print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    else:
        print("No result")

except requests.exceptions.HTTPError as e:
    print("Error code:", e.response.status_code)
except requests.exceptions.RequestException as e:
    print("Error:", e)
except ValueError:
    print("Not a valid JSON")

