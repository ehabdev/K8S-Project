pipeline {
    environment {
        dockerImage =''
        registry ="ehabdevopscourse/restapp_image"
        registryCredential = "Docker_ID"
        
    }
    
    agent any
    stages {
    stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('30 * * * *')])])
                    properties([buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '5', numToKeepStr: '20'))])
                }
                git 'https://github.com/ehabdev/DEVOPSCourse1.git'
            }
        }
   
    stage('run rest_app') {
            steps {
                script {
                    
                        bat  'start /min python rest_app.py'
                }
            }
        }
		
    stage('run backend testing') {
            steps {
                script {
                   
                        bat  'python backend_testing.py'
                }
            }
        
        }

    stage('run clean environment') {
            steps {
                script {
                   
                        bat  'python clean_environment.py'
                }
            }
        }   
    stage ('Build Docker Image')  
        {
            steps{
                script{
                      dockerImage = docker.build registry+ ":$BUILD_NUMBER"
                }
            }
        }
    stage ('Uploading Image')
        {
            steps{
                script{
                    
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
            }
                    
                
            }
                
            }
        }
        
    stage('set version') {
	
        steps {
                bat "echo IMAGE_TAG=${BUILD_NUMBER}>.env"
                 }
            }
        
   
        
    stage('docker-compose up') {
        steps {
                script {
                    
                    bat  'docker-compose up -d --wait '
                        
                }
            }
            }
            
        stage('Test dockerized app') {
            steps {
                script {
                    
                        bat  'start /min python docker_backend_testing.py '
                        bat  'python docker_backend_validation.py'
                }
            }
            
        }
    }
    post {  
          
         always {  
             
                      bat  'docker-compose down'
                      bat  'docker rmi  ehabdevopscourse/restapp_image:'+ "${BUILD_NUMBER}" 
                      
             
         }  
        
  
}
}
