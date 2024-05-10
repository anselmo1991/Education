pipeline {
    agent {
        docker {
            image 'python:latest'
            args '-v C:\Users\Sofia_Shilova\PycharmProjects\Education>:/app'
        }
    }
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
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
