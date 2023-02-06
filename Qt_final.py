# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt_final.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget
import test_LessMotion1
import test_LessMotion2
import test_LessMotion3
import test_LessMotion4
import test_LessMotion5
import LESS_analysis_refer
import picture_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 430)
        MainWindow.setStyleSheet("background-image:url(:/1.png)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 200, 161, 61))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"   test-decoration:none;\n"
"   background:#2f435e;\n"
"   color:#f2f2f2;\n"
"\n"
"   padding:10px 30px 10px 30px;\n"
"   font-size:16px;\n"
"   font-family:微软雅黑,宋\n"
"体,Arial,Helvetica,Verdana,sans-serif;\n"
"   font-weight:bold;\n"
"   border-radius:3px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 200, 161, 61))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"   test-decoration:none;\n"
"   background:#2f435e;\n"
"   color:#f2f2f2;\n"
"\n"
"   padding:10px 30px 10px 30px;\n"
"   font-size:16px;\n"
"   font-family:微软雅黑,宋\n"
"体,Arial,Helvetica,Verdana,sans-serif;\n"
"   font-weight:bold;\n"
"   border-radius:3px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 310, 161, 61))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"   test-decoration:none;\n"
"   background:#2f435e;\n"
"   color:#f2f2f2;\n"
"\n"
"   padding:10px 30px 10px 30px;\n"
"   font-size:16px;\n"
"   font-family:微软雅黑,宋\n"
"体,Arial,Helvetica,Verdana,sans-serif;\n"
"   font-weight:bold;\n"
"   border-radius:3px;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(490, 310, 161, 61))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"   test-decoration:none;\n"
"   background:#2f435e;\n"
"   color:#f2f2f2;\n"
"\n"
"   padding:10px 30px 10px 30px;\n"
"   font-size:16px;\n"
"   font-family:微软雅黑,宋\n"
"体,Arial,Helvetica,Verdana,sans-serif;\n"
"   font-weight:bold;\n"
"   border-radius:3px;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(270, 200, 161, 61))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"   test-decoration:none;\n"
"   background:#2f435e;\n"
"   color:#f2f2f2;\n"
"\n"
"   padding:10px 30px 10px 30px;\n"
"   font-size:16px;\n"
"   font-family:微软雅黑,宋\n"
"体,Arial,Helvetica,Verdana,sans-serif;\n"
"   font-weight:bold;\n"
"   border-radius:3px;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 310, 161, 61))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"   test-decoration:none;\n"
"   background:#2f435e;\n"
"   color:#f2f2f2;\n"
"\n"
"   padding:10px 30px 10px 30px;\n"
"   font-size:16px;\n"
"   font-family:微软雅黑,宋\n"
"体,Arial,Helvetica,Verdana,sans-serif;\n"
"   font-weight:bold;\n"
"   border-radius:3px;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_2.clicked.connect(test_LessMotion1.run_final)
        self.pushButton_8.clicked.connect(test_LessMotion2.run_final)
        self.pushButton_4.clicked.connect(test_LessMotion3.run_final)
        self.pushButton_5.clicked.connect(test_LessMotion4.run_final)
        self.pushButton_6.clicked.connect(test_LessMotion5.run_final)
        self.pushButton_7.clicked.connect(LESS_analysis_refer.report_sum)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于视觉技术的自动化运动评估系统"))
        self.pushButton_2.setText(_translate("MainWindow", "A1：屈膝测试"))
        self.pushButton_4.setText(_translate("MainWindow", "A3：躯体测试"))
        self.pushButton_5.setText(_translate("MainWindow", "D1：踝膝测试"))
        self.pushButton_7.setText(_translate("MainWindow", "生成分析报告"))
        self.pushButton_8.setText(_translate("MainWindow", "A2：躯腿测试"))
        self.pushButton_6.setText(_translate("MainWindow", "D2：踝肩测试"))

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建一个application，app
    MainWindow = QtWidgets.QMainWindow()#创建一个QMainwindow，装各种组建和控件

    demo=Ui_MainWindow()#实例化对象
    demo.setupUi(MainWindow)#执行类中的setupUi方法
    MainWindow.show()

    sys.exit(app.exec_())