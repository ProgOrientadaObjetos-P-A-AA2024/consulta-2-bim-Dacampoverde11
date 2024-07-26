class Estudiante:
    # Constructor para inicializar los atributos
    def __init__(self, nombres, apellidos, identificacion, edad):
        self._nombres_estudiante = nombres
        self._apellidos_estudiante = apellidos
        self._identificacion_estudiante = identificacion
        self._edad_estudiante = edad

    # Métodos establecer
    def establecer_nombres_estudiante(self, nombres):
        self._nombres_estudiante = nombres

    def establecer_apellidos_estudiante(self, apellidos):
        self._apellidos_estudiante = apellidos

    def establecer_identificacion_estudiante(self, identificacion):
        self._identificacion_estudiante = identificacion

    def establecer_edad_estudiante(self, edad):
        self._edad_estudiante = edad

    # Métodos obtener
    def obtener_nombres_estudiante(self):
        return self._nombres_estudiante

    def obtener_apellidos_estudiante(self):
        return self._apellidos_estudiante

    def obtener_identificacion_estudiante(self):
        return self._identificacion_estudiante

    def obtener_edad_estudiante(self):
        return self._edad_estudiante


class EstudianteDistancia(Estudiante):
    # Constructor para inicializar los atributos
    def __init__(self, nombres, apellidos, identificacion, edad, num_asignaturas, costo_asignatura):
        super().__init__(nombres, apellidos, identificacion, edad)
        self._numero_asignaturas = num_asignaturas
        self._costo_asignatura = costo_asignatura
        self._matricula_distancia = 0

    # Métodos establecer
    def establecer_numero_asignaturas(self, numero):
        self._numero_asignaturas = numero

    def establecer_costo_asignatura(self, valor):
        self._costo_asignatura = valor

    # Método calcular
    def calcular_matricula_distancia(self):
        self._matricula_distancia = self._numero_asignaturas * self._costo_asignatura

    # Métodos obtener
    def obtener_numero_asignaturas(self):
        return self._numero_asignaturas

    def obtener_costo_asignatura(self):
        return self._costo_asignatura

    def obtener_matricula_distancia(self):
        return self._matricula_distancia

    # Método para imprimir información
    def __str__(self):
        return (f"ESTUDIANTE A DISTANCIA\n"
                f"Nombre: {self._nombres_estudiante}\n"
                f"Apellidos: {self._apellidos_estudiante}\n"
                f"Identificación Estudiante: {self._identificacion_estudiante}\n"
                f"Edad Estudiante: {self._edad_estudiante}\n"
                f"Numero de Asignaturas: {self._numero_asignaturas}\n"
                f"Costo de Asignatura: {self._costo_asignatura:.2f}\n"
                f"Costo Matricula: {self._matricula_distancia:.2f}")


class EstudiantePresencial(Estudiante):
    # Constructor para inicializar los atributos
    def __init__(self, nombres, apellidos, identificacion, edad, num_creditos, costo_credito):
        super().__init__(nombres, apellidos, identificacion, edad)
        self._numero_creditos = num_creditos
        self._costo_credito = costo_credito
        self._matricula_presencial = 0

    # Métodos establecer
    def establecer_numero_creditos(self, numero):
        self._numero_creditos = numero

    def establecer_costo_credito(self, valor):
        self._costo_credito = valor

    # Método calcular
    def calcular_matricula_presencial(self):
        self._matricula_presencial = self._numero_creditos * self._costo_credito

    # Métodos obtener
    def obtener_numero_creditos(self):
        return self._numero_creditos

    def obtener_costo_credito(self):
        return self._costo_credito

    def obtener_matricula_presencial(self):
        return self._matricula_presencial

    # Método para imprimir información
    def __str__(self):
        return (f"ESTUDIANTE PRESENCIAL\n"
                f"Nombre: {self._nombres_estudiante}\n"
                f"Apellidos: {self._apellidos_estudiante}\n"
                f"Identificación Estudiante: {self._identificacion_estudiante}\n"
                f"Edad Estudiante: {self._edad_estudiante}\n"
                f"Numero de Creditos: {self._numero_creditos}\n"
                f"Costo de Creditos: {self._costo_credito:.2f}\n"
                f"Costo Matricula: {self._matricula_presencial:.2f}")


# Ejemplo de uso
if __name__ == "__main__":
    # Objeto de tipo Estudiante Presencial
    e1 = EstudiantePresencial("René Rolando", "Elizalde Solano", "1104111111", 38, 30, 15)
    e1.calcular_matricula_presencial()

    print(f"Nombres: {e1.obtener_nombres_estudiante()}\n"
          f"Apellidos: {e1.obtener_apellidos_estudiante()}\n"
          f"Identificación: {e1.obtener_identificacion_estudiante()}\n"
          f"Edad: {e1.obtener_edad_estudiante()}\n"
          f"Número de créditos: {e1.obtener_numero_creditos()}\n"
          f"Costo Crédito: {e1.obtener_costo_credito():.1f}\n"
          f"Costo matrícula: {e1.obtener_matricula_presencial():.1f}")

    # Objeto de tipo Estudiante a Distancia
    e2 = EstudianteDistancia("Juan", "Perez", "123456789", 20, 5, 100.0)
    e2.calcular_matricula_distancia()

    print(f"\nNombres: {e2.obtener_nombres_estudiante()}\n"
          f"Apellidos: {e2.obtener_apellidos_estudiante()}\n"
          f"Identificación: {e2.obtener_identificacion_estudiante()}\n"
          f"Edad: {e2.obtener_edad_estudiante()}\n"
          f"Número de asignaturas: {e2.obtener_numero_asignaturas()}\n"
          f"Costo Asignatura: {e2.obtener_costo_asignatura():.1f}\n"
          f"Costo matrícula: {e2.obtener_matricula_distancia():.1f}")

