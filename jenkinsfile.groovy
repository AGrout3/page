pipeline {
    agent { docker { image 'python:3.7' } }

    stages {
        stage('1-Build') {
            steps {
                echo "Start of Stage Build"
                echo "Building......."
                sh   "pip install --upgrade pip"
                sh   "pip install -r requirements.txt"
                sh   "python --version"
                echo "End of Stage Build"
            }
        }
        stage('2-Test') {
            steps {
                echo "Start of Stage Test"
                echo "Testing......."
                sh   "pytest -v --tb=line --language=en -m need_review"
                echo "End of Stage Build"
            }
        }
        stage('3-Deploy') {
            steps {
                echo "Start of Stage Deploy"
                echo "Deploying......."
                echo "End of Stage Build"
            }
        }
   }
}