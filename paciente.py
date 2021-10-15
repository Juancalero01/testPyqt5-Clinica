import conexion as conn

db = conn.DataBase()


class Paciente():
    def registrarPaciente(self, nombre, apellido, documento, obraSocial, fechaNacimiento):
        sql = """
        INSERT INTO PACIENTES (NOMBRE,APELLIDO,DOCUMENTO,OBRA_SOCIAL,FECHA_NACIMIENTO)
        VALUES ('{}','{}','{}','{}','{}')
        """.format(nombre, apellido, documento, obraSocial, fechaNacimiento)
        db.consulta(sql)

    def modificarPaciente(self, nombre, apellido, documento, obraSocial, fechaNacimiento):
        sql = """
        UPDATE PACIENTES SET NOMBRE = '{}', APELLIDO = '{}', OBRA_SOCIAL = '{}', FECHA_NACIMIENTO = '{}'
        WHERE DOCUMENTO = '{}'
        """.format(nombre, apellido, obraSocial, fechaNacimiento, documento)
        db.consulta(sql)

    def eliminarPaciente(self): pass

    def mostrarPaciente(self):
        sql = """
        SELECT * FROM PACIENTES
        """
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def buscarPaciente(self, documento):
        sql = """
        SELECT * FROM PACIENTES 
        WHERE DOCUMENTO = '{}'
        """.format(documento)
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def mostrarObraSocial(self):
        sql = """
        SELECT NOMBRE FROM OBRA_SOCIAL
        """
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos
