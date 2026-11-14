import requests

url = "https://api.github.com/users/dummygame012022-a11y/repos"
r = requests.get(url, timeout=10)
repos = r.json()

for repo in repos:
    print(repo["name"], "-", repo["language"])
