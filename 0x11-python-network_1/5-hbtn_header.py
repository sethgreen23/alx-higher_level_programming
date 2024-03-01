#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status and
   get the 'X-Request-Id' value
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    id = response.headers.get('X-Request-Id')
    if id:
        print(id)
