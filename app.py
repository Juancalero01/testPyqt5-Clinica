import sys
import webbrowser as wb
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Views.principal import Ui_Principal
from modificarMedico import ModificarMedico
from registroPaciente import RegistroPaciente
from modificarPaciente import ModificarPaciente
from registroMedico import RegistroMedico
from paciente import Paciente
from medico import Medico


class PrincipalApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        self.datosPaciente = Paciente()
        self.datosMedico = Medico()
        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle("Mensaje")

        # BOTONES DEL MENU
        self.ui.btnInicio.clicked.connect(
            lambda: self.ui.stkPages.setCurrentWidget(self.ui.inicioPage))
        self.ui.btnPaciente.clicked.connect(
            lambda: self.ui.stkPages.setCurrentWidget(self.ui.pacientePage))
        self.ui.btnMedico.clicked.connect(
            lambda: self.ui.stkPages.setCurrentWidget(self.ui.medicoPage))
        self.ui.btnCita.clicked.connect(
            lambda: self.ui.stkPages.setCurrentWidget(self.ui.citaPage))
        self.ui.btnGitHub.clicked.connect(self.abrirGitHub)
        # VISTA PACIENTE
        self.ui.btnAgregarPaciente.clicked.connect(self.abrirRegistroPaciente)
        self.ui.btnEditarPaciente.clicked.connect(self.abrirModificarPaciente)
        self.ui.btnBuscarPaciente.clicked.connect(self.buscarPaciente)
        self.mostrarPaciente()
        # PROXIMAMENTE
        self.ui.btnEliminarPaciente.clicked.connect(self.eliminarPaciente)

        # VISTA MEDICO
        self.ui.btnAgregarMedico.clicked.connect(self.abrirRegistroMedico)
        self.ui.btnEditarMedico.clicked.connect(self.abrirModificarMedico)
        self.ui.btnBuscarMedico.clicked.connect(self.buscarMedico)
        self.mostrarMedico()
        self.mostrarEspecialidad()
        # PROXIMAMENTE
        self.ui.btnEliminarMedico.clicked.connect(self.eliminarMedico)

    # FUNCIONES ESTANDAR

    def abrirGitHub(self):
        wb.open("https://github.com/Juancalero01")

    # FUNCIONES VISTA PACIENTE

    def abrirRegistroPaciente(self):
        self.window = RegistroPaciente()
        self.window.show()

    def abrirModificarPaciente(self):
        seleccion = self.ui.tblPaciente.selectedItems()
        if seleccion == []:
            self.mensaje.setText(
                "Selecciona la fila para modificar!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
        elif seleccion != []:
            seleccion = [dato.text() for dato in seleccion]
            self.window = ModificarPaciente()
            self.window.show()
            self.window.traerDatos(seleccion)
            self.ui.tblPaciente.clearSelection()

    def mostrarPaciente(self):
        datos = self.datosPaciente.mostrarPaciente()
        i = len(datos)
        self.ui.tblPaciente.setRowCount(i)
        filaTabla = 0
        for fila in datos:
            self.ui.tblPaciente.setItem(
                filaTabla, 0, QtWidgets.QTableWidgetItem(fila[1]))
            self.ui.tblPaciente.setItem(
                filaTabla, 1, QtWidgets.QTableWidgetItem(fila[2]))
            self.ui.tblPaciente.setItem(
                filaTabla, 2, QtWidgets.QTableWidgetItem(fila[3]))
            self.ui.tblPaciente.setItem(
                filaTabla, 3, QtWidgets.QTableWidgetItem(fila[4]))
            self.ui.tblPaciente.setItem(
                filaTabla, 4, QtWidgets.QTableWidgetItem(fila[5]))
            filaTabla += 1

    def buscarPaciente(self):
        documento = self.ui.txtBuscarPaciente.text()
        if len(documento) == 0:
            self.mostrarPaciente()
        elif len(documento) == 8:
            datos = self.datosPaciente.buscarPaciente(documento)
            i = len(datos)
            self.ui.tblPaciente.setRowCount(i)
            filaTabla = 0
            for fila in datos:
                self.ui.tblPaciente.setItem(
                    filaTabla, 0, QtWidgets.QTableWidgetItem(fila[1]))
                self.ui.tblPaciente.setItem(
                    filaTabla, 1, QtWidgets.QTableWidgetItem(fila[2]))
                self.ui.tblPaciente.setItem(
                    filaTabla, 2, QtWidgets.QTableWidgetItem(fila[3]))
                self.ui.tblPaciente.setItem(
                    filaTabla, 3, QtWidgets.QTableWidgetItem(fila[4]))
                self.ui.tblPaciente.setItem(
                    filaTabla, 4, QtWidgets.QTableWidgetItem(fila[5]))
                filaTabla += 1

    def eliminarPaciente(): pass

    # FUNCIONES VISTA MEDICO
    def abrirRegistroMedico(self):
        self.window = RegistroMedico()
        self.window.show()

    def abrirModificarMedico(self):
        seleccion = self.ui.tblMedico.selectedItems()
        if seleccion == []:
            self.mensaje.setText(
                "Selecciona la fila para modificar!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
        elif seleccion != []:
            seleccion = [dato.text() for dato in seleccion]
            self.window = ModificarMedico()
            self.window.show()
            self.window.traerDatos(seleccion)
            self.ui.tblMedico.clearSelection()

    def mostrarMedico(self):
        datos = self.datosMedico.mostrarMedico()
        i = len(datos)
        self.ui.tblMedico.setRowCount(i)
        filaTabla = 0
        for fila in datos:
            self.ui.tblMedico.setItem(
                filaTabla, 0, QtWidgets.QTableWidgetItem(fila[1]))
            self.ui.tblMedico.setItem(
                filaTabla, 1, QtWidgets.QTableWidgetItem(fila[2]))
            self.ui.tblMedico.setItem(
                filaTabla, 2, QtWidgets.QTableWidgetItem(fila[3]))
            self.ui.tblMedico.setItem(
                filaTabla, 3, QtWidgets.QTableWidgetItem(fila[4]))
            self.ui.tblMedico.setItem(
                filaTabla, 4, QtWidgets.QTableWidgetItem(fila[5]))
            filaTabla += 1

    def mostrarEspecialidad(self):
        datos = self.datosMedico.mostrarEspecialidad()
        for i in datos:
            self.ui.cmbMedico.addItem(i[0])

    def buscarMedico(self):
        especialidad = self.ui.cmbMedico.currentText()
        if especialidad == "Seleccionar especialidad":
            self.mostrarMedico()
        elif especialidad != "Seleccionar especialidad":
            datos = self.datosMedico.buscarMedico(especialidad)
            i = len(datos)
            self.ui.tblMedico.setRowCount(i)
            filaTabla = 0
            for fila in datos:
                self.ui.tblMedico.setItem(
                    filaTabla, 0, QtWidgets.QTableWidgetItem(fila[1]))
                self.ui.tblMedico.setItem(
                    filaTabla, 1, QtWidgets.QTableWidgetItem(fila[2]))
                self.ui.tblMedico.setItem(
                    filaTabla, 2, QtWidgets.QTableWidgetItem(fila[3]))
                self.ui.tblMedico.setItem(
                    filaTabla, 3, QtWidgets.QTableWidgetItem(fila[4]))
                self.ui.tblMedico.setItem(
                    filaTabla, 4, QtWidgets.QTableWidgetItem(fila[5]))
                filaTabla += 1

    def eliminarMedico(): pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    windows = PrincipalApp()
    windows.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
