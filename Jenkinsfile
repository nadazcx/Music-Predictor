pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'  // Specify the Docker Compose file if it's not named 'docker-compose.yml'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out repository...'
                git branch: 'main', url: 'https://github.com/nadazcx/Music-Predictor.git'
            }
        }

        stage('Build and Start Services with Docker Compose') {
            steps {
                script {
                    // Disable sandbox for the shell execution command
                    runDockerComposeBuild()
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests (e.g., inside the relevant service container)
                    runDockerComposeExec()
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    // Push Docker images (disable sandbox for this step)
                    runDockerComposePush()
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy the application
                echo 'Deploying app...'
            }
        }
    }
}

// Use @NonCPS to run outside the Groovy CPS sandbox if necessary
@NonCPS
def runDockerComposeBuild() {
    sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} up --build -d'
}

@NonCPS
def runDockerComposeExec() {
    sh 'docker-compose exec <service_name> pytest tests/'
}

@NonCPS
def runDockerComposePush() {
    sh 'docker-compose push'
}
