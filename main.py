from PyQt6.QtWidgets import QApplication
from first_win import Home

app = QApplication([])
home = Home()
home.show()
app.exec()
