# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui1/off_trade.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_off_trade(object):
    def setupUi(self, off_trade):
        off_trade.setObjectName("off_trade")
        off_trade.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(off_trade)
        self.centralwidget.setObjectName("centralwidget")
        self.off_bt = QtWidgets.QPushButton(self.centralwidget)
        self.off_bt.setGeometry(QtCore.QRect(320, 420, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.off_bt.setFont(font)
        self.off_bt.setObjectName("off_bt")
        self.tomain = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.tomain.setGeometry(QtCore.QRect(500, 330, 91, 51))
        self.tomain.setObjectName("tomain")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(200, 30, 391, 287))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.trade_id = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.trade_id.setFont(font)
        self.trade_id.setObjectName("trade_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.trade_id)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.goods_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goods_name.setFont(font)
        self.goods_name.setObjectName("goods_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.goods_name)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.goods_type = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goods_type.setFont(font)
        self.goods_type.setObjectName("goods_type")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.goods_type)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.shop_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.shop_name.setFont(font)
        self.shop_name.setObjectName("shop_name")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.shop_name)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.trade_num = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.trade_num.setFont(font)
        self.trade_num.setObjectName("trade_num")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.trade_num)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.trade_money = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.trade_money.setFont(font)
        self.trade_money.setObjectName("trade_money")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.trade_money)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.trade_time = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.trade_time.setFont(font)
        self.trade_time.setObjectName("trade_time")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.trade_time)
        off_trade.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(off_trade)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        off_trade.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(off_trade)
        self.statusbar.setObjectName("statusbar")
        off_trade.setStatusBar(self.statusbar)

        self.retranslateUi(off_trade)
        QtCore.QMetaObject.connectSlotsByName(off_trade)

    def retranslateUi(self, off_trade):
        _translate = QtCore.QCoreApplication.translate
        off_trade.setWindowTitle(_translate("off_trade", "取消交易"))
        self.off_bt.setText(_translate("off_trade", "取消交易"))
        self.tomain.setText(_translate("off_trade", "首页"))
        self.label_10.setText(_translate("off_trade", "交易id"))
        self.label.setText(_translate("off_trade", "商品名称"))
        self.label_7.setText(_translate("off_trade", "商品类型"))
        self.label_3.setText(_translate("off_trade", "店铺名称"))
        self.label_8.setText(_translate("off_trade", "交易数量"))
        self.label_9.setText(_translate("off_trade", "交易金额"))
        self.label_2.setText(_translate("off_trade", "交易时间"))
