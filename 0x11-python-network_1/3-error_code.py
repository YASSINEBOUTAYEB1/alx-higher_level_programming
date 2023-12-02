import urllib.request
import urllib.error
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)

except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
except urllib.error.URLError as e:
    print("URL Error:", e)
