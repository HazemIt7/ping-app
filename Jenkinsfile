pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python') {
            steps {
                sh '''
                python -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                python -m pytest tests/
                '''
            }
        }
        
        stage('Run Application') {
            steps {
                sh '''
                . venv/bin/activate
                nohup python app.py > app.log 2>&1 &
                echo $! > app.pid
                '''
            }
        }
    }
    
    post {
        always {
            sh 'pkill -F app.pid || true'
            sh 'rm -f app.pid app.log'
        }
    }
}