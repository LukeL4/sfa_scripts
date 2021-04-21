import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance


def maya_main_window():
    """return the maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class ScatterUI(QtWidgets.QDialog):
    """ Simple UI class"""

    def __init__(self):
        """contructor"""
        # passing the obhect SimpleUI as an argument to support
        # makes this line python 2 and 3 compatible
        super(ScatterUI, self).__init__(parent=maya_main_window())
        self.setWindowTitle("Scatter Tool")
        self.setMinimumWidth(400)
        self.setMinimumHeight(600)
        self.setWindowFlags(self.windowFlags() ^ # ^ means except
                            QtCore.Qt.WindowContextHelpButtonHint) #controls icons like min and max and cancel
        self.create_ui()

    def create_ui(self):
        self.title_lbl = QtWidgets.QLabel("Scatter Tool")
        self.title_lbl.setStyleSheet("font:  bold 20px")

        self.main_lay = QtWidgets.QVBoxLayout() # stacking top to bottom layout group
        self.main_lay.addWidget(self.title_lbl)
        self.setLayout(self.main_lay)