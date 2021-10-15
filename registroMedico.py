from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from Views.registroMedicos import Ui_RegistroMedico
from medico import Medico
from PyQt5.QtWidgets import QMessageBox


class RegistroMedico(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegistroMedico()
        self.ui.setupUi(self)
        self.datos = Medico()
        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle("Mensaje")

        # VISTA REGISTRO MEDICO
        self.ui.btnRegistrarMedico.clicked.connect(self.registrarDatos)
        self.ui.btnCancelarMedico.clicked.connect(self.cancelarDatos)
        self.mostrarEspecialidad()

    def registrarDatos(self):
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
            self.datos.registrarMedico(
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
