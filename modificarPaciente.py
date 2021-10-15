from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from Views.modificarPacientes import Ui_ModificarPaciente
from paciente import Paciente
from PyQt5.QtWidgets import QMessageBox


class ModificarPaciente(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ModificarPaciente()
        self.ui.setupUi(self)
        self.datos = Paciente()
        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle("Mensaje")

        # VISTA MODIFICAR PACIENTE
        self.ui.btnActualizarPaciente.clicked.connect(self.actualizarDatos)
        self.ui.btnCancelarPaciente.clicked.connect(self.cancelarDatos)
        self.mostrarObraSocial()

    def traerDatos(self, datos):
        self.ui.txtNombrePaciente.setText(datos[0])
        self.ui.txtApellidoPaciente.setText(datos[1])
        self.ui.txtDocumentoPaciente.setText(datos[2])
        fecha = datos[4]
        anio = fecha[0:4]
        mes = fecha[5:7]
        dia = fecha[8:10]
        self.ui.datePaciente.setDate(QDate(int(anio), int(mes), int(dia)))
        contador = self.ui.cmbPaciente.count()
        for i in range(0, contador):
            self.ui.cmbPaciente.setCurrentIndex(i)
            obraSocial = self.ui.cmbPaciente.currentText()
            if obraSocial == datos[3]:
                self.ui.cmbPaciente.setCurrentIndex(i)
                break

    def actualizarDatos(self):
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
        elif nombre != "" and apellido != "" and documento != "" and fechaNacimiento != "" and obraSocial != "":
            self.datos.modificarPaciente(
                nombre, apellido, documento, obraSocial, fechaNacimiento)
            self.mensaje.setText(
                "Paciente modificado!")
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
