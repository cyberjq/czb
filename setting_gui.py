# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(927, 727)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 781, 722))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.line_44 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_44.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_44.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_44.setObjectName("line_44")
        self.verticalLayout_2.addWidget(self.line_44)

        # Генерируем комбобоксы в лейаут 2
        font = QtGui.QFont()
        font.setPointSize(10)
        items = [str(i + 1) for i in range(16)]
        self.combo_list = []
        for item in items:
            horizontal_layout = QtWidgets.QHBoxLayout()
            horizontal_layout.setContentsMargins(0, 6, 0, 6)
            combo = QComboBox(self.verticalLayoutWidget)
            combo.setMaximumSize(QtCore.QSize(50, 16777215))
            combo.setFont(font)
            combo.addItems(items)
            combo.setCurrentText(item)
            horizontal_layout.addWidget(combo)
            self.combo_list.append(combo)
            self.verticalLayout_2.addLayout(horizontal_layout)
            line = QtWidgets.QFrame(self.verticalLayoutWidget)
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.verticalLayout_2.addWidget(line)


        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_5.addWidget(self.line_3)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_5.addWidget(self.line_4)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.line_5 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_5.addWidget(self.line_5)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.line_6 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_5.addWidget(self.line_6)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.line_7 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_5.addWidget(self.line_7)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.line_8 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_5.addWidget(self.line_8)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.line_9 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_5.addWidget(self.line_9)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.line_10 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_5.addWidget(self.line_10)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.line_11 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_5.addWidget(self.line_11)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.line_12 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_5.addWidget(self.line_12)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.line_13 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout_5.addWidget(self.line_13)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.line_14 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout_5.addWidget(self.line_14)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_5.addWidget(self.label_17)
        self.line_15 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.verticalLayout_5.addWidget(self.line_15)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_4.addWidget(self.label_19)
        self.line_16 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.verticalLayout_4.addWidget(self.line_16)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBox_16 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_16.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_16.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_16.setFont(font)
        self.spinBox_16.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_16.setReadOnly(False)
        self.spinBox_16.setObjectName("spinBox_16")
        self.horizontalLayout_2.addWidget(self.spinBox_16)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.line_17 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.verticalLayout_4.addWidget(self.line_17)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spinBox_18 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_18.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_18.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_18.setFont(font)
        self.spinBox_18.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_18.setReadOnly(False)
        self.spinBox_18.setObjectName("spinBox_18")
        self.horizontalLayout_4.addWidget(self.spinBox_18)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.line_18 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.verticalLayout_4.addWidget(self.line_18)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.spinBox_19 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_19.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_19.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_19.setFont(font)
        self.spinBox_19.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_19.setReadOnly(False)
        self.spinBox_19.setObjectName("spinBox_19")
        self.horizontalLayout_5.addWidget(self.spinBox_19)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.line_19 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.verticalLayout_4.addWidget(self.line_19)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.spinBox_20 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_20.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_20.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_20.setFont(font)
        self.spinBox_20.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_20.setReadOnly(False)
        self.spinBox_20.setObjectName("spinBox_20")
        self.horizontalLayout_6.addWidget(self.spinBox_20)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.line_20 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.verticalLayout_4.addWidget(self.line_20)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.spinBox_21 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_21.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_21.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_21.setFont(font)
        self.spinBox_21.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_21.setReadOnly(False)
        self.spinBox_21.setObjectName("spinBox_21")
        self.horizontalLayout_7.addWidget(self.spinBox_21)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.line_21 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.verticalLayout_4.addWidget(self.line_21)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.spinBox_22 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_22.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_22.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_22.setFont(font)
        self.spinBox_22.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_22.setReadOnly(False)
        self.spinBox_22.setObjectName("spinBox_22")
        self.horizontalLayout_8.addWidget(self.spinBox_22)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.line_22 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.verticalLayout_4.addWidget(self.line_22)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.spinBox_23 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_23.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_23.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_23.setFont(font)
        self.spinBox_23.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_23.setReadOnly(False)
        self.spinBox_23.setObjectName("spinBox_23")
        self.horizontalLayout_9.addWidget(self.spinBox_23)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.line_30 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.verticalLayout_4.addWidget(self.line_30)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.spinBox_25 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_25.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_25.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_25.setFont(font)
        self.spinBox_25.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_25.setReadOnly(False)
        self.spinBox_25.setObjectName("spinBox_25")
        self.horizontalLayout_11.addWidget(self.spinBox_25)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.line_23 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.verticalLayout_4.addWidget(self.line_23)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.spinBox_24 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_24.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_24.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_24.setFont(font)
        self.spinBox_24.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_24.setReadOnly(False)
        self.spinBox_24.setObjectName("spinBox_24")
        self.horizontalLayout_10.addWidget(self.spinBox_24)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.line_29 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_29.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.verticalLayout_4.addWidget(self.line_29)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.spinBox_26 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_26.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_26.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_26.setFont(font)
        self.spinBox_26.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_26.setReadOnly(False)
        self.spinBox_26.setObjectName("spinBox_26")
        self.horizontalLayout_12.addWidget(self.spinBox_26)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.line_28 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.verticalLayout_4.addWidget(self.line_28)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.spinBox_27 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_27.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_27.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_27.setFont(font)
        self.spinBox_27.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_27.setReadOnly(False)
        self.spinBox_27.setObjectName("spinBox_27")
        self.horizontalLayout_13.addWidget(self.spinBox_27)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.line_26 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.verticalLayout_4.addWidget(self.line_26)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.spinBox_28 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_28.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_28.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_28.setFont(font)
        self.spinBox_28.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_28.setReadOnly(False)
        self.spinBox_28.setObjectName("spinBox_28")
        self.horizontalLayout_14.addWidget(self.spinBox_28)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.line_27 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.verticalLayout_4.addWidget(self.line_27)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.spinBox_29 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_29.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_29.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_29.setFont(font)
        self.spinBox_29.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_29.setReadOnly(False)
        self.spinBox_29.setObjectName("spinBox_29")
        self.horizontalLayout_15.addWidget(self.spinBox_29)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.line_25 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_25.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.verticalLayout_4.addWidget(self.line_25)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.spinBox_30 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_30.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_30.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_30.setFont(font)
        self.spinBox_30.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_30.setReadOnly(False)
        self.spinBox_30.setObjectName("spinBox_30")
        self.horizontalLayout_16.addWidget(self.spinBox_30)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.line_24 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.verticalLayout_4.addWidget(self.line_24)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.spinBox_31 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_31.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_31.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_31.setFont(font)
        self.spinBox_31.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_31.setReadOnly(False)
        self.spinBox_31.setObjectName("spinBox_31")
        self.horizontalLayout_17.addWidget(self.spinBox_31)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_3.addWidget(self.label_20)
        self.line_32 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_32.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_32.setObjectName("line_32")
        self.verticalLayout_3.addWidget(self.line_32)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_33 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setObjectName("line_33")
        self.verticalLayout.addWidget(self.line_33)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButtonSetting = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSetting.sizePolicy().hasHeightForWidth())
        self.pushButtonSetting.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonSetting.setFont(font)
        self.pushButtonSetting.setObjectName("pushButtonSetting")
        self.horizontalLayout_3.addWidget(self.pushButtonSetting)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройки плагина"))
        self.label.setText(_translate("Dialog", "Выберете подходящие настройки:"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Приоритет </p><p align=\"center\">выделения</p><p align=\"center\"> цвета</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Название настройки</p></body></html>"))
        self.label_4.setText(_translate("Dialog", "Длина предложения"))
        self.label_5.setText(_translate("Dialog", "Количество запятых"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p>Количество других знаков препинания</p></body></html>"))
        self.label_7.setText(_translate("Dialog", "Количество существительных"))
        self.label_8.setText(_translate("Dialog", "Количество глаголов"))
        self.label_9.setText(_translate("Dialog", "Количество пригательных"))
        self.label_13.setText(_translate("Dialog", "Количество местоимений"))
        self.label_10.setText(_translate("Dialog", "Количество наречий"))
        self.label_11.setText(_translate("Dialog", "Количество причастий"))
        self.label_12.setText(_translate("Dialog", "Количество деепричастий"))
        self.label_14.setText(_translate("Dialog", "Количество союзов"))
        self.label_15.setText(_translate("Dialog", "Количество частиц"))
        self.label_16.setText(_translate("Dialog", "Количество компаративов"))
        self.label_17.setText(_translate("Dialog", "Количество числительных"))
        self.label_18.setText(_translate("Dialog", "Количество цифр"))
        self.label_19.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Количество</p></body></html>"))
        self.label_20.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Цвета предложений</p></body></html>"))
        self.pushButtonSetting.setText(_translate("Dialog", "Принять настройки"))