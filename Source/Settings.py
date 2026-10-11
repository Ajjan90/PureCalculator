from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QSettings
import qtawesome as qta
from Source.config import Settings

settings = Settings()


class SettingPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        Mainlayout = QtWidgets.QVBoxLayout(self)
        Mainlayout.setContentsMargins(10, 10, 10, 10)

        # The Title
        Lbl = QtWidgets.QLabel("Preferences")
        font = QtGui.QFont("Arial", 14)
        font.setBold(True)
        Lbl.setFont(font)

        # Rounding Contents Card
        roundingInput = QtWidgets.QSpinBox()
        roundingInput.setRange(0, 9)
        roundingInput.setValue(settings.RoundingValue)
        roundingInput.valueChanged.connect(self.ApplyRoundChange)

        roundingContent = self.Additional_Widget("Provide rounding options", roundingInput)
        roundingCard = self.Create_Card("Rounding numbers", roundingContent)

        # Open/Close Side panel at startup
        sideCheck = QtWidgets.QCheckBox("Enable")
        sideCheck.setChecked(settings.SidePanelView)
        sideCheck.checkStateChanged.connect(self.ApplySidepnlChange)

        SidePnlCard = self.Create_Card("Open side panel at startup", sideCheck)

        # Startup calculators
        CalCombo = QtWidgets.QComboBox()
        CalCombo.addItems(["Standard", "Scientific", "Paper Mode"])
        CalCombo.setCurrentText(settings.DefaultCal)
        CalCombo.currentTextChanged.connect(self.ApplyCalChange)

        calLayout = self.Additional_Widget("Select the default calculator", CalCombo)

        CalCard = self.Create_Card("Appearance", calLayout)

        Mainlayout.addWidget(Lbl)
        Mainlayout.addWidget(roundingCard)
        Mainlayout.addWidget(SidePnlCard)
        Mainlayout.addWidget(CalCard)
        Mainlayout.addStretch()

    def ApplyRoundChange(self, value):
        settings.RoundingValue = value

    def ApplySidepnlChange(self, value):
        settings.SidePanelView = value

    def ApplyCalChange(self, value):
        settings.DefaultCal = value

    def Create_Card(self, title, *items):
        base = QtWidgets.QFrame()
        base.setObjectName("card")
        base.setStyleSheet("""
            QFrame#card {
                border: 1px solid gray;
                border-radius: 12px;
            }
        """)

        layout = QtWidgets.QVBoxLayout(base)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        # Card title
        Lbl = QtWidgets.QLabel(title)
        font = QtGui.QFont("Arial", 12)
        Lbl.setFont(font)
        layout.addWidget(Lbl)

        # Add widgets OR layouts
        for item in items:
            if isinstance(item, QtWidgets.QLayout):
                layout.addLayout(item)
            elif isinstance(item, QtWidgets.QWidget):
                layout.addWidget(item)

        return base

    def Additional_Widget(self, txt, widget):
        layoutBase = QtWidgets.QHBoxLayout()
        layoutBase.setObjectName("baseLayout")

        text = QtWidgets.QLabel(txt)
        font = QtGui.QFont("Arial", 10)
        text.setFont(font)
        text.setStyleSheet("color: gray;")

        layoutBase.addWidget(text)
        layoutBase.addStretch()
        layoutBase.addWidget(widget)

        return layoutBase