# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowLzAheK.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(230, 160)
        MainWindow.setMinimumSize(QSize(230, 160))
        MainWindow.setMaximumSize(QSize(230, 160))
        MainWindow.setBaseSize(QSize(230, 160))
        MainWindow.setMouseTracking(True)
        self.actionClick_Settings = QAction(MainWindow)
        self.actionClick_Settings.setObjectName(u"actionClick_Settings")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        font = QFont()
        font.setUnderline(False)
        font.setKerning(False)
        self.actionExit.setFont(font)
        self.actionRepition = QAction(MainWindow)
        self.actionRepition.setObjectName(u"actionRepition")
        self.actionClick_Settings_2 = QAction(MainWindow)
        self.actionClick_Settings_2.setObjectName(u"actionClick_Settings_2")
        self.actionClick_Settings_2.setEnabled(True)
        font1 = QFont()
        font1.setKerning(False)
        self.actionClick_Settings_2.setFont(font1)
        self.actionRecording = QAction(MainWindow)
        self.actionRecording.setObjectName(u"actionRecording")
        self.actionRecording.setFont(font1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.changeActiveButton = QPushButton(self.centralwidget)
        self.changeActiveButton.setObjectName(u"changeActiveButton")
        self.changeActiveButton.setGeometry(QRect(10, 20, 201, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 230, 22))
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(True)
        font2.setStrikeOut(False)
        font2.setKerning(False)
        self.menubar.setFont(font2)
        self.menubar.setMouseTracking(False)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        font3 = QFont()
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        self.menuFile.setFont(font3)
        self.menuFile.setMouseTracking(True)
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuOptions.setEnabled(True)
        self.menuOptions.setMouseTracking(True)
        self.menuOptions.setAcceptDrops(True)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionClick_Settings_2)
        self.menuOptions.addAction(self.actionRecording)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionClick_Settings.setText(QCoreApplication.translate("MainWindow", u"Click Settings", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionRepition.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.actionClick_Settings_2.setText(QCoreApplication.translate("MainWindow", u"Click Settings", None))
        self.actionRecording.setText(QCoreApplication.translate("MainWindow", u"Recording", None))
        self.changeActiveButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

