pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t event-registration-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f event-app-container || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name event-app-container event-registration-app'
            }
        }

        stage('Test Application') {
            steps {
                sh 'echo "Application Deployed Successfully"'
            }
        }
    }
}