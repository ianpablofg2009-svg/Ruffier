from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from second_win import Pulses

class Home(QWidget):
    def __init__(self):
        super().__init__()
        #configuración de la ventana
        self.setWindowTitle("Inicio")
        self.resize(700, 500)
        #crear y asignar un layout
        layout_home = QVBoxLayout()
        self.setLayout(layout_home)
        #crear un label para crear el subtítulo de la aplicación
        self.lbl_subtitle = QLabel("App Ruffier")
        #crear un label para información de la aplicación
        self.lbl_info = QLabel("Esta aplicacion permite calcular el indice de Ruffier, que es un indice de rendimiento cardiovascular.")
        #crear un botón para iniciar la prueba
        self.btn_start = QPushButton("Iniciar prueba")
        self.btn_start.clicked.connect(self.show_pulses_window)

        #asignar widgets al layout
        layout_home.addWidget(self.lbl_subtitle)
        layout_home.addWidget(self.lbl_info)
        layout_home.addWidget(self.btn_start)

    def show_pulses_window(self):
        self.pulses = Pulses()
        self.pulses.show()
        self.hide()