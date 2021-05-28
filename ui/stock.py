# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_stock(object):
    def setupUi(self, stock):
        stock.setObjectName("stock")
        stock.resize(681, 446)
        self.gridLayout = QtWidgets.QGridLayout(stock)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_5 = QtWidgets.QFrame(stock)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableStock = QtWidgets.QTableWidget(self.frame_5)
        self.tableStock.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableStock.sizePolicy().hasHeightForWidth())
        self.tableStock.setSizePolicy(sizePolicy)
        self.tableStock.setMaximumSize(QtCore.QSize(800, 16777215))
        self.tableStock.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableStock.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableStock.setObjectName("tableStock")
        self.tableStock.setColumnCount(6)
        self.tableStock.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(5, item)
        self.tableStock.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.tableStock, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.buttonUpdateStock = QtWidgets.QPushButton(self.frame_6)
        self.buttonUpdateStock.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonUpdateStock.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonUpdateStock.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonUpdateStock.setObjectName("buttonUpdateStock")
        self.horizontalLayout_4.addWidget(self.buttonUpdateStock)
        self.buttonUpdatePrize = QtWidgets.QPushButton(self.frame_6)
        self.buttonUpdatePrize.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonUpdatePrize.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonUpdatePrize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonUpdatePrize.setObjectName("buttonUpdatePrize")
        self.horizontalLayout_4.addWidget(self.buttonUpdatePrize)
        self.gridLayout_4.addWidget(self.frame_6, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout.addWidget(self.frame_5, 5, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(stock)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(925, 16777215))
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("")
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonClear = QtWidgets.QPushButton(self.frame_2)
        self.buttonClear.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonClear.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setFamily("Centular")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buttonClear.setFont(font)
        self.buttonClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonClear.setIconSize(QtCore.QSize(16, 16))
        self.buttonClear.setObjectName("buttonClear")
        self.horizontalLayout.addWidget(self.buttonClear)
        self.buttonLoad = QtWidgets.QPushButton(self.frame_2)
        self.buttonLoad.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonLoad.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setFamily("Centular")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buttonLoad.setFont(font)
        self.buttonLoad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonLoad.setObjectName("buttonLoad")
        self.horizontalLayout.addWidget(self.buttonLoad)
        self.gridLayout_2.addWidget(self.frame_2, 3, 1, 1, 2, QtCore.Qt.AlignRight)
        self.fieldCategory = QtWidgets.QComboBox(self.frame)
        self.fieldCategory.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldCategory.setMaximumSize(QtCore.QSize(300, 25))
        self.fieldCategory.setObjectName("fieldCategory")
        self.gridLayout_2.addWidget(self.fieldCategory, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)
        self.fieldType = QtWidgets.QComboBox(self.frame)
        self.fieldType.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldType.setMaximumSize(QtCore.QSize(300, 25))
        self.fieldType.setStyleSheet("")
        self.fieldType.setObjectName("fieldType")
        self.fieldType.addItem("")
        self.fieldType.addItem("")
        self.fieldType.addItem("")
        self.gridLayout_2.addWidget(self.fieldType, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Centular")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.fieldBrand = QtWidgets.QComboBox(self.frame)
        self.fieldBrand.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldBrand.setMaximumSize(QtCore.QSize(300, 25))
        self.fieldBrand.setBaseSize(QtCore.QSize(300, 25))
        self.fieldBrand.setStyleSheet("")
        self.fieldBrand.setObjectName("fieldBrand")
        self.gridLayout_2.addWidget(self.fieldBrand, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Centular")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Centular")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.retranslateUi(stock)
        QtCore.QMetaObject.connectSlotsByName(stock)

    def retranslateUi(self, stock):
        _translate = QtCore.QCoreApplication.translate
        stock.setWindowTitle(_translate("stock", "Form"))
        stock.setProperty("type", _translate("stock", "main"))
        self.frame_5.setProperty("type", _translate("stock", "mainframe"))
        item = self.tableStock.horizontalHeaderItem(0)
        item.setText(_translate("stock", "Product Code"))
        item = self.tableStock.horizontalHeaderItem(1)
        item.setText(_translate("stock", "Product Name"))
        item = self.tableStock.horizontalHeaderItem(2)
        item.setText(_translate("stock", "Brand"))
        item = self.tableStock.horizontalHeaderItem(3)
        item.setText(_translate("stock", "category"))
        item = self.tableStock.horizontalHeaderItem(4)
        item.setText(_translate("stock", "Stock (Units)"))
        item = self.tableStock.horizontalHeaderItem(5)
        item.setText(_translate("stock", "Prize/Unit (Rs.)"))
        self.label_5.setText(_translate("stock", "Stock"))
        self.label_5.setProperty("type", _translate("stock", "heading"))
        self.buttonUpdateStock.setText(_translate("stock", "Update Stock"))
        self.buttonUpdatePrize.setText(_translate("stock", "Update Prize"))
        self.frame_3.setProperty("type", _translate("stock", "mainframe"))
        self.buttonClear.setText(_translate("stock", "Clear"))
        self.buttonLoad.setText(_translate("stock", "Load"))
        self.label.setText(_translate("stock", "Filter stock"))
        self.label.setProperty("type", _translate("stock", "heading"))
        self.fieldType.setItemText(0, _translate("stock", "All"))
        self.fieldType.setItemText(1, _translate("stock", "In Stock"))
        self.fieldType.setItemText(2, _translate("stock", "Out Of Stock"))
        self.label_4.setText(_translate("stock", "Catagory"))
        self.label_3.setText(_translate("stock", "Brand"))
        self.label_2.setText(_translate("stock", "Type"))
