class Estudiante:
    def __init__(self, nombres, apellidos, identificacion, edad):
        self.nombres_estudiante = nombres
        self.apellidos_estudiante = apellidos
        self.identificacion_estudiante = identificacion
        self.edad_estudiante = edad
        self.matricula = 0.0

    def establecer_nombres_estudiante(self, nombres):
        self.nombres_estudiante = nombres

    def establecer_apellidos_estudiante(self, apellidos):
        self.apellidos_estudiante = apellidos

    def establecer_identificacion_estudiante(self, identificacion):
        self.identificacion_estudiante = identificacion

    def establecer_edad_estudiante(self, edad):
        self.edad_estudiante = edad

    def obtener_nombres_estudiante(self):
        return self.nombres_estudiante

    def obtener_apellidos_estudiante(self):
        return self.apellidos_estudiante

    def obtener_identificacion_estudiante(self):
        return self.identificacion_estudiante

    def obtener_edad_estudiante(self):
        return self.edad_estudiante

    def calcular_matricula(self):
        raise NotImplementedError("Debe implementar este método en las subclases")

    def obtener_matricula(self):
        return self.matricula

    def __str__(self):
        return (f"Nombre estudiante: {self.nombres_estudiante}\n"
                f"Apellido estudiante: {self.apellidos_estudiante}\n"
                f"Identificacion estudiante: {self.identificacion_estudiante}\n"
                f"Edad estudiante: {self.edad_estudiante}\n"
                f"Costo matricula: {self.obtener_matricula():.2f}\n")


class EstudianteDistancia(Estudiante):
    def __init__(self, nombres, apellidos, identificacion, edad, num_asignaturas, costo_asignatura):
        super().__init__(nombres, apellidos, identificacion, edad)
        self.numero_asignaturas = num_asignaturas
        self.costo_asignatura = costo_asignatura

    def establecer_numero_asignaturas(self, numero):
        self.numero_asignaturas = numero

    def establecer_costo_asignatura(self, valor):
        self.costo_asignatura = valor

    def calcular_matricula(self):
        self.matricula = self.numero_asignaturas * self.costo_asignatura

    def obtener_numero_asignaturas(self):
        return self.numero_asignaturas

    def obtener_costo_asignatura(self):
        return self.costo_asignatura

    def __str__(self):
        return (f"ESTUDIANTE A DISTANCIA\n"
                f"Nombre: {self.nombres_estudiante}\n"
                f"Apellidos: {self.apellidos_estudiante}\n"
                f"Identificación Estudiante: {self.identificacion_estudiante}\n"
                f"Edad Estudiante: {self.edad_estudiante}\n"
                f"Numero de Asignaturas: {self.numero_asignaturas}\n"
                f"Costo de Asignatura: {self.costo_asignatura:.2f}\n"
                f"Costo Matricula: {self.matricula:.2f}\n")


class EstudiantePresencial(Estudiante):
    def __init__(self, nombres, apellidos, identificacion, edad, num_creditos, costo_credito):
        super().__init__(nombres, apellidos, identificacion, edad)
        self.numero_creditos = num_creditos
        self.costo_credito = costo_credito

    def establecer_numero_creditos(self, numero):
        self.numero_creditos = numero

    def establecer_costo_credito(self, valor):
        self.costo_credito = valor

    def calcular_matricula(self):
        self.matricula = self.numero_creditos * self.costo_credito

    def obtener_numero_creditos(self):
        return self.numero_creditos

    def obtener_costo_credito(self):
        return self.costo_credito

    def __str__(self):
        return (f"ESTUDIANTE PRESENCIAL\n"
                f"Nombre: {self.nombres_estudiante}\n"
                f"Apellidos: {self.apellidos_estudiante}\n"
                f"Identificación Estudiante: {self.identificacion_estudiante}\n"
                f"Edad Estudiante: {self.edad_estudiante}\n"
                f"Numero de Creditos: {self.numero_creditos}\n"
                f"Costo de Creditos: {self.costo_credito:.2f}\n"
                f"Costo Matricula: {self.matricula:.2f}\n")


if __name__ == "__main__":
    import sys

    estudiantes = []

    for contador in range(4):
        tipo_estudiante = int(input("Tipo de Estudiante a ingresar\n"
                                    "Ingrese (1) para Estudiante Presencial\n"
                                    "Ingrese (2) para Estudiante Distancia\n"))

        nombres_est = input("Ingrese los nombres del estudiante: ")
        apellidos_est = input("Ingrese los apellidos del estudiante: ")
        identificacion_est = input("Ingrese la identificación del estudiante: ")
        edad_est = int(input("Ingrese la edad del estudiante: "))

        if tipo_estudiante == 1:
            numero_creds = int(input("Ingrese el número de créditos: "))
            costo_cred = float(input("Ingrese el costo de cada crédito: "))

            estudiante = EstudiantePresencial(nombres_est, apellidos_est, identificacion_est, edad_est, numero_creds, costo_cred)
        else:
            numero_asigs = int(input("Ingrese el número de asignaturas: "))
            costo_asig = float(input("Ingrese el costo de cada asignatura: "))

            estudiante = EstudianteDistancia(nombres_est, apellidos_est, identificacion_est, edad_est, numero_asigs, costo_asig)

        estudiante.calcular_matricula()
        estudiantes.append(estudiante)

    for estudiante in estudiantes:
        print("Datos Estudiante\n"
              f"Nombres: {estudiante.obtener_nombres_estudiante()}\n"
              f"Apellidos: {estudiante.obtener_apellidos_estudiante()}\n"
              f"Identificación: {estudiante.obtener_identificacion_estudiante()}\n"
              f"Edad: {estudiante.obtener_edad_estudiante()}\n"
              f"Costo Matricula: {estudiante.obtener_matricula():.2f}\n")
