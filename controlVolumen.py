"""
Control de Volúmen. Crea una clase ControlVolumen que permita establecer el
volumen de un parlante (1 mínimo volumen, 10 máximo volumen). El constructor
establecerá el volumen en un nivel medio. Agrega métodos para: 1- ajustar el
volumen permitiendo que el mismo sume o reste sin salirse de los límites y 2-
mostrar el nivel de volúmen actual. Además, escribe una aplicación de consola que
permita al usuario manipular y consultar el volumen hasta que decida salir. Al
finalizar deberá mostrar el nivel actual de volumen.
"""

class manejoVolumen:
    def __init__(self, volumen):
        self.__volumen = volumen

    def get_volumen(self):
        return(self._volumen)

    def modificarVolumen(self, volumen):
        volumenNuevo = input("ingrese un nuevo valor")
        if volumenNuevo < 1 and volumenNuevo > 10:
            return(f'El volumen tiene un minimo de 1 y un máximo de 10')
        elif volumenNuevo > 1 and volumenNuevo < 10:
            self.get_volumen=volumenNuevo
        else:
            return('ingrese un valor válido')
        
    def mostrarVolumenActual(self):
        return f'El volumen actual es: {self.__volumen}.'