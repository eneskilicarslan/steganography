from PyQt5 import QtCore, QtGui, QtWidgets
import funcs


class Ui_MainWindow(object):
    def __init__(self):
        self.name2 = None
        self.name = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1140, 588)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cipherView = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cipherView.sizePolicy().hasHeightForWidth())
        self.cipherView.setSizePolicy(sizePolicy)
        self.cipherView.setMinimumSize(QtCore.QSize(400, 360))
        self.cipherView.setMaximumSize(QtCore.QSize(600, 360))
        self.cipherView.setText("")
        self.cipherView.setObjectName("cipherView")
        self.verticalLayout_2.addWidget(self.cipherView)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.cipherText = QtWidgets.QPlainTextEdit(Dialog)
        self.cipherText.setMinimumSize(QtCore.QSize(0, 50))
        self.cipherText.setMaximumSize(QtCore.QSize(16777215, 160))
        self.cipherText.setObjectName("cipherText")
        self.verticalLayout_2.addWidget(self.cipherText)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.stage = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage.sizePolicy().hasHeightForWidth())
        self.stage.setSizePolicy(sizePolicy)
        self.stage.setMinimumSize(QtCore.QSize(0, 600))
        self.stage.setMaximumSize(QtCore.QSize(50, 16777215))
        self.stage.setObjectName("stage")
        self.horizontalLayout.addWidget(self.stage)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.decipherView = QtWidgets.QLabel(Dialog)
        self.decipherView.setMinimumSize(QtCore.QSize(400, 360))
        self.decipherView.setMaximumSize(QtCore.QSize(600, 360))
        self.decipherView.setText("")
        self.decipherView.setObjectName("decipherView")
        self.verticalLayout.addWidget(self.decipherView)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.cipheredText = QtWidgets.QPlainTextEdit(Dialog)
        self.cipheredText.setMinimumSize(QtCore.QSize(0, 50))
        self.cipheredText.setMaximumSize(QtCore.QSize(16777215, 80))
        self.cipheredText.setObjectName("cipheredText")
        self.verticalLayout.addWidget(self.cipheredText)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.decipheredText = QtWidgets.QPlainTextEdit(Dialog)
        self.decipheredText.setMinimumSize(QtCore.QSize(0, 50))
        self.decipheredText.setMaximumSize(QtCore.QSize(16777215, 80))
        self.decipheredText.setObjectName("decipheredText")
        self.verticalLayout.addWidget(self.decipheredText)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ############## My Code ################
        self.pushButton.clicked.connect(self.loadImg)
        self.stage.clicked.connect(self.stageClicked)

    def loadImg(self):
        self.name = QtWidgets.QFileDialog.getOpenFileName(None, 'Insert Image', '',
                                                          "Image files (*.jpg *.png *.jpeg *.bmp)")
        self.cipherView.setPixmap(QtGui.QPixmap(self.name[0]))

    def stageClicked(self):
        message = funcs.string_to_binary_string(self.cipherText.toPlainText())
        self.cipheredText.setPlainText(message)
        try:
            self.name2 = funcs.embed_text(self.name[0], message)
            self.decipherView.setPixmap(QtGui.QPixmap(self.name2))
            extract_text = funcs.extract_text(self.name2)
            self.decipheredText.setPlainText(extract_text)
        except Exception as e:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setText("Error: " + str(e))
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)

            returnValue = msgBox.exec()

            print("Error: ", e)
            return

        funcs.compare_images(self.name[0], self.name2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Steganography"))
        self.label.setText(_translate("Dialog", "Text To Cipher into Picture"))
        self.pushButton.setText(_translate("Dialog", "Load From File"))
        self.stage.setText(_translate("Dialog", ">>>"))
        self.label_3.setText(_translate("Dialog", "Binarized Text"))
        self.label_2.setText(_translate("Dialog", "Deciphered Text from Picture"))
        self.cipherView.setPixmap(QtGui.QPixmap("key.jpeg"))
        self.decipherView.setPixmap(QtGui.QPixmap("key.jpeg"))
