# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pov_main.ui'
#
# Created: Mon Oct 19 21:59:38 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1321, 807)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.panZoomToolButton = QtGui.QToolButton(self.centralwidget)
        self.panZoomToolButton.setObjectName(_fromUtf8("panZoomToolButton"))
        self.horizontalLayout_2.addWidget(self.panZoomToolButton)
        self.pointSelectButton = QtGui.QToolButton(self.centralwidget)
        self.pointSelectButton.setObjectName(_fromUtf8("pointSelectButton"))
        self.horizontalLayout_2.addWidget(self.pointSelectButton)
        self.regionSelectButton = QtGui.QToolButton(self.centralwidget)
        self.regionSelectButton.setObjectName(_fromUtf8("regionSelectButton"))
        self.horizontalLayout_2.addWidget(self.regionSelectButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cursorProbeText = QtGui.QLabel(self.centralwidget)
        self.cursorProbeText.setMinimumSize(QtCore.QSize(240, 0))
        self.cursorProbeText.setMaximumSize(QtCore.QSize(256, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(17, 71, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 71, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 71, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 71, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.cursorProbeText.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Andale Mono"))
        font.setPointSize(14)
        self.cursorProbeText.setFont(font)
        self.cursorProbeText.setObjectName(_fromUtf8("cursorProbeText"))
        self.horizontalLayout_2.addWidget(self.cursorProbeText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.mainWidgets = QtGui.QTabWidget(self.centralwidget)
        self.mainWidgets.setObjectName(_fromUtf8("mainWidgets"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.mainWidgets.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.mainWidgets.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.mainWidgets)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.queueButton = QtGui.QToolButton(self.groupBox)
        self.queueButton.setMinimumSize(QtCore.QSize(0, 0))
        self.queueButton.setObjectName(_fromUtf8("queueButton"))
        self.horizontalLayout.addWidget(self.queueButton)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.progressText = QtGui.QLabel(self.groupBox)
        self.progressText.setMinimumSize(QtCore.QSize(240, 0))
        self.progressText.setMaximumSize(QtCore.QSize(256, 16777215))
        self.progressText.setAlignment(QtCore.Qt.AlignCenter)
        self.progressText.setObjectName(_fromUtf8("progressText"))
        self.verticalLayout_10.addWidget(self.progressText)
        self.progressBar = QtGui.QProgressBar(self.groupBox)
        self.progressBar.setMaximumSize(QtCore.QSize(256, 16777215))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_10.addWidget(self.progressBar)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.animationLabel = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Andale Mono"))
        font.setPointSize(14)
        self.animationLabel.setFont(font)
        self.animationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.animationLabel.setObjectName(_fromUtf8("animationLabel"))
        self.verticalLayout_11.addWidget(self.animationLabel)
        self.animationSlider = QtGui.QSlider(self.groupBox)
        self.animationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.animationSlider.setObjectName(_fromUtf8("animationSlider"))
        self.verticalLayout_11.addWidget(self.animationSlider)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.animBack = QtGui.QToolButton(self.groupBox)
        self.animBack.setToolTip(_fromUtf8(""))
        self.animBack.setObjectName(_fromUtf8("animBack"))
        self.horizontalLayout.addWidget(self.animBack)
        self.animPlayPause = QtGui.QToolButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Andale Mono"))
        font.setPointSize(18)
        font.setItalic(False)
        self.animPlayPause.setFont(font)
        self.animPlayPause.setObjectName(_fromUtf8("animPlayPause"))
        self.horizontalLayout.addWidget(self.animPlayPause)
        self.animForward = QtGui.QToolButton(self.groupBox)
        self.animForward.setObjectName(_fromUtf8("animForward"))
        self.horizontalLayout.addWidget(self.animForward)
        self.verticalLayout_2.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1321, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.probeAPane = QtGui.QDockWidget(MainWindow)
        self.probeAPane.setObjectName(_fromUtf8("probeAPane"))
        self.probeAWidget = QtGui.QWidget()
        self.probeAWidget.setObjectName(_fromUtf8("probeAWidget"))
        self.probeAPane.setWidget(self.probeAWidget)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.probeAPane)
        self.probeBPane = QtGui.QDockWidget(MainWindow)
        self.probeBPane.setObjectName(_fromUtf8("probeBPane"))
        self.probeBWidget = QtGui.QWidget()
        self.probeBWidget.setObjectName(_fromUtf8("probeBWidget"))
        self.probeBPane.setWidget(self.probeBWidget)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.probeBPane)
        self.layersPane = QtGui.QDockWidget(MainWindow)
        self.layersPane.setObjectName(_fromUtf8("layersPane"))
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setObjectName(_fromUtf8("dockWidgetContents_5"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.layerSetTabs = QtGui.QTabWidget(self.dockWidgetContents_5)
        self.layerSetTabs.setObjectName(_fromUtf8("layerSetTabs"))
        self.layerSet1Tab = QtGui.QWidget()
        self.layerSet1Tab.setObjectName(_fromUtf8("layerSet1Tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layerSet1Tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.layerSet1Table = QtGui.QListView(self.layerSet1Tab)
        self.layerSet1Table.setObjectName(_fromUtf8("layerSet1Table"))
        self.verticalLayout_4.addWidget(self.layerSet1Table)
        self.layerSetTabs.addTab(self.layerSet1Tab, _fromUtf8(""))
        self.layerSet2Tab = QtGui.QWidget()
        self.layerSet2Tab.setObjectName(_fromUtf8("layerSet2Tab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layerSet2Tab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.layerSet2Table = QtGui.QListView(self.layerSet2Tab)
        self.layerSet2Table.setObjectName(_fromUtf8("layerSet2Table"))
        self.verticalLayout_5.addWidget(self.layerSet2Table)
        self.layerSetTabs.addTab(self.layerSet2Tab, _fromUtf8(""))
        self.layerSet3Tab = QtGui.QWidget()
        self.layerSet3Tab.setObjectName(_fromUtf8("layerSet3Tab"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layerSet3Tab)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.layerSet3Table = QtGui.QListView(self.layerSet3Tab)
        self.layerSet3Table.setObjectName(_fromUtf8("layerSet3Table"))
        self.verticalLayout_6.addWidget(self.layerSet3Table)
        self.layerSetTabs.addTab(self.layerSet3Tab, _fromUtf8(""))
        self.layerSet4Tab = QtGui.QWidget()
        self.layerSet4Tab.setObjectName(_fromUtf8("layerSet4Tab"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.layerSet4Tab)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.layerSet4Table = QtGui.QListView(self.layerSet4Tab)
        self.layerSet4Table.setObjectName(_fromUtf8("layerSet4Table"))
        self.verticalLayout_7.addWidget(self.layerSet4Table)
        self.layerSetTabs.addTab(self.layerSet4Tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.layerSetTabs)
        self.layersPane.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.layersPane)
        self.layerConfigPane = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layerConfigPane.sizePolicy().hasHeightForWidth())
        self.layerConfigPane.setSizePolicy(sizePolicy)
        self.layerConfigPane.setObjectName(_fromUtf8("layerConfigPane"))
        self.dockWidgetContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.layerNameEdit = QtGui.QLineEdit(self.dockWidgetContents)
        self.layerNameEdit.setObjectName(_fromUtf8("layerNameEdit"))
        self.verticalLayout_8.addWidget(self.layerNameEdit)
        self.colorBarButton = QtGui.QPushButton(self.dockWidgetContents)
        self.colorBarButton.setMinimumSize(QtCore.QSize(0, 32))
        self.colorBarButton.setObjectName(_fromUtf8("colorBarButton"))
        self.verticalLayout_8.addWidget(self.colorBarButton)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.layerConfigPane.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.layerConfigPane)

        self.retranslateUi(MainWindow)
        self.mainWidgets.setCurrentIndex(0)
        self.layerSetTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SIFT Beta Test", None))
        self.panZoomToolButton.setText(_translate("MainWindow", "Pan/Zoom", None))
        self.pointSelectButton.setText(_translate("MainWindow", "Point", None))
        self.regionSelectButton.setText(_translate("MainWindow", "Region", None))
        self.cursorProbeText.setToolTip(_translate("MainWindow", "Value under cursor", None))
        self.cursorProbeText.setStatusTip(_translate("MainWindow", "Selected layer value under cursor", None))
        self.cursorProbeText.setText(_translate("MainWindow", "Cursor Value", None))
        self.mainWidgets.setTabText(self.mainWidgets.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.mainWidgets.setTabText(self.mainWidgets.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.queueButton.setToolTip(_translate("MainWindow", "Show Activity", None))
        self.queueButton.setStatusTip(_translate("MainWindow", "Show activities in progress", None))
        self.queueButton.setText(_translate("MainWindow", "Queue...", None))
        self.progressText.setText(_translate("MainWindow", "idle", None))
        self.progressBar.setToolTip(_translate("MainWindow", "Activity Progress", None))
        self.animationLabel.setText(_translate("MainWindow", "HH:MM", None))
        self.animBack.setStatusTip(_translate("MainWindow", "Step backward", None))
        self.animBack.setText(_translate("MainWindow", "|◀", None))
        self.animPlayPause.setStatusTip(_translate("MainWindow", "Start or stop animation", None))
        self.animPlayPause.setText(_translate("MainWindow", "▶", None))
        self.animForward.setStatusTip(_translate("MainWindow", "Step forward", None))
        self.animForward.setText(_translate("MainWindow", "▶|", None))
        self.probeAPane.setWindowTitle(_translate("MainWindow", "A Probe", None))
        self.probeBPane.setWindowTitle(_translate("MainWindow", "B Probe", None))
        self.layersPane.setWindowTitle(_translate("MainWindow", "Layers", None))
        self.layerSetTabs.setToolTip(_translate("MainWindow", "Alternate layer sets", None))
        self.layerSetTabs.setStatusTip(_translate("MainWindow", "Select alternate layer set", None))
        self.layerSet1Table.setStatusTip(_translate("MainWindow", "Current layers", None))
        self.layerSetTabs.setTabText(self.layerSetTabs.indexOf(self.layerSet1Tab), _translate("MainWindow", "1", None))
        self.layerSetTabs.setTabToolTip(self.layerSetTabs.indexOf(self.layerSet1Tab), _translate("MainWindow", "Layer Set 1", None))
        self.layerSetTabs.setTabText(self.layerSetTabs.indexOf(self.layerSet2Tab), _translate("MainWindow", "2", None))
        self.layerSetTabs.setTabToolTip(self.layerSetTabs.indexOf(self.layerSet2Tab), _translate("MainWindow", "Layer Set 2", None))
        self.layerSetTabs.setTabText(self.layerSetTabs.indexOf(self.layerSet3Tab), _translate("MainWindow", "3", None))
        self.layerSetTabs.setTabToolTip(self.layerSetTabs.indexOf(self.layerSet3Tab), _translate("MainWindow", "Layer Set 3", None))
        self.layerSetTabs.setTabText(self.layerSetTabs.indexOf(self.layerSet4Tab), _translate("MainWindow", "4", None))
        self.layerSetTabs.setTabToolTip(self.layerSetTabs.indexOf(self.layerSet4Tab), _translate("MainWindow", "Layer Set 4", None))
        self.layerConfigPane.setStatusTip(_translate("MainWindow", "Selected layer information", None))
        self.layerConfigPane.setWindowTitle(_translate("MainWindow", "Layer Details", None))
        self.layerNameEdit.setText(_translate("MainWindow", "Layer Name", None))
        self.colorBarButton.setText(_translate("MainWindow", "ColorBar", None))

