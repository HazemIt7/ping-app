pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'devops_tool_app'
        DOCKER_TAG = 'latest'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    // Exemple: exécution des tests dans le conteneur
                    docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").inside {
                        sh 'python -m pytest tests/'
                    }
                }
            }
        }
        
        stage('Deploy to Dev') {
            steps {
                script {
                    // Arrête et supprime l'ancien conteneur si existant
                    sh 'docker stop devops_tool_app-dev || true'
                    sh 'docker rm devops_tool_app-dev || true'
                    
                    // Lance le nouveau conteneur
                    sh "docker run -d -p 5000:5000 --name devops_tool_app-dev ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
        

    }
    
    post {
        always {
            echo 'Nettoyage...'
            // Nettoyage des conteneurs et images intermédiaires
            sh 'docker system prune -f'
        }
        success {
            echo 'Pipeline réussi!'
        }
        failure {
            echo 'Pipeline échoué!'
        }
    }
}