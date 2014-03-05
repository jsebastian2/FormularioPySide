import sys
from PySide import QtGui


app = QtGui.QApplication(sys.argv)


class VentanaBoton(QtGui.QDialog):
	def __init__(self):
		super(VentanaBoton, self).__init__()

		self.setGeometry(120, 120, 200, 200)

		label1 = QtGui.QLabel(self)
		label1.setText("Nombre")
		label1.setGeometry(40, 60, 60, 40)

		label2 = QtGui.QLabel(self)
		label2.setText("Apellido")
		label2.setGeometry(40, 90, 60, 60)

		label3 = QtGui.QLabel(self)
		label3.setText("Edad")
		label3.setGeometry(40, 120, 120, 120)

		label4 = QtGui.QLabel(self)
		label4.setText("Sexo")
		label4.setGeometry(40, 150, 180, 180)

		label5 = QtGui.QLabel(self)
		label5.setText("Hobby")
		label5.setGeometry(40, 170, 240, 240)

		line = QtGui.QLineEdit(self)
		line.setText("Escribe aqui")
		line.setGeometry(90, 170, 90, 20)

		line1 = QtGui.QLineEdit(self)
		line1.setText("Escribe aqui")
		line1.setGeometry(90, 110, 90, 20)

		line2 = QtGui.QLineEdit(self)
		line2.setText("Escribe aqui")
		line2.setGeometry(90, 70, 90, 20)

		box = QtGui.QComboBox(self)
		box.setGeometry(90, 230, 40, 20)
		
		box1 = QtGui.QComboBox(self)
		box1.setGeometry(90, 280, 40, 20)


		btn = QtGui.QPushButton(self)
		btn.setText("Cancelar")
		btn.setGeometry(130, 350, 60, 40)

		btn1 = QtGui.QPushButton(self)
		btn1.setText("Aceptar")
		# x, y, ancho, largo
		btn1.setGeometry(50, 350, 60, 40)






vent = VentanaBoton()
vent.show()

sys.exit(app.exec_())