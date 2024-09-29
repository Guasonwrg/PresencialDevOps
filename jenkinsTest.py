class JenkinsTest:
    def __init__(self, build_id, status):
        """
        Constructor para inicializar los parámetros del test de Jenkins.
        :param build_id: El ID del build de Jenkins.
        :param status: El estado del build (exitoso o fallido).
        """
        self.build_id = build_id
        self.status = status

    def execute_test(self):
        """
        Método principal para simular la ejecución de Jenkins y devolver un mensaje
        dependiendo del estado del build.
        """
        if self.status.lower() == "success":
            return f"Build #{self.build_id} ejecutado exitosamente en Jenkins."
        elif self.status.lower() == "failure":
            return f"Build #{self.build_id} falló durante la ejecución en Jenkins."
        else:
            return f"Build #{self.build_id} tiene un estado desconocido: {self.status}"

# Ejemplo de uso
if __name__ == "__main__":
    # Simulación de un build exitoso
    jenkins_test = JenkinsTest(build_id=101, status="success")
    message = jenkins_test.execute_test()
    print(message)

    # Simulación de un build fallido
    jenkins_test_failure = JenkinsTest(build_id=102, status="failure")
    message_failure = jenkins_test_failure.execute_test()
    print(message_failure)
