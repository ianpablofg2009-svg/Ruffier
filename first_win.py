from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

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
        #asignar widgets al layout
        layout_home.addWidget(self.lbl_subtitle)