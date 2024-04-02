# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Additional_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Additional_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 466)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.PerGroup = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PerGroup.setFont(font)
        self.PerGroup.setStyleSheet("color: rgb(0, 255, 255);")
        self.PerGroup.setObjectName("PerGroup")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.PerGroup)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.Weight = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Weight.setFont(font)
        self.Weight.setStyleSheet("color: rgb(0, 255, 255);")
        self.Weight.setObjectName("Weight")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Weight)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Density = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Density.setFont(font)
        self.Density.setStyleSheet("color: rgb(0, 255, 255);")
        self.Density.setObjectName("Density")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Density)
        self.label_7 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.Melting = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Melting.setFont(font)
        self.Melting.setStyleSheet("color: rgb(0, 255, 255);")
        self.Melting.setObjectName("Melting")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Melting)
        self.label_8 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.Boiling = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Boiling.setFont(font)
        self.Boiling.setStyleSheet("color: rgb(0, 255, 255);")
        self.Boiling.setObjectName("Boiling")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Boiling)
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.Year = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Year.setFont(font)
        self.Year.setStyleSheet("color: rgb(0, 255, 255);")
        self.Year.setObjectName("Year")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Year)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.Discoverer = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Discoverer.setFont(font)
        self.Discoverer.setStyleSheet("color: rgb(0, 255, 255);")
        self.Discoverer.setObjectName("Discoverer")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Discoverer)
        self.label_9 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.Energy = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Energy.setFont(font)
        self.Energy.setStyleSheet("color: rgb(0, 255, 255);")
        self.Energy.setObjectName("Energy")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.Energy)
        self.label_10 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.Section = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Section.setFont(font)
        self.Section.setStyleSheet("color: rgb(0, 255, 255);")
        self.Section.setText("")
        self.Section.setFlat(True)
        self.Section.setObjectName("Section")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.Section)
        self.verticalLayout.addLayout(self.formLayout)
        self.back = QtWidgets.QPushButton(Form)
        self.back.setMinimumSize(QtCore.QSize(75, 23))
        self.back.setMaximumSize(QtCore.QSize(75, 23))
        self.back.setStyleSheet("color: rgb(0, 255, 255);\n"
"background-color: rgb(75, 75, 75);\n"
"")
        self.back.setObjectName("back")
        self.verticalLayout.addWidget(self.back)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Дополнительная информация"))
        self.label_2.setText(_translate("Form", "Период, Группа"))
        self.label_5.setText(_translate("Form", "Атомная масса(а.е.м.)"))
        self.label_4.setText(_translate("Form", "Плотность г/см3"))
        self.label_7.setText(_translate("Form", "Температура плавления"))
        self.label_8.setText(_translate("Form", "Температура кипения"))
        self.label_6.setText(_translate("Form", "Год открытия"))
        self.label_3.setText(_translate("Form", "Первооткрываетль"))
        self.label_9.setText(_translate("Form", "Энергетические уровни"))
        self.label_10.setText(_translate("Form", "Статья"))
        self.back.setText(_translate("Form", "Назад"))
