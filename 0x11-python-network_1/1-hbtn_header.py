#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status and
   get the 'X-Request-Id' value
"""


if __name__ == "__main__":
    from urllib.request import urlopen
    import sys

    url = sys.argv[1]
    with urlopen(url) as response:
        content = response.info()
        dic = content.__dict__
        head = dic.get('_headers')
        for row in head:
            if row[0] == 'X-Request-Id':
                print(row[1])
