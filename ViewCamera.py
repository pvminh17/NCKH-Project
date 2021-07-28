# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Drive\PythonProject\NCKH-Project\design\ViewCamera.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UiFrameCameraView(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1360, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.captureImageButton = QtWidgets.QPushButton(Frame)
        self.captureImageButton.setGeometry(QtCore.QRect(390, 620, 101, 23))
        self.captureImageButton.setObjectName("captureImageButton")
        self.saveImageButton = QtWidgets.QPushButton(Frame)
        self.saveImageButton.setGeometry(QtCore.QRect(570, 620, 75, 23))
        self.saveImageButton.setObjectName("saveImageButton")
        self.capturedImage = QtWidgets.QWidget(Frame)
        self.capturedImage.setGeometry(QtCore.QRect(1030, 610, 201, 131))
        self.capturedImage.setObjectName("capturedImage")
        self.toolBox = QtWidgets.QToolBox(Frame)
        self.toolBox.setGeometry(QtCore.QRect(20, 10, 411, 281))
        self.toolBox.setFrameShape(QtWidgets.QFrame.Box)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 409, 237))
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 0, 411, 241))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setText("")
        self.label.setObjectName("label")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 409, 237))
        self.page_2.setObjectName("page_2")
        self.recordPushButton = QtWidgets.QPushButton(self.page_2)
        self.recordPushButton.setGeometry(QtCore.QRect(60, 70, 75, 23))
        self.recordPushButton.setObjectName("recordPushButton")
        self.stopRecordPushButton = QtWidgets.QPushButton(self.page_2)
        self.stopRecordPushButton.setGeometry(QtCore.QRect(190, 70, 75, 23))
        self.stopRecordPushButton.setObjectName("stopRecordPushButton")
        self.filenameLineEdit = QtWidgets.QLineEdit(self.page_2)
        self.filenameLineEdit.setGeometry(QtCore.QRect(110, 110, 181, 20))
        self.filenameLineEdit.setObjectName("filenameLineEdit")
        self.pathLineEdit = QtWidgets.QLineEdit(self.page_2)
        self.pathLineEdit.setGeometry(QtCore.QRect(110, 140, 181, 20))
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.choosePathToolButton = QtWidgets.QToolButton(self.page_2)
        self.choosePathToolButton.setGeometry(QtCore.QRect(300, 140, 25, 21))
        self.choosePathToolButton.setObjectName("choosePathToolButton")
        self.addCamerapushButton = QtWidgets.QPushButton(self.page_2)
        self.addCamerapushButton.setGeometry(QtCore.QRect(60, 30, 131, 23))
        self.addCamerapushButton.setObjectName("addCamerapushButton")
        self.warningSettingpushButton = QtWidgets.QPushButton(self.page_2)
        self.warningSettingpushButton.setGeometry(QtCore.QRect(220, 30, 91, 23))
        self.warningSettingpushButton.setObjectName("warningSettingpushButton")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(46, 110, 51, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(50, 140, 51, 20))
        self.label_8.setObjectName("label_8")
        self.disconnectPushButton = QtWidgets.QPushButton(self.page_2)
        self.disconnectPushButton.setGeometry(QtCore.QRect(230, 200, 161, 23))
        self.disconnectPushButton.setObjectName("disconnectPushButton")
        self.toolBox.addItem(self.page_2, "")
        
        self.toolBox_2 = QtWidgets.QToolBox(Frame)
        self.toolBox_2.setGeometry(QtCore.QRect(470, 10, 411, 281))
        self.toolBox_2.setFrameShape(QtWidgets.QFrame.Box)
        self.toolBox_2.setObjectName("toolBox_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 409, 237))
        self.page_3.setObjectName("page_3")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 411, 241))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setLineWidth(1)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.toolBox_2.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 409, 237))
        self.page_4.setObjectName("page_4")
        self.label_10 = QtWidgets.QLabel(self.page_4)
        self.label_10.setGeometry(QtCore.QRect(50, 140, 51, 20))
        self.label_10.setObjectName("label_10")
        self.pathLineEdit_2 = QtWidgets.QLineEdit(self.page_4)
        self.pathLineEdit_2.setGeometry(QtCore.QRect(110, 140, 181, 20))
        self.pathLineEdit_2.setObjectName("pathLineEdit_2")
        self.stopRecordPushButton_2 = QtWidgets.QPushButton(self.page_4)
        self.stopRecordPushButton_2.setGeometry(QtCore.QRect(190, 70, 75, 23))
        self.stopRecordPushButton_2.setObjectName("stopRecordPushButton_2")
        self.addCamerapushButton_2 = QtWidgets.QPushButton(self.page_4)
        self.addCamerapushButton_2.setGeometry(QtCore.QRect(60, 30, 131, 23))
        self.addCamerapushButton_2.setObjectName("addCamerapushButton_2")
        self.label_9 = QtWidgets.QLabel(self.page_4)
        self.label_9.setGeometry(QtCore.QRect(46, 110, 51, 20))
        self.label_9.setObjectName("label_9")
        self.warningSettingpushButton_2 = QtWidgets.QPushButton(self.page_4)
        self.warningSettingpushButton_2.setGeometry(QtCore.QRect(220, 30, 91, 23))
        self.warningSettingpushButton_2.setObjectName("warningSettingpushButton_2")
        self.filenameLineEdit_2 = QtWidgets.QLineEdit(self.page_4)
        self.filenameLineEdit_2.setGeometry(QtCore.QRect(110, 110, 181, 20))
        self.filenameLineEdit_2.setObjectName("filenameLineEdit_2")
        self.recordPushButton_2 = QtWidgets.QPushButton(self.page_4)
        self.recordPushButton_2.setGeometry(QtCore.QRect(60, 70, 75, 23))
        self.recordPushButton_2.setObjectName("recordPushButton_2")
        self.choosePathToolButton_2 = QtWidgets.QToolButton(self.page_4)
        self.choosePathToolButton_2.setGeometry(QtCore.QRect(300, 140, 25, 21))
        self.choosePathToolButton_2.setObjectName("choosePathToolButton_2")
        self.disconnectPushButton_2 = QtWidgets.QPushButton(self.page_4)
        self.disconnectPushButton_2.setGeometry(QtCore.QRect(230, 200, 161, 23))
        self.disconnectPushButton_2.setObjectName("disconnectPushButton_2")
        self.toolBox_2.addItem(self.page_4, "")
        self.toolBox_3 = QtWidgets.QToolBox(Frame)
        self.toolBox_3.setGeometry(QtCore.QRect(920, 10, 411, 281))
        self.toolBox_3.setFrameShape(QtWidgets.QFrame.Box)
        self.toolBox_3.setObjectName("toolBox_3")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 409, 237))
        self.page_5.setObjectName("page_5")
        self.label_3 = QtWidgets.QLabel(self.page_5)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 411, 241))
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setLineWidth(1)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.toolBox_3.addItem(self.page_5, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 409, 237))
        self.page_6.setObjectName("page_6")
        self.choosePathToolButton_3 = QtWidgets.QToolButton(self.page_6)
        self.choosePathToolButton_3.setGeometry(QtCore.QRect(300, 140, 25, 21))
        self.choosePathToolButton_3.setObjectName("choosePathToolButton_3")
        self.filenameLineEdit_3 = QtWidgets.QLineEdit(self.page_6)
        self.filenameLineEdit_3.setGeometry(QtCore.QRect(110, 110, 181, 20))
        self.filenameLineEdit_3.setObjectName("filenameLineEdit_3")
        self.addCamerapushButton_3 = QtWidgets.QPushButton(self.page_6)
        self.addCamerapushButton_3.setGeometry(QtCore.QRect(60, 30, 131, 23))
        self.addCamerapushButton_3.setObjectName("addCamerapushButton_3")
        self.label_11 = QtWidgets.QLabel(self.page_6)
        self.label_11.setGeometry(QtCore.QRect(46, 110, 51, 20))
        self.label_11.setObjectName("label_11")
        self.pathLineEdit_3 = QtWidgets.QLineEdit(self.page_6)
        self.pathLineEdit_3.setGeometry(QtCore.QRect(110, 140, 181, 20))
        self.pathLineEdit_3.setObjectName("pathLineEdit_3")
        self.warningSettingpushButton_3 = QtWidgets.QPushButton(self.page_6)
        self.warningSettingpushButton_3.setGeometry(QtCore.QRect(220, 30, 91, 23))
        self.warningSettingpushButton_3.setObjectName("warningSettingpushButton_3")
        self.recordPushButton_3 = QtWidgets.QPushButton(self.page_6)
        self.recordPushButton_3.setGeometry(QtCore.QRect(60, 70, 75, 23))
        self.recordPushButton_3.setObjectName("recordPushButton_3")
        self.stopRecordPushButton_3 = QtWidgets.QPushButton(self.page_6)
        self.stopRecordPushButton_3.setGeometry(QtCore.QRect(190, 70, 75, 23))
        self.stopRecordPushButton_3.setObjectName("stopRecordPushButton_3")
        self.label_12 = QtWidgets.QLabel(self.page_6)
        self.label_12.setGeometry(QtCore.QRect(50, 140, 51, 20))
        self.label_12.setObjectName("label_12")
        self.disconnectPushButton_3 = QtWidgets.QPushButton(self.page_6)
        self.disconnectPushButton_3.setGeometry(QtCore.QRect(230, 200, 161, 23))
        self.disconnectPushButton_3.setObjectName("disconnectPushButton_3")
        self.toolBox_3.addItem(self.page_6, "")
        self.toolBox_4 = QtWidgets.QToolBox(Frame)
        self.toolBox_4.setGeometry(QtCore.QRect(20, 300, 411, 281))
        self.toolBox_4.setFrameShape(QtWidgets.QFrame.Box)
        self.toolBox_4.setObjectName("toolBox_4")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setGeometry(QtCore.QRect(0, 0, 409, 237))
        self.page_7.setObjectName("page_7")
        self.label_4 = QtWidgets.QLabel(self.page_7)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 411, 241))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setLineWidth(1)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.toolBox_4.addItem(self.page_7, "")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setGeometry(QtCore.QRect(0, 0, 409, 237))
        self.page_8.setObjectName("page_8")
        self.choosePathToolButton_4 = QtWidgets.QToolButton(self.page_8)
        self.choosePathToolButton_4.setGeometry(QtCore.QRect(300, 140, 25, 21))
        self.choosePathToolButton_4.setObjectName("choosePathToolButton_4")
        self.filenameLineEdit_4 = QtWidgets.QLineEdit(self.page_8)
        self.filenameLineEdit_4.setGeometry(QtCore.QRect(110, 110, 181, 20))
        self.filenameLineEdit_4.setObjectName("filenameLineEdit_4")
        self.addCamerapushButton_4 = QtWidgets.QPushButton(self.page_8)
        self.addCamerapushButton_4.setGeometry(QtCore.QRect(60, 30, 131, 23))
        self.addCamerapushButton_4.setObjectName("addCamerapushButton_4")
        self.label_13 = QtWidgets.QLabel(self.page_8)
        self.label_13.setGeometry(QtCore.QRect(46, 110, 51, 20))
        self.label_13.setObjectName("label_13")
        self.pathLineEdit_4 = QtWidgets.QLineEdit(self.page_8)
        self.pathLineEdit_4.setGeometry(QtCore.QRect(110, 140, 181, 20))
        self.pathLineEdit_4.setObjectName("pathLineEdit_4")
        self.warningSettingpushButton_4 = QtWidgets.QPushButton(self.page_8)
        self.warningSettingpushButton_4.setGeometry(QtCore.QRect(220, 30, 91, 23))
        self.warningSettingpushButton_4.setObjectName("warningSettingpushButton_4")
        self.recordPushButton_4 = QtWidgets.QPushButton(self.page_8)
        self.recordPushButton_4.setGeometry(QtCore.QRect(60, 70, 75, 23))
        self.recordPushButton_4.setObjectName("recordPushButton_4")
        self.stopRecordPushButton_4 = QtWidgets.QPushButton(self.page_8)
        self.stopRecordPushButton_4.setGeometry(QtCore.QRect(190, 70, 75, 23))
        self.stopRecordPushButton_4.setObjectName("stopRecordPushButton_4")
        self.label_14 = QtWidgets.QLabel(self.page_8)
        self.label_14.setGeometry(QtCore.QRect(50, 140, 51, 20))
        self.label_14.setObjectName("label_14")
        self.disconnectPushButton_4 = QtWidgets.QPushButton(self.page_8)
        self.disconnectPushButton_4.setGeometry(QtCore.QRect(230, 200, 161, 23))
        self.disconnectPushButton_4.setObjectName("disconnectPushButton_4")
        self.toolBox_4.addItem(self.page_8, "")
        self.toolBox_5 = QtWidgets.QToolBox(Frame)
        self.toolBox_5.setGeometry(QtCore.QRect(470, 300, 411, 281))
        self.toolBox_5.setFrameShape(QtWidgets.QFrame.Box)
        self.toolBox_5.setObjectName("toolBox_5")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setGeometry(QtCore.QRect(0, 0, 409, 237))
        self.page_9.setObjectName("page_9")
        self.label_5 = QtWidgets.QLabel(self.page_9)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 411, 241))
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setLineWidth(1)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.toolBox_5.addItem(self.page_9, "")
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setGeometry(QtCore.QRect(0, 0, 409, 237))
        self.page_10.setObjectName("page_10")
        self.choosePathToolButton_5 = QtWidgets.QToolButton(self.page_10)
        self.choosePathToolButton_5.setGeometry(QtCore.QRect(300, 140, 25, 21))
        self.choosePathToolButton_5.setObjectName("choosePathToolButton_5")
        self.filenameLineEdit_5 = QtWidgets.QLineEdit(self.page_10)
        self.filenameLineEdit_5.setGeometry(QtCore.QRect(110, 110, 181, 20))
        self.filenameLineEdit_5.setObjectName("filenameLineEdit_5")
        self.addCamerapushButton_5 = QtWidgets.QPushButton(self.page_10)
        self.addCamerapushButton_5.setGeometry(QtCore.QRect(60, 30, 131, 23))
        self.addCamerapushButton_5.setObjectName("addCamerapushButton_5")
        self.label_15 = QtWidgets.QLabel(self.page_10)
        self.label_15.setGeometry(QtCore.QRect(46, 110, 51, 20))
        self.label_15.setObjectName("label_15")
        self.pathLineEdit_5 = QtWidgets.QLineEdit(self.page_10)
        self.pathLineEdit_5.setGeometry(QtCore.QRect(110, 140, 181, 20))
        self.pathLineEdit_5.setObjectName("pathLineEdit_5")
        self.warningSettingpushButton_5 = QtWidgets.QPushButton(self.page_10)
        self.warningSettingpushButton_5.setGeometry(QtCore.QRect(220, 30, 91, 23))
        self.warningSettingpushButton_5.setObjectName("warningSettingpushButton_5")
        self.recordPushButton_5 = QtWidgets.QPushButton(self.page_10)
        self.recordPushButton_5.setGeometry(QtCore.QRect(60, 70, 75, 23))
        self.recordPushButton_5.setObjectName("recordPushButton_5")
        self.stopRecordPushButton_5 = QtWidgets.QPushButton(self.page_10)
        self.stopRecordPushButton_5.setGeometry(QtCore.QRect(190, 70, 75, 23))
        self.stopRecordPushButton_5.setObjectName("stopRecordPushButton_5")
        self.label_16 = QtWidgets.QLabel(self.page_10)
        self.label_16.setGeometry(QtCore.QRect(50, 140, 51, 20))
        self.label_16.setObjectName("label_16")
        self.disconnectPushButton_5 = QtWidgets.QPushButton(self.page_10)
        self.disconnectPushButton_5.setGeometry(QtCore.QRect(230, 200, 161, 23))
        self.disconnectPushButton_5.setObjectName("disconnectPushButton_5")
        self.toolBox_5.addItem(self.page_10, "")
        self.toolBox_6 = QtWidgets.QToolBox(Frame)
        self.toolBox_6.setGeometry(QtCore.QRect(920, 300, 411, 281))
        self.toolBox_6.setFrameShape(QtWidgets.QFrame.Box)
        self.toolBox_6.setObjectName("toolBox_6")
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setGeometry(QtCore.QRect(0, 0, 409, 237))
        self.page_11.setObjectName("page_11")
        self.label_6 = QtWidgets.QLabel(self.page_11)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 411, 241))
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setLineWidth(1)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.toolBox_6.addItem(self.page_11, "")
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setGeometry(QtCore.QRect(0, 0, 409, 237))
        self.page_12.setObjectName("page_12")
        self.choosePathToolButton_6 = QtWidgets.QToolButton(self.page_12)
        self.choosePathToolButton_6.setGeometry(QtCore.QRect(300, 140, 25, 21))
        self.choosePathToolButton_6.setObjectName("choosePathToolButton_6")
        self.filenameLineEdit_6 = QtWidgets.QLineEdit(self.page_12)
        self.filenameLineEdit_6.setGeometry(QtCore.QRect(110, 110, 181, 20))
        self.filenameLineEdit_6.setObjectName("filenameLineEdit_6")
        self.addCamerapushButton_6 = QtWidgets.QPushButton(self.page_12)
        self.addCamerapushButton_6.setGeometry(QtCore.QRect(60, 30, 131, 23))
        self.addCamerapushButton_6.setObjectName("addCamerapushButton_6")
        self.label_17 = QtWidgets.QLabel(self.page_12)
        self.label_17.setGeometry(QtCore.QRect(46, 110, 51, 20))
        self.label_17.setObjectName("label_17")
        self.pathLineEdit_6 = QtWidgets.QLineEdit(self.page_12)
        self.pathLineEdit_6.setGeometry(QtCore.QRect(110, 140, 181, 20))
        self.pathLineEdit_6.setObjectName("pathLineEdit_6")
        self.warningSettingpushButton_6 = QtWidgets.QPushButton(self.page_12)
        self.warningSettingpushButton_6.setGeometry(QtCore.QRect(220, 30, 91, 23))
        self.warningSettingpushButton_6.setObjectName("warningSettingpushButton_6")
        self.recordPushButton_6 = QtWidgets.QPushButton(self.page_12)
        self.recordPushButton_6.setGeometry(QtCore.QRect(60, 70, 75, 23))
        self.recordPushButton_6.setObjectName("recordPushButton_6")
        self.stopRecordPushButton_6 = QtWidgets.QPushButton(self.page_12)
        self.stopRecordPushButton_6.setGeometry(QtCore.QRect(190, 70, 75, 23))
        self.stopRecordPushButton_6.setObjectName("stopRecordPushButton_6")
        self.label_18 = QtWidgets.QLabel(self.page_12)
        self.label_18.setGeometry(QtCore.QRect(50, 140, 51, 20))
        self.label_18.setObjectName("label_18")
        self.disconnectPushButton_6 = QtWidgets.QPushButton(self.page_12)
        self.disconnectPushButton_6.setGeometry(QtCore.QRect(230, 200, 161, 23))
        self.disconnectPushButton_6.setObjectName("disconnectPushButton_6")
        self.toolBox_6.addItem(self.page_12, "")

        self.retranslateUi(Frame)
        self.toolBox.setCurrentIndex(1)
        self.toolBox.layout().setSpacing(0)
        self.toolBox_2.setCurrentIndex(1)
        self.toolBox_2.layout().setSpacing(0)
        self.toolBox_3.setCurrentIndex(1)
        self.toolBox_3.layout().setSpacing(0)
        self.toolBox_4.setCurrentIndex(1)
        self.toolBox_4.layout().setSpacing(0)
        self.toolBox_5.setCurrentIndex(1)
        self.toolBox_5.layout().setSpacing(0)
        self.toolBox_6.setCurrentIndex(1)
        self.toolBox_6.layout().setSpacing(0)
        QtCore.QMetaObject.connectSlotsByName(Frame)

        
    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.captureImageButton.setText(_translate("Frame", "Capture Image"))
        self.saveImageButton.setText(_translate("Frame", "Save Image"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Frame", "Camera x"))
        self.recordPushButton.setText(_translate("Frame", "Record"))
        self.stopRecordPushButton.setText(_translate("Frame", "Stop record"))
        self.pathLineEdit.setText(_translate("Frame", "C:/Video/"))
        self.choosePathToolButton.setText(_translate("Frame", "..."))
        self.addCamerapushButton.setText(_translate("Frame", "Add/Replace Camera"))
        self.warningSettingpushButton.setText(_translate("Frame", "Warning setting"))
        self.label_7.setText(_translate("Frame", "File name:"))
        self.label_8.setText(_translate("Frame", "Path:"))
        self.disconnectPushButton.setText(_translate("Frame", "Disconnet camera"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Frame", "Tùy chọn"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_3), _translate("Frame", "Camera x"))
        self.label_10.setText(_translate("Frame", "Path:"))
        self.pathLineEdit_2.setText(_translate("Frame", "C:/Video/"))
        self.stopRecordPushButton_2.setText(_translate("Frame", "Stop record"))
        self.addCamerapushButton_2.setText(_translate("Frame", "Add/Replace Camera"))
        self.label_9.setText(_translate("Frame", "File name:"))
        self.warningSettingpushButton_2.setText(_translate("Frame", "Warning setting"))
        self.recordPushButton_2.setText(_translate("Frame", "Record"))
        self.choosePathToolButton_2.setText(_translate("Frame", "..."))
        self.disconnectPushButton_2.setText(_translate("Frame", "Disconnet camera"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_4), _translate("Frame", "Tùy chọn"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_5), _translate("Frame", "Camera x"))
        self.choosePathToolButton_3.setText(_translate("Frame", "..."))
        self.addCamerapushButton_3.setText(_translate("Frame", "Add/Replace Camera"))
        self.label_11.setText(_translate("Frame", "File name:"))
        self.pathLineEdit_3.setText(_translate("Frame", "C:/Video/"))
        self.warningSettingpushButton_3.setText(_translate("Frame", "Warning setting"))
        self.recordPushButton_3.setText(_translate("Frame", "Record"))
        self.stopRecordPushButton_3.setText(_translate("Frame", "Stop record"))
        self.label_12.setText(_translate("Frame", "Path:"))
        self.disconnectPushButton_3.setText(_translate("Frame", "Disconnet camera"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_6), _translate("Frame", "Tùy chọn"))
        self.toolBox_4.setItemText(self.toolBox_4.indexOf(self.page_7), _translate("Frame", "Camera x"))
        self.choosePathToolButton_4.setText(_translate("Frame", "..."))
        self.addCamerapushButton_4.setText(_translate("Frame", "Add/Replace Camera"))
        self.label_13.setText(_translate("Frame", "File name:"))
        self.pathLineEdit_4.setText(_translate("Frame", "C:/Video/"))
        self.warningSettingpushButton_4.setText(_translate("Frame", "Warning setting"))
        self.recordPushButton_4.setText(_translate("Frame", "Record"))
        self.stopRecordPushButton_4.setText(_translate("Frame", "Stop record"))
        self.label_14.setText(_translate("Frame", "Path:"))
        self.disconnectPushButton_4.setText(_translate("Frame", "Disconnet camera"))
        self.toolBox_4.setItemText(self.toolBox_4.indexOf(self.page_8), _translate("Frame", "Tùy chọn"))
        self.toolBox_5.setItemText(self.toolBox_5.indexOf(self.page_9), _translate("Frame", "Camera x"))
        self.choosePathToolButton_5.setText(_translate("Frame", "..."))
        self.addCamerapushButton_5.setText(_translate("Frame", "Add/Replace Camera"))
        self.label_15.setText(_translate("Frame", "File name:"))
        self.pathLineEdit_5.setText(_translate("Frame", "C:/Video/"))
        self.warningSettingpushButton_5.setText(_translate("Frame", "Warning setting"))
        self.recordPushButton_5.setText(_translate("Frame", "Record"))
        self.stopRecordPushButton_5.setText(_translate("Frame", "Stop record"))
        self.label_16.setText(_translate("Frame", "Path:"))
        self.disconnectPushButton_5.setText(_translate("Frame", "Disconnet camera"))
        self.toolBox_5.setItemText(self.toolBox_5.indexOf(self.page_10), _translate("Frame", "Tùy chọn"))
        self.toolBox_6.setItemText(self.toolBox_6.indexOf(self.page_11), _translate("Frame", "Camera x"))
        self.choosePathToolButton_6.setText(_translate("Frame", "..."))
        self.addCamerapushButton_6.setText(_translate("Frame", "Add/Replace Camera"))
        self.label_17.setText(_translate("Frame", "File name:"))
        self.pathLineEdit_6.setText(_translate("Frame", "C:/Video/"))
        self.warningSettingpushButton_6.setText(_translate("Frame", "Warning setting"))
        self.recordPushButton_6.setText(_translate("Frame", "Record"))
        self.stopRecordPushButton_6.setText(_translate("Frame", "Stop record"))
        self.label_18.setText(_translate("Frame", "Path:"))
        self.disconnectPushButton_6.setText(_translate("Frame", "Disconnet camera"))
        self.toolBox_6.setItemText(self.toolBox_6.indexOf(self.page_12), _translate("Frame", "Tùy chọn"))
