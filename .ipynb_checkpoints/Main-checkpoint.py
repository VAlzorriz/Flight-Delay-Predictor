# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:56:57 2017

@author: 1761
"""
import sys
import Control, Vista
from PyQt5.QtWidgets import QApplication

# creamos la aplicación
app = QApplication(sys.argv)

#creamos el controlador
ctr=Control.Control()

#creamos la ventana
view=Vista.Vista(ctr)

#asociamos la ventana al controlados
ctr.asignarVentana(view)

#mostramos todo
view.show()

sys.exit(app.exec_())