# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Subtitle import Subtitle

class Ui_MainWindow(object):

    sub = Subtitle()
    cbgs = False
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 200)
        MainWindow.setMinimumSize(QtCore.QSize(688, 200))
        MainWindow.setMaximumSize(QtCore.QSize(688, 200))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.labelVideo = QtWidgets.QLineEdit(self.centralwidget)
        self.labelVideo.setGeometry(QtCore.QRect(100, 20, 391, 21))
        self.labelVideo.setObjectName("labelVideo")
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setGeometry(QtCore.QRect(500, 20, 75, 23))
        self.btnBrowse.setObjectName("btnBrowse")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 20))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(190, 130, 141, 20))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.btnDownload = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownload.setGeometry(QtCore.QRect(580, 130, 75, 23))
        self.btnDownload.setObjectName("btnDownload")
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(580, 20, 75, 23))
        self.btnSearch.setObjectName("btnSearch")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 101, 16))
        self.label_2.setObjectName("label_2")
        self.langBox = QtWidgets.QComboBox(self.centralwidget)
        self.langBox.setGeometry(QtCore.QRect(110, 130, 69, 22))
        self.langBox.setObjectName("langBox")
        self.langBox.addItem("")
        self.langBox.addItem("")
        self.langBox.addItem("")
        self.langBox.addItem("")
        self.langBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(460, 130, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(390, 130, 71, 20))
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(100, 50, 391, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelStatus = QtWidgets.QLabel(self.frame)
        self.labelStatus.setGeometry(QtCore.QRect(20, 20, 351, 20))
        self.labelStatus.setText("")
        self.labelStatus.setObjectName("labelStatus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnBrowse.clicked.connect(self.selectFile)
        self.btnSearch.clicked.connect(self.onSearch)
        self.btnDownload.clicked.connect(self.onDownload)
        self.checkBox.stateChanged.connect(self.onCheckbox)
  

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "Video location"))
        self.checkBox.setText(_translate("MainWindow", "Use same name as video"))
        self.btnDownload.setText(_translate("MainWindow", "Download"))
        self.btnSearch.setText(_translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "Choose language"))
        self.langBox.setItemText(0, _translate("MainWindow", "English"))
        self.langBox.setItemText(1, _translate("MainWindow", "Portuguese"))
        self.langBox.setItemText(2, _translate("MainWindow", "Spanish"))
        self.langBox.setItemText(3, _translate("MainWindow", "French"))
        self.langBox.setItemText(4, _translate("MainWindow", "Italian"))
        self.label_3.setText(_translate("MainWindow", "Subtitle name"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
    
    def selectFile(self):
        self.labelVideo.setText(QtWidgets.QFileDialog.getOpenFileName()[0])
    
    def onSearch(self):
        if self.labelVideo.text() != "":
            self.sub.setVideo(self.labelVideo.text())
            self.labelStatus.setText(self.sub.getLang(verbose=True))
        else:
            self.labelStatus.setText("No file selected")
    
    def onDownload(self):
        if not self.cbgs:
            self.sub.getSub(self.langBox.currentText())
        else:
            self.sub.getSub(self.langBox.currentText(), newname=self.lineEdit.text() if self.lineEdit.text() != "" else None)

    def onCheckbox(self, state):
        if state != QtCore.Qt.Checked:
            self.lineEdit.setEnabled(True)
            self.label_3.setEnabled(True)
            self.cbgs = True
        else:
            self.lineEdit.setEnabled(False)
            self.label_3.setEnabled(False)
            self.cbgs = False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
