# -*- coding: utf-8 -*-
import os
from subprocess import run
from typing import Final


REPOS_PATH: Final[str] = "/home/ota/metrics_analyze/repos"
METRICS_PATH: Final[str] = "/home/ota/metrics_analyze/metricses"


def main() -> None:
  directlies: list[str] = os.listdir(REPOS_PATH)

  for dire in directlies:
    tmp_path: str = "/".join([REPOS_PATH, dire])
    unded_paths: list[str] = ["/".join([tmp_path, tmp2]) for tmp2 in os.listdir(tmp_path)]

    for path in unded_paths:
      file_name: str = "_".join(path.split("/")[-2:])
      und_file_name: str = "/".join([METRICS_PATH, file_name])
      print(f"und create -languages python {und_file_name}.und")
      print(f"und add {path} {und_file_name}.und")
      print(f"und metrics {und_file_name}.und")
      # 実行する時はここのコメントアウトを外すこと
      #run(f"und create -languages python {und_file_name}.und")
      #run(f"und add {path} {und_file_name}.und")
      #run(f"und metrics {und_file_name}.und")


if __name__ == "__main__":
  main()
