#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status and
   get the 'X-Request-Id' value
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) >= 3:
        repo = sys.argv[1]
        author = sys.argv[2]
        url = 'https://api.github.com/repos/'+author+'/'+repo+'/commits'
        login = requests.get(url)
        body = login.json()

        commits_list = []

        for value in body:
            commits = {}
            commits["sha"] = value.get("sha")
            commits["name"] = value.get("commit").get("author").get("name")
            commits["date"] = value.get("commit").get("author").get("date")
            commits_list.append(commits)
        commits_list = sorted(commits_list, key=lambda d: d['date'],
                              reverse=True)
        num = len(commits_list) if len(commits_list) < 10 else 10
        for index in range(0, num):
            value = commits_list[index]
            result = "{}: {}".format(value.get("sha"), value.get("name"))
            print(result)
