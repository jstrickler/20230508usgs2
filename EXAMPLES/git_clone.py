import os
from git import Git, Repo
#TODO: FIX!!!

github_url = 'https://github.com/jstrickler/myproject.git'
home_dir = os.path.expanduser('~')
repo_dir = os.path.join(home_dir, 'myproject')
clone_dir = os.path.join(home_dir, 'myproject_clone')

repo = Repo(repo_dir)

os.chdir(repo_dir)

Repo.clone_from(github_url, clone_dir)  # Clone existing repo to new repo

