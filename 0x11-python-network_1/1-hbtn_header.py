import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')

        if x_request_id:
            print("X-Request-Id:", x_request_id)
        else:
            print("X-Request-Id not found in the response headers.")

except urllib.error.HTTPError as e:
    print("HTTP Error:", e)
except urllib.error.URLError as e:
    print("URL Error:", e)
