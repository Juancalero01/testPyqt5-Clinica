from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegistroMedico(object):
    def setupUi(self, RegistrarMedico):
        RegistrarMedico.setObjectName("RegistrarMedico")
        RegistrarMedico.resize(350, 450)
        RegistrarMedico.setMinimumSize(QtCore.QSize(350, 450))
        RegistrarMedico.setMaximumSize(QtCore.QSize(350, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "Views/Icons/iconPrincipal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RegistrarMedico.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(RegistrarMedico)
        self.centralwidget.setObjectName("centralwidget")
        self.txtNombreMedico = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombreMedico.setGeometry(QtCore.QRect(20, 20, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.txtNombreMedico.setFont(font)
        self.txtNombreMedico.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtNombreMedico.setStyleSheet("")
        self.txtNombreMedico.setMaxLength(50)
        self.txtNombreMedico.setAlignment(QtCore.Qt.AlignCenter)
        self.txtNombreMedico.setClearButtonEnabled(True)
        self.txtNombreMedico.setObjectName("txtNombreMedico")
        self.txtApellidoMedico = QtWidgets.QLineEdit(self.centralwidget)
        self.txtApellidoMedico.setGeometry(QtCore.QRect(20, 90, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.txtApellidoMedico.setFont(font)
        self.txtApellidoMedico.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtApellidoMedico.setStyleSheet("")
        self.txtApellidoMedico.setMaxLength(50)
        self.txtApellidoMedico.setAlignment(QtCore.Qt.AlignCenter)
        self.txtApellidoMedico.setClearButtonEnabled(True)
        self.txtApellidoMedico.setObjectName("txtApellidoMedico")
        self.txtDocumentoMedico = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDocumentoMedico.setGeometry(QtCore.QRect(20, 160, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.txtDocumentoMedico.setFont(font)
        self.txtDocumentoMedico.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtDocumentoMedico.setStyleSheet("")
        self.txtDocumentoMedico.setMaxLength(8)
        self.txtDocumentoMedico.setAlignment(QtCore.Qt.AlignCenter)
        self.txtDocumentoMedico.setClearButtonEnabled(True)
        self.txtDocumentoMedico.setObjectName("txtDocumentoMedico")
        self.dateMedico = QtWidgets.QDateEdit(self.centralwidget)
        self.dateMedico.setGeometry(QtCore.QRect(20, 230, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.dateMedico.setFont(font)
        self.dateMedico.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateMedico.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dateMedico.setStyleSheet("")
        self.dateMedico.setAlignment(QtCore.Qt.AlignCenter)
        self.dateMedico.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateMedico.setCalendarPopup(True)
        self.dateMedico.setObjectName("dateMedico")
        self.btnRegistrarMedico = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegistrarMedico.setGeometry(QtCore.QRect(220, 370, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnRegistrarMedico.setFont(font)
        self.btnRegistrarMedico.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegistrarMedico.setStyleSheet("QPushButton{\n"
                                              "background: #0090D9;\n"
                                              "border:none;\n"
                                              "border-radius: 5px;\n"
                                              "color: #fff;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "background: #0089D7;\n"
                                              "}\n"
                                              "")
        self.btnRegistrarMedico.setObjectName("btnRegistrarMedico")
        self.btnCancelarMedico = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelarMedico.setGeometry(QtCore.QRect(110, 370, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnCancelarMedico.setFont(font)
        self.btnCancelarMedico.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancelarMedico.setStyleSheet("QPushButton{\n"
                                             "background: #F14242;\n"
                                             "border:none;\n"
                                             "border-radius: 5px;\n"
                                             "color: #fff\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "background: #ED4D4D;\n"
                                             "}")
        self.btnCancelarMedico.setObjectName("btnCancelarMedico")
        self.cmbMedico = QtWidgets.QComboBox(self.centralwidget)
        self.cmbMedico.setGeometry(QtCore.QRect(20, 300, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.cmbMedico.setFont(font)
        self.cmbMedico.setWhatsThis("")
        self.cmbMedico.setStyleSheet("")
        self.cmbMedico.setEditable(False)
        self.cmbMedico.setInsertPolicy(
            QtWidgets.QComboBox.InsertAlphabetically)
        self.cmbMedico.setIconSize(QtCore.QSize(16, 16))
        self.cmbMedico.setDuplicatesEnabled(False)
        self.cmbMedico.setFrame(True)
        self.cmbMedico.setObjectName("cmbMedico")
        self.cmbMedico.addItem("Seleccionar especialidad")
        RegistrarMedico.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegistrarMedico)
        QtCore.QMetaObject.connectSlotsByName(RegistrarMedico)

    def retranslateUi(self, RegistrarMedico):
        _translate = QtCore.QCoreApplication.translate
        RegistrarMedico.setWindowTitle(_translate(
            "RegistrarMedico", "Registrar Medico"))
        self.txtNombreMedico.setPlaceholderText(
            _translate("RegistrarMedico", " INGRESE EL NOMBRE"))
        self.txtApellidoMedico.setPlaceholderText(
            _translate("RegistrarMedico", " INGRESE EL APELLIDO"))
        self.txtDocumentoMedico.setPlaceholderText(_translate(
            "RegistrarMedico", " INGRESE EL NUMERO DE DOCUMENTO"))
        self.dateMedico.setDisplayFormat(
            _translate("RegistrarMedico", "yyyy/MM/dd"))
        self.btnRegistrarMedico.setText(
            _translate("RegistrarMedico", "REGISTRAR"))
        self.btnCancelarMedico.setText(
            _translate("RegistrarMedico", "CANCELAR"))
        self.cmbMedico.setPlaceholderText(
            _translate("RegistrarMedico", "Seleccione"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegistrarMedico = QtWidgets.QMainWindow()
    ui = Ui_RegistroMedico()
    ui.setupUi(RegistrarMedico)
    RegistrarMedico.show()
    sys.exit(app.exec_())
