#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status and
   get the 'X-Request-Id' value
"""


if __name__ == "__main__":
    import requests
    from requests.exceptions import RequestException
    import sys

    if len(sys.argv) >= 2:
        letter = sys.argv[1]
    else:
        letter = ""
    data = {'q': letter}
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=data)
    if response.status_code == 200:
        try:
            body = response.json()
            if len(body) == 0:
                print("No result")
            else:
                id = body.get('id')
                name = body.get('name')
                print('[{}] {}'.format(id, name))
        except ValueError as ve:
            print("Not a valid JSON")
