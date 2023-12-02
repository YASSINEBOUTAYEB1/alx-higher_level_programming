import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')

        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)

except urllib.error.HTTPError as e:
    print("Error:", e)
except urllib.error.URLError as e:
    print("Error:", e)
