import requests
import base64


def get_repo_contents(url, filepath):
    # Parse the URL to extract owner, repo, and ref
    path_parts = url.split("/")[
        3:
    ]  # Split the URL and ignore the first 4 parts (http:, , localhost:3000, admin)
    owner = path_parts[0]  # str | owner of the repo
    repo = path_parts[1]  # str | name of the repo
    ref = path_parts[-1]  # str | The name of the commit/branch/tag
    url = f"http://gitea:3000/api/v1/repos/{owner}/{repo}/contents/{filepath}?ref={ref}"
    headers = {
        "accept": "application/json",
        "Authorization": "token 87282d54cd23a690e80f658e9043416f637ad469",
    }

    response = requests.get(url, headers=headers)
    d = response.json()
    # Decode the base64-encoded content
    decoded_bytes = base64.b64decode(d["content"])

    # Convert bytes to a string (assuming the content is UTF-8 encoded)
    decoded_string = decoded_bytes.decode("utf-8")
    return decoded_string


# Call the function with the example URL and the README.md file
c = get_repo_contents(
    "http://localhost:3000/admin/Test/commit/24447a4339ab18618bd2dcb2935fb26fe036322c",
    "README.md",
)

print(c)
