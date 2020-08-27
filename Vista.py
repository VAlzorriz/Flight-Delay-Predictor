# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vista.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Vista:
    def __init__ (self, ctrl):
        print("Vista creada")
        self.controlador=ctrl
        
        self.Clasificador = QtWidgets.QWidget()
        ui = Vista
        ui.setupUi(self, self.Clasificador)
        
    def show (self):
        print('Ventana Mostrada')
        self.Clasificador.show()
        
    def setupUi(self, Clasificador):
        Clasificador.setObjectName("Clasificador")
        Clasificador.resize(722, 639)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Clasificador)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Clasificador)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Entrenamiento = QtWidgets.QWidget()
        self.tab_Entrenamiento.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab_Entrenamiento.setObjectName("tab_Entrenamiento")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_Entrenamiento)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem)
        self.label_Fichero = QtWidgets.QLabel(self.tab_Entrenamiento)
        self.label_Fichero.setObjectName("label_Fichero")
        self.horizontalLayout_1.addWidget(self.label_Fichero)
        self.lineEdit_FicheroEntrenar = QtWidgets.QLineEdit(self.tab_Entrenamiento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_FicheroEntrenar.sizePolicy().hasHeightForWidth())
        self.lineEdit_FicheroEntrenar.setSizePolicy(sizePolicy)
        self.lineEdit_FicheroEntrenar.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_FicheroEntrenar.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit_FicheroEntrenar.setObjectName("lineEdit_FicheroEntrenar")
        self.horizontalLayout_1.addWidget(self.lineEdit_FicheroEntrenar)
        self.pushButton_BuscarFicheroEntrenar = QtWidgets.QPushButton(self.tab_Entrenamiento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_BuscarFicheroEntrenar.sizePolicy().hasHeightForWidth())
        self.pushButton_BuscarFicheroEntrenar.setSizePolicy(sizePolicy)
        self.pushButton_BuscarFicheroEntrenar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_BuscarFicheroEntrenar.setObjectName("pushButton_BuscarFicheroEntrenar")
        self.horizontalLayout_1.addWidget(self.pushButton_BuscarFicheroEntrenar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_Algoritmos = QtWidgets.QLabel(self.tab_Entrenamiento)
        self.label_Algoritmos.setObjectName("label_Algoritmos")
        self.horizontalLayout_2.addWidget(self.label_Algoritmos)
        self.comboBox_Algoritmos = QtWidgets.QComboBox(self.tab_Entrenamiento)
        self.comboBox_Algoritmos.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Algoritmos.sizePolicy().hasHeightForWidth())
        self.comboBox_Algoritmos.setSizePolicy(sizePolicy)
        self.comboBox_Algoritmos.setObjectName("comboBox_Algoritmos")
        self.comboBox_Algoritmos.addItem("")
        self.comboBox_Algoritmos.addItem("")
        self.comboBox_Algoritmos.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_Algoritmos)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.label_DatosDataset = QtWidgets.QLabel(self.tab_Entrenamiento)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_DatosDataset.setFont(font)
        self.label_DatosDataset.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DatosDataset.setObjectName("label_DatosDataset")
        self.verticalLayout_5.addWidget(self.label_DatosDataset)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_FechaEntrenamientoTitulo = QtWidgets.QLabel(self.tab_Entrenamiento)
        self.label_FechaEntrenamientoTitulo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_FechaEntrenamientoTitulo.setObjectName("label_FechaEntrenamientoTitulo")
        self.horizontalLayout_8.addWidget(self.label_FechaEntrenamientoTitulo)
        self.label_FechaEntrenamientoDato = QtWidgets.QLabel(self.tab_Entrenamiento)
        self.label_FechaEntrenamientoDato.setText("")
        self.label_FechaEntrenamientoDato.setObjectName("label_FechaEntrenamientoDato")
        self.horizontalLayout_8.addWidget(self.label_FechaEntrenamientoDato)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_EjemplaresEntrenamientoTitulo = QtWidgets.QLabel(self.tab_Entrenamiento)
        self.label_EjemplaresEntrenamientoTitulo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_EjemplaresEntrenamientoTitulo.setObjectName("label_EjemplaresEntrenamientoTitulo")
        self.horizontalLayout_9.addWidget(self.label_EjemplaresEntrenamientoTitulo)
        self.label_EjemplaresEntrenamientoDato = QtWidgets.QLabel(self.tab_Entrenamiento)
        self.label_EjemplaresEntrenamientoDato.setText("")
        self.label_EjemplaresEntrenamientoDato.setObjectName("label_EjemplaresEntrenamientoDato")
        self.horizontalLayout_9.addWidget(self.label_EjemplaresEntrenamientoDato)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_AtributosEntrenamientoTitulo = QtWidgets.QLabel(self.tab_Entrenamiento)
        self.label_AtributosEntrenamientoTitulo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_AtributosEntrenamientoTitulo.setObjectName("label_AtributosEntrenamientoTitulo")
        self.horizontalLayout_10.addWidget(self.label_AtributosEntrenamientoTitulo)
        self.label_AtributosEntrenamientoDato = QtWidgets.QLabel(self.tab_Entrenamiento)
        self.label_AtributosEntrenamientoDato.setText("")
        self.label_AtributosEntrenamientoDato.setObjectName("label_AtributosEntrenamientoDato")
        self.horizontalLayout_10.addWidget(self.label_AtributosEntrenamientoDato)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pushButton_Entrenar = QtWidgets.QPushButton(self.tab_Entrenamiento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Entrenar.sizePolicy().hasHeightForWidth())
        self.pushButton_Entrenar.setSizePolicy(sizePolicy)
        self.pushButton_Entrenar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Entrenar.setObjectName("pushButton_Entrenar")
        self.horizontalLayout_3.addWidget(self.pushButton_Entrenar)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.label_ResultadoEntrenamiento = QtWidgets.QLabel(self.tab_Entrenamiento)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_ResultadoEntrenamiento.setFont(font)
        self.label_ResultadoEntrenamiento.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ResultadoEntrenamiento.setObjectName("label_ResultadoEntrenamiento")
        self.verticalLayout_5.addWidget(self.label_ResultadoEntrenamiento)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.tableWidget_Resultado = QtWidgets.QTableWidget(self.tab_Entrenamiento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_Resultado.sizePolicy().hasHeightForWidth())
        self.tableWidget_Resultado.setSizePolicy(sizePolicy)
        self.tableWidget_Resultado.setSizeIncrement(QtCore.QSize(0, 0))
        self.tableWidget_Resultado.setBaseSize(QtCore.QSize(0, 0))
        self.tableWidget_Resultado.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget_Resultado.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_Resultado.setAutoFillBackground(False)
        self.tableWidget_Resultado.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_Resultado.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget_Resultado.setShowGrid(True)
        self.tableWidget_Resultado.setWordWrap(True)
        self.tableWidget_Resultado.setCornerButtonEnabled(True)
        self.tableWidget_Resultado.setRowCount(3)
        self.tableWidget_Resultado.setColumnCount(3)
        self.tableWidget_Resultado.setObjectName("tableWidget_Resultado")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget_Resultado.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget_Resultado.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget_Resultado.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Resultado.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Resultado.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Resultado.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Resultado.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Resultado.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Resultado.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Resultado.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Resultado.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Resultado.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Resultado.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Resultado.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Resultado.setItem(2, 2, item)
        self.tableWidget_Resultado.horizontalHeader().setVisible(True)
        self.tableWidget_Resultado.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Resultado.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget_Resultado.horizontalHeader().setHighlightSections(True)
        self.tableWidget_Resultado.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget_Resultado.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_Resultado.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_Resultado.verticalHeader().setVisible(True)
        self.tableWidget_Resultado.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Resultado.verticalHeader().setDefaultSectionSize(60)
        self.tableWidget_Resultado.verticalHeader().setHighlightSections(True)
        self.tableWidget_Resultado.verticalHeader().setMinimumSectionSize(0)
        self.tableWidget_Resultado.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_Resultado.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_12.addWidget(self.tableWidget_Resultado)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem8)
        self.label_NombreFichero = QtWidgets.QLabel(self.tab_Entrenamiento)
        self.label_NombreFichero.setObjectName("label_NombreFichero")
        self.horizontalLayout_20.addWidget(self.label_NombreFichero)
        self.lineEdit_NombreFichero = QtWidgets.QLineEdit(self.tab_Entrenamiento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_NombreFichero.sizePolicy().hasHeightForWidth())
        self.lineEdit_NombreFichero.setSizePolicy(sizePolicy)
        self.lineEdit_NombreFichero.setText("")
        self.lineEdit_NombreFichero.setObjectName("lineEdit_NombreFichero")
        self.horizontalLayout_20.addWidget(self.lineEdit_NombreFichero)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.pushButton_GuardarModelo = QtWidgets.QPushButton(self.tab_Entrenamiento)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GuardarModelo.sizePolicy().hasHeightForWidth())
        self.pushButton_GuardarModelo.setSizePolicy(sizePolicy)
        self.pushButton_GuardarModelo.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_GuardarModelo.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_GuardarModelo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_GuardarModelo.setObjectName("pushButton_GuardarModelo")
        self.horizontalLayout_4.addWidget(self.pushButton_GuardarModelo)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_Entrenamiento, "")
        self.tab_Clasificacion = QtWidgets.QWidget()
        self.tab_Clasificacion.setObjectName("tab_Clasificacion")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_Clasificacion)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.label = QtWidgets.QLabel(self.tab_Clasificacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.lineEdit_FicheroClasificar = QtWidgets.QLineEdit(self.tab_Clasificacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_FicheroClasificar.sizePolicy().hasHeightForWidth())
        self.lineEdit_FicheroClasificar.setSizePolicy(sizePolicy)
        self.lineEdit_FicheroClasificar.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_FicheroClasificar.setObjectName("lineEdit_FicheroClasificar")
        self.horizontalLayout_5.addWidget(self.lineEdit_FicheroClasificar)
        self.pushButton_BuscarFicheroClasificar = QtWidgets.QPushButton(self.tab_Clasificacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_BuscarFicheroClasificar.sizePolicy().hasHeightForWidth())
        self.pushButton_BuscarFicheroClasificar.setSizePolicy(sizePolicy)
        self.pushButton_BuscarFicheroClasificar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_BuscarFicheroClasificar.setObjectName("pushButton_BuscarFicheroClasificar")
        self.horizontalLayout_5.addWidget(self.pushButton_BuscarFicheroClasificar)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.label_2 = QtWidgets.QLabel(self.tab_Clasificacion)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.lineEdit_ModeloClasificar = QtWidgets.QLineEdit(self.tab_Clasificacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ModeloClasificar.sizePolicy().hasHeightForWidth())
        self.lineEdit_ModeloClasificar.setSizePolicy(sizePolicy)
        self.lineEdit_ModeloClasificar.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_ModeloClasificar.setObjectName("lineEdit_ModeloClasificar")
        self.horizontalLayout_6.addWidget(self.lineEdit_ModeloClasificar)
        self.pushButton_BuscarModeloClasificar = QtWidgets.QPushButton(self.tab_Clasificacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_BuscarModeloClasificar.sizePolicy().hasHeightForWidth())
        self.pushButton_BuscarModeloClasificar.setSizePolicy(sizePolicy)
        self.pushButton_BuscarModeloClasificar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_BuscarModeloClasificar.setObjectName("pushButton_BuscarModeloClasificar")
        self.horizontalLayout_6.addWidget(self.pushButton_BuscarModeloClasificar)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.label_DatosModelo = QtWidgets.QLabel(self.tab_Clasificacion)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_DatosModelo.setFont(font)
        self.label_DatosModelo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DatosModelo.setObjectName("label_DatosModelo")
        self.verticalLayout_2.addWidget(self.label_DatosModelo)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_AlgoritmoClasificacionTitulo = QtWidgets.QLabel(self.tab_Clasificacion)
        self.label_AlgoritmoClasificacionTitulo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_AlgoritmoClasificacionTitulo.setObjectName("label_AlgoritmoClasificacionTitulo")
        self.horizontalLayout_17.addWidget(self.label_AlgoritmoClasificacionTitulo)
        self.label_AlgoritmoClasificacionDato = QtWidgets.QLabel(self.tab_Clasificacion)
        self.label_AlgoritmoClasificacionDato.setText("")
        self.label_AlgoritmoClasificacionDato.setObjectName("label_AlgoritmoClasificacionDato")
        self.horizontalLayout_17.addWidget(self.label_AlgoritmoClasificacionDato)
        self.verticalLayout_2.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_FechaClasificacionTitulo = QtWidgets.QLabel(self.tab_Clasificacion)
        self.label_FechaClasificacionTitulo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_FechaClasificacionTitulo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_FechaClasificacionTitulo.setObjectName("label_FechaClasificacionTitulo")
        self.horizontalLayout_13.addWidget(self.label_FechaClasificacionTitulo)
        self.label_FechaClasificacionDato = QtWidgets.QLabel(self.tab_Clasificacion)
        self.label_FechaClasificacionDato.setText("")
        self.label_FechaClasificacionDato.setObjectName("label_FechaClasificacionDato")
        self.horizontalLayout_13.addWidget(self.label_FechaClasificacionDato)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_EjemplaresClasificacionTitulo = QtWidgets.QLabel(self.tab_Clasificacion)
        self.label_EjemplaresClasificacionTitulo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_EjemplaresClasificacionTitulo.setObjectName("label_EjemplaresClasificacionTitulo")
        self.horizontalLayout_14.addWidget(self.label_EjemplaresClasificacionTitulo)
        self.label_EjemplaresClasificacionDato = QtWidgets.QLabel(self.tab_Clasificacion)
        self.label_EjemplaresClasificacionDato.setText("")
        self.label_EjemplaresClasificacionDato.setObjectName("label_EjemplaresClasificacionDato")
        self.horizontalLayout_14.addWidget(self.label_EjemplaresClasificacionDato)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_AtributosClasificacionTitulo = QtWidgets.QLabel(self.tab_Clasificacion)
        self.label_AtributosClasificacionTitulo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_AtributosClasificacionTitulo.setObjectName("label_AtributosClasificacionTitulo")
        self.horizontalLayout_15.addWidget(self.label_AtributosClasificacionTitulo)
        self.label_AtributosClasificacionDato = QtWidgets.QLabel(self.tab_Clasificacion)
        self.label_AtributosClasificacionDato.setText("")
        self.label_AtributosClasificacionDato.setObjectName("label_AtributosClasificacionDato")
        self.horizontalLayout_15.addWidget(self.label_AtributosClasificacionDato)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_PrecisionClasificacionTitulo = QtWidgets.QLabel(self.tab_Clasificacion)
        self.label_PrecisionClasificacionTitulo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_PrecisionClasificacionTitulo.setObjectName("label_PrecisionClasificacionTitulo")
        self.horizontalLayout_18.addWidget(self.label_PrecisionClasificacionTitulo)
        self.label_PrecisionClasificacionDato = QtWidgets.QLabel(self.tab_Clasificacion)
        self.label_PrecisionClasificacionDato.setText("")
        self.label_PrecisionClasificacionDato.setObjectName("label_PrecisionClasificacionDato")
        self.horizontalLayout_18.addWidget(self.label_PrecisionClasificacionDato)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_RecallClasificacionTitulo = QtWidgets.QLabel(self.tab_Clasificacion)
        self.label_RecallClasificacionTitulo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_RecallClasificacionTitulo.setObjectName("label_RecallClasificacionTitulo")
        self.horizontalLayout_19.addWidget(self.label_RecallClasificacionTitulo)
        self.label_RecallClasificacionDato = QtWidgets.QLabel(self.tab_Clasificacion)
        self.label_RecallClasificacionDato.setText("")
        self.label_RecallClasificacionDato.setObjectName("label_RecallClasificacionDato")
        self.horizontalLayout_19.addWidget(self.label_RecallClasificacionDato)
        self.verticalLayout_2.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem16)
        self.pushButton_Clasificar = QtWidgets.QPushButton(self.tab_Clasificacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Clasificar.sizePolicy().hasHeightForWidth())
        self.pushButton_Clasificar.setSizePolicy(sizePolicy)
        self.pushButton_Clasificar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Clasificar.setObjectName("pushButton_Clasificar")
        self.horizontalLayout_7.addWidget(self.pushButton_Clasificar)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem17)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.label_ResultadoClasificacion = QtWidgets.QLabel(self.tab_Clasificacion)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_ResultadoClasificacion.setFont(font)
        self.label_ResultadoClasificacion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ResultadoClasificacion.setObjectName("label_ResultadoClasificacion")
        self.verticalLayout_2.addWidget(self.label_ResultadoClasificacion)
        self.tableView_Clasificacion = QtWidgets.QTableView(self.tab_Clasificacion)
        self.tableView_Clasificacion.setObjectName("tableView_Clasificacion")
        self.tableView_Clasificacion.horizontalHeader().setVisible(False)
        self.tableView_Clasificacion.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableView_Clasificacion)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem18)
        self.label_NombreClasificacion = QtWidgets.QLabel(self.tab_Clasificacion)
        self.label_NombreClasificacion.setObjectName("label_NombreClasificacion")
        self.horizontalLayout_21.addWidget(self.label_NombreClasificacion)
        self.lineEdit_NombreClasificacion = QtWidgets.QLineEdit(self.tab_Clasificacion)
        self.lineEdit_NombreClasificacion.setObjectName("lineEdit_NombreClasificacion")
        self.horizontalLayout_21.addWidget(self.lineEdit_NombreClasificacion)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem19)
        self.verticalLayout_2.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem20)
        self.pushButton_GuardarClasificacion = QtWidgets.QPushButton(self.tab_Clasificacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GuardarClasificacion.sizePolicy().hasHeightForWidth())
        self.pushButton_GuardarClasificacion.setSizePolicy(sizePolicy)
        self.pushButton_GuardarClasificacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_GuardarClasificacion.setObjectName("pushButton_GuardarClasificacion")
        self.horizontalLayout_11.addWidget(self.pushButton_GuardarClasificacion)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem21)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_Clasificacion, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Clasificador)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Clasificador)

    def retranslateUi(self, Clasificador):
        _translate = QtCore.QCoreApplication.translate
        Clasificador.setWindowTitle(_translate("Clasificador", "Vuelos Retrasados"))
        self.label_Fichero.setText(_translate("Clasificador", "Fichero de entrenamiento:"))
        self.pushButton_BuscarFicheroEntrenar.setText(_translate("Clasificador", "Buscar"))
        self.label_Algoritmos.setText(_translate("Clasificador", " Algoritmo de aprendizaje:"))
        self.comboBox_Algoritmos.setItemText(0, _translate("Clasificador", "KNeighbors"))
        self.comboBox_Algoritmos.setItemText(1, _translate("Clasificador", "GradientBoosting"))
        self.comboBox_Algoritmos.setItemText(2, _translate("Clasificador", "Naive Bayes"))
        self.label_DatosDataset.setText(_translate("Clasificador", "Datos del Dataset:"))
        self.label_FechaEntrenamientoTitulo.setText(_translate("Clasificador", "Fecha del Dataset:"))
        self.label_EjemplaresEntrenamientoTitulo.setText(_translate("Clasificador", "Ejemplares:"))
        self.label_AtributosEntrenamientoTitulo.setText(_translate("Clasificador", "Atributos:"))
        self.pushButton_Entrenar.setText(_translate("Clasificador", "Entrenar"))
        self.label_ResultadoEntrenamiento.setText(_translate("Clasificador", "Resultado de Entrenamiento:"))
        self.tableWidget_Resultado.setSortingEnabled(False)
        item = self.tableWidget_Resultado.verticalHeaderItem(0)
        item.setText(_translate("Clasificador", "Predecido Si:"))
        item = self.tableWidget_Resultado.verticalHeaderItem(1)
        item.setText(_translate("Clasificador", "Predecido No:"))
        item = self.tableWidget_Resultado.verticalHeaderItem(2)
        item.setText(_translate("Clasificador", "Class Recall:"))
        item = self.tableWidget_Resultado.horizontalHeaderItem(0)
        item.setText(_translate("Clasificador", "Retrasado Si:"))
        item = self.tableWidget_Resultado.horizontalHeaderItem(1)
        item.setText(_translate("Clasificador", "Retrasado No:"))
        item = self.tableWidget_Resultado.horizontalHeaderItem(2)
        item.setText(_translate("Clasificador", "Class Precision:"))
        __sortingEnabled = self.tableWidget_Resultado.isSortingEnabled()
        self.tableWidget_Resultado.setSortingEnabled(False)
        self.tableWidget_Resultado.setSortingEnabled(__sortingEnabled)
        self.label_NombreFichero.setText(_translate("Clasificador", "Nombre del modelo:"))
        self.pushButton_GuardarModelo.setText(_translate("Clasificador", "Guardar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Entrenamiento), _translate("Clasificador", "Entrenamiento"))
        self.label.setText(_translate("Clasificador", "Fichero a clasificar: "))
        self.pushButton_BuscarFicheroClasificar.setText(_translate("Clasificador", "Buscar"))
        self.label_2.setText(_translate("Clasificador", "Fichero del modelo para clasificar:"))
        self.pushButton_BuscarModeloClasificar.setText(_translate("Clasificador", "Buscar"))
        self.label_DatosModelo.setText(_translate("Clasificador", "Datos del Modelo:"))
        self.label_AlgoritmoClasificacionTitulo.setText(_translate("Clasificador", "Algoritmo:"))
        self.label_FechaClasificacionTitulo.setText(_translate("Clasificador", "Fecha del Dataset:"))
        self.label_EjemplaresClasificacionTitulo.setText(_translate("Clasificador", "Ejemplares:"))
        self.label_AtributosClasificacionTitulo.setText(_translate("Clasificador", "Atributos:"))
        self.label_PrecisionClasificacionTitulo.setText(_translate("Clasificador", "Precision True:"))
        self.label_RecallClasificacionTitulo.setText(_translate("Clasificador", "Recall True:"))
        self.pushButton_Clasificar.setText(_translate("Clasificador", "Clasificar"))
        self.label_ResultadoClasificacion.setText(_translate("Clasificador", "Resultado de la Clasificacion:"))
        self.label_NombreClasificacion.setText(_translate("Clasificador", "Nombre de la clasificacion:"))
        self.pushButton_GuardarClasificacion.setText(_translate("Clasificador", "Guardar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Clasificacion), _translate("Clasificador", "Clasificacion"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Clasificador = QtWidgets.QWidget()
    ui = Ui_Clasificador()
    ui.setupUi(Clasificador)
    Clasificador.show()
    sys.exit(app.exec_())
"""
