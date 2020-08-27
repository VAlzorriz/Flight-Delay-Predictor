# -*- coding: utf-8 -*-
class Persona:
    
    def __init__ (self, nuevoNombre, nuevaEdad):
        self.nombre=nuevoNombre
        self.edad=nuevaEdad

    def __str__ (self):
        return self.nombre+'('+str(self.edad)+')'
    
    