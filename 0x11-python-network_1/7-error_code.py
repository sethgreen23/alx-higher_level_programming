#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status and
   get the 'X-Request-Id' value
"""


if __name__ == "__main__":
    import requests
    from requests.exceptions import RequestException
    import sys

    url = sys.argv[1]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
        elif response.status_code >= 400:
            print('Error code: {}'.format(response.status_code))
    except RequestException as error:
        print('Error: {}'.format(error))
