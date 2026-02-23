pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t event-registration-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker rm -f event-app-container || exit 0'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name event-app-container event-registration-app'
            }
        }

        stage('Test Application') {
            steps {
                bat 'echo Application Deployed Successfully'
            }
        }
    }
}