from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from Views.registroPacientes import Ui_RegistroPaciente
from paciente import Paciente
from PyQt5.QtWidgets import QMessageBox


class RegistroPaciente(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegistroPaciente()
        self.ui.setupUi(self)
        self.datos = Paciente()
        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle("Mensaje")

        # VISTA REGISTRO PACIENTE
        self.ui.btnRegistrarPaciente.clicked.connect(self.registrarDatos)
        self.ui.btnCancelarPaciente.clicked.connect(self.cancelarDatos)
        self.mostrarObraSocial()

    def registrarDatos(self):
        nombre = self.ui.txtNombrePaciente.text().capitalize()
        apellido = self.ui.txtApellidoPaciente.text().capitalize()
        documento = self.ui.txtDocumentoPaciente.text()
        fechaNacimiento = self.ui.datePaciente.text()
        obraSocial = self.ui.cmbPaciente.currentText()
        if len(nombre) == 0 or len(apellido) == 0 or len(documento) == 0 or len(fechaNacimiento) == 0 or obraSocial == "Seleccionar obra social":
            self.mensaje.setText(
                "Compruebe si todos los campos estan completos!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
        elif nombre != "" and apellido != "" and documento != "" and fechaNacimiento != "" and obraSocial != "Seleccionar obra social":
            self.datos.registrarPaciente(
                nombre, apellido, documento, obraSocial, fechaNacimiento)
            self.mensaje.setText(
                "Paciente registrado!")
            self.mensaje.setIcon(QMessageBox.Information)
            x = self.mensaje.exec_()
            self.ui.txtNombrePaciente.clear()
            self.ui.txtApellidoPaciente.clear()
            self.ui.txtDocumentoPaciente.clear()
            self.ui.datePaciente.setDate(QDate(2000, 1, 1))
            self.ui.cmbPaciente.setCurrentIndex(0)

    def cancelarDatos(self):
        self.ui.txtNombrePaciente.clear()
        self.ui.txtApellidoPaciente.clear()
        self.ui.txtDocumentoPaciente.clear()
        self.ui.datePaciente.setDate(QDate(2000, 1, 1))
        self.ui.cmbPaciente.setCurrentIndex(0)

    def mostrarObraSocial(self):
        datos = self.datos.mostrarObraSocial()
        for i in datos:
            self.ui.cmbPaciente.addItem(i[0])
