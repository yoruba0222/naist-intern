# -*- coding: utf-8 -*-
"""
aw_.jsonからデータを取得してくる用
"""

import json
import copy
from pprint import pprint
from typing import Final


AW_PATH: Final[str] = "/workspace/autoware-2024-08/aw_.json"


class AwData:
  __repo_list: list[str] = []
  __changed_repos: dict[str,list[str]] = {}

  def __init__(self, file_name: str = AW_PATH):
    file = open(file_name, "r")
    data = json.load(file)

    for repo in data:
      repo_name = repo.get("full_name")
      self.__repo_list += [repo_name]

      changed_files: list[str] = []
      for commit in repo.get("changed_files"):
        changed_files += commit[1]
      changed_files = set(changed_files)
      changed_files = [s for s in changed_files if ".repos" in s]

      self.__changed_repos[repo_name] = changed_files

  def get_repo_list(self) -> list[str]:
    return copy.deepcopy(self.__repo_list)

  def get_changed_repos(self) -> dict[str, list[str]]:
    return copy.deepcopy(self.__changed_repos)

