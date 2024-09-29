pipeline {
    agent any

    stages {
        stage('Verify Docker') {
            steps {
                // Verificar que Docker esté instalado y accesible
                sh 'docker --version'
            }
        }

        stage('Checkout') {
            steps {
                // Clonar el repositorio desde Git
                git branch: 'main', url: 'https://github.com/Guasonwrg/PresencialDevOps.git'
            }
        }

        stage('Build and Test') {
            steps {
                // Aquí puedes agregar comandos para compilar o probar tu aplicación
                echo 'Building and Testing...'
            }
        }

        stage('Levantar Contenedor') {
            steps {
                script {
                    // Levantar un contenedor Docker (ejemplo: MySQL)
                    sh 'docker run -d --name mysql-db -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=mydb -p 3306:3306 mysql:5.7'
                }
            }
        }
    }

    post {
        always {
            // Limpiar el contenedor, detenerlo y eliminarlo después de que finalice el pipeline
            script {
                sh 'docker stop mysql-db || true'
                sh 'docker rm mysql-db || true'
            }
        }
    }
}
