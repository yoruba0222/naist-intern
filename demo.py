import requests
from pprint import pprint

# SonarQubeの設定
SONARQUBE_URL = 'http://localhost:9000'  # SonarQubeサーバーのURL
API_TOKEN = 'squ_8544a6f921cbe16f882d9761056e0699fbd18a3d'  # APIトークン（必要に応じて）

# プロジェクトのキーリスト
project_key = "naist"  # プロジェクトのキーを設定

# メトリクスを取得する関数
def get_metrics(project_key):
    url = f"{SONARQUBE_URL}/api/measures/component"
    params = {
        'component': project_key,
        'metricKeys': 'ncloc,complexity,coverage,bugs,code_smells,reliability_rating,security_hotspots,vulnerabilities,cognitive_complexity,duplicated_lines,sqale_debt_ratio'  # 取得したいメトリクスを指定
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

# 各プロジェクトのメトリクスを取得

metrics = get_metrics(project_key)
if metrics:
    pprint(metrics)

