pipeline {
    agent any
    parameters {
        choice(choices: ['api', 'web'], description: 'Select test type to run', name: 'TEST_TYPE')
    }
    stages {
        stage('Install dependencies') {
            steps {
                sh '/var/jenkins_home/venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh "/var/jenkins_home/venv/bin/pytest --alluredir=allure-results -n auto --reruns 2 -k '${params.TEST_TYPE}'"
            }
        }
    }
    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}

