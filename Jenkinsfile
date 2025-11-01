pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-u root -p 5000:5000'
        }
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/I-am-satya/Jenkins_poc.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }
        stage('Run Application') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
