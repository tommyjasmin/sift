# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_image_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ExportImageDialog(object):
    def setupUi(self, ExportImageDialog):
        ExportImageDialog.setObjectName(_fromUtf8("ExportImageDialog"))
        ExportImageDialog.resize(340, 416)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ExportImageDialog.sizePolicy().hasHeightForWidth())
        ExportImageDialog.setSizePolicy(sizePolicy)
        ExportImageDialog.setStyleSheet(_fromUtf8(""))
        self.buttonBox = QtGui.QDialogButtonBox(ExportImageDialog)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(10, 370, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.frameRangeGroupBox = QtGui.QGroupBox(ExportImageDialog)
        self.frameRangeGroupBox.setGeometry(QtCore.QRect(10, 30, 321, 111))
        self.frameRangeGroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frameRangeGroupBox.setFlat(False)
        self.frameRangeGroupBox.setCheckable(False)
        self.frameRangeGroupBox.setObjectName(_fromUtf8("frameRangeGroupBox"))
        self.frameCurrentRadio = QtGui.QRadioButton(self.frameRangeGroupBox)
        self.frameCurrentRadio.setGeometry(QtCore.QRect(10, 20, 121, 21))
        self.frameCurrentRadio.setChecked(True)
        self.frameCurrentRadio.setObjectName(_fromUtf8("frameCurrentRadio"))
        self.frameAllRadio = QtGui.QRadioButton(self.frameRangeGroupBox)
        self.frameAllRadio.setGeometry(QtCore.QRect(10, 50, 100, 21))
        self.frameAllRadio.setObjectName(_fromUtf8("frameAllRadio"))
        self.frameRangeRadio = QtGui.QRadioButton(self.frameRangeGroupBox)
        self.frameRangeRadio.setGeometry(QtCore.QRect(10, 80, 100, 21))
        self.frameRangeRadio.setObjectName(_fromUtf8("frameRangeRadio"))
        self.label = QtGui.QLabel(self.frameRangeGroupBox)
        self.label.setGeometry(QtCore.QRect(110, 80, 41, 21))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.frameRangeFrom = QtGui.QLineEdit(self.frameRangeGroupBox)
        self.frameRangeFrom.setGeometry(QtCore.QRect(150, 80, 61, 21))
        self.frameRangeFrom.setText(_fromUtf8(""))
        self.frameRangeFrom.setReadOnly(False)
        self.frameRangeFrom.setPlaceholderText(_fromUtf8(""))
        self.frameRangeFrom.setProperty("clearButtonEnabled", False)
        self.frameRangeFrom.setObjectName(_fromUtf8("frameRangeFrom"))
        self.label_2 = QtGui.QLabel(self.frameRangeGroupBox)
        self.label_2.setGeometry(QtCore.QRect(230, 80, 21, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frameRangeTo = QtGui.QLineEdit(self.frameRangeGroupBox)
        self.frameRangeTo.setGeometry(QtCore.QRect(250, 80, 61, 21))
        self.frameRangeTo.setObjectName(_fromUtf8("frameRangeTo"))
        self.includeFooterCheckbox = QtGui.QCheckBox(ExportImageDialog)
        self.includeFooterCheckbox.setGeometry(QtCore.QRect(20, 340, 121, 21))
        self.includeFooterCheckbox.setChecked(True)
        self.includeFooterCheckbox.setObjectName(_fromUtf8("includeFooterCheckbox"))
        self.saveAsLineEdit = QtGui.QLineEdit(ExportImageDialog)
        self.saveAsLineEdit.setGeometry(QtCore.QRect(10, 10, 291, 21))
        self.saveAsLineEdit.setText(_fromUtf8(""))
        self.saveAsLineEdit.setObjectName(_fromUtf8("saveAsLineEdit"))
        self.saveAsButton = QtGui.QPushButton(ExportImageDialog)
        self.saveAsButton.setGeometry(QtCore.QRect(300, 10, 31, 21))
        self.saveAsButton.setObjectName(_fromUtf8("saveAsButton"))
        self.animationGroupBox = QtGui.QGroupBox(ExportImageDialog)
        self.animationGroupBox.setGeometry(QtCore.QRect(10, 140, 141, 61))
        self.animationGroupBox.setObjectName(_fromUtf8("animationGroupBox"))
        self.loopRadio = QtGui.QRadioButton(self.animationGroupBox)
        self.loopRadio.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.loopRadio.setChecked(True)
        self.loopRadio.setObjectName(_fromUtf8("loopRadio"))
        self.rockRadio = QtGui.QRadioButton(self.animationGroupBox)
        self.rockRadio.setGeometry(QtCore.QRect(80, 30, 61, 18))
        self.rockRadio.setObjectName(_fromUtf8("rockRadio"))
        self.frameDelayGroup = QtGui.QGroupBox(ExportImageDialog)
        self.frameDelayGroup.setGeometry(QtCore.QRect(10, 200, 261, 131))
        self.frameDelayGroup.setObjectName(_fromUtf8("frameDelayGroup"))
        self.timeLapseRadio = QtGui.QRadioButton(self.frameDelayGroup)
        self.timeLapseRadio.setGeometry(QtCore.QRect(10, 30, 97, 21))
        self.timeLapseRadio.setChecked(True)
        self.timeLapseRadio.setObjectName(_fromUtf8("timeLapseRadio"))
        self.constantDelayRadio = QtGui.QRadioButton(self.frameDelayGroup)
        self.constantDelayRadio.setGeometry(QtCore.QRect(10, 60, 81, 21))
        self.constantDelayRadio.setObjectName(_fromUtf8("constantDelayRadio"))
        self.constantDelaySpin = QtGui.QSpinBox(self.frameDelayGroup)
        self.constantDelaySpin.setGeometry(QtCore.QRect(90, 60, 81, 21))
        self.constantDelaySpin.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.constantDelaySpin.setFrame(True)
        self.constantDelaySpin.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.constantDelaySpin.setAccelerated(True)
        self.constantDelaySpin.setKeyboardTracking(True)
        self.constantDelaySpin.setMinimum(25)
        self.constantDelaySpin.setMaximum(5000)
        self.constantDelaySpin.setObjectName(_fromUtf8("constantDelaySpin"))
        self.fpsDelayRadio = QtGui.QRadioButton(self.frameDelayGroup)
        self.fpsDelayRadio.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.fpsDelayRadio.setObjectName(_fromUtf8("fpsDelayRadio"))
        self.fpsDelaySpin = QtGui.QSpinBox(self.frameDelayGroup)
        self.fpsDelaySpin.setGeometry(QtCore.QRect(90, 90, 81, 21))
        self.fpsDelaySpin.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fpsDelaySpin.setFrame(True)
        self.fpsDelaySpin.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.fpsDelaySpin.setAccelerated(True)
        self.fpsDelaySpin.setKeyboardTracking(True)
        self.fpsDelaySpin.setSuffix(_fromUtf8(""))
        self.fpsDelaySpin.setMinimum(1)
        self.fpsDelaySpin.setMaximum(60)
        self.fpsDelaySpin.setProperty("value", 1)
        self.fpsDelaySpin.setObjectName(_fromUtf8("fpsDelaySpin"))
        self.label_3 = QtGui.QLabel(ExportImageDialog)
        self.label_3.setGeometry(QtCore.QRect(150, 340, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.footerFontSizeSpinBox = QtGui.QSpinBox(ExportImageDialog)
        self.footerFontSizeSpinBox.setGeometry(QtCore.QRect(210, 340, 61, 20))
        self.footerFontSizeSpinBox.setMinimum(8)
        self.footerFontSizeSpinBox.setMaximum(72)
        self.footerFontSizeSpinBox.setProperty("value", 11)
        self.footerFontSizeSpinBox.setObjectName(_fromUtf8("footerFontSizeSpinBox"))

        self.retranslateUi(ExportImageDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ExportImageDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ExportImageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExportImageDialog)

    def retranslateUi(self, ExportImageDialog):
        ExportImageDialog.setWindowTitle(_translate("ExportImageDialog", "Export Image", None))
        self.frameRangeGroupBox.setTitle(_translate("ExportImageDialog", "Frame Range", None))
        self.frameCurrentRadio.setText(_translate("ExportImageDialog", "Current", None))
        self.frameAllRadio.setText(_translate("ExportImageDialog", "All", None))
        self.frameRangeRadio.setText(_translate("ExportImageDialog", "Frames", None))
        self.label.setText(_translate("ExportImageDialog", "from:", None))
        self.label_2.setText(_translate("ExportImageDialog", "to:", None))
        self.includeFooterCheckbox.setText(_translate("ExportImageDialog", "Include Footer", None))
        self.saveAsButton.setText(_translate("ExportImageDialog", "...", None))
        self.animationGroupBox.setTitle(_translate("ExportImageDialog", "Animation Type", None))
        self.loopRadio.setText(_translate("ExportImageDialog", "Loop", None))
        self.rockRadio.setText(_translate("ExportImageDialog", "Rock", None))
        self.frameDelayGroup.setTitle(_translate("ExportImageDialog", "Frame Delay", None))
        self.timeLapseRadio.setToolTip(_translate("ExportImageDialog", "delay based on layer observation time", None))
        self.timeLapseRadio.setText(_translate("ExportImageDialog", "Time Lapse", None))
        self.constantDelayRadio.setText(_translate("ExportImageDialog", "Constant:", None))
        self.constantDelaySpin.setSuffix(_translate("ExportImageDialog", "ms", None))
        self.fpsDelayRadio.setText(_translate("ExportImageDialog", "FPS:", None))
        self.label_3.setText(_translate("ExportImageDialog", "Font Size:", None))
        self.footerFontSizeSpinBox.setSuffix(_translate("ExportImageDialog", "px", None))

