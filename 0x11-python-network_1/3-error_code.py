#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status and
   get the 'X-Request-Id' value
"""


if __name__ == "__main__":
    from urllib import parse, request
    from urllib.error import HTTPError
    import sys
    import urllib

    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except HTTPError as error:
        print("Error code: {}".format(error.status))
