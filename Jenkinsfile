pipeline {
    agent { docker { image 'python:3.11-slim'; args '-u root:root' } }
 
    environment {
        PYTHONUNBUFFERED = '1'
        PYTHONPATH       = '.'
    }
    options {
        timestamps()
        timeout(time: 15, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '10',
                                  artifactNumToKeepStr: '5'))
    }
    triggers { pollSCM('H/2 * * * *') }   // o githubPush() con webhook
 
    stages {
        stage('Checkout') { steps { checkout scm } }
        // ... continúa en la siguiente lámina
        stage('Build') {
            steps { sh 'pip install -r requirements-dev.txt && mkdir -p reports output' }
        }
        stage('Test') {
            steps { sh 'pytest -v --junitxml=reports/junit.xml' }
        }
        stage('Run') {
            steps {
                sh '''python run_pipeline.py \
                        --input  data/ventas.csv \
                        --output output/ventas_limpias.csv'''
            }
        }
    }
    post {
        always {
            junit 'reports/junit.xml'
            archiveArtifacts artifacts: 'output/**', fingerprint: true
        }
        failure { echo "Revisar: ${env.BUILD_URL}console" }
    }
}
