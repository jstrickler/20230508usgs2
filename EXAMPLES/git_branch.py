import os
from git import Git, Repo

home_dir = os.path.expanduser('~')
repo_dir = os.path.join(home_dir, 'myproject')

repo = Repo(repo_dir)

os.chdir(repo_dir)

g = Git(repo)

g.checkout('-b', 'myfeature')  # Create new branch named "myfeature"

g.add('tyger.py')  # tyger.py is only added and committed to branch "myfeature", not main branch
g.commit('tyger.py', message='new file')

