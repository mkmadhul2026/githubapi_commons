import requests

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = ${GITHUB_TOKEN}

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}   

response = requests.get(f"{GITHUB_API_URL}/user", headers=headers)
response.raise_for_status()

repo_info = response.json()

print(f"Authenticated as: {repo_info['login']}")
print(f"User ID: {repo_info['id']}")
print(f"Public Repos: {repo_info['public_repos']}")
