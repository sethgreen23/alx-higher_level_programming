#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status and
   get the 'X-Request-Id' value
"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) >= 3:
        username = sys.argv[1]
        token = sys.argv[2]
        headers = {
                "Accept": "application/vnd.github+json",
                "Authorization": "Bearer {}".format(token),
                "X-GitHub-Api-Version": "2022-11-28"
                }
        url = 'https://api.github.com/user'
        login = requests.get(url, headers=headers)
        body = login.json()
        print(body.get("id"))
