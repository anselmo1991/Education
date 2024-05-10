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
                sh '/var/jenkins_home/venv/bin/pytest --alluredir=allure_results -n auto --reruns 2 --clean-alluredir'
            }
        }
        stage('Prepare test results') {
            steps {
                sh 'allure serve allure_results'
            }
        }
    }
}
