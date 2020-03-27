from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout

app = QApplication([])
window = QWidget()
layout = QHBoxLayout()
layout.addWidget(QPushButton("Añadir nodo"))
layout.addWidget(QPushButton("Añadir arista"))
window.setLayout(layout)
window.showMaximized()
window.show()
app.exec_()