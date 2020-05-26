#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:40:10 2020

@author: brash
"""

# tools
import sys
import numpy as np
# PyQt libraries
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 180))    
        self.setWindowTitle("Area/Circumference Calculator") 

        self.radiusLabel = QLabel(self)
        self.radiusLabel.setText('Enter the radius:')
        self.radiusLabel.move(20, 20)
                
        self.inputData = QLineEdit(self)
        self.inputData.move(140, 20)
        self.inputData.resize(100, 32)
        
        self.outLabel = QLabel(self)
        self.outLabel.setText('Area:')
        self.outLabel.move(20, 100)

        self.outputData = QLineEdit(self)
        self.outputData.move(140, 100)
        self.outputData.resize(100, 32)
        
        self.outLabel2 = QLabel(self)
        self.outLabel2.setText('Circumference:')
        self.outLabel2.move(20, 140)

        self.outputData2 = QLineEdit(self)
        self.outputData2.move(140, 140)
        self.outputData2.resize(100, 32)
        
        pybutton = QPushButton('Calculate', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(80,32)
        pybutton.move(80, 60)        

    def clickMethod(self):
        
        try:
            #print('The radius of the circle: ' + self.inputData.text())
            radius = float(self.inputData.text())
            ##### The following two lines are the only ones related to science!
            area = np.pi*radius*radius
            circ = 2.0*np.pi*radius
            #####
            outputText = ("%.2f" % area)
            outputText2 = ("%.2f" % circ)    
            self.outputData.setText(outputText)
            self.outputData2.setText(outputText2)
        except ValueError:
            print('The radius must be a number!!')
        
# Here is the main program
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # the following statement creates an object called mainWin,
    # which is of type MainWindow().
    # it will call the __init__ method of the MainWindow class
    mainWin = MainWindow()
    #
    mainWin.show()
    sys.exit( app.exec_() )



