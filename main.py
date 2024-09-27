# -*- coding: utf-8 -*-
"""
"""
from typing import Final
from git import Repo
from csvRead import csvData
from reposFileRepo import ReposFileRepo


REPOS_PATH: Final[str] = "/home/ota/metrics_analyze/autoware-2024-08-02-11-07-43"
AUTOWARE_PATH: Final[str] = "/home/ota/autoware-2024-08-02-11-07-43/autoware"
TOOLS: Final[str] = "tools.repos"
SIMULATOR: Final[str] = "simulator.repos"
AUTOWARE: Final[str] = "autoware.repos"
CLONE_PATH: Final[str] = "https://github.com"
GITEX: Final[str] = ".git"


def cal_diff_set(a: list, b: list) -> list:
  return set(a) - set(b)
  

def main() -> None:
  # 追加情報の取得
  aw = csvData()
  repos_list: dict[str,list[str]] = aw.get_changed_repos()

  # ニュートラルな.repos情報を取得
  tools_repos: list[str] = ReposFileRepo.get_reposfile_repo(AUTOWARE_PATH, TOOLS)
  simulator_repos: list[str] = ReposFileRepo.get_reposfile_repo(AUTOWARE_PATH, SIMULATOR)
  autoware_repos: list[str] = ReposFileRepo.get_reposfile_repo(AUTOWARE_PATH, AUTOWARE)

  repos_diff: list[str] = []

  for repo_name, changed_files in repos_list.items():
  # ここで差分を確かめる
    for file in changed_files:
      spesicif_repos: list[str] = ReposFileRepo.get_reposfile_repo("/".join([REPOS_PATH ,repo_name]), file).get(file[:-6])
      print(spesicif_repos)
      if file == TOOLS:
        repos_diff += cal_diff_set(spesicif_repos, tools_repos)
      elif file == SIMULATOR:
        repos_diff += cal_diff_set(spesicif_repos, simulator_repos)
      elif file == AUTOWARE:
        repos_diff += cal_diff_set(spesicif_repos, autoware_repos)
      else:
        repos_diff += spesicif_repos

  repos_diff = set(repos_diff)

  # クローンしていく
  for repo in repos_diff:
    repo = repo.replace("git@github.com:", "https://github.com/")
    try:
      Repo.clone_from(repo , to_path="/home/ota/metrics_analyze/repos/"+repo[19:-6])
    except:
      pass

if __name__ == "__main__":
  main()
