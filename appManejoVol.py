from controlVolumen import manejoVolumen

parlante = manejoVolumen(5)

info = parlante.mostrarVolumenActual()

while True:
    print(info)
    valorEntrada = str(input('Ingrese el nuevo valor de volumen. Si no quiere modificar más el volumen, escriba "salir".'))
    if valorEntrada != 'salir':
        volumenNuevo = int(valorEntrada)

        parlante.modificarVolumen(volumenNuevo)
        print(info)

    elif valorEntrada == 'salir':
        break

    else:
        print('Ingresa bien la wea (algo ta mal)')
        print('Acá hay un cambio')
        print ('Acá otro cambio')

    


