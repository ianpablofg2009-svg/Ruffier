from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class Result(QWidget):
    def __init__(self):
        super().__init__()
        #configuración de la ventana
        self.setWindowTitle("Resultado")
        self.resize(700, 500)
        #crear layout principal
        layout_result = QVBoxLayout()
        #crear resultado
        self.lbl = QLabel("Tu resultado:")
        #agregar layout principal
        self.setLayout(layout_result)
        #agregar widgets al layout principal
        layout_result.addWidget(self.lbl)