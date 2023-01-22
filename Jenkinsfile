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
        stage("Testing"){
            steps{
                script{
                    bat "cd tests"
                    bat "pytest test_module.py"
                }
            }
        }
    }
}