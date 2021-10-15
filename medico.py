import conexion as conn

db = conn.DataBase()


class Medico():
    def registrarMedico(self, nombre, apellido, documento, especialidad, fechaNacimiento):
        sql = """
        INSERT INTO MEDICOS (NOMBRE,APELLIDO,DOCUMENTO,ESPECIALIDAD,FECHA_NACIMIENTO)
        VALUES ('{}','{}','{}','{}','{}')
        """.format(nombre, apellido, documento, especialidad, fechaNacimiento)
        db.consulta(sql)

    def modificarMedico(self, nombre, apellido, documento, especialidad, fechaNacimiento):
        sql = """
        UPDATE MEDICOS SET NOMBRE = '{}', APELLIDO = '{}', ESPECIALIDAD = '{}', FECHA_NACIMIENTO = '{}'
        WHERE DOCUMENTO = '{}'
        """.format(nombre, apellido, especialidad, fechaNacimiento, documento)
        db.consulta(sql)

    def eliminarMedico(): pass

    def mostrarMedico(self):
        sql = """
        SELECT * FROM MEDICOS
        """
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def buscarMedico(self, especialidad):
        sql = """
        SELECT * FROM MEDICOS
        WHERE ESPECIALIDAD = '{}'
        """.format(especialidad)
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def mostrarEspecialidad(self):
        sql = """
        SELECT NOMBRE FROM ESPECIALIDAD
        """
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos
