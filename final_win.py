from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class Result(QWidget):
    def __init__(self, name, age, p1, p2, p3):
        super().__init__()
        self.name = name
        self.age = age
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        #configuración de la ventana
        self.setWindowTitle("Resultado")
        self.resize(700, 500)
        #crear layout principal
        layout_result = QVBoxLayout()
        #crear resultado
        result = self.result_info()
        self.lbl = QLabel(self.name + " Tu resultado:" + result)
        #agregar layout principal
        self.setLayout(layout_result)
        #agregar widgets al layout principal
        layout_result.addWidget(self.lbl)

    def result_info(self):
        number = (4*(self.p1 + self.p2 + self.p3)-200)/10
        if self.age >= 15:
            if number <= 0.4:
                return "Alto"
            elif number <= 5.9:
                return "Más alto del promedio"
            elif number <= 10.9:
                return "Promedio"
            elif number <= 14.9:
                return "Satisfactorio"
            else:
                return "Bajo"
        elif self.age in (13, 14):
            if number <= 1.9:
                return "Alto"
            elif number <= 7.4:
                return "Más alto del promedio"
            elif number <= 12.4:
                return "Promedio"
            elif number <= 16.4:
                return "Satisfactorio"
            else:
                return "Bajo"
        elif self.age in (11, 12):
            if number <= 3.4:
                return "Alto"
            elif number <= 8.9:
                return "Más alto del promedio"
            elif number <= 13.9:
                return "Promedio"
            elif number <= 17.9:
                return "Satisfactorio"
            else:
                return "Bajo"
        elif self.age in (9, 10):
            if number <= 4.9:
                return "Alto"
            elif number <= 10.4:
                return "Más alto del promedio"
            elif number <= 15.4:
                return "Promedio"
            elif number <= 19.4:
                return "Satisfactorio"
            else:
                return "Bajo"
        elif self.age in (7, 8):
            if number <= 6.4:
                return "Alto"
            elif number <= 11.9:
                return "Más alto del promedio"
            elif number <= 16.9:
                return "Promedio"
            elif number <= 20.9:
                return "Satisfactorio"
            else:
                return "Bajo"
        else:
            return "Edad fuera de rango"
