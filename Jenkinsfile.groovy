pipeline {
    agent any
    stages {
        stage('Activate venv') {
            steps {
                sh '. /var/jenkins_home/venv/bin/activate'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest --alluredir=allure_results -n auto --reruns 2 --clean-alluredir'
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
