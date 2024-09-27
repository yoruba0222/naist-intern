from sonarqube import SonarQubeClient

sonar = SonarQubeClient(sonarqube_url="http://localhost:9001", username='admin', password='adad')

result = sonar.auth.check_credentials()

print(result)
