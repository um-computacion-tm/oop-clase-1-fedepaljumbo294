# 1.Agregar test para clase Materia y Profesor incluyendo test de constructor y demás metodos
# 2.La clase materia deberia tener un atributo __ alumnos __ equivalente a una lista de Alumnos. 
#   Empezando por los tests:
#   a.Implementar la clase Alumno
#   b.Agregar atributo __ alumno __ a clase Materia
#   c.Agregar metodo obtener_alumnos(self) que devuelva __ alumnos __ 
import unittest

class Alumno:
    def __init__(self, nombre, legajo, edad, mail):
        self.__nombre__ = nombre
        self.__legajo__ = legajo
        self.__edad__ = edad
        self.__mail__ = mail
        self.__inasistencia__ = 0
        self.__mentor__ = None

    def agregar_mentor(self, mentor):
        self.__mentor__ = mentor
    
    def cambiar_mail(self, mail):
        self.__mail__ = mail

class Materia:
    def __init__(self, nombre, profesores):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = []
    
    def obtener_alumnos(self):
        return self.__alumnos__

    def obtener_profesores(self):
        return self.__profesores__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

    def agregar_alumno(self, alumno):
        self.__alumnos__.append(alumno)

class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__


alumno = Alumno(nombre="Camila",legajo=4321,edad=21,mail=None)
profesor = Profesor(nombre ="Daniel",cargo = "profesor",legajo = 1234)

class TestAlumno(unittest.TestCase):
    def test_obtener_alumno(self):
        materia = Materia(nombre="Computacion", profesores=[profesor])
        # Obtener la lista de alumnos de la materia
        alumnos = materia.obtener_alumnos()
        # Verificar que la lista de alumnos esté vacía inicialmente
        self.assertEqual(len(alumnos), 0)

    def test_agregar_alumno(self):
        materia = Materia(nombre="Computacion", profesores=[profesor])
        alumno = Alumno("Juan", legajo=123, edad=20, mail="juan@example.com")
        materia.agregar_alumno(alumno)
        # Obtener la lista de alumnos de la materia
        alumnos = materia.obtener_alumnos()
        # Verificar que el alumno se agregó correctamente
        self.assertIn(alumno, alumnos)

class TestProfesor(unittest.TestCase):
    def test_nombre(self):
        self.assertEqual(profesor.obtener_nombre(), "Daniel")

    def test_legajo(self):
        self.assertEqual(profesor.obtener_legajo(), 1234)


if __name__ == "__main__":
    unittest.main()