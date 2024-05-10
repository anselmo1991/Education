pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pipx install requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest --alluredir=allure_results -n auto --reruns 2 --clean-alluredir' //
            }
        }
        stage('Prepare test results') {
            steps {
                sh 'allure serve allure_results' //
            }
        }
    }
}
