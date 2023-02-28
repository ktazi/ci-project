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
    stage('test') {
			steps {
        sh 'echo test'
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
