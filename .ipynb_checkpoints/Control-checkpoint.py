# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:39:32 2017

@author: 1761
"""
import Persona

class Control:
    
    listaPersonas = []
   
    def __init__ (self):
        print("Controlador creado")
    
    def asignarVentana (self, window):
        self.v=window
    
    def crearPersona (self):
        nombre=self.v.nameLine.text()
        edad=self.v.edadLine.text()
        print("Creando a "+nombre+
              " de "+edad+" años")
        persona = Persona.Persona(nombre, edad)
        self.listaPersonas.append(persona)
    
    def mostrarPersonas (self):
        
        print("Mostrando Lista de Personas")
        for señores in self.listaPersonas:
            print(str(señores))
        print("The End")

