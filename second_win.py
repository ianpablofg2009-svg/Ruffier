from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

class Pulses(QWidget):
    def __init__(self):
        super().__init__()
        #configuración de la ventana
        self.setWindowTitle("Toma de pulsos")
        self.resize(700, 500)
        #crear layout principal
        layout_pulses = QVBoxLayout()
        #ingresar datos del usuario
        self.lbl_name = QLabel("Nombre del paciente:")
        self.txt_name = QLineEdit()

        self.lbl_age = QLabel("Edad del paciente:")
        self.txt_age = QLineEdit()
        #ingresar pulsos
        self.lbl_p1 = QLabel("Descansa por algunos minutos y toma el pulso por 15 segundos")
        self.txt_p1 = QLineEdit()

        self.lbl_p2 = QLabel("Realiza 30 sentadillas en 45 segundos. Toma el pulso por 15 segundos")
        self.txt_p2 = QLineEdit()

        self.lbl_p3 = QLabel("Descansa por 30 segundos. Toma el pulso por 15 segundos")
        self.txt_p3 = QLineEdit()
        #Crear botón de resultados
        self.btn_result = QPushButton("Resultado")

        #agregar layout principal
        self.setLayout(layout_pulses)
        #agregar widgets al layout principal
        layout_pulses.addWidget(self.lbl_name)
        layout_pulses.addWidget(self.txt_name)
        layout_pulses.addWidget(self.lbl_age)
        layout_pulses.addWidget(self.txt_age)
        layout_pulses.addWidget(self.lbl_p1)
        layout_pulses.addWidget(self.txt_p1)
        layout_pulses.addWidget(self.lbl_p2)
        layout_pulses.addWidget(self.txt_p2)
        layout_pulses.addWidget(self.lbl_p3)
        layout_pulses.addWidget(self.txt_p3)
        layout_pulses.addWidget(self.btn_result)
