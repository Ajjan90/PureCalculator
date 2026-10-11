from PySide6 import QtCore


class Settings:
    def __init__(self):
        self.settings = QtCore.QSettings("Ajjan09", "PureCalculator")

    @property
    def RoundingValue(self):
        return self.settings.value("RoundingValue", 2, type=int)

    @RoundingValue.setter
    def RoundingValue(self, value):
        self.settings.setValue("RoundingValue", value)

    @property
    def SidePanelView(self):
        return self.settings.value("Side Panel View", True, type=bool)

    @SidePanelView.setter
    def SidePanelView(self, value):
        self.settings.setValue("Side Panel View", value)

    @property
    def AppTheme(self):
        return self.settings.value("AppTheme", "Auto", type=str)

    @AppTheme.setter
    def AppTheme(self, value):
        self.settings.setValue("AppTheme", value)