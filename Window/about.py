from PySide6 import QtWidgets, QtCore, QtGui
import qtawesome as qta

buttonHeight = 45

class AboutDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Define the title font type with bold enabled
        TitleFont = QtGui.QFont("Arial", 15)
        TitleFont.setBold(True)

        # Define the version font type
        versFont = QtGui.QFont("Arial", 9)

        # Initalzing the window/dialog
        self.setWindowTitle("About PureCalculator")
        self.setModal(True)
        self.setWindowIcon(QtGui.QIcon("PiMaths1.ico")) # Use the PureCalculator app icon
        self.setFixedSize(400, 300)

        # Create the main layout frame
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

        # Creating the title for the name of the calculator app
        self.AppLbl = QtWidgets.QLabel("PureCalculator")
        self.AppLbl.setFont(TitleFont)
        self.AppLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        # To display the version 
        self.verLbl = QtWidgets.QLabel("v1.0")
        self.verLbl.setFont(versFont)
        self.verLbl.setStyleSheet("color: gray;")
        self.verLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        # Create a button that will direct the user to the Github Repo
        self.gitBtn = QtWidgets.QPushButton(" Github")
        self.gitBtn.setIcon(qta.icon("fa6b.github"))
        self.gitBtn.setFixedHeight(buttonHeight)
        self.gitBtn.clicked.connect(self.OpenGithubPage) # Calling the OpenGithubPage() function

        # This button will direct users to the Github Repo's license
        self.licBtn = QtWidgets.QPushButton(" MIT License")
        self.licBtn.setIcon(qta.icon("msc.law"))
        self.licBtn.setFixedHeight(buttonHeight)
        self.licBtn.clicked.connect(self.OpenLicensePage) # Calling the OpenLicensePage() function

        # Apply the widgets into the mainlayout
        self.MainLayout.addWidget(self.LogoLabel)
        self.MainLayout.addWidget(self.AppLbl)
        self.MainLayout.addWidget(self.verLbl)
        self.MainLayout.addWidget(self.gitBtn)
        self.MainLayout.addWidget(self.licBtn)

    # This function will be called to the Github Button
    # which will direct the users to the Github page
    def OpenGithubPage(self):
        url = QtCore.QUrl("https://github.com/Ajjan90/PureCalculator")
        QtGui.QDesktopServices.openUrl(url)


    # This function will be assigned to the license button
    # which will direct the users to the license page of the project
    def OpenLicensePage(self):
        url = QtCore.QUrl("https://github.com/Ajjan90/PureCalculator/blob/main/LICENSE")
        QtGui.QDesktopServices.openUrl(url)

