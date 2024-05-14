pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                sh '/var/jenkins_home/venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Clean artefacts') {
            steps {
                sh 'rm ./allure-results -r'
            }
            steps {
                sh 'rm ./allure-report -r'
            }
        }
        stage('Run tests') {
            steps {
                sh '/var/jenkins_home/venv/bin/pytest --alluredir=allure-results -n auto --reruns 2'
            }
        }
    }
    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}

