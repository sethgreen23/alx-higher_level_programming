#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status and
   get the 'X-Request-Id' value
"""


if __name__ == "__main__":
    from urllib import parse, request
    from urllib.error import HTTPError, URLError
    import sys
    import urllib

    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode({'email': email}).encode('utf-8')
    req = request.Request(url, data=data)
    try:
        with request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8')
            print(content)
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")
