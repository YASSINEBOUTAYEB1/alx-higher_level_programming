import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py YASSINEBOUTAYEB1 <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>")
    sys.exit(1)

username = sys.argv[1]
personal_access_token = sys.argv[2]

url = 'https://api.github.com/user'

# Set up authentication using the personal access token
auth = (username, personal_access_token)

try:
    response = requests.get(url, auth=auth)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

    user_data = response.json()

    print("Your GitHub user id:", user_data.get('id'))

except requests.exceptions.HTTPError as e:
    print("Error code:", e.response.status_code)
except requests.exceptions.RequestException as e:
    print("Error:", e)
except ValueError:
    print("Not a valid JSON")
