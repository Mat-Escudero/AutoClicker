# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changeButtonWindowJgOxuj.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_changeButtonWindow(object):
    def setupUi(self, changeButtonWindow):
        if not changeButtonWindow.objectName():
            changeButtonWindow.setObjectName(u"changeButtonWindow")
        changeButtonWindow.resize(277, 169)
        changeButtonWindow.setMinimumSize(QSize(277, 169))
        changeButtonWindow.setMaximumSize(QSize(277, 169))
        self.pushButton = QPushButton(changeButtonWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 40, 91, 41))
        self.label = QLabel(changeButtonWindow)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(150, 30, 71, 51))
        font = QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setMargin(0)
        self.OKButton = QPushButton(changeButtonWindow)
        self.OKButton.setObjectName(u"OKButton")
        self.OKButton.setGeometry(QRect(60, 130, 75, 24))
        self.CancelButton = QPushButton(changeButtonWindow)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.setGeometry(QRect(140, 130, 75, 24))

        self.retranslateUi(changeButtonWindow)

        QMetaObject.connectSlotsByName(changeButtonWindow)
    # setupUi

    def retranslateUi(self, changeButtonWindow):
        changeButtonWindow.setWindowTitle(QCoreApplication.translate("changeButtonWindow", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("changeButtonWindow", u"Change button", None))
        self.label.setText(QCoreApplication.translate("changeButtonWindow", u"F8", None))
        self.OKButton.setText(QCoreApplication.translate("changeButtonWindow", u"OK", None))
        self.CancelButton.setText(QCoreApplication.translate("changeButtonWindow", u"Cancel", None))
    # retranslateUi

