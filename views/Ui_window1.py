# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\window1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.TitleLabel = TitleLabel(self.centralwidget)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout_3.addWidget(self.TitleLabel)
        self.BodyFrame = QtWidgets.QFrame(self.centralwidget)
        self.BodyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BodyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BodyFrame.setObjectName("BodyFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.BodyFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.BodyFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CardWidget = CardWidget(self.frame_2)
        self.CardWidget.setObjectName("CardWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.CardWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame = QtWidgets.QFrame(self.CardWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SubtitleLabel_2 = SubtitleLabel(self.frame_5)
        self.SubtitleLabel_2.setObjectName("SubtitleLabel_2")
        self.horizontalLayout.addWidget(self.SubtitleLabel_2)
        self.verticalLayout_7.addWidget(self.frame_5)
        self.ScrollArea = ScrollArea(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScrollArea.sizePolicy().hasHeightForWidth())
        self.ScrollArea.setSizePolicy(sizePolicy)
        self.ScrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ScrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ScrollArea.setWidgetResizable(True)
        self.ScrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ScrollArea.setObjectName("ScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 389))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.buttonsFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.buttonsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonsFrame.setObjectName("buttonsFrame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.buttonsFrame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8.addWidget(self.buttonsFrame)
        self.frame_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 277, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_8.addWidget(self.frame_7)
        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_7.addWidget(self.ScrollArea)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout_4.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.CardWidget)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.BodyFrame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CardWidget_2 = CardWidget(self.frame_3)
        self.CardWidget_2.setObjectName("CardWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.CardWidget_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.SubtitleFrame = QtWidgets.QFrame(self.CardWidget_2)
        self.SubtitleFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.SubtitleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SubtitleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SubtitleFrame.setObjectName("SubtitleFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.SubtitleFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.SubtitleLabel = SubtitleLabel(self.SubtitleFrame)
        self.SubtitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SubtitleLabel.setWordWrap(False)
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.verticalLayout_4.addWidget(self.SubtitleLabel)
        self.verticalLayout_6.addWidget(self.SubtitleFrame)
        self.frame_4 = QtWidgets.QFrame(self.CardWidget_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.PlainTextEdit = PlainTextEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlainTextEdit.sizePolicy().hasHeightForWidth())
        self.PlainTextEdit.setSizePolicy(sizePolicy)
        self.PlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.PlainTextEdit.setObjectName("PlainTextEdit")
        self.verticalLayout_5.addWidget(self.PlainTextEdit)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.ButtonFrame = QtWidgets.QFrame(self.CardWidget_2)
        self.ButtonFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.ButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButtonFrame.setObjectName("ButtonFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.ButtonFrame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ToolButton_2 = ToolButton(self.ButtonFrame)
        self.ToolButton_2.setIconSize(QtCore.QSize(50, 50))
        self.ToolButton_2.setObjectName("ToolButton_2")
        self.horizontalLayout_7.addWidget(self.ToolButton_2)
        self.verticalLayout_6.addWidget(self.ButtonFrame)
        self.verticalLayout.addWidget(self.CardWidget_2)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.BodyFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TitleLabel.setText(_translate("MainWindow", "Choix de l\'activité à corriger automatiquement"))
        self.SubtitleLabel_2.setText(_translate("MainWindow", "Corriger une activité récente..."))
        self.SubtitleLabel.setText(_translate("MainWindow", "...Ou entrer le lien de la nouvelle activité"))
        self.PlainTextEdit.setPlaceholderText(_translate("MainWindow", "https://capytale2.ac-paris.fr/web/assignments/1911196"))
from qfluentwidgets import CardWidget, PlainTextEdit, ScrollArea, SubtitleLabel, TitleLabel, ToolButton
