import sys
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
  
class Window(QMainWindow):
    
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
  
        self.setWindowTitle("Kalkulack V2 ")
  
        self.setGeometry(100, 100, 460, 350)
  
        self.UiComponents()
  
        self.show()
  
    def switch(self):
        self.switch_window
    
    def UiComponents(self):
        
        self.label = QLabel(self)

        self.label.setGeometry(5, 5, 350, 70)

        self.label.setWordWrap(True)

        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border: 2px solid black;"
                                 "background-color: grey;"
                                 "}")

        self.label.setFont(QFont('Arial', 15))

        push1 = QPushButton("1", self)
        push1.setGeometry(5, 150, 80, 40)

        push2 = QPushButton("2", self)
        push2.setGeometry(95, 150, 80, 40)

        push3 = QPushButton("3", self)
        push3.setGeometry(185, 150, 80, 40)

        push4 = QPushButton("4", self)
        push4.setGeometry(5, 200, 80, 40)

        push5 = QPushButton("5", self)
        push5.setGeometry(95, 200, 80, 40)

        push6 = QPushButton("6", self)
        push6.setGeometry(185, 200, 80, 40)

        push7 = QPushButton("7", self)
        push7.setGeometry(5, 250, 80, 40)

        push8 = QPushButton("8", self)
        push8.setGeometry(95, 250, 80, 40)

        push9 = QPushButton("9", self)
        push9.setGeometry(185, 250, 80, 40)

        push0 = QPushButton("0", self)
        push0.setGeometry(5, 300, 80, 40)

        push_equal = QPushButton("=", self)
        push_equal.setGeometry(275, 300, 80, 40)

        push_plus = QPushButton("+", self)
        push_plus.setGeometry(275, 150, 80, 40)

        push_minus = QPushButton("-", self)
        push_minus.setGeometry(275, 200, 80, 40)

        push_mul = QPushButton("*", self)
        push_mul.setGeometry(275, 250, 80, 40)
        
        push_div = QPushButton("/", self)
        push_div.setGeometry(185, 300, 80, 40)

        push_point = QPushButton(".", self)
        push_point.setGeometry(95, 300, 80, 40)

        push_clear = QPushButton("C", self)
        push_clear.setGeometry(5, 100, 200, 40)

        push_del = QPushButton("Del", self)
        push_del.setGeometry(210, 100, 145, 40)

        push_obsah = QPushButton("Obsah", self)
        push_obsah.setGeometry(365, 5, 80, 40)

        push_objem = QPushButton("Objem", self)
        push_objem.setGeometry(365, 50, 80, 40)

        push_obvod = QPushButton("Obvod", self)
        push_obvod.setGeometry(365, 100, 80, 40)

        push_rovnice = QPushButton("Rovnice", self)
        push_rovnice.setGeometry(365, 150, 80, 40)

        push_kvadraticka = QPushButton("Kvadraticka", self)
        push_kvadraticka.setGeometry(365, 200, 80, 40)

        push_vedecka = QPushButton("Vedecka", self)
        push_vedecka.setGeometry(365, 250, 80, 40)

        push_klasicka = QPushButton("Klasicka", self)
        push_klasicka.setGeometry(365, 300, 80, 40)



        push_minus.clicked.connect(self.action_minus)
        push_equal.clicked.connect(self.action_equal)
        push0.clicked.connect(self.action_0)
        push1.clicked.connect(self.action_1)
        push2.clicked.connect(self.action_2)
        push3.clicked.connect(self.action_3)
        push4.clicked.connect(self.action_4)
        push5.clicked.connect(self.action_5)
        push6.clicked.connect(self.action_6)
        push7.clicked.connect(self.action_7)
        push8.clicked.connect(self.action_8)
        push9.clicked.connect(self.action_9)
        push_plus.clicked.connect(self.action_plus)
        push_mul.clicked.connect(self.action_mul)
        push_div.clicked.connect(self.action_div)
        push_point.clicked.connect(self.action_point)
        push_clear.clicked.connect(self.action_clear)
        push_del.clicked.connect(self.action_del)

        push_obsah.clicked.connect(self.show_window_obsah)
        push_objem.clicked.connect(self.switch)
        push_obvod.clicked.connect(self.switch)
        push_rovnice.clicked.connect(self.switch)
        push_kvadraticka.clicked.connect(self.switch)
        push_vedecka.clicked.connect(self.switch)
        push_klasicka.clicked.connect(self.switch)


    def action_equal(self):
        equation = self.label.text()

        try:
            ans = eval(equation)
            self.label.setText(str(ans))

        except:
            self.label.setText("Wrong Input")

    def action_plus(self):
        text = self.label.text()
        self.label.setText(text + "+")
    def action_minus(self):
        text = self.label.text()
        self.label.setText(text + "-")
    def action_div(self):
        text = self.label.text()
        self.label.setText(text + "/")
    def action_mul(self):
        text = self.label.text()
        self.label.setText(text + "*")
    def action_point(self):
        text = self.label.text()
        self.label.setText(text + ".")
    def action_0(self):
        text = self.label.text()
        self.label.setText(text + "0") 
    def action_1(self):
        text = self.label.text()
        self.label.setText(text + "1")
    def action_2(self):
        text = self.label.text()
        self.label.setText(text + "2")
    def action_3(self):
        text = self.label.text()
        self.label.setText(text + "3")
    def action_4(self):
        text = self.label.text()
        self.label.setText(text + "4")
    def action_5(self):
        text = self.label.text()
        self.label.setText(text + "5")
    def action_6(self):
        text = self.label.text()
        self.label.setText(text + "6")
    def action_7(self):
        text = self.label.text()
        self.label.setText(text + "7")
    def action_8(self):
        text = self.label.text()
        self.label.setText(text + "8")
    def action_9(self):
        text = self.label.text()
        self.label.setText(text + "9")
    def action_clear(self):
        self.label.setText("")
    def action_del(self):
        text = self.label.text()
        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1])
    
    def show_window_obsah(self, text):
        self.window_two = Obsah()
        self.close()
    

class Obsah(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Obsahova kalkulacka")
        self.setGeometry(500, 500, 460, 400)
        self.UiComponents()
        self.show()
    

    def UiComponents(self):
        
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(70, 150)
        self.textbox1.resize(80,40)
        self.a = str(self.textbox1.text())
        

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(170, 150)
        self.textbox2.resize(80,40)
        self.b = self.textbox2.text()
        
        push_equal = QPushButton("Vypocitat", self)
        push_equal.move(160, 210)
        
        self.label = QLabel(self)

        self.label.setGeometry(270, 150, 80, 40)

        self.label.setWordWrap(True)

        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border: 2px grey;"
                                 "background-color: white;"
                                 "}")

        self.label.setFont(QFont('Arial', 15))

        r_stvoruholnik = QRadioButton("Stvoruholnik", self)
        r_stvoruholnik.setGeometry(10, 10, 100, 40)
        
        r_trojuholnik = QRadioButton("Trojuholnik", self)
        r_trojuholnik.setGeometry(10, 40, 100, 40)

        

        push_obsah = QPushButton("Obsah", self)
        push_obsah.setGeometry(365, 5, 80, 40)

        push_objem = QPushButton("Objem", self)
        push_objem.setGeometry(365, 50, 80, 40)

        push_obvod = QPushButton("Obvod", self)
        push_obvod.setGeometry(365, 100, 80, 40)

        push_rovnice = QPushButton("Rovnice", self)
        push_rovnice.setGeometry(365, 150, 80, 40)

        push_kvadraticka = QPushButton("Kvadraticka", self)
        push_kvadraticka.setGeometry(365, 200, 80, 40)

        push_vedecka = QPushButton("Vedecka", self)
        push_vedecka.setGeometry(365, 250, 80, 40)

        push_klasicka = QPushButton("Klasicka", self)
        push_klasicka.setGeometry(365, 300, 80, 40)
        

        push_equal.clicked.connect(self.action_equal)


    def action_equal(self):
        a = eval(self.textbox1.text())
        b = eval(self.textbox2.text())

        fig, ax = plt.subplots()
        
        rectangle = matplotlib.patches.Rectangle((0, 0), a, b, color = "blue")
        ax.add_patch(rectangle)
        
        plt.show()
        

    


    



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == "__main__":
    main()

