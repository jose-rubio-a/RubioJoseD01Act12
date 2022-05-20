from random import randint
import time
from PySide2.QtWidgets import QMainWindow, QApplication
from views.Ui_main import Ui_MainWindow
from PySide2.QtCore import Slot

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.productos = 0
        self.productoActualProductor = 1
        self.productoActualConsumidor = 1
        self.estadoProductor = -1
        self.estadoConsumidor = -1
        self.tiempoTotal = 0
        self.tiempoEntraP = 0
        self.tiempoEntraC = 0

        self.ui.inicio_pushButton.clicked.connect(self.iniciar)
        self.ui.actionSalir.triggered.connect(self.salir)
    
    def trabajoConsumidor(self):
        self.ui.label_estadoCon.setText("Trabajando")
        random = randint(3, 6)
        i = 0
        while i < random and self.productos > 0:
            if self.productoActualConsumidor == 1:
                self.ui.producto.setStyleSheet("")
            elif self.productoActualConsumidor == 2:
                self.ui.producto_2.setStyleSheet("")
            elif self.productoActualConsumidor == 3:
                self.ui.producto_3.setStyleSheet("")
            elif self.productoActualConsumidor == 4:
                self.ui.producto_4.setStyleSheet("")
            elif self.productoActualConsumidor == 5:
                self.ui.producto_5.setStyleSheet("")
            elif self.productoActualConsumidor == 6:
                self.ui.producto_6.setStyleSheet("")
            elif self.productoActualConsumidor == 7:
                self.ui.producto_7.setStyleSheet("")
            elif self.productoActualConsumidor == 8:
                self.ui.producto_8.setStyleSheet("")
            elif self.productoActualConsumidor == 9:
                self.ui.producto_9.setStyleSheet("")
            elif self.productoActualConsumidor == 10:
                self.ui.producto_10.setStyleSheet("")
            elif self.productoActualConsumidor == 11:
                self.ui.producto_11.setStyleSheet("")
            elif self.productoActualConsumidor == 12:
                self.ui.producto_12.setStyleSheet("")
            elif self.productoActualConsumidor == 13:
                self.ui.producto_13.setStyleSheet("")
            elif self.productoActualConsumidor == 14:
                self.ui.producto_14.setStyleSheet("")
            elif self.productoActualConsumidor == 15:
                self.ui.producto_15.setStyleSheet("")
            elif self.productoActualConsumidor == 16:
                self.ui.producto_16.setStyleSheet("")
            elif self.productoActualConsumidor == 17:
                self.ui.producto_17.setStyleSheet("")
            elif self.productoActualConsumidor == 18:
                self.ui.producto_18.setStyleSheet("")
            elif self.productoActualConsumidor == 19:
                self.ui.producto_19.setStyleSheet("")
            elif self.productoActualConsumidor == 20:
                self.ui.producto_20.setStyleSheet("")
                self.productoActualConsumidor = 0
            self.productoActualConsumidor += 1
            self.productos -= 1
            i += 1
            if self.tiempoTotal == self.tiempoEntraP:
                self.estadoProductor = 1
                self.ui.pushButton_4.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(221, 221, 110);"
	                                                "border: None;"
                                                "}")
                self.ui.label_estadoPro.setText("En espera")
            self.tiempoTotal += 1
            QApplication.processEvents()
            time.sleep(1)
            self.ui.lcdNumber.display(self.tiempoTotal)
            print("Tiempo del consumidor trabajando: " + str(self.tiempoTotal))
    
    def trabajoProductor(self):
        self.ui.label_estadoPro.setText("Trabajando")
        random = randint(3, 6)
        i = 0
        while i < random and self.productos < 20:
            if self.productoActualProductor == 1:
                self.ui.producto.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 2:
                self.ui.producto_2.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 3:
                self.ui.producto_3.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 4:
                self.ui.producto_4.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 5:
                self.ui.producto_5.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 6:
                self.ui.producto_6.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 7:
                self.ui.producto_7.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 8:
                self.ui.producto_8.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 9:
                self.ui.producto_9.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 10:
                self.ui.producto_10.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 11:
                self.ui.producto_11.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 12:
                self.ui.producto_12.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 13:
                self.ui.producto_13.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 14:
                self.ui.producto_14.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 15:
                self.ui.producto_15.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 16:
                self.ui.producto_16.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 17:
                self.ui.producto_17.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 18:
                self.ui.producto_18.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 19:
                self.ui.producto_19.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
            elif self.productoActualProductor == 20:
                self.ui.producto_20.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(0, 170, 255);"
	                                                "border: None;"
                                                "}")
                self.productoActualProductor = 0
            self.productoActualProductor += 1
            self.productos += 1
            i += 1
            if self.tiempoTotal == self.tiempoEntraC:
                self.estadoConsumidor = 1
                self.ui.pushButton_5.setStyleSheet("QPushButton{"
	                                                "background-color: rgb(221, 221, 110);"
	                                                "border: None;"
                                                "}")
                self.ui.label_estadoCon.setText("En espera")
            self.tiempoTotal += 1
            QApplication.processEvents()
            time.sleep(1)
            self.ui.lcdNumber.display(self.tiempoTotal)
            print("Tiempo del Productor trabajando: " + str(self.tiempoTotal))
        
    @Slot()
    def salir(self):
        self.close()
        exit()

    @Slot()
    def iniciar(self):
        self.ui.inicio_pushButton.setEnabled(False)
        while True:
            if self.estadoProductor == -1 and self.tiempoTotal >= self.tiempoEntraP:
                self.tiempoEntraP = randint(5, 16) + self.tiempoTotal
                self.estadoProductor = 0
                self.ui.pushButton_4.setText(str(self.tiempoEntraP))
                print("Tiempo entrada Productor: " + str(self.tiempoEntraP))
            if self.estadoConsumidor == -1 and self.tiempoTotal >= self.tiempoEntraC:
                self.tiempoEntraC = randint(5, 16) + self.tiempoTotal
                self.estadoConsumidor = 0
                self.ui.pushButton_5.setText(str(self.tiempoEntraC))
                print("Tiempo entrada Consumidor: " + str(self.tiempoEntraC))
            if (self.tiempoEntraP <= self.tiempoTotal and self.estadoProductor == 1) or (self.tiempoEntraP <= self.tiempoTotal and self.estadoProductor == 0):
                print("Analizando condiciones del Productor")
                if self.productos < 20:
                    self.ui.pushButton_4.setStyleSheet("QPushButton{"
	                                                    "background-color: rgb(85, 170, 0);"
	                                                    "border: None;"
                                                    "}")
                    self.trabajoProductor()
                    self.ui.pushButton_4.setStyleSheet("")
                    self.ui.label_estadoPro.setText("Dormido")
                self.estadoProductor = -1
            elif (self.tiempoEntraC <= self.tiempoTotal and self.estadoConsumidor == 1) or (self.tiempoEntraC <= self.tiempoTotal and self.estadoConsumidor == 0):
                print("Analizando condiciones del Consumidor")
                if self.productos > 0:
                    self.ui.pushButton_5.setStyleSheet("QPushButton{"
	                                                    "background-color: rgb(85, 170, 0);"
	                                                    "border: None;"
                                                    "}")
                    self.trabajoConsumidor()
                    self.ui.pushButton_5.setStyleSheet("")
                    self.ui.label_estadoCon.setText("Dormido")
                self.estadoConsumidor = -1
            self.tiempoTotal += 1
            QApplication.processEvents()
            time.sleep(1)
            self.ui.lcdNumber.display(self.tiempoTotal)
            print("Tiempo transcurrido: " + str(self.tiempoTotal))
