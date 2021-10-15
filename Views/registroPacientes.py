from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegistroPaciente(object):
    def setupUi(self, RegistroPaciente):
        RegistroPaciente.setObjectName("RegistroPaciente")
        RegistroPaciente.resize(350, 450)
        RegistroPaciente.setMinimumSize(QtCore.QSize(350, 450))
        RegistroPaciente.setMaximumSize(QtCore.QSize(350, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Views/Icons/iconPrincipal.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RegistroPaciente.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(RegistroPaciente)
        self.centralwidget.setObjectName("centralwidget")
        self.txtNombrePaciente = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombrePaciente.setGeometry(QtCore.QRect(20, 20, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.txtNombrePaciente.setFont(font)
        self.txtNombrePaciente.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtNombrePaciente.setStyleSheet("")
        self.txtNombrePaciente.setMaxLength(50)
        self.txtNombrePaciente.setAlignment(QtCore.Qt.AlignCenter)
        self.txtNombrePaciente.setClearButtonEnabled(True)
        self.txtNombrePaciente.setObjectName("txtNombrePaciente")
        self.txtApellidoPaciente = QtWidgets.QLineEdit(self.centralwidget)
        self.txtApellidoPaciente.setGeometry(QtCore.QRect(20, 90, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.txtApellidoPaciente.setFont(font)
        self.txtApellidoPaciente.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtApellidoPaciente.setStyleSheet("")
        self.txtApellidoPaciente.setMaxLength(50)
        self.txtApellidoPaciente.setAlignment(QtCore.Qt.AlignCenter)
        self.txtApellidoPaciente.setClearButtonEnabled(True)
        self.txtApellidoPaciente.setObjectName("txtApellidoPaciente")
        self.txtDocumentoPaciente = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDocumentoPaciente.setGeometry(QtCore.QRect(20, 160, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.txtDocumentoPaciente.setFont(font)
        self.txtDocumentoPaciente.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtDocumentoPaciente.setStyleSheet("")
        self.txtDocumentoPaciente.setMaxLength(8)
        self.txtDocumentoPaciente.setAlignment(QtCore.Qt.AlignCenter)
        self.txtDocumentoPaciente.setClearButtonEnabled(True)
        self.txtDocumentoPaciente.setObjectName("txtDocumentoPaciente")
        self.datePaciente = QtWidgets.QDateEdit(self.centralwidget)
        self.datePaciente.setGeometry(QtCore.QRect(20, 230, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.datePaciente.setFont(font)
        self.datePaciente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.datePaciente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.datePaciente.setStyleSheet("")
        self.datePaciente.setAlignment(QtCore.Qt.AlignCenter)
        self.datePaciente.setCurrentSection(
            QtWidgets.QDateTimeEdit.YearSection)
        self.datePaciente.setCalendarPopup(True)
        self.datePaciente.setObjectName("datePaciente")
        self.btnRegistrarPaciente = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegistrarPaciente.setGeometry(QtCore.QRect(220, 370, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnRegistrarPaciente.setFont(font)
        self.btnRegistrarPaciente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegistrarPaciente.setStyleSheet("QPushButton{\n"
                                                "background: #0090D9;\n"
                                                "border:none;\n"
                                                "border-radius: 5px;\n"
                                                "color: #fff;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "background: #0089D7;\n"
                                                "}\n"
                                                "")
        self.btnRegistrarPaciente.setObjectName("btnRegistrarPaciente")
        self.btnCancelarPaciente = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelarPaciente.setGeometry(QtCore.QRect(110, 370, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnCancelarPaciente.setFont(font)
        self.btnCancelarPaciente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancelarPaciente.setStyleSheet("QPushButton{\n"
                                               "background: #F14242;\n"
                                               "border:none;\n"
                                               "border-radius: 5px;\n"
                                               "color: #fff\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "background: #ED4D4D;\n"
                                               "}")
        self.btnCancelarPaciente.setObjectName("btnCancelarPaciente")
        self.cmbPaciente = QtWidgets.QComboBox(self.centralwidget)
        self.cmbPaciente.setGeometry(QtCore.QRect(20, 300, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.cmbPaciente.setFont(font)
        self.cmbPaciente.setWhatsThis("")
        self.cmbPaciente.setStyleSheet("")
        self.cmbPaciente.setEditable(False)
        self.cmbPaciente.setInsertPolicy(
            QtWidgets.QComboBox.InsertAlphabetically)
        self.cmbPaciente.setIconSize(QtCore.QSize(16, 16))
        self.cmbPaciente.setDuplicatesEnabled(False)
        self.cmbPaciente.setFrame(True)
        self.cmbPaciente.addItem("Seleccionar obra social")
        self.cmbPaciente.setObjectName("cmbPaciente")
        RegistroPaciente.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegistroPaciente)
        QtCore.QMetaObject.connectSlotsByName(RegistroPaciente)

    def retranslateUi(self, RegistroPaciente):
        _translate = QtCore.QCoreApplication.translate
        RegistroPaciente.setWindowTitle(_translate(
            "RegistroPaciente", "Registrar Paciente"))
        self.txtNombrePaciente.setPlaceholderText(
            _translate("RegistroPaciente", " INGRESE EL NOMBRE"))
        self.txtApellidoPaciente.setPlaceholderText(
            _translate("RegistroPaciente", " INGRESE EL APELLIDO"))
        self.txtDocumentoPaciente.setPlaceholderText(_translate(
            "RegistroPaciente", " INGRESE EL NUMERO DE DOCUMENTO"))
        self.datePaciente.setDisplayFormat(
            _translate("RegistroPaciente", "yyyy/MM/dd"))
        self.btnRegistrarPaciente.setText(
            _translate("RegistroPaciente", "REGISTRAR"))
        self.btnCancelarPaciente.setText(
            _translate("RegistroPaciente", "CANCELAR"))
        self.cmbPaciente.setPlaceholderText(
            _translate("RegistroPaciente", "Seleccione"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegistroPaciente = QtWidgets.QMainWindow()
    ui = Ui_RegistroPaciente()
    ui.setupUi(RegistroPaciente)
    RegistroPaciente.show()
    sys.exit(app.exec_())
