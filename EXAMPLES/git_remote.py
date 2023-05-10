import os
from git import Git, Repo

home_dir = os.path.expanduser('~')
repo_dir = os.path.join(home_dir, 'myproject')

repo = Repo(repo_dir)

os.chdir(repo_dir)

g = Git(repo)

g.remote('add', 'origin', 'https://github.com/jstrickler/myproject.git')  # Add remote repo named 'origin'

g.push('-u', 'origin', 'master')  # Push local files to remote and track 'origin' as the "master" repo so push() will automatically use it


