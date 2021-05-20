# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'purchase.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_purchase(object):
    def setupUi(self, purchase):
        purchase.setObjectName("purchase")
        purchase.resize(703, 375)
        purchase.setStyleSheet("QLabel{\n"
"    font: 15px  \"Centular\";\n"
"}\n"
"\n"
"QLabel#labelCart , QLabel#labelSearchProduct{\n"
"    font: bold 16px  \"Centular\";\n"
"}\n"
"\n"
"QFrame#frameSearchProduct, QFrame#frameCart{\n"
"    background-color:#ddd;\n"
"    border-radius:6px;\n"
"}\n"
"\n"
"QComboBox,QSpinBox{\n"
"    background-color:#eee;\n"
"    border: 0.1em solid;\n"
"    color:#000;\n"
"    border-radius:5px;\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(purchase)
        self.gridLayout.setObjectName("gridLayout")
        self.frameSearchProduct = QtWidgets.QFrame(purchase)
        self.frameSearchProduct.setMinimumSize(QtCore.QSize(0, 170))
        self.frameSearchProduct.setMaximumSize(QtCore.QSize(16777215, 170))
        self.frameSearchProduct.setStyleSheet("")
        self.frameSearchProduct.setObjectName("frameSearchProduct")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frameSearchProduct)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelCategory = QtWidgets.QLabel(self.frameSearchProduct)
        self.labelCategory.setStyleSheet("")
        self.labelCategory.setObjectName("labelCategory")
        self.gridLayout_2.addWidget(self.labelCategory, 6, 2, 1, 1)
        self.fieldUnits = QtWidgets.QSpinBox(self.frameSearchProduct)
        self.fieldUnits.setMinimumSize(QtCore.QSize(100, 25))
        self.fieldUnits.setMaximumSize(QtCore.QSize(100, 25))
        self.fieldUnits.setStyleSheet("")
        self.fieldUnits.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.fieldUnits.setObjectName("fieldUnits")
        self.gridLayout_2.addWidget(self.fieldUnits, 17, 4, 1, 1)
        self.fieldBrand = QtWidgets.QComboBox(self.frameSearchProduct)
        self.fieldBrand.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldBrand.setStyleSheet("")
        self.fieldBrand.setObjectName("fieldBrand")
        self.gridLayout_2.addWidget(self.fieldBrand, 17, 3, 1, 1)
        self.labelUnits = QtWidgets.QLabel(self.frameSearchProduct)
        self.labelUnits.setStyleSheet("")
        self.labelUnits.setObjectName("labelUnits")
        self.gridLayout_2.addWidget(self.labelUnits, 6, 4, 1, 1)
        self.frameSearchButtons = QtWidgets.QFrame(self.frameSearchProduct)
        self.frameSearchButtons.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frameSearchButtons.setStyleSheet("")
        self.frameSearchButtons.setObjectName("frameSearchButtons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameSearchButtons)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonClear = QtWidgets.QPushButton(self.frameSearchButtons)
        self.buttonClear.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonClear.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonClear.setIconSize(QtCore.QSize(16, 16))
        self.buttonClear.setObjectName("buttonClear")
        self.horizontalLayout.addWidget(self.buttonClear)
        self.buttonAdd = QtWidgets.QPushButton(self.frameSearchButtons)
        self.buttonAdd.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonAdd.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonAdd.setObjectName("buttonAdd")
        self.horizontalLayout.addWidget(self.buttonAdd)
        self.gridLayout_2.addWidget(self.frameSearchButtons, 18, 3, 1, 2, QtCore.Qt.AlignRight)
        self.labelBrand = QtWidgets.QLabel(self.frameSearchProduct)
        self.labelBrand.setStyleSheet("")
        self.labelBrand.setObjectName("labelBrand")
        self.gridLayout_2.addWidget(self.labelBrand, 6, 3, 1, 1)
        self.labelSearchProduct = QtWidgets.QLabel(self.frameSearchProduct)
        self.labelSearchProduct.setEnabled(True)
        self.labelSearchProduct.setMinimumSize(QtCore.QSize(0, 30))
        self.labelSearchProduct.setMaximumSize(QtCore.QSize(16777215, 30))
        self.labelSearchProduct.setStyleSheet("")
        self.labelSearchProduct.setObjectName("labelSearchProduct")
        self.gridLayout_2.addWidget(self.labelSearchProduct, 0, 0, 1, 4)
        self.fieldCode = QtWidgets.QSpinBox(self.frameSearchProduct)
        self.fieldCode.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldCode.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fieldCode.setStyleSheet("")
        self.fieldCode.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.fieldCode.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.fieldCode.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.fieldCode.setObjectName("fieldCode")
        self.gridLayout_2.addWidget(self.fieldCode, 17, 0, 1, 1)
        self.labelCode = QtWidgets.QLabel(self.frameSearchProduct)
        self.labelCode.setStyleSheet("")
        self.labelCode.setObjectName("labelCode")
        self.gridLayout_2.addWidget(self.labelCode, 6, 0, 1, 1)
        self.labelName = QtWidgets.QLabel(self.frameSearchProduct)
        self.labelName.setMaximumSize(QtCore.QSize(16777215, 25))
        self.labelName.setStyleSheet("")
        self.labelName.setObjectName("labelName")
        self.gridLayout_2.addWidget(self.labelName, 6, 1, 1, 1)
        self.fieldName = QtWidgets.QComboBox(self.frameSearchProduct)
        self.fieldName.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldName.setStyleSheet("")
        self.fieldName.setObjectName("fieldName")
        self.gridLayout_2.addWidget(self.fieldName, 17, 1, 1, 1)
        self.fieldCategory = QtWidgets.QComboBox(self.frameSearchProduct)
        self.fieldCategory.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldCategory.setStyleSheet("")
        self.fieldCategory.setObjectName("fieldCategory")
        self.gridLayout_2.addWidget(self.fieldCategory, 17, 2, 1, 1)
        self.gridLayout.addWidget(self.frameSearchProduct, 0, 0, 1, 1)
        self.frameCart = QtWidgets.QFrame(purchase)
        self.frameCart.setEnabled(True)
        self.frameCart.setStyleSheet("")
        self.frameCart.setObjectName("frameCart")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frameCart)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frameCost = QtWidgets.QFrame(self.frameCart)
        self.frameCost.setMinimumSize(QtCore.QSize(0, 30))
        self.frameCost.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frameCost.setObjectName("frameCost")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameCost)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelTotal = QtWidgets.QLabel(self.frameCost)
        self.labelTotal.setStyleSheet("")
        self.labelTotal.setObjectName("labelTotal")
        self.horizontalLayout_2.addWidget(self.labelTotal)
        self.labelCost = QtWidgets.QLabel(self.frameCost)
        self.labelCost.setStyleSheet("")
        self.labelCost.setObjectName("labelCost")
        self.horizontalLayout_2.addWidget(self.labelCost)
        self.labelRs = QtWidgets.QLabel(self.frameCost)
        self.labelRs.setStyleSheet("")
        self.labelRs.setObjectName("labelRs")
        self.horizontalLayout_2.addWidget(self.labelRs)
        self.gridLayout_4.addWidget(self.frameCost, 3, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.frameCartButtons = QtWidgets.QFrame(self.frameCart)
        self.frameCartButtons.setMinimumSize(QtCore.QSize(0, 50))
        self.frameCartButtons.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frameCartButtons.setObjectName("frameCartButtons")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frameCartButtons)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonClearAll = QtWidgets.QPushButton(self.frameCartButtons)
        self.buttonClearAll.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonClearAll.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonClearAll.setObjectName("buttonClearAll")
        self.horizontalLayout_3.addWidget(self.buttonClearAll)
        self.buttonRemove = QtWidgets.QPushButton(self.frameCartButtons)
        self.buttonRemove.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonRemove.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonRemove.setObjectName("buttonRemove")
        self.horizontalLayout_3.addWidget(self.buttonRemove)
        self.buttonPurchase = QtWidgets.QPushButton(self.frameCartButtons)
        self.buttonPurchase.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonPurchase.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonPurchase.setObjectName("buttonPurchase")
        self.horizontalLayout_3.addWidget(self.buttonPurchase)
        self.gridLayout_4.addWidget(self.frameCartButtons, 3, 1, 1, 1, QtCore.Qt.AlignRight)
        self.tableCart = QtWidgets.QTableWidget(self.frameCart)
        self.tableCart.setEnabled(True)
        self.tableCart.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableCart.setGridStyle(QtCore.Qt.DashLine)
        self.tableCart.setObjectName("tableCart")
        self.tableCart.setColumnCount(7)
        self.tableCart.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCart.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCart.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCart.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCart.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCart.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCart.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCart.setHorizontalHeaderItem(6, item)
        self.tableCart.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.tableCart, 2, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.labelCart = QtWidgets.QLabel(self.frameCart)
        self.labelCart.setMinimumSize(QtCore.QSize(0, 30))
        self.labelCart.setMaximumSize(QtCore.QSize(16777215, 30))
        self.labelCart.setStyleSheet("")
        self.labelCart.setObjectName("labelCart")
        self.gridLayout_4.addWidget(self.labelCart, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.frameCart, 1, 0, 1, 1)

        self.retranslateUi(purchase)
        QtCore.QMetaObject.connectSlotsByName(purchase)

    def retranslateUi(self, purchase):
        _translate = QtCore.QCoreApplication.translate
        purchase.setWindowTitle(_translate("purchase", "Form"))
        self.labelCategory.setText(_translate("purchase", "Category"))
        self.labelUnits.setText(_translate("purchase", "Units"))
        self.buttonClear.setText(_translate("purchase", "Clear"))
        self.buttonAdd.setText(_translate("purchase", "Add to cart"))
        self.labelBrand.setText(_translate("purchase", "Brand"))
        self.labelSearchProduct.setText(_translate("purchase", "Search Product"))
        self.labelCode.setText(_translate("purchase", "Product Code"))
        self.labelName.setText(_translate("purchase", "Product Name"))
        self.labelTotal.setText(_translate("purchase", "Total Cost :"))
        self.labelCost.setText(_translate("purchase", "0.0"))
        self.labelRs.setText(_translate("purchase", "Rs."))
        self.buttonClearAll.setText(_translate("purchase", "Clear All"))
        self.buttonRemove.setText(_translate("purchase", "Remove"))
        self.buttonPurchase.setText(_translate("purchase", "Purchase"))
        self.tableCart.setSortingEnabled(False)
        item = self.tableCart.horizontalHeaderItem(0)
        item.setText(_translate("purchase", "Product Code"))
        item = self.tableCart.horizontalHeaderItem(1)
        item.setText(_translate("purchase", "Product Name"))
        item = self.tableCart.horizontalHeaderItem(2)
        item.setText(_translate("purchase", "Brand"))
        item = self.tableCart.horizontalHeaderItem(3)
        item.setText(_translate("purchase", "category"))
        item = self.tableCart.horizontalHeaderItem(4)
        item.setText(_translate("purchase", "Units"))
        item = self.tableCart.horizontalHeaderItem(5)
        item.setText(_translate("purchase", "Cost/Unit"))
        item = self.tableCart.horizontalHeaderItem(6)
        item.setText(_translate("purchase", "Cost"))
        self.labelCart.setText(_translate("purchase", "Cart"))