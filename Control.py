# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:39:32 2017

@author: Victor Alzorriz
"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.externals import joblib

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog

import os
import datetime

class Control:
    
    def __init__ (self):
        print("Controlador creado")
    
    def asignarVentana (self, window):
        self.view = window
        
        self.view.pushButton_Entrenar.clicked.connect(self.entrenarModelo)
        self.view.pushButton_GuardarModelo.clicked.connect(self.guardarModelo)
        self.view.pushButton_Clasificar.clicked.connect(self.clasificarDatos)
        self.view.pushButton_GuardarClasificacion.clicked.connect(self.guardarClasificacion)
        
        self.view.pushButton_BuscarFicheroEntrenar.clicked.connect(self.fileChooserEntrenar)
        self.view.pushButton_BuscarFicheroClasificar.clicked.connect(self.fileChooserClasificar)
        self.view.pushButton_BuscarModeloClasificar.clicked.connect(self.fileChooserModelo)
        
    def entrenarModelo (self):
        print('Entrenando modelo')
        QApplication.setOverrideCursor(Qt.WaitCursor)
        
        if self.view.lineEdit_FicheroEntrenar.text() != '':
            address = self.view.lineEdit_FicheroEntrenar.text()
        
            vuelos = pd.read_csv(address)
            vuelos.columns = ['destino','aerolinea', 'horaPrevista', 'horaSalida','temperatura', 'presion', 'velocidadViento', 'direccionViento', 'visibilidad', 'tipoNubosidad', 'alturaNubosidad', 'retrasado']
        
            X_prime = vuelos.ix[:,(0,1,2,3,4,5,6,7,8,9,10)].values
        
            X_prime[:,3] = pd.to_numeric(X_prime[:,3], errors='coerce')
            X_prime[:,8] = pd.to_numeric(X_prime[:,8], errors='coerce')
        
            X_prime = self.transformarNumeros(X_prime)
        
            scaler = MinMaxScaler()
            X = scaler.fit_transform(X_prime)
            Y = vuelos.ix[:,11].values
        
            test_size = .33
            random_state = 17
        
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=random_state)
        
            if str(self.view.comboBox_Algoritmos.currentText()) == 'KNeighbors':
                self.clf = KNeighborsClassifier()
                self.algoritmo = 'KNeighbors'
                self.view.lineEdit_NombreFichero.setText('KNeighbors')
            
            elif str(self.view.comboBox_Algoritmos.currentText()) == 'GradientBoosting':
                self.clf = GradientBoostingClassifier(n_estimators=20, learning_rate=0.5, max_features=2, max_depth=2, random_state=0)
                self.algoritmo = 'GradientBoosting'
                self.view.lineEdit_NombreFichero.setText('GradientBoosting')
            
            elif str(self.view.comboBox_Algoritmos.currentText()) == 'Naive Bayes':
                self.clf = GaussianNB()
                self.algoritmo = 'Naive Bayes'
                self.view.lineEdit_NombreFichero.setText('NaiveBayes')
        
            self.clf.fit(X_train, Y_train)
        
            print(self.clf)
        
            Y_expect = Y_test
            Y_pred = self.clf.predict(X_test)
        
            self.estadisticasResultado(Y_expect, Y_pred)
        
        QApplication.restoreOverrideCursor()
        
    def guardarModelo(self):
        print('Guardando Modelo')
        if self.view.lineEdit_NombreFichero.text() == '':
            nombre = 'modelo.mdl'
        else:
            nombre = str(self.view.lineEdit_NombreFichero.text()) + '.mdl'
        
        joblib.dump(self.modelo, nombre)
        
    def clasificarDatos(self):
        print('Clasificando Datos')
        QApplication.setOverrideCursor(Qt.WaitCursor)
        
        if self.view.lineEdit_ModeloClasificar.text() != '' and self.view.lineEdit_FicheroClasificar.text() != '':
            addressClasificador = self.view.lineEdit_ModeloClasificar.text()
            addressVuelos = self.view.lineEdit_FicheroClasificar.text()
        
            vuelos = pd.read_csv(addressVuelos)
            vuelos.columns = ['destino','aerolinea', 'horaPrevista', 'horaSalida','temperatura', 'presion', 'velocidadViento', 'direccionViento', 'visibilidad', 'tipoNubosidad', 'alturaNubosidad']
        
            X_prime = vuelos.ix[:,(0,1,2,3,4,5,6,7,8,9,10)].values
        
            X_prime = self.transformarNumeros(X_prime)
        
            scaler = MinMaxScaler()
            X = scaler.fit_transform(X_prime)
        
            self.openModelo = joblib.load(addressClasificador)
            
            nombre = 'Clasificacion ' + str(self.openModelo.algoritmo)
            self.view.lineEdit_NombreClasificacion.setText(nombre)
        
            Xresult = vuelos.ix[:,:].values
            Yresult = self.openModelo.clf.predict(X)
        
            dfX = pd.DataFrame(Xresult)
            dfY = pd.DataFrame(Yresult)
        
            self.result = pd.merge(dfX, dfY, left_index=True, right_index=True)
        
            model = PandasModel(self.result)
            self.view.tableView_Clasificacion.setModel(model)
        
        QApplication.restoreOverrideCursor()
        
    def guardarClasificacion(self):
        print('Guardando Clasificacion')
        if self.view.lineEdit_NombreClasificacion.text() == '':
            nombre = 'Clasificacion.csv'
        else:
            nombre = str(self.view.lineEdit_NombreClasificacion.text()) + '.csv'
            
        self.result.to_csv(nombre, encoding='utf-8', index=False)
        
    def fileChooserEntrenar (self):
        filename = QFileDialog.getOpenFileName(self.view.Clasificador, 'Open file', '', 'csv(*.csv)')
        self.view.lineEdit_FicheroEntrenar.setText(filename[0])
        print(filename[0])
        
        dataset = pd.read_csv(filename[0])
        self.fecha = datetime.datetime.fromtimestamp(os.path.getctime(filename[0]))
        datasetDf = pd.DataFrame(dataset)
        self.ejemplares, self.atributos = datasetDf.shape
        
        self.view.label_EjemplaresEntrenamientoDato.setText(str(self.ejemplares))
        self.view.label_AtributosEntrenamientoDato.setText(str(self.atributos))
        self.view.label_FechaEntrenamientoDato.setText(str(self.fecha))
        
    def fileChooserClasificar (self):
        filename = QFileDialog.getOpenFileName(self.view.Clasificador, 'Open file', '', 'csv(*.csv)')
        self.view.lineEdit_FicheroClasificar.setText(filename[0])
        print(filename[0])
        
    def fileChooserModelo (self):
        filename = QFileDialog.getOpenFileName(self.view.Clasificador, 'Open file', '', 'mdl(*.mdl)')
        self.view.lineEdit_ModeloClasificar.setText(filename[0])
        print(filename[0])
        
        modelo = joblib.load(filename[0])
        self.view.label_AlgoritmoClasificacionDato.setText(str(modelo.algoritmo))
        self.view.label_EjemplaresClasificacionDato.setText(str(modelo.ejemplares))
        self.view.label_AtributosClasificacionDato.setText(str(modelo.atributos))
        self.view.label_FechaClasificacionDato.setText(str(modelo.fecha))
        self.view.label_PrecisionClasificacionDato.setText(str(modelo.precision))
        self.view.label_RecallClasificacionDato.setText(str(modelo.recall))
    
    def transformarNumeros (self, X_prime):
        print('Transformando a numeros')
        le = LabelEncoder()
        for index_1 in range(0, 10):
            X_prime[:,index_1] = le.fit_transform(X_prime[:,index_1])
        
        return X_prime
    
    def estadisticasResultado (self, Y_expect, Y_pred):
        print('Calculando estadisticas')
        confusion = metrics.confusion_matrix(Y_expect, Y_pred)
        
        self.view.tableWidget_Resultado.setItem(0, 0, QtWidgets.QTableWidgetItem(str(confusion[0,0])))
        self.view.tableWidget_Resultado.setItem(0, 1, QtWidgets.QTableWidgetItem(str(confusion[0,1])))
        self.view.tableWidget_Resultado.setItem(1, 0, QtWidgets.QTableWidgetItem(str(confusion[1,0])))
        self.view.tableWidget_Resultado.setItem(1, 1, QtWidgets.QTableWidgetItem(str(confusion[1,1])))
        
        clasification = metrics.classification_report(Y_expect, Y_pred, output_dict=True)
        no = clasification.get('No')
        si = clasification.get('Si')
        
        self.view.tableWidget_Resultado.setItem(2, 0, QtWidgets.QTableWidgetItem(str(si.get('recall'))))
        self.view.tableWidget_Resultado.setItem(2, 1, QtWidgets.QTableWidgetItem(str(no.get('recall'))))
        self.view.tableWidget_Resultado.setItem(0, 2, QtWidgets.QTableWidgetItem(str(si.get('precision'))))
        self.view.tableWidget_Resultado.setItem(1, 2, QtWidgets.QTableWidgetItem(str(no.get('precision'))))
        print(confusion[1,1])
        print(confusion)
        print(clasification)
        
        self.modelo = Modelo(self.clf, self.algoritmo, self.fecha, self.ejemplares, self.atributos, si.get('precision'), si.get('recall'))
        
class Modelo():
    def __init__(self, clf, algoritmo, fecha, ejemplares, atributos, precision, recall):
        self.clf = clf
        self.algoritmo = algoritmo
        self.fecha = fecha
        self.ejemplares = ejemplares
        self.atributos = atributos
        self.precision = precision
        self.recall = recall

class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None