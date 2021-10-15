from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principal(object):
    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(1000, 600)
        Principal.setMinimumSize(QtCore.QSize(1000, 600))
        Principal.setMaximumSize(QtCore.QSize(1000, 600))
        Principal.setTabletTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Views/icons/iconPrincipal.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Principal.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.frmSidebar = QtWidgets.QFrame(self.centralwidget)
        self.frmSidebar.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.frmSidebar.setStyleSheet("QFrame{\n"
                                      "background: #FFF;\n"
                                      "}")
        self.frmSidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmSidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmSidebar.setObjectName("frmSidebar")
        self.btnCita = QtWidgets.QPushButton(self.frmSidebar)
        self.btnCita.setGeometry(QtCore.QRect(250, 0, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnCita.setFont(font)
        self.btnCita.setStyleSheet("QPushButton{\n"
                                   "background: #FFF;\n"
                                   "border: none;\n"
                                   "text-align: left;\n"
                                   "color: #000\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background: #0089D7;\n"
                                   "color: #FFF\n"
                                   "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Views/icons/iconCitas.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCita.setIcon(icon1)
        self.btnCita.setIconSize(QtCore.QSize(50, 50))
        self.btnCita.setCheckable(False)
        self.btnCita.setObjectName("btnCita")
        self.btnMedico = QtWidgets.QPushButton(self.frmSidebar)
        self.btnMedico.setEnabled(True)
        self.btnMedico.setGeometry(QtCore.QRect(500, 0, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnMedico.setFont(font)
        self.btnMedico.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnMedico.setAutoFillBackground(False)
        self.btnMedico.setStyleSheet("QPushButton{\n"
                                     "background: #FFF;\n"
                                     "border: none;\n"
                                     "text-align: left;\n"
                                     "color: #000\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background: #0089D7;\n"
                                     "color: #FFF\n"
                                     "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Views/icons/iconDoctor.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMedico.setIcon(icon2)
        self.btnMedico.setIconSize(QtCore.QSize(50, 50))
        self.btnMedico.setCheckable(False)
        self.btnMedico.setAutoRepeat(False)
        self.btnMedico.setAutoExclusive(False)
        self.btnMedico.setAutoDefault(False)
        self.btnMedico.setFlat(False)
        self.btnMedico.setObjectName("btnMedico")
        self.btnPaciente = QtWidgets.QPushButton(self.frmSidebar)
        self.btnPaciente.setGeometry(QtCore.QRect(750, 0, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnPaciente.setFont(font)
        self.btnPaciente.setStyleSheet("QPushButton{\n"
                                       "background: #FFF;\n"
                                       "border: none;\n"
                                       "text-align: left;\n"
                                       "color: #000\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background: #0089D7;\n"
                                       "color: #FFF\n"
                                       "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Views/icons/iconPaciente.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPaciente.setIcon(icon3)
        self.btnPaciente.setIconSize(QtCore.QSize(50, 50))
        self.btnPaciente.setObjectName("btnPaciente")
        self.btnInicio = QtWidgets.QPushButton(self.frmSidebar)
        self.btnInicio.setGeometry(QtCore.QRect(0, 0, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnInicio.setFont(font)
        self.btnInicio.setStyleSheet("QPushButton{\n"
                                     "background: #FFF;\n"
                                     "border: none;\n"
                                     "text-align: left;\n"
                                     "color: #000;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background: #0089D7;\n"
                                     "color: #FFF\n"
                                     "}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Views/icons/iconInicio.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInicio.setIcon(icon4)
        self.btnInicio.setIconSize(QtCore.QSize(50, 50))
        self.btnInicio.setObjectName("btnInicio")
        self.lineSeparador = QtWidgets.QFrame(self.frmSidebar)
        self.lineSeparador.setGeometry(QtCore.QRect(0, 50, 1000, 16))
        self.lineSeparador.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSeparador.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSeparador.setObjectName("lineSeparador")
        self.frmBody = QtWidgets.QFrame(self.centralwidget)
        self.frmBody.setGeometry(QtCore.QRect(0, 60, 1000, 590))
        self.frmBody.setStyleSheet("QFrame{\n"
                                   "background: #FFF;\n"
                                   "}")
        self.frmBody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmBody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmBody.setObjectName("frmBody")
        self.stkPages = QtWidgets.QStackedWidget(self.frmBody)
        self.stkPages.setGeometry(QtCore.QRect(0, -20, 1000, 620))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.stkPages.setFont(font)
        self.stkPages.setStyleSheet("QStackedWidget{\n"
                                    "background: #FFF;\n"
                                    "border: none;\n"
                                    "border-radius: 5px;\n"
                                    "color: #000\n"
                                    "}")
        self.stkPages.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stkPages.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stkPages.setLineWidth(1)
        self.stkPages.setObjectName("stkPages")
        self.inicioPage = QtWidgets.QWidget()
        self.inicioPage.setObjectName("inicioPage")
        self.imgInicio = QtWidgets.QLabel(self.inicioPage)
        self.imgInicio.setGeometry(QtCore.QRect(0, 20, 1000, 600))
        self.imgInicio.setText("")
        self.imgInicio.setPixmap(QtGui.QPixmap("Views/Logo/logo.PNG"))
        self.imgInicio.setAlignment(QtCore.Qt.AlignCenter)
        self.imgInicio.setObjectName("imgInicio")
        self.btnGitHub = QtWidgets.QPushButton(self.inicioPage)
        self.btnGitHub.setObjectName(u"btnGitHub")
        self.btnGitHub.setEnabled(True)
        self.btnGitHub.setGeometry(QtCore.QRect(970, 530, 31, 31))
        self.btnGitHub.setFont(font)
        self.btnGitHub.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGitHub.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnGitHub.setAutoFillBackground(False)
        self.btnGitHub.setStyleSheet(u"QPushButton{\n"
                                     "background: #000;\n"
                                     "border-radius: 3px;\n"
                                     "color: #000\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background: #d74b64;\n"
                                     "color: #FFF\n"
                                     "}")
        icon10 = QtGui.QIcon()
        icon10.addFile(u"Views/Icons/iconGitHub.png",
                       QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGitHub.setIcon(icon10)
        self.btnGitHub.setIconSize(QtCore.QSize(50, 50))
        self.btnGitHub.setCheckable(False)
        self.btnGitHub.setAutoRepeat(False)
        self.btnGitHub.setAutoExclusive(False)
        self.btnGitHub.setAutoDefault(False)
        self.btnGitHub.setFlat(False)
        self.stkPages.addWidget(self.inicioPage)
        self.medicoPage = QtWidgets.QWidget()
        self.medicoPage.setObjectName("medicoPage")
        self.btnAgregarMedico = QtWidgets.QPushButton(self.medicoPage)
        self.btnAgregarMedico.setGeometry(QtCore.QRect(910, 80, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btnAgregarMedico.setFont(font)
        self.btnAgregarMedico.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAgregarMedico.setStyleSheet("QPushButton{\n"
                                            "background: #07CD1B;\n"
                                            "border:none;\n"
                                            "border-radius: 5px;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "background: #21D233;\n"
                                            "color: #000\n"
                                            "}\n"
                                            "")
        self.btnAgregarMedico.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Views/icons/iconAñadir.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAgregarMedico.setIcon(icon5)
        self.btnAgregarMedico.setIconSize(QtCore.QSize(30, 30))
        self.btnAgregarMedico.setObjectName("btnAgregarMedico")
        self.btnEliminarMedico = QtWidgets.QPushButton(self.medicoPage)
        self.btnEliminarMedico.setGeometry(QtCore.QRect(770, 80, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btnEliminarMedico.setFont(font)
        self.btnEliminarMedico.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEliminarMedico.setStyleSheet("QPushButton{\n"
                                             "background: #F14242;\n"
                                             "border:none;\n"
                                             "border-radius: 5px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "background: #ED4D4D;\n"
                                             "color: #000\n"
                                             "}\n"
                                             "")
        self.btnEliminarMedico.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Views/icons/iconEliminar.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminarMedico.setIcon(icon6)
        self.btnEliminarMedico.setIconSize(QtCore.QSize(30, 30))
        self.btnEliminarMedico.setObjectName("btnEliminarMedico")
        self.btnEditarMedico = QtWidgets.QPushButton(self.medicoPage)
        self.btnEditarMedico.setGeometry(QtCore.QRect(840, 80, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btnEditarMedico.setFont(font)
        self.btnEditarMedico.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEditarMedico.setStyleSheet("QPushButton{\n"
                                           "background: #FAE73F;\n"
                                           "border:none;\n"
                                           "border-radius: 5px;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "background: #FDEB4C;\n"
                                           "color: #000\n"
                                           "}\n"
                                           "")
        self.btnEditarMedico.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Views/icons/iconEditar.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEditarMedico.setIcon(icon7)
        self.btnEditarMedico.setIconSize(QtCore.QSize(30, 30))
        self.btnEditarMedico.setObjectName("btnEditarMedico")
        self.btnBuscarMedico = QtWidgets.QPushButton(self.medicoPage)
        self.btnBuscarMedico.setGeometry(QtCore.QRect(320, 80, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btnBuscarMedico.setFont(font)
        self.btnBuscarMedico.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBuscarMedico.setStyleSheet("QPushButton{\n"
                                           "background: #0090D9;\n"
                                           "border:none;\n"
                                           "border-radius: 5px;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "background: #0089D7;\n"
                                           "color: #000\n"
                                           "}\n"
                                           "")
        self.btnBuscarMedico.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Views/icons/iconBuscar.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscarMedico.setIcon(icon8)
        self.btnBuscarMedico.setIconSize(QtCore.QSize(20, 20))
        self.btnBuscarMedico.setObjectName("btnBuscarMedico")
        self.tblMedico = QtWidgets.QTableWidget(self.medicoPage)
        self.tblMedico.setGeometry(QtCore.QRect(10, 150, 980, 400))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.tblMedico.setFont(font)
        self.tblMedico.setAutoFillBackground(False)
        self.tblMedico.setStyleSheet("QTableWidget{\n"
                                     "color: #000;\n"
                                     "border: none;\n"
                                     "}\n"
                                     "QHeaderView::section{\n"
                                     "background: #0089D7;\n"
                                     "border: none;\n"
                                     "padding: 10px;\n"
                                     "color: #fff;\n"
                                     "}\n"
                                     "")
        self.tblMedico.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblMedico.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblMedico.setTabKeyNavigation(False)
        self.tblMedico.setProperty("showDropIndicator", False)
        self.tblMedico.setDragEnabled(False)
        self.tblMedico.setDragDropOverwriteMode(False)
        self.tblMedico.setAlternatingRowColors(True)
        self.tblMedico.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tblMedico.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tblMedico.setShowGrid(True)
        self.tblMedico.setGridStyle(QtCore.Qt.SolidLine)
        self.tblMedico.setWordWrap(True)
        self.tblMedico.setCornerButtonEnabled(False)
        self.tblMedico.setRowCount(0)
        self.tblMedico.setObjectName("tblMedico")
        self.tblMedico.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        item.setFont(font)
        self.tblMedico.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        item.setFont(font)
        self.tblMedico.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        item.setFont(font)
        self.tblMedico.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        item.setFont(font)
        self.tblMedico.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        item.setFont(font)
        self.tblMedico.setHorizontalHeaderItem(4, item)
        self.tblMedico.horizontalHeader().setVisible(True)
        self.tblMedico.horizontalHeader().setCascadingSectionResizes(False)
        self.tblMedico.horizontalHeader().setDefaultSectionSize(190)
        self.tblMedico.horizontalHeader().setHighlightSections(False)
        self.tblMedico.horizontalHeader().setMinimumSectionSize(40)
        self.tblMedico.horizontalHeader().setSortIndicatorShown(False)
        self.tblMedico.horizontalHeader().setStretchLastSection(True)
        self.tblMedico.verticalHeader().setVisible(False)
        self.tblMedico.verticalHeader().setHighlightSections(True)
        self.tblMedico.verticalHeader().setSortIndicatorShown(False)
        self.tblMedico.verticalHeader().setStretchLastSection(False)
        self.btnAgendaMedico = QtWidgets.QPushButton(self.medicoPage)
        self.btnAgendaMedico.setGeometry(QtCore.QRect(700, 80, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btnAgendaMedico.setFont(font)
        self.btnAgendaMedico.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAgendaMedico.setStyleSheet("QPushButton{\n"
                                           "background: #0090D9;\n"
                                           "border:none;\n"
                                           "border-radius: 5px;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "background: #0089D7;\n"
                                           "color: #000\n"
                                           "}\n"
                                           "")
        self.btnAgendaMedico.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Views/icons/iconAgenda.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAgendaMedico.setIcon(icon9)
        self.btnAgendaMedico.setIconSize(QtCore.QSize(30, 30))
        self.btnAgendaMedico.setObjectName("btnAgendaMedico")
        self.cmbMedico = QtWidgets.QComboBox(self.medicoPage)
        self.cmbMedico.setGeometry(QtCore.QRect(10, 80, 300, 50))
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
        self.cmbMedico.setPlaceholderText("")
        self.cmbMedico.setDuplicatesEnabled(False)
        self.cmbMedico.setFrame(True)
        self.cmbMedico.setObjectName("cmbMedico")
        self.cmbMedico.addItem("Seleccionar especialidad")
        self.lblTituloMedico = QtWidgets.QLabel(self.medicoPage)
        self.lblTituloMedico.setGeometry(QtCore.QRect(10, 30, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.lblTituloMedico.setFont(font)
        self.lblTituloMedico.setStyleSheet("QLabel{\n"
                                           "background: transparent\n"
                                           "}")
        self.lblTituloMedico.setObjectName("lblTituloMedico")
        self.stkPages.addWidget(self.medicoPage)
        self.citaPage = QtWidgets.QWidget()
        self.citaPage.setObjectName("citaPage")
        self.stkPages.addWidget(self.citaPage)
        self.pacientePage = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pacientePage.setFont(font)
        self.pacientePage.setObjectName("pacientePage")
        self.txtBuscarPaciente = QtWidgets.QLineEdit(self.pacientePage)
        self.txtBuscarPaciente.setGeometry(QtCore.QRect(10, 80, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.txtBuscarPaciente.setFont(font)
        self.txtBuscarPaciente.setStyleSheet("")
        self.txtBuscarPaciente.setMaxLength(8)
        self.txtBuscarPaciente.setAlignment(QtCore.Qt.AlignCenter)
        self.txtBuscarPaciente.setClearButtonEnabled(True)
        self.txtBuscarPaciente.setObjectName("txtBuscarPaciente")
        self.tblPaciente = QtWidgets.QTableWidget(self.pacientePage)
        self.tblPaciente.setGeometry(QtCore.QRect(10, 150, 980, 400))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.tblPaciente.setFont(font)
        self.tblPaciente.setAutoFillBackground(False)
        self.tblPaciente.setStyleSheet("QTableWidget{\n"
                                       "color: #000;\n"
                                       "border: none;\n"
                                       "}\n"
                                       "QHeaderView::section{\n"
                                       "background: #0089D7;\n"
                                       "border: none;\n"
                                       "padding: 10px;\n"
                                       "color: #fff;\n"
                                       "}\n"
                                       "")
        self.tblPaciente.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblPaciente.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblPaciente.setTabKeyNavigation(False)
        self.tblPaciente.setProperty("showDropIndicator", False)
        self.tblPaciente.setDragEnabled(False)
        self.tblPaciente.setDragDropOverwriteMode(False)
        self.tblPaciente.setAlternatingRowColors(True)
        self.tblPaciente.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tblPaciente.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tblPaciente.setShowGrid(True)
        self.tblPaciente.setGridStyle(QtCore.Qt.SolidLine)
        self.tblPaciente.setWordWrap(True)
        self.tblPaciente.setCornerButtonEnabled(False)
        self.tblPaciente.setRowCount(0)
        self.tblPaciente.setObjectName("tblPaciente")
        self.tblPaciente.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        item.setFont(font)
        self.tblPaciente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        item.setFont(font)
        self.tblPaciente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        item.setFont(font)
        self.tblPaciente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        item.setFont(font)
        self.tblPaciente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        item.setFont(font)
        self.tblPaciente.setHorizontalHeaderItem(4, item)
        self.tblPaciente.horizontalHeader().setVisible(True)
        self.tblPaciente.horizontalHeader().setCascadingSectionResizes(False)
        self.tblPaciente.horizontalHeader().setDefaultSectionSize(190)
        self.tblPaciente.horizontalHeader().setHighlightSections(False)
        self.tblPaciente.horizontalHeader().setMinimumSectionSize(40)
        self.tblPaciente.horizontalHeader().setSortIndicatorShown(False)
        self.tblPaciente.horizontalHeader().setStretchLastSection(True)
        self.tblPaciente.verticalHeader().setVisible(False)
        self.tblPaciente.verticalHeader().setCascadingSectionResizes(False)
        self.tblPaciente.verticalHeader().setHighlightSections(True)
        self.tblPaciente.verticalHeader().setSortIndicatorShown(False)
        self.tblPaciente.verticalHeader().setStretchLastSection(False)
        self.btnBuscarPaciente = QtWidgets.QPushButton(self.pacientePage)
        self.btnBuscarPaciente.setGeometry(QtCore.QRect(320, 80, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btnBuscarPaciente.setFont(font)
        self.btnBuscarPaciente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBuscarPaciente.setStyleSheet("QPushButton{\n"
                                             "background: #0090D9;\n"
                                             "border:none;\n"
                                             "border-radius: 5px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "background: #0089D7;\n"
                                             "color: #000\n"
                                             "}\n"
                                             "")
        self.btnBuscarPaciente.setText("")
        self.btnBuscarPaciente.setIcon(icon8)
        self.btnBuscarPaciente.setIconSize(QtCore.QSize(20, 20))
        self.btnBuscarPaciente.setObjectName("btnBuscarPaciente")
        self.btnEliminarPaciente = QtWidgets.QPushButton(self.pacientePage)
        self.btnEliminarPaciente.setGeometry(QtCore.QRect(770, 80, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btnEliminarPaciente.setFont(font)
        self.btnEliminarPaciente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEliminarPaciente.setStyleSheet("QPushButton{\n"
                                               "background: #F14242;\n"
                                               "border:none;\n"
                                               "border-radius: 5px;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "background: #ED4D4D;\n"
                                               "color: #000\n"
                                               "}\n"
                                               "")
        self.btnEliminarPaciente.setText("")
        self.btnEliminarPaciente.setIcon(icon6)
        self.btnEliminarPaciente.setIconSize(QtCore.QSize(30, 30))
        self.btnEliminarPaciente.setObjectName("btnEliminarPaciente")
        self.btnEditarPaciente = QtWidgets.QPushButton(self.pacientePage)
        self.btnEditarPaciente.setGeometry(QtCore.QRect(840, 80, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btnEditarPaciente.setFont(font)
        self.btnEditarPaciente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEditarPaciente.setStyleSheet("QPushButton{\n"
                                             "background: #FAE73F;\n"
                                             "border:none;\n"
                                             "border-radius: 5px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "background: #FDEB4C;\n"
                                             "color: #000\n"
                                             "}\n"
                                             "")
        self.btnEditarPaciente.setText("")
        self.btnEditarPaciente.setIcon(icon7)
        self.btnEditarPaciente.setIconSize(QtCore.QSize(30, 30))
        self.btnEditarPaciente.setObjectName("btnEditarPaciente")
        self.btnAgregarPaciente = QtWidgets.QPushButton(self.pacientePage)
        self.btnAgregarPaciente.setGeometry(QtCore.QRect(910, 80, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btnAgregarPaciente.setFont(font)
        self.btnAgregarPaciente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAgregarPaciente.setStyleSheet("QPushButton{\n"
                                              "background: #07CD1B;\n"
                                              "border:none;\n"
                                              "border-radius: 5px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "background: #21D233;\n"
                                              "color: #000\n"
                                              "}\n"
                                              "")
        self.btnAgregarPaciente.setText("")
        self.btnAgregarPaciente.setIcon(icon5)
        self.btnAgregarPaciente.setIconSize(QtCore.QSize(30, 30))
        self.btnAgregarPaciente.setObjectName("btnAgregarPaciente")
        self.lblTituloPaciente = QtWidgets.QLabel(self.pacientePage)
        self.lblTituloPaciente.setGeometry(QtCore.QRect(10, 30, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.lblTituloPaciente.setFont(font)
        self.lblTituloPaciente.setStyleSheet("QLabel{\n"
                                             "background: transparent\n"
                                             "}")
        self.lblTituloPaciente.setObjectName("lblTituloPaciente")
        self.stkPages.addWidget(self.pacientePage)
        Principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Principal)
        self.stkPages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Clinica Jhonson"))
        self.btnCita.setText(_translate("Principal", " Citas"))
        self.btnMedico.setText(_translate("Principal", " Medicos"))
        self.btnPaciente.setText(_translate("Principal", " Pacientes"))
        self.btnInicio.setText(_translate("Principal", " Inicio"))
        self.tblMedico.setSortingEnabled(False)
        item = self.tblMedico.horizontalHeaderItem(0)
        item.setText(_translate("Principal", "Nombre"))
        item = self.tblMedico.horizontalHeaderItem(1)
        item.setText(_translate("Principal", "Apellido"))
        item = self.tblMedico.horizontalHeaderItem(2)
        item.setText(_translate("Principal", "Documento"))
        item = self.tblMedico.horizontalHeaderItem(3)
        item.setText(_translate("Principal", "Especialidad"))
        item = self.tblMedico.horizontalHeaderItem(4)
        item.setText(_translate("Principal", "Fecha de nacimiento"))
        self.lblTituloMedico.setText(_translate("Principal", "MEDICOS"))
        self.txtBuscarPaciente.setPlaceholderText(
            _translate("Principal", "BUSCAR POR DNI"))
        self.tblPaciente.setSortingEnabled(False)
        item = self.tblPaciente.horizontalHeaderItem(0)
        item.setText(_translate("Principal", "Nombre"))
        item = self.tblPaciente.horizontalHeaderItem(1)
        item.setText(_translate("Principal", "Apellido"))
        item = self.tblPaciente.horizontalHeaderItem(2)
        item.setText(_translate("Principal", "Documento"))
        item = self.tblPaciente.horizontalHeaderItem(3)
        item.setText(_translate("Principal", "Obra Social"))
        item = self.tblPaciente.horizontalHeaderItem(4)
        item.setText(_translate("Principal", "Fecha de nacimiento"))
        self.lblTituloPaciente.setText(_translate("Principal", "PACIENTES"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_Principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
