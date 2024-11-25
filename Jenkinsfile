pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'music-predictor'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/nadazcx/Music-Predictor.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_TAG} .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh 'docker push ${DOCKER_IMAGE_NAME}:${DOCKER_TAG}'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run your tests here
                    sh 'pytest tests/'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy your app here, if needed (e.g., to cloud or server)
                echo 'Deploying app...'
            }
        }
    }
}
