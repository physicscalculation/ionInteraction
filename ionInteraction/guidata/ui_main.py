# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, Ion_Interaction):
        if not Ion_Interaction.objectName():
            Ion_Interaction.setObjectName(u"Ion_Interaction")
        Ion_Interaction.resize(1301, 702)
        Ion_Interaction.setMinimumSize(QSize(1301, 702))
        Ion_Interaction.setStyleSheet(u"*{\n"
"	border: 0px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"#line{\n"
"	border: 7px solid rgb(44, 49, 58);\n"
"}")
        self.stylesheet = QWidget(Ion_Interaction)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setStyleSheet(u"#main ,#page_main,#page_about{	\n"
"	background-color: rgb(192,192,192);\n"
"}\n"
"\n"
"QLabel {color : #113e68; }\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"/* Top Buttons */\n"
"#toprightbuttons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 0px; }\n"
"#toprightbuttons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 0px; }\n"
"#toprightbuttons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 0px; }\n"
"\n"
"\n"
"\n"
"/* MEnu Buttons */\n"
"#menubutton .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 0px; }\n"
"#menubutton .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 0px; }\n"
"#menubutton .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 0px; }\n"
"\n"
"/* /////////////////////////////"
                        "////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#page_a_composition,#page_formula_a_mat,#page_two_composition,#page_formula_two_mat,#page_anenergy,#page_allenergy,#header_frame,#left_menu,#scrollAreaWidgetContents_7{\n"
"	background-color: rgb(192,192,192);border-style: solid; border-color: #113e68; border-radius: 2px;\n"
"}\n"
"#label_3 { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#label_3 { font: 9pt \"Segoe UI\"; color: rgb(80, 177, 200); font-weight: bold;}\n"
"#left_menu {border-width:1px; border-radius:4px;border-style: solid; border-color: #113e68 }\n"
"#main_body {border-width:1px; border-radius:4px ;border-style: solid; border-color: #113e68}\n"
"#footerdesc QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"#line {border-width:1px; border-radius:4px ;border-style: solid; border-color: #113e68; background-color: #113e68}\n"
"#line_2 {border-width:1px; border-radius:4px ;border-style: solid; "
                        "border-color: #113e68; background-color: #113e68}\n"
"#BtnDownload { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#BtnDownload , #BtnCalculate { font: 14pt \"Segoe UI\"; color: #113E68; font-weight: bold; border-style: solid; border-color: #113e68; background-color:rgba(80, 177, 200, 156); border-radius:8px}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QPushButton:BtnDownload {\n"
"    border: solid;\n"
"    background: rgb(52, 59, 72);\n"
"    color: #113e68;\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(80, 177, 2"
                        "00);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	b"
                        "ackground: rgb(80, 177, 200);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transpare"
                        "nt;\n"
"	padding: 10px;\n"
"    color: 113e68;\n"
"	border-radius: 5px;\n"
"	gridline-color: #113e68;\n"
"	border-bottom: 1px solid #113e68;\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"	border-color: #113e68;\n"
"    color: #113e68;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: #113e68;\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(80, 177, 200);\n"
"}\n"
"\n"
"QHeaderView {\n"
"	background-color: transparent;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(17, 62, 104);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"	color: #fff;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(17, 62, 104);\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(17, 62, 104);\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-colo"
                        "r: rgb(17, 62, 104);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	border:none;\n"
"	border-bottom:2px solid rgba(80, 177, 200, 200);\n"
"	border-radius: 8px;\n"
"	color:#113e68;\n"
"	padding-bottom:7px;\n"
"}\n"
"\n"
"\n"
"QLineEdit::focus {\n"
"	color:#113e68;\n"
"}\n"
"\n"
"/*//////////////////////COMBOBOX/////////////////////////////////////*/\n"
"\n"
"QComboBox {\n"
"	border: 1px  solid #fff;\n"
"	color: #113e68;\n"
"	background-color : rgba(80, 177, 200, 156);\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 13px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/guidata/cil-arrow-bottom.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border: 4px soli"
                        "d #c2dbfe;\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"	font-size:12px;\n"
"	color : #fff;\n"
"	padding: 5px;\n"
"	border-radius: 0px;\n"
"	background-color : rgba(80, 177, 200, 156);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.stylesheet)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.stylesheet)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(300, 16777215))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.left_menu)
        self.slide_menu.setObjectName(u"slide_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slide_menu.sizePolicy().hasHeightForWidth())
        self.slide_menu.setSizePolicy(sizePolicy)
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.logoapp = QFrame(self.slide_menu)
        self.logoapp.setObjectName(u"logoapp")
        self.logoapp.setFrameShape(QFrame.StyledPanel)
        self.logoapp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.logoapp)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 8, 0)
        self.label_3 = QLabel(self.logoapp)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#113e68;\">Ion Interaction</span></p></body></html>")
        self.label_3.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_3)


        self.verticalLayout_5.addWidget(self.logoapp)

        self.scrollArea = QScrollArea(self.slide_menu)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 280, 631))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_7.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_7.setSizePolicy(sizePolicy1)
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents_7)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 630))
        self.frame.setToolTipDuration(-7)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setSpacing(9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(274, 306))
        self.frame_3.setMaximumSize(QSize(274, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ionRspLine = QFrame(self.frame_3)
        self.ionRspLine.setObjectName(u"ionRspLine")
        self.ionRspLine.setMinimumSize(QSize(0, 10))
        palette = QPalette()
        brush = QBrush(QColor(17, 62, 104, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush)
        brush2 = QBrush(QColor(8, 31, 52, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        brush3 = QBrush(QColor(239, 239, 239, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        brush4 = QBrush(QColor(145, 145, 145, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        self.ionRspLine.setPalette(palette)
        self.ionRspLine.setLineWidth(1)
        self.ionRspLine.setFrameShape(QFrame.HLine)
        self.ionRspLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.ionRspLine)

        self.RSPorMSPlabel_5 = QLabel(self.frame_3)
        self.RSPorMSPlabel_5.setObjectName(u"RSPorMSPlabel_5")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        self.RSPorMSPlabel_5.setPalette(palette1)
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.RSPorMSPlabel_5.setFont(font1)
        self.RSPorMSPlabel_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.RSPorMSPlabel_5)

        self.CmbMethod = QComboBox(self.frame_3)
        self.CmbMethod.addItem("")
        self.CmbMethod.addItem("")
        self.CmbMethod.setObjectName(u"CmbMethod")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.CmbMethod.sizePolicy().hasHeightForWidth())
        self.CmbMethod.setSizePolicy(sizePolicy2)
        self.CmbMethod.setMinimumSize(QSize(0, 30))
        self.CmbMethod.setMaximumSize(QSize(16777215, 30))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush5 = QBrush(QColor(80, 177, 200, 156))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.CmbMethod.setPalette(palette2)
        self.CmbMethod.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.CmbMethod.setLayoutDirection(Qt.LeftToRight)
        self.CmbMethod.setAutoFillBackground(False)
        self.CmbMethod.setInsertPolicy(QComboBox.InsertAfterCurrent)
        self.CmbMethod.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.CmbMethod.setDuplicatesEnabled(False)
        self.CmbMethod.setFrame(True)

        self.verticalLayout_6.addWidget(self.CmbMethod, 0, Qt.AlignVCenter)

        self.line_6 = QFrame(self.frame_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_6)

        self.line_7 = QFrame(self.frame_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_7)

        self.FormulaOrCompositionlabel_5 = QLabel(self.frame_3)
        self.FormulaOrCompositionlabel_5.setObjectName(u"FormulaOrCompositionlabel_5")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        self.FormulaOrCompositionlabel_5.setPalette(palette3)
        self.FormulaOrCompositionlabel_5.setFont(font1)
        self.FormulaOrCompositionlabel_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.FormulaOrCompositionlabel_5)

        self.CmbChemical = QComboBox(self.frame_3)
        self.CmbChemical.addItem("")
        self.CmbChemical.addItem("")
        self.CmbChemical.setObjectName(u"CmbChemical")
        sizePolicy2.setHeightForWidth(self.CmbChemical.sizePolicy().hasHeightForWidth())
        self.CmbChemical.setSizePolicy(sizePolicy2)
        self.CmbChemical.setMinimumSize(QSize(0, 30))
        self.CmbChemical.setMaximumSize(QSize(16777215, 30))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.CmbChemical.setPalette(palette4)
        self.CmbChemical.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.CmbChemical.setLayoutDirection(Qt.LeftToRight)
        self.CmbChemical.setAutoFillBackground(False)
        self.CmbChemical.setInsertPolicy(QComboBox.InsertAfterCurrent)
        self.CmbChemical.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.CmbChemical.setDuplicatesEnabled(False)
        self.CmbChemical.setFrame(True)

        self.verticalLayout_6.addWidget(self.CmbChemical, 0, Qt.AlignVCenter)

        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(200, 200))
        self.stackedWidget.setMaximumSize(QSize(16777215, 200))
        self.stackedWidget.setLineWidth(1)
        self.page_formula_a_mat = QWidget()
        self.page_formula_a_mat.setObjectName(u"page_formula_a_mat")
        self.page_formula_a_mat.setMaximumSize(QSize(16777215, 16777215))
        palette5 = QPalette()
        brush6 = QBrush(QColor(192, 192, 192, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.page_formula_a_mat.setPalette(palette5)
        self.verticalLayout_8 = QVBoxLayout(self.page_formula_a_mat)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 0, -1, 125)
        self.label_7 = QLabel(self.page_formula_a_mat)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(12)
        self.label_7.setFont(font2)

        self.verticalLayout_22.addWidget(self.label_7)

        self.LneChemicalFormula = QLineEdit(self.page_formula_a_mat)
        self.LneChemicalFormula.setObjectName(u"LneChemicalFormula")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.LneChemicalFormula.sizePolicy().hasHeightForWidth())
        self.LneChemicalFormula.setSizePolicy(sizePolicy4)
        self.LneChemicalFormula.setMinimumSize(QSize(0, 0))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 0))
        brush7.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.LneChemicalFormula.setPalette(palette6)
        self.LneChemicalFormula.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.LneChemicalFormula)


        self.verticalLayout_8.addLayout(self.verticalLayout_22)

        self.stackedWidget.addWidget(self.page_formula_a_mat)
        self.page_formula_two_mat = QWidget()
        self.page_formula_two_mat.setObjectName(u"page_formula_two_mat")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.page_formula_two_mat.setPalette(palette7)
        self.verticalLayout_81 = QVBoxLayout(self.page_formula_two_mat)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, 0, -1, 75)
        self.label_71 = QLabel(self.page_formula_two_mat)
        self.label_71.setObjectName(u"label_71")
        sizePolicy3.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy3)
        self.label_71.setFont(font2)

        self.verticalLayout_23.addWidget(self.label_71)

        self.LneChemicalFormula1 = QLineEdit(self.page_formula_two_mat)
        self.LneChemicalFormula1.setObjectName(u"LneChemicalFormula1")
        sizePolicy4.setHeightForWidth(self.LneChemicalFormula1.sizePolicy().hasHeightForWidth())
        self.LneChemicalFormula1.setSizePolicy(sizePolicy4)
        self.LneChemicalFormula1.setMinimumSize(QSize(0, 30))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.LneChemicalFormula1.setPalette(palette8)
        self.LneChemicalFormula1.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.LneChemicalFormula1)

        self.label_72 = QLabel(self.page_formula_two_mat)
        self.label_72.setObjectName(u"label_72")
        sizePolicy3.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy3)
        self.label_72.setFont(font2)

        self.verticalLayout_23.addWidget(self.label_72)

        self.LneChemicalFormula2 = QLineEdit(self.page_formula_two_mat)
        self.LneChemicalFormula2.setObjectName(u"LneChemicalFormula2")
        sizePolicy4.setHeightForWidth(self.LneChemicalFormula2.sizePolicy().hasHeightForWidth())
        self.LneChemicalFormula2.setSizePolicy(sizePolicy4)
        self.LneChemicalFormula2.setMinimumSize(QSize(0, 30))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.LneChemicalFormula2.setPalette(palette9)
        self.LneChemicalFormula2.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.LneChemicalFormula2)


        self.verticalLayout_81.addLayout(self.verticalLayout_23)

        self.stackedWidget.addWidget(self.page_formula_two_mat)
        self.page_a_composition = QWidget()
        self.page_a_composition.setObjectName(u"page_a_composition")
        self.verticalLayout_10 = QVBoxLayout(self.page_a_composition)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_6 = QFrame(self.page_a_composition)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_8eg = QLabel(self.frame_6)
        self.label_8eg.setObjectName(u"label_8eg")
        sizePolicy3.setHeightForWidth(self.label_8eg.sizePolicy().hasHeightForWidth())
        self.label_8eg.setSizePolicy(sizePolicy3)
        self.label_8eg.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_8eg, 0, Qt.AlignTop)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_8, 0, Qt.AlignTop)

        self.Lneacomposition = QLineEdit(self.frame_6)
        self.Lneacomposition.setObjectName(u"Lneacomposition")
        sizePolicy4.setHeightForWidth(self.Lneacomposition.sizePolicy().hasHeightForWidth())
        self.Lneacomposition.setSizePolicy(sizePolicy4)
        self.Lneacomposition.setMinimumSize(QSize(0, 30))

        self.verticalLayout_11.addWidget(self.Lneacomposition, 0, Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_a_composition)
        self.page_two_composition = QWidget()
        self.page_two_composition.setObjectName(u"page_two_composition")
        self.verticalLayout_101 = QVBoxLayout(self.page_two_composition)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.frame_61 = QFrame(self.page_two_composition)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.frame_61)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.label_8eg1 = QLabel(self.frame_61)
        self.label_8eg1.setObjectName(u"label_8eg1")
        sizePolicy3.setHeightForWidth(self.label_8eg1.sizePolicy().hasHeightForWidth())
        self.label_8eg1.setSizePolicy(sizePolicy3)
        self.label_8eg1.setFont(font2)

        self.verticalLayout_111.addWidget(self.label_8eg1, 0, Qt.AlignTop)

        self.LneElements1 = QLineEdit(self.frame_61)
        self.LneElements1.setObjectName(u"LneElements1")
        sizePolicy4.setHeightForWidth(self.LneElements1.sizePolicy().hasHeightForWidth())
        self.LneElements1.setSizePolicy(sizePolicy4)
        self.LneElements1.setMinimumSize(QSize(0, 30))

        self.verticalLayout_111.addWidget(self.LneElements1)

        self.label_8eg2 = QLabel(self.frame_61)
        self.label_8eg2.setObjectName(u"label_8eg2")
        sizePolicy3.setHeightForWidth(self.label_8eg2.sizePolicy().hasHeightForWidth())
        self.label_8eg2.setSizePolicy(sizePolicy3)
        self.label_8eg2.setFont(font2)

        self.verticalLayout_111.addWidget(self.label_8eg2, 0, Qt.AlignTop)

        self.LneElements2 = QLineEdit(self.frame_61)
        self.LneElements2.setObjectName(u"LneElements2")
        sizePolicy4.setHeightForWidth(self.LneElements2.sizePolicy().hasHeightForWidth())
        self.LneElements2.setSizePolicy(sizePolicy4)
        self.LneElements2.setMinimumSize(QSize(0, 30))

        self.verticalLayout_111.addWidget(self.LneElements2, 0, Qt.AlignTop)


        self.verticalLayout_101.addWidget(self.frame_61, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_two_composition)

        self.verticalLayout_6.addWidget(self.stackedWidget, 0, Qt.AlignTop)

        self.RSPorMSPlabel_5.raise_()
        self.CmbMethod.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.CmbChemical.raise_()
        self.stackedWidget.raise_()
        self.ionRspLine.raise_()
        self.FormulaOrCompositionlabel_5.raise_()

        self.verticalLayout_9.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(274, 305))
        self.frame_4.setMaximumSize(QSize(274, 16777215))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush)
        brush8 = QBrush(QColor(25, 93, 156, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush8)
        brush9 = QBrush(QColor(21, 77, 130, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush9)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush10 = QBrush(QColor(11, 41, 69, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush10)
        brush11 = QBrush(QColor(255, 255, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush11)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush12 = QBrush(QColor(255, 255, 220, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush12)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush11)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush12)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush12)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        self.frame_4.setPalette(palette10)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_14, 0, Qt.AlignTop)

        self.CmbSentIon = QComboBox(self.frame_4)
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.addItem("")
        self.CmbSentIon.setObjectName(u"CmbSentIon")
        self.CmbSentIon.setMinimumSize(QSize(0, 30))
        self.CmbSentIon.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_7.addWidget(self.CmbSentIon, 0, Qt.AlignTop)

        self.line_3 = QFrame(self.frame_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_3)

        self.sentIonEnergyLine = QFrame(self.frame_4)
        self.sentIonEnergyLine.setObjectName(u"sentIonEnergyLine")
        self.sentIonEnergyLine.setMinimumSize(QSize(25, 0))
        self.sentIonEnergyLine.setMaximumSize(QSize(16777215, 16777215))
        self.sentIonEnergyLine.setFrameShape(QFrame.HLine)
        self.sentIonEnergyLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.sentIonEnergyLine)

        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_12)

        self.CmbEnergy = QComboBox(self.frame_4)
        self.CmbEnergy.addItem("")
        self.CmbEnergy.addItem("")
        self.CmbEnergy.setObjectName(u"CmbEnergy")
        self.CmbEnergy.setMinimumSize(QSize(0, 30))
        self.CmbEnergy.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_7.addWidget(self.CmbEnergy)

        self.stackedWidget_2 = QStackedWidget(self.frame_4)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMaximumSize(QSize(282, 150))
        self.page_allenergy = QWidget()
        self.page_allenergy.setObjectName(u"page_allenergy")
        self.verticalLayout_12 = QVBoxLayout(self.page_allenergy)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, -1, -1, 30)
        self.gridLayout_79 = QGridLayout()
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.gridLayout_79.setContentsMargins(-1, -1, -1, 30)
        self.label_139 = QLabel(self.page_allenergy)
        self.label_139.setObjectName(u"label_139")
        sizePolicy3.setHeightForWidth(self.label_139.sizePolicy().hasHeightForWidth())
        self.label_139.setSizePolicy(sizePolicy3)
        self.label_139.setMinimumSize(QSize(0, 0))
        self.label_139.setMaximumSize(QSize(16777215, 200))
        self.label_139.setFont(font2)
        self.label_139.setAlignment(Qt.AlignCenter)

        self.gridLayout_79.addWidget(self.label_139, 0, 0, 1, 1, Qt.AlignVCenter)


        self.gridLayout_8.addLayout(self.gridLayout_79, 0, 0, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_8)

        self.stackedWidget_2.addWidget(self.page_allenergy)
        self.page_anenergy = QWidget()
        self.page_anenergy.setObjectName(u"page_anenergy")
        self.verticalLayout_121 = QVBoxLayout(self.page_anenergy)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.gridLayout_81 = QGridLayout()
        self.gridLayout_81.setSpacing(0)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.gridLayout_81.setContentsMargins(-1, -1, -1, 50)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, -1, -1, 30)
        self.label_13 = QLabel(self.page_anenergy)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setFont(font2)

        self.gridLayout_7.addWidget(self.label_13, 0, 0, 1, 1, Qt.AlignVCenter)

        self.LneEnergy = QLineEdit(self.page_anenergy)
        self.LneEnergy.setObjectName(u"LneEnergy")
        sizePolicy4.setHeightForWidth(self.LneEnergy.sizePolicy().hasHeightForWidth())
        self.LneEnergy.setSizePolicy(sizePolicy4)
        self.LneEnergy.setMinimumSize(QSize(0, 30))
        self.LneEnergy.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.LneEnergy, 1, 0, 1, 1)


        self.gridLayout_81.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.verticalLayout_121.addLayout(self.gridLayout_81)

        self.stackedWidget_2.addWidget(self.page_anenergy)

        self.verticalLayout_7.addWidget(self.stackedWidget_2)


        self.verticalLayout_9.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.verticalLayout_21.addWidget(self.frame, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main = QFrame(self.stylesheet)
        self.main.setObjectName(u"main")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menubutton = QFrame(self.header_frame)
        self.menubutton.setObjectName(u"menubutton")
        self.menubutton.setFrameShape(QFrame.StyledPanel)
        self.menubutton.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.menubutton)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.menubutton, 0, Qt.AlignLeft|Qt.AlignTop)

        self.toprightbuttons = QFrame(self.header_frame)
        self.toprightbuttons.setObjectName(u"toprightbuttons")
        self.toprightbuttons.setFrameShape(QFrame.StyledPanel)
        self.toprightbuttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.toprightbuttons)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.toprightbuttons, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body = QFrame(self.main)
        self.main_body.setObjectName(u"main_body")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy5)
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.main_body)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.stackedWidget_3 = QStackedWidget(self.main_body)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.verticalLayout_15 = QVBoxLayout(self.page_main)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_7 = QFrame(self.page_main)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_29 = QLabel(self.frame_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(945, 20))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        self.label_29.setPalette(palette11)
        self.label_29.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_29)

        self.tableWidget_Chemical_Formula = QTableWidget(self.frame_7)
        if (self.tableWidget_Chemical_Formula.columnCount() < 1):
            self.tableWidget_Chemical_Formula.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_Chemical_Formula.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget_Chemical_Formula.rowCount() < 2):
            self.tableWidget_Chemical_Formula.setRowCount(2)
        self.tableWidget_Chemical_Formula.setObjectName(u"tableWidget_Chemical_Formula")
        self.tableWidget_Chemical_Formula.setMaximumSize(QSize(16777215, 120))
        self.tableWidget_Chemical_Formula.setAutoFillBackground(False)
        self.tableWidget_Chemical_Formula.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_Chemical_Formula.setAutoScrollMargin(16)
        self.tableWidget_Chemical_Formula.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_Chemical_Formula.setAlternatingRowColors(False)
        self.tableWidget_Chemical_Formula.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_Chemical_Formula.setRowCount(2)
        self.tableWidget_Chemical_Formula.horizontalHeader().setVisible(True)
        self.tableWidget_Chemical_Formula.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Chemical_Formula.horizontalHeader().setHighlightSections(True)
        self.tableWidget_Chemical_Formula.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_Chemical_Formula.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_Chemical_Formula.verticalHeader().setVisible(True)
        self.tableWidget_Chemical_Formula.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Chemical_Formula.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_16.addWidget(self.tableWidget_Chemical_Formula)


        self.verticalLayout_15.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.page_main)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_30 = QLabel(self.frame_8)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(945, 20))
        self.label_30.setFont(font1)

        self.verticalLayout_18.addWidget(self.label_30)

        self.tableWidget_Variables = QTableWidget(self.frame_8)
        if (self.tableWidget_Variables.columnCount() < 2):
            self.tableWidget_Variables.setColumnCount(2)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_Variables.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_Variables.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        if (self.tableWidget_Variables.rowCount() < 1):
            self.tableWidget_Variables.setRowCount(1)
        self.tableWidget_Variables.setObjectName(u"tableWidget_Variables")
        self.tableWidget_Variables.setMaximumSize(QSize(16777215, 90))
        self.tableWidget_Variables.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_Variables.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_Variables.setRowCount(1)
        self.tableWidget_Variables.setColumnCount(2)
        self.tableWidget_Variables.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_18.addWidget(self.tableWidget_Variables)


        self.verticalLayout_15.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.frame_9 = QFrame(self.page_main)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_31 = QLabel(self.frame_9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)

        self.verticalLayout_17.addWidget(self.label_31)

        self.tableWidget_Results = QTableWidget(self.frame_9)
        if (self.tableWidget_Results.columnCount() < 5):
            self.tableWidget_Results.setColumnCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        if (self.tableWidget_Results.rowCount() < 1):
            self.tableWidget_Results.setRowCount(1)
        self.tableWidget_Results.setObjectName(u"tableWidget_Results")
        self.tableWidget_Results.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_Results.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_Results.setRowCount(1)
        self.tableWidget_Results.setColumnCount(5)
        self.tableWidget_Results.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_17.addWidget(self.tableWidget_Results)


        self.verticalLayout_15.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.page_main)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.BtnCalculate = QPushButton(self.frame_10)
        self.BtnCalculate.setObjectName(u"BtnCalculate")
        self.BtnCalculate.setBaseSize(QSize(0, 0))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.BtnCalculate.setPalette(palette12)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        self.BtnCalculate.setFont(font3)
        self.BtnCalculate.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.BtnCalculate)

        self.BtnDownload = QPushButton(self.frame_10)
        self.BtnDownload.setObjectName(u"BtnDownload")
        self.BtnDownload.setFont(font3)
        self.BtnDownload.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.BtnDownload)


        self.verticalLayout_15.addWidget(self.frame_10)

        self.stackedWidget_3.addWidget(self.page_main)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.stackedWidget_3.addWidget(self.page_about)

        self.verticalLayout_13.addWidget(self.stackedWidget_3)


        self.verticalLayout.addWidget(self.main_body)

        self.footer = QFrame(self.main)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.footerdesc = QFrame(self.footer)
        self.footerdesc.setObjectName(u"footerdesc")
        self.footerdesc.setFrameShape(QFrame.StyledPanel)
        self.footerdesc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.footerdesc)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.footerdesc)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.AutoText)

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.footerdesc, 0, Qt.AlignBottom)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(15, 15))
        self.size_grip.setMaximumSize(QSize(15, 15))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.size_grip)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.size_grip)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/guidata/cil-size-grip.png"))
        self.label.setScaledContents(False)

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main)

        Ion_Interaction.setCentralWidget(self.stylesheet)

        self.retranslateUi(Ion_Interaction)

        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Ion_Interaction)
    # setupUi

    def retranslateUi(self, Ion_Interaction):
        Ion_Interaction.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ion Interaction", None))
        self.RSPorMSPlabel_5.setText(QCoreApplication.translate("MainWindow", u"RSP or MSP", None))
        self.CmbMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"Relative Stopping Power", None))
        self.CmbMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"MSP, Sigma, Z_eff, N_e, and WRSP", None))

        self.CmbMethod.setCurrentText(QCoreApplication.translate("MainWindow", u"Relative Stopping Power", None))
        self.FormulaOrCompositionlabel_5.setText(QCoreApplication.translate("MainWindow", u"Formula or Composition", None))
        self.CmbChemical.setItemText(0, QCoreApplication.translate("MainWindow", u"Chemical formula", None))
        self.CmbChemical.setItemText(1, QCoreApplication.translate("MainWindow", u"Chemical composition", None))

        self.CmbChemical.setCurrentText(QCoreApplication.translate("MainWindow", u"Chemical formula", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Write the chemical formula.", None))
        self.LneChemicalFormula.setText(QCoreApplication.translate("MainWindow", u"H2O", None))
        self.LneChemicalFormula.setPlaceholderText("")
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Write the first chemical formula.", None))
        self.LneChemicalFormula1.setText(QCoreApplication.translate("MainWindow", u"H2O", None))
        self.LneChemicalFormula1.setPlaceholderText("")
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Write the second chemical formula.", None))
        self.LneChemicalFormula2.setText(QCoreApplication.translate("MainWindow", u"H2O", None))
        self.LneChemicalFormula2.setPlaceholderText("")
        self.label_8eg.setText(QCoreApplication.translate("MainWindow", u"The elements in the composition", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"(e.g. 0.1119H0.8881O)", None))
        self.Lneacomposition.setText(QCoreApplication.translate("MainWindow", u"0.1119H0.8881O", None))
        self.Lneacomposition.setPlaceholderText("")
        self.label_8eg1.setText(QCoreApplication.translate("MainWindow", u"The elements in the first composition", None))
        self.LneElements1.setText(QCoreApplication.translate("MainWindow", u"0.1119H0.8881O", None))
        self.LneElements1.setPlaceholderText("")
        self.label_8eg2.setText(QCoreApplication.translate("MainWindow", u"The elements in the second composition", None))
        self.LneElements2.setText(QCoreApplication.translate("MainWindow", u"0.1119H0.8881O", None))
        self.LneElements2.setPlaceholderText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"SentIon (Al, Be, Cl, Cu, H, Li, etc.)", None))
        self.CmbSentIon.setItemText(0, QCoreApplication.translate("MainWindow", u"Al", None))
        self.CmbSentIon.setItemText(1, QCoreApplication.translate("MainWindow", u"Be", None))
        self.CmbSentIon.setItemText(2, QCoreApplication.translate("MainWindow", u"Cl", None))
        self.CmbSentIon.setItemText(3, QCoreApplication.translate("MainWindow", u"Cu", None))
        self.CmbSentIon.setItemText(4, QCoreApplication.translate("MainWindow", u"H", None))
        self.CmbSentIon.setItemText(5, QCoreApplication.translate("MainWindow", u"Li", None))
        self.CmbSentIon.setItemText(6, QCoreApplication.translate("MainWindow", u"N", None))
        self.CmbSentIon.setItemText(7, QCoreApplication.translate("MainWindow", u"Ni", None))
        self.CmbSentIon.setItemText(8, QCoreApplication.translate("MainWindow", u"S", None))
        self.CmbSentIon.setItemText(9, QCoreApplication.translate("MainWindow", u"Ti", None))
        self.CmbSentIon.setItemText(10, QCoreApplication.translate("MainWindow", u"Ar", None))
        self.CmbSentIon.setItemText(11, QCoreApplication.translate("MainWindow", u"C", None))
        self.CmbSentIon.setItemText(12, QCoreApplication.translate("MainWindow", u"Co", None))
        self.CmbSentIon.setItemText(13, QCoreApplication.translate("MainWindow", u"F", None))
        self.CmbSentIon.setItemText(14, QCoreApplication.translate("MainWindow", u"He", None))
        self.CmbSentIon.setItemText(15, QCoreApplication.translate("MainWindow", u"Mg", None))
        self.CmbSentIon.setItemText(16, QCoreApplication.translate("MainWindow", u"Na", None))
        self.CmbSentIon.setItemText(17, QCoreApplication.translate("MainWindow", u"O", None))
        self.CmbSentIon.setItemText(18, QCoreApplication.translate("MainWindow", u"Sc", None))
        self.CmbSentIon.setItemText(19, QCoreApplication.translate("MainWindow", u"V", None))
        self.CmbSentIon.setItemText(20, QCoreApplication.translate("MainWindow", u"B", None))
        self.CmbSentIon.setItemText(21, QCoreApplication.translate("MainWindow", u"Ca", None))
        self.CmbSentIon.setItemText(22, QCoreApplication.translate("MainWindow", u"Cr", None))
        self.CmbSentIon.setItemText(23, QCoreApplication.translate("MainWindow", u"Fe", None))
        self.CmbSentIon.setItemText(24, QCoreApplication.translate("MainWindow", u"K", None))
        self.CmbSentIon.setItemText(25, QCoreApplication.translate("MainWindow", u"Mn", None))
        self.CmbSentIon.setItemText(26, QCoreApplication.translate("MainWindow", u"Ne", None))
        self.CmbSentIon.setItemText(27, QCoreApplication.translate("MainWindow", u"P", None))
        self.CmbSentIon.setItemText(28, QCoreApplication.translate("MainWindow", u"Si", None))
        self.CmbSentIon.setItemText(29, QCoreApplication.translate("MainWindow", u"Zn", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Energy", None))
        self.CmbEnergy.setItemText(0, QCoreApplication.translate("MainWindow", u"Single energy value", None))
        self.CmbEnergy.setItemText(1, QCoreApplication.translate("MainWindow", u"All energy values", None))

        self.label_139.setText(QCoreApplication.translate("MainWindow", u"All energy values", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Energy (keV)", None))
        self.LneEnergy.setText(QCoreApplication.translate("MainWindow", u"500.0", None))
        self.LneEnergy.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Energy (keV)", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Chemical Formula", None))
        ___qtablewidgetitem = self.tableWidget_Chemical_Formula.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Formula", None));
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Variables", None))
        ___qtablewidgetitem1 = self.tableWidget_Variables.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Energy", None));
        ___qtablewidgetitem2 = self.tableWidget_Variables.horizontalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"SentIon", None));
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        ___qtablewidgetitem3 = self.tableWidget_Results.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"MSP Target", None));
        ___qtablewidgetitem4 = self.tableWidget_Results.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Sigma Target", None));
        ___qtablewidgetitem5 = self.tableWidget_Results.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Z_eff", None));
        ___qtablewidgetitem6 = self.tableWidget_Results.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"N_e", None));
        ___qtablewidgetitem7 = self.tableWidget_Results.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"WRSP", None));
        self.BtnCalculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.BtnDownload.setText(QCoreApplication.translate("MainWindow", u"Export Results in Excel Format", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ion Interaction", None))
        self.label.setText("")
    # retranslateUi

