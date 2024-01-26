#!/usr/bin/python3
"""Retrieve and display recent commits from a GitHub repository."""
import requests
import sys

if __name__ == "__main__":
    """Check if the correct number of args provided."""
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    """Get repository and owner names"""
    the_repo = sys.argv[1]
    user_name = sys.argv[2]

    """Ask GitHub API to get commits."""
    res = requests.get(f'https://api.github.com/repos/{user_name}/{the_repo}/commits')

    """Check if the request was successful"""
    if res.status_code == 200:
        commits = res.json()

        """Print details of the 10resent commits."""
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Unable to fetch commits. Status code: {res.status_code}")
