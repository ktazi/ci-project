pipeline {
	agent any
   	stages {
		stage('Creating staging branch') {
			steps {
                		sh 'git checkout dev'
                		sh 'git pull origin dev'
                		echo 'Creating a staging branch'
                		sh  'if [[ $(git branch -l | grep staging) != "" ]];then git branch -d staging; fi'
               			sh 'git branch staging'
            
            		}
		}
    		stage('Training the AI') {
			steps {
        			sh '''
				#!/usr/bin/env bash
				source ~/opt/anaconda3/etc/profile.d/conda.sh
				conda activate mlops
				~/opt/anaconda3/envs/mlops/bin/python ./server/train_model.py
				'''
      			}
    		}
		stage('Building the docker image of the server') {
			steps {
        			sh 'docker image build ./server -t kenztaz/server-anime-app'
				sh 'docker push kenztaz/server-anime-app'
      			}
    		}
		
		stage('Building the client and the monitor app') {
			steps {
				echo "test"
			}
    		}
		stage('Deploying and merging staging branch'){
			steps {
				echo 'Merging to the git master'
				sh 'git checkout master'
				sh 'git pull'
				sh 'git merge staging -m "incorporating build"'
				echo 'Deleting the staging branch'
				sh 'git branch -d staging'
			}
		}
	}
}
