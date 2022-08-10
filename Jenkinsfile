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
                git 'https://github.com/ehabdev/K8S-Project.git'
            }
        }
    
	   
    stage('run rest_app') {
            steps {
                script {
                    
                        bat  'start /b /min python rest_app.py'
                }
            }
        }
		
    stage('run backend testing') {
            steps {
                script {
                   
                        bat  'python backend_testing.py'
                        sleep 3
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
		
	                  
	stage('Clean compose environment') {
        steps {
                script {
                    
                        bat  'docker-compose down'
    	                bat  'docker rmi  ehabdevopscourse/restapp_image:'+ "${BUILD_NUMBER}" 
                }
            }
            
        }	
	
	
	stage('Install helm chart ') {
        steps {
                script {
                    
                    
                    bat  'helm install  k8schart  projectchart --set image.version=ehabdevopscourse/restapp_image:'+ "${BUILD_NUMBER}"  
                        
                }
            }
        }
		

     
    stage('Write URL to text file ') {
        steps {
                script {
                    
                    
                    bat  ' start /b /min  minikube service restapp-service --url > k8s_url.txt' 
                    sleep 3
                    bat  'clear'    
                }
            }
        }
		
    stage('Test deployed app ') {
        steps {
                script {
                    
                    
                    bat  'start /min K8S_backend_testing.py '
                    bat  'python K8S_backend-testvalidation.py'
                        
                }
            }
        }
		
	

    stage('Clean Helm release ') {
        steps {
                script {
                    
                    
                    bat  'helm uninstall k8schart' 
                        
                }
            }
        } 
	
    }  
}
	
	
	
	
	
	
