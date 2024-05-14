pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                sh '/var/jenkins_home/venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh '/var/jenkins_home/venv/bin/pytest --alluredir=allure_results -n auto --reruns 2'
            }
        }
    }
    post {
        always {
            sh 'allure serve allure_results'
        }
    }
}

