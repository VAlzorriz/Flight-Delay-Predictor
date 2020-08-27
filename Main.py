# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:56:57 2017

@author: Victor Alzorriz
"""
import sys
import Control, Vista
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile, QTextStream
from PyQt5 import QtCore, QtGui

# creamos la aplicación
app = QApplication(sys.argv)

file = QFile("stylesheet.qss")
file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(file)
app.setStyleSheet(stream.readAll())

app_icon = QtGui.QIcon()
app_icon.addFile('icon.png', QtCore.QSize(256,256))
app.setWindowIcon(app_icon)

#creamos el controlador
ctr=Control.Control()

#creamos la ventana
view=Vista.Vista(ctr)

#asociamos la ventana al controlados
ctr.asignarVentana(view)

#mostramos todo
view.show()

sys.exit(app.exec_())