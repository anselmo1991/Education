pipeline {
    agent {
        docker {
            image 'python:3.9.7'
            args '-v C:/Users/Sofia_Shilova/PycharmProjects/Education'
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
