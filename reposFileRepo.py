# -*- coding: utf-8 -*-
"""
特定のリポジトリ上の.repoファイルからデータを取得してくる用
"""
import yaml
from typing import Final


class ReposFileRepo:
  @classmethod
  def get_reposfile_repo(cls, repo_path: str, repo_file_name: str) -> dict[str,list]:
    repo_dict: [dict[str, list]] = {repo_file_name[:-6]: []}
    
    try: 
      file = open("/".join([repo_path,repo_file_name]), "r")
      data = yaml.safe_load(file)
      repos: list[dict] = data.get("repositories")
    except:
      return repo_dict


    for key, repo in repos.items():
      url = repo.get("url")
      repo_dict[repo_file_name[:-6]] += [url]
	
    return repo_dict
