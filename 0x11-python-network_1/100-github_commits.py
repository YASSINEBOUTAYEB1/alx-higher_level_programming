import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <repository_name> <owner_name>")
    sys.exit(1)

repository_name = sys.argv[1]
owner_name = sys.argv[2]

url = f'https://api.github.com/repos/{owner_name}/{repository_name}/commits'
params = {'per_page': 10}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

    commits = response.json()

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

except requests.exceptions.HTTPError as e:
    print("Error code:", e.response.status_code)
except requests.exceptions.RequestException as e:
    print("Error:", e)
except ValueError:
    print("Not a valid JSON")
