import requests

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = "${COMMON_TOKEN}"  # Replace with your GitHub personal access token

owner = "mkmadhul2026"
repo = "githubapi_commons"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}   

response = requests.get(f"{GITHUB_API_URL}/repos/{owner}/{repo}", headers=headers)
response.raise_for_status()

repo_info = response.json()

print(f"Authenticated as: {repo_info['login']}")
print(f"User ID: {repo_info['id']}")
print(f"Public Repos: {repo_info['public_repos']}")
print(f"Followers: {repo_info['followers']}")
print(f"Following: {repo_info['following']}")
print(f"Account Created At: {repo_info['created_at']}")
print(f"Account Updated At: {repo_info['updated_at']}")
print(f"Account Type: {repo_info['type']}")
print(f"Account Site Admin: {repo_info['site_admin']}")
print(f"Account Bio: {repo_info['bio']}")
print(f"Account Location: {repo_info['location']}")
