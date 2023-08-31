# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Programmation\Python\Cool Projects\CapytaleAutoCorrect\ui\window2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleCard = CardWidget(self.centralwidget)
        self.TitleCard.setMaximumSize(QtCore.QSize(16777215, 100))
        self.TitleCard.setObjectName("TitleCard")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.TitleCard)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.TitleLabel = TitleLabel(self.TitleCard)
        self.TitleLabel.setMaximumSize(QtCore.QSize(16777215, 100))
        self.TitleLabel.setObjectName("TitleLabel")
        self.horizontalLayout_6.addWidget(self.TitleLabel)
        self.PushButton = PushButton(self.TitleCard)
        self.PushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.PushButton.setObjectName("PushButton")
        self.horizontalLayout_6.addWidget(self.PushButton)
        self.verticalLayout.addWidget(self.TitleCard)
        self.CardWidget = CardWidget(self.centralwidget)
        self.CardWidget.setObjectName("CardWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.CardWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TableView = TableWidget(self.CardWidget)
        self.TableView.setShowGrid(True)
        self.TableView.setSortingEnabled(True)
        self.TableView.setObjectName("TableView")
        self.horizontalLayout.addWidget(self.TableView)
        self.verticalLayout.addWidget(self.CardWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.PushButton.clicked.connect(self.clicked)
        self.initialize_table()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TitleLabel.setText(_translate("MainWindow", "Téléchargement des fichiers d\'élèves"))
        self.PushButton.setText(_translate("MainWindow", "Push button"))

    def initialize_table(self):
        self.TableView.setColumnCount(3)
        self.TableView.setHorizontalHeaderLabels(["Name", "Time", "File Name"])

    def clicked(self):
        # Define your placeholder data
        name = "John Doe"
        time = "10:30 AM"
        file_name = "example.txt"
        # Determine the next available row
        row_position = self.TableView.rowCount()
        self.TableView.insertRow(row_position)
        # Insert items into the table
        self.TableView.setItem(row_position, 0, QTableWidgetItem(name))
        self.TableView.setItem(row_position, 1, QTableWidgetItem(time))
        self.TableView.setItem(row_position, 2, QTableWidgetItem(file_name))


from qfluentwidgets import CardWidget, PushButton, TitleLabel, TableWidget