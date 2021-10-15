from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from Views.modificarMedicos import Ui_ModificarMedico
from medico import Medico
from PyQt5.QtWidgets import QMessageBox


class ModificarMedico(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ModificarMedico()
        self.ui.setupUi(self)
        self.datos = Medico()
        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle("Mensaje")

        # VISTA MODIFICAR PACIENTE
        self.ui.btnActualizarMedico.clicked.connect(self.actualizarDatos)
        self.ui.btnCancelarMedico.clicked.connect(self.cancelarDatos)
        self.mostrarEspecialidad()

    def traerDatos(self, datos):
        self.ui.txtNombreMedico.setText(datos[0])
        self.ui.txtApellidoMedico.setText(datos[1])
        self.ui.txtDocumentoMedico.setText(datos[2])
        fecha = datos[4]
        anio = fecha[0:4]
        mes = fecha[5:7]
        dia = fecha[8:10]
        self.ui.dateMedico.setDate(QDate(int(anio), int(mes), int(dia)))
        contador = self.ui.cmbMedico.count()
        for i in range(0, contador):
            self.ui.cmbMedico.setCurrentIndex(i)
            especialidad = self.ui.cmbMedico.currentText()
            if especialidad == datos[3]:
                self.ui.cmbMedico.setCurrentIndex(i)
                break

    def actualizarDatos(self):
        nombre = self.ui.txtNombreMedico.text().capitalize()
        apellido = self.ui.txtApellidoMedico.text().capitalize()
        documento = self.ui.txtDocumentoMedico.text()
        fechaNacimiento = self.ui.dateMedico.text()
        especialidad = self.ui.cmbMedico.currentText()
        if len(nombre) == 0 or len(apellido) == 0 or len(documento) == 0 or len(fechaNacimiento) == 0 or especialidad == "Seleccionar especialidad":
            self.mensaje.setText(
                "Compruebe si todos los campos estan completos!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
        elif nombre != "" and apellido != "" and documento != "" and fechaNacimiento != "" and especialidad != "Seleccionar especialidad":
            self.datos.modificarMedico(
                nombre, apellido, documento, especialidad, fechaNacimiento)
            self.mensaje.setText(
                "Medico registrado!")
            self.mensaje.setIcon(QMessageBox.Information)
            x = self.mensaje.exec_()
            self.ui.txtNombreMedico.clear()
            self.ui.txtApellidoMedico.clear()
            self.ui.txtDocumentoMedico.clear()
            self.ui.dateMedico.setDate(QDate(2000, 1, 1))
            self.ui.cmbMedico.setCurrentIndex(0)

    def cancelarDatos(self):
        self.ui.txtNombreMedico.clear()
        self.ui.txtApellidoMedico.clear()
        self.ui.txtDocumentoMedico.clear()
        self.ui.dateMedico.setDate(QDate(2000, 1, 1))
        self.ui.cmbMedico.setCurrentIndex(0)

    def mostrarEspecialidad(self):
        datos = self.datos.mostrarEspecialidad()
        for i in datos:
            self.ui.cmbMedico.addItem(i[0])
