//use 'sh' in place of 'bat' if using linus OS
pipeline{
    agent any
    stages{
        stage("Checkout"){
            steps{
            script{
                git branch: 'testing2', credentialsId: 'git_credentials', url: 'https://github.com/Abhinavkaul/duplicate-question-pairs.git'
                bat "dir"
            }
            }
        }
        stage("BuildDocker"){
            steps{
                script{
                    //bat "docker build -t test ."
                    //bat "docker run -it test /bin/bash -c "python -m pytest --cov=tests/ ./tests""
                    bat "docker-compose up"
                    bat "docker-compose down"
                }
            }
        }
        stage("Pytest"){
            steps{
                script{
                    bat "python -m pytest --cov=tests/ ./tests"
                }
            }
        }
    }
}