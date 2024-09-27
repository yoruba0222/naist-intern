import os
from github import Github
from git import Repo

# GitHubのアクセストークンを入力
g = Github()

# 対象リポジトリを取得
repo = g.get_repo("autowarefoundation/autoware")

# フォークを取得
forks = repo.get_forks()

# フォークをスターの数でソート
sorted_forks = sorted(forks, key=lambda x: x.stargazers_count, reverse=True)

# クローン先のディレクトリを指定
clone_dir = "cloned_forks"
os.makedirs(clone_dir, exist_ok=True)

i: int = 0
# フォークをクローン
for fork in forks:
    repo_url = fork.clone_url
    fork_name = fork.full_name
    print(f"Cloning {fork.full_name} - Stars: {fork.stargazers_count}")
    
    # クローンするディレクトリを指定
    target_dir = os.path.join(clone_dir, fork_name)
    
    # クローン実行
    Repo.clone_from(repo_url, target_dir)

    i += 1
    if i == 10:
        break

print("Cloning completed.")

