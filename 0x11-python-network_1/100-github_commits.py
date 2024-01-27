#!/usr/bin/python3
"""
Script that lists 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
using the GitHub API.

Usage: ./100-github_commits.py [repository_name] [owner_name]
"""

import requests
import sys

if __name__ == "__main__":
    rep_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{rep_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]  # Limit to 10 most recent commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.status_code)
