# -*- coding: utf-8 -*-
"""
for fetching data from csv file
"""

import copy
import pandas as pd
from typing import Final


FILE_NAME: Final[str] = "autoware_fork_status.csv"


def main() -> None:
    df = pd.read_csv(FILE_NAME)

    for i, row in df.iterrows():
        print(df["repository_url"]) 


class csvData:
    __repo_list: list[str] = []
    __changed_repos: dict[str, list[str]] = {}

    def __init__(self, file_name: str = FILE_NAME):
        df = pd.read_csv(FILE_NAME)

        for i, row in df.iterrows():
            repo_name: str = "/".join(row["path"].split("/")[-2:])
            self.__repo_list += [repo_name]

            self.__changed_repos[repo_name] = row["repos"].split(":")

    def get_repo_list(self) -> list[str]:
        return copy.deepcopy(self.__repo_list)


    def get_changed_repos(self) -> dict[str, list[str]]:
        return copy.deepcopy(self.__changed_repos)


if __name__ == "__main__":
    ccc = csvData()
    print(ccc.get_repo_list())
    print(ccc.get_changed_repos())

