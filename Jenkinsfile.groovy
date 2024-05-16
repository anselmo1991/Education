pipeline {
    agent any
    parameters {
        choice(choices: ['api', 'web'], description: 'Select test type to run', name: 'TEST_TYPE')
    }
    triggers {
        parameterizedCron('''
            # leave spaces where you want them around the parameters. They'll be trimmed.
            # we let the build run with the default name
            0 * * * * %TEST_TYPE=web
            10 0/1 * * * %TEST_TYPE=api
        ''')
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

