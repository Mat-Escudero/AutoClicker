# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recordingWindowFMkqyr.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QWidget)

class Ui_recordingWindow(object):
    def setupUi(self, recordingWindow):
        if not recordingWindow.objectName():
            recordingWindow.setObjectName(u"recordingWindow")
        recordingWindow.resize(550, 300)
        recordingWindow.setMinimumSize(QSize(550, 300))
        recordingWindow.setMaximumSize(QSize(550, 300))
        self.radioButton = QRadioButton(recordingWindow)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(50, 40, 161, 20))
        self.radioButton.setMouseTracking(False)
        self.radioButton.setAcceptDrops(False)
        self.radioButton.setChecked(False)
        self.radioButton.setAutoExclusive(True)
        self.label = QLabel(recordingWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 120, 81, 16))
        self.label_2 = QLabel(recordingWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 120, 49, 16))
        self.pushButton = QPushButton(recordingWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 120, 91, 51))
        self.pushButton.setMouseTracking(True)
        self.pushButton_2 = QPushButton(recordingWindow)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 170, 75, 24))
        self.label_3 = QLabel(recordingWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 240, 41, 16))
        self.spinBox = QSpinBox(recordingWindow)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(100, 240, 51, 22))
        self.spinBox.setMaximum(2)
        self.label_4 = QLabel(recordingWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 240, 31, 16))
        self.spinBox_2 = QSpinBox(recordingWindow)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(200, 240, 51, 22))
        self.spinBox_2.setMaximum(59)
        self.label_5 = QLabel(recordingWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(260, 240, 49, 16))
        self.spinBox_3 = QSpinBox(recordingWindow)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(310, 240, 51, 22))
        self.spinBox_3.setMaximum(59)
        self.label_6 = QLabel(recordingWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, 240, 49, 16))
        self.spinBox_4 = QSpinBox(recordingWindow)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(420, 240, 51, 22))
        self.spinBox_4.setMaximum(999)
        self.label_7 = QLabel(recordingWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(480, 240, 71, 16))
        self.label_8 = QLabel(recordingWindow)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 220, 481, 20))

        self.retranslateUi(recordingWindow)

        QMetaObject.connectSlotsByName(recordingWindow)
    # setupUi

    def retranslateUi(self, recordingWindow):
        recordingWindow.setWindowTitle(QCoreApplication.translate("recordingWindow", u"Dialog", None))
        self.radioButton.setText(QCoreApplication.translate("recordingWindow", u"Record and replay clicks", None))
        self.label.setText(QCoreApplication.translate("recordingWindow", u"Clicks records:", None))
        self.label_2.setText(QCoreApplication.translate("recordingWindow", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("recordingWindow", u"Pick point", None))
        self.pushButton_2.setText(QCoreApplication.translate("recordingWindow", u"Clear", None))
        self.label_3.setText(QCoreApplication.translate("recordingWindow", u"Interval", None))
        self.label_4.setText(QCoreApplication.translate("recordingWindow", u"hours", None))
        self.label_5.setText(QCoreApplication.translate("recordingWindow", u"minutes", None))
        self.label_6.setText(QCoreApplication.translate("recordingWindow", u"seconds", None))
        self.label_7.setText(QCoreApplication.translate("recordingWindow", u"miliseconds", None))
        self.label_8.setText(QCoreApplication.translate("recordingWindow", u"Set the interval before picking a point \u2014 each point can have its own interval", None))
    # retranslateUi

