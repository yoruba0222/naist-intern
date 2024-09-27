import requests

# SonarQubeのURLとAPIトークン
SONAR_URL = 'localhost:9001/api'
API_TOKEN = 'sqp_9d284e2fc7c0bdc7b2044ff2560b1f11f2633b81'

# プロジェクトのメトリクスを取得する関数
def get_project_metrics(project_key):
    url = f"{SONAR_URL}/measures/component"
    params = {
        'component': project_key,
        'metricKeys': 'ncloc,complexity,coverage'  # 必要なメトリクスを指定
    }
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'  # APIトークンを設定
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# 使用例
project_key = 'naist-intern'
metrics = get_project_metrics(project_key)

if metrics:
    print(metrics)
