pipeline{
    agent any
    stages{
        stage("Checkout"){
            script{
                git branch: 'testing2', credentialsId: 'git_credentials', url: 'https://github.com/Abhinavkaul/duplicate-question-pairs.git'
                bat "dir"
            }
        }
    }
}