pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'  // Specify the Docker Compose file if it's not named 'docker-compose.yml'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/nadazcx/Music-Predictor.git'
            }
        }

        stage('Build and Start Services with Docker Compose') {
            steps {
                script {
                    // Build and start the services defined in the docker-compose.yml
                    sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} up --build -d'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests (e.g., inside the relevant service container)
                    sh 'docker-compose exec <service_name> pytest tests/'
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    // If you need to push the images to Docker Hub or a private registry, do that here
                    sh 'docker-compose push'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy the application, typically by scaling services or bringing them up on a cloud server
                echo 'Deploying app...'
            }
        }
    }
}
