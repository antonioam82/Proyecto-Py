from login_ui import *

''' Se realiza el import desde la carpeta ui del archivo login_ui
    el cual contiene todo el diseño de la ventana
    para seguir con buenas practicas sera conveniente seguir el mismo modo de
    trabajo, separando la logica del diseño como en este caso '''


# Constructor de ventana
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

# Llamada de inicio de la aplicacion
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
