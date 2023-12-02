import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Prepare data to be sent in the POST request
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    # Send POST request
    with urllib.request.urlopen(url, data) as response:
        content = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)

except urllib.error.HTTPError as e:
    print("HTTP Error:", e)
except urllib.error.URLError as e:
    print("URL Error:", e)

