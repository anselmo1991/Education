pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                sh '/var/jenkins_home/venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Activate venv') {
            steps {
                sh 'source /var/jenkins_home/venv/bin/activate'
            }
        }
        stage('Run tests') {
            steps {
                sh '/var/jenkins_home/venv/bin/python pytest --alluredir=allure_results -n auto --reruns 2 --clean-alluredir'
            }
        }
        stage('Prepare test results') {
            steps {
                sh 'allure serve allure_results'
            }
        }
        stage('Deactivate venv') {
            steps {
                sh 'source /var/jenkins_home/venv/bin/activate'
            }
        }
    }
}
