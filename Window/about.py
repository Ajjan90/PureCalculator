from PySide6 import QtWidgets, QtCore, QtGui
import qtawesome as qta

buttonHeight = 45

class AboutDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        TitleFont = QtGui.QFont("Arial", 15)
        TitleFont.setBold(True)

        versFont = QtGui.QFont("Arial", 9)

        self.setWindowTitle("About PureCalculator")
        self.setModal(True)
        self.setWindowIcon(QtGui.QIcon("PiMaths1.ico"))
        self.setFixedSize(400, 300)

        self.MainLayout = QtWidgets.QVBoxLayout(self)

        # Load the calculator logo
        CalLogo = QtGui.QPixmap("PiMaths1.ico")

        # Display the logo using a QLabel
        self.LogoLabel = QtWidgets.QLabel()
        self.LogoLabel.setPixmap(CalLogo.scaled(
            128, 128, 
            QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation
            ))
        self.LogoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.AppLbl = QtWidgets.QLabel("PureCalculator")
        self.AppLbl.setFont(TitleFont)
        self.AppLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.verLbl = QtWidgets.QLabel("v1.0")
        self.verLbl.setFont(versFont)
        self.verLbl.setStyleSheet("color: gray;")
        self.verLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.gitBtn = QtWidgets.QPushButton(" Github")
        self.gitBtn.setIcon(qta.icon("fa6b.github"))
        self.gitBtn.setFixedHeight(buttonHeight)
        self.gitBtn.clicked.connect(self.OpenGithubPage)

        self.licBtn = QtWidgets.QPushButton(" MIT License")
        self.licBtn.setIcon(qta.icon("msc.law"))
        self.licBtn.setFixedHeight(buttonHeight)
        self.licBtn.clicked.connect(self.OpenLicensePage)

        self.MainLayout.addWidget(self.LogoLabel)
        self.MainLayout.addWidget(self.AppLbl)
        self.MainLayout.addWidget(self.verLbl)
        self.MainLayout.addWidget(self.gitBtn)
        self.MainLayout.addWidget(self.licBtn)

    def OpenGithubPage(self):
        url = QtCore.QUrl("https://github.com/Ajjan90/PureCalculator")
        QtGui.QDesktopServices.openUrl(url)
    
    def OpenLicensePage(self):
        url = QtCore.QUrl("https://github.com/Ajjan90/PureCalculator/blob/main/LICENSE")
        QtGui.QDesktopServices.openUrl(url)

