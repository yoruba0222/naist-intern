# -*- coding: utf-8 -*-
import os
import csv
import subprocess
from typing import Final
import requests
import time
from pprint import pprint


# analyze command
ANALYZE: Final[list[str]] = "sonar-scanner -Dsonar.projectKey=naist -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.token=sqp_578572cd397a61b93ebab2bcfe1ae6eb08952f11"
# sonarqube settings
SONARQUBE_URL: Final[str] = 'http://localhost:9000'  # SonarQubeサーバーのURL
API_TOKEN: Final[str] = 'squ_8544a6f921cbe16f882d9761056e0699fbd18a3d'  # APIトークン（必要に応じて）
PROJECT_KEY: Final[str] = "naist"

FILE_PATH: Final[str] = "/home/ota/metrics_analyze/data/demo2.csv"


# メトリクスを取得する関数
def get_metrics(project_key) -> dict:
    url = f"{SONARQUBE_URL}/api/measures/component"
    params = {
        'component': project_key,
        #'metricKeys': 'ncloc,complexity,coverage,bugs,code_smells,reliability_rating,security_hotspots,vulnerabilities,cognitive_complexity,duplicated_lines,spale_dept_ratio'  # 取得したいメトリクスを指定
        'metricKeys': 'ncloc,complexity,coverage,bugs,code_smells,reliability_rating,security_hotspots,vulnerabilities,cognitive_complexity,duplicated_lines,sqale_debt_ratio'
    }
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'  # ベーシック認証（トークンを使用する場合）
    }

    response = requests.get(url, params=params, headers=headers)
    print(response)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching metrics for {project_key}: {response.status_code}")
        return None

def append_row_to_csv(file_path, row):
    # 追記モードでCSVファイルを開く
    with open(file_path, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)  # 行を追加


def main() -> None:
    # 1. /reposディレクトリ以下にあるディレクトリをリストで取得
    base_dir = '/home/ota/metrics_analyze/cloned_forks'

    # 基本ディレクトリが存在するか確認
    if not os.path.exists(base_dir):
        print(f"{base_dir} が見つかりません。")
    else:
        # 2. for文で各ディレクトリに入る
        for entry in os.listdir(base_dir):
            path = os.path.join(base_dir, entry)
        
            if os.path.isdir(path):  # ディレクトリかどうか確認
                #print(f"ディレクトリ: {path}")
            
                # 3. ディレクトリの中のディレクトリをリストで取得
                for sub_entry in os.listdir(path):
                    sub_path = os.path.join(path, sub_entry)
                
                    if os.path.isdir(sub_path):  # サブディレクトリかどうか確認
                        # ディレクトリに入る
                        os.chdir(sub_path)
                        #print(f"  サブディレクトリ: {sub_path}")
                    
                        # 4. echoコマンドを実行
                        try:
                            print(f"{sub_path}を解析中")
                            result = subprocess.run(ANALYZE,shell=True, capture_output=True)
                            time.sleep(10)
                            metrics = get_metrics(PROJECT_KEY)
                            if metrics:
                                pprint(metrics)

                            # ここからcsvで出力していく
                            measures = metrics.get("component").get("measures")
                            metric = {m.get("metric"): m.get("value") for m in measures}
                            print(metric)
                            row = [sub_path,metric.get("bugs"),metric.get("code_smells"),metric.get("reliability_rating"),metric.get("security_hotspots"),metric.get("vulnerabilities"),metric.get("complexity"),metric.get("cognitive_complexity"),metric.get("duplicated_lines"),metric.get("sqale_debt_ratio"),metric.get("ncloc")]
                            append_row_to_csv(FILE_PATH, row)

                        except subprocess.CalledProcessError as e:
                            print(f"コマンド実行エラー: {e}")


if __name__ == "__main__":
    main()


