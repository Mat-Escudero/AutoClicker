# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clickSettingsWindowbBsZqO.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QSizePolicy, QSpinBox, QWidget)

class Ui_clickSettingsWindow(object):
    def setupUi(self, clickSettingsWindow):
        if not clickSettingsWindow.objectName():
            clickSettingsWindow.setObjectName(u"clickSettingsWindow")
        clickSettingsWindow.resize(568, 290)
        clickSettingsWindow.setMinimumSize(QSize(568, 290))
        clickSettingsWindow.setMaximumSize(QSize(568, 290))
        self.label = QLabel(clickSettingsWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 49, 16))
        self.comboBox = QComboBox(clickSettingsWindow)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 30, 69, 22))
        self.label_2 = QLabel(clickSettingsWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 70, 49, 16))
        self.comboBox_2 = QComboBox(clickSettingsWindow)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(100, 70, 69, 22))
        self.label_3 = QLabel(clickSettingsWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 160, 41, 16))
        self.spinBox = QSpinBox(clickSettingsWindow)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(110, 160, 51, 22))
        self.spinBox.setMaximum(2)
        self.spinBox_2 = QSpinBox(clickSettingsWindow)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(210, 160, 51, 22))
        self.spinBox_2.setMaximum(59)
        self.label_4 = QLabel(clickSettingsWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 160, 31, 16))
        self.label_5 = QLabel(clickSettingsWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 160, 49, 16))
        self.spinBox_3 = QSpinBox(clickSettingsWindow)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(320, 160, 51, 22))
        self.spinBox_3.setMaximum(59)
        self.label_6 = QLabel(clickSettingsWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(380, 160, 49, 16))
        self.spinBox_4 = QSpinBox(clickSettingsWindow)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(430, 160, 51, 22))
        self.spinBox_4.setMaximum(999)
        self.label_7 = QLabel(clickSettingsWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(490, 160, 71, 16))
        self.line = QFrame(clickSettingsWindow)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 120, 568, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(clickSettingsWindow)

        QMetaObject.connectSlotsByName(clickSettingsWindow)
    # setupUi

    def retranslateUi(self, clickSettingsWindow):
        clickSettingsWindow.setWindowTitle(QCoreApplication.translate("clickSettingsWindow", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("clickSettingsWindow", u"Mouse:", None))
        self.label_2.setText(QCoreApplication.translate("clickSettingsWindow", u"Click:", None))
        self.label_3.setText(QCoreApplication.translate("clickSettingsWindow", u"Interval", None))
        self.label_4.setText(QCoreApplication.translate("clickSettingsWindow", u"hours", None))
        self.label_5.setText(QCoreApplication.translate("clickSettingsWindow", u"minutes", None))
        self.label_6.setText(QCoreApplication.translate("clickSettingsWindow", u"seconds", None))
        self.label_7.setText(QCoreApplication.translate("clickSettingsWindow", u"miliseconds", None))
    # retranslateUi

