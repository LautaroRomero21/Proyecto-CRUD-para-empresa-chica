from vista import generar_ventanas
import modulo
from PyQt5 import QtWidgets

if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    base_datos = modulo.Base()

    ventana_bienvenida = generar_ventanas(base_datos)
    ventana_bienvenida.show()
    app.exec_()
