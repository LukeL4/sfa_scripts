import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import maya.cmds as cmds
import random



# if order length is nto 2 put up message to  select 2 objects


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
        self.setMinimumWidth(275)
        self.setMaximumWidth(275)
        self.setMinimumHeight(300)
        self.setWindowFlags(self.windowFlags() ^ # ^ means except
                            QtCore.Qt.WindowContextHelpButtonHint) #controls icons like min and max and cancel
        self.create_ui()

    def create_ui(self):
        #  labels
        self.title_lbl = QtWidgets.QLabel("Scatter Tool")
        self.title_lbl.setStyleSheet("font:  bold 20px")
        self.random_lbl = QtWidgets.QLabel("Add Randomness")
        self.random_lbl.setStyleSheet("font:  bold 12px")
        self.arg_lbl = QtWidgets.QLabel("Argument")
        self.arg_lbl.setStyleSheet("font:  bold 10px")
        self.min_lbl = QtWidgets.QLabel("Minimum")
        self.min_lbl.setStyleSheet("font:  bold 10px")
        self.max_lbl = QtWidgets.QLabel("Maximum")
        self.max_lbl.setStyleSheet("font:  bold 10px")
        self.rotX_lbl = QtWidgets.QLabel("Rotate X")
        self.rotX_lbl.setStyleSheet("font:  bold 10px")
        self.rotY_lbl = QtWidgets.QLabel("Rotate Y")
        self.rotY_lbl.setStyleSheet("font:  bold 10px")
        self.rotZ_lbl = QtWidgets.QLabel("Rotate Z")
        self.rotZ_lbl.setStyleSheet("font:  bold 10px")
        self.scaleX_lbl = QtWidgets.QLabel("Scale X")
        self.scaleX_lbl.setStyleSheet("font:  bold 10px")
        self.scaleY_lbl = QtWidgets.QLabel("Scale Y")
        self.scaleY_lbl.setStyleSheet("font:  bold 10px")
        self.scaleZ_lbl = QtWidgets.QLabel("Scale Z")
        self.scaleZ_lbl.setStyleSheet("font:  bold 10px")

        self.gridlay = QtWidgets.QGridLayout()
        self.gridlay.addWidget(self.title_lbl, 0, 0)
        self.gridlay.addWidget(self.random_lbl, 1, 0)
        self.gridlay.addWidget(self.arg_lbl, 2, 0)
        self.gridlay.addWidget(self.min_lbl, 2, 1)
        self.gridlay.addWidget(self.max_lbl, 2, 2)
        self.gridlay.addWidget(self.rotX_lbl, 3, 0)
        self.gridlay.addWidget(self.rotY_lbl, 4, 0)
        self.gridlay.addWidget(self.rotZ_lbl, 5, 0)
        self.gridlay.addWidget(self.scaleX_lbl, 6, 0)
        self.gridlay.addWidget(self.scaleY_lbl, 7, 0)
        self.gridlay.addWidget(self.scaleZ_lbl, 8, 0)
        self.setLayout(self.gridlay)

# spin boxs
        self.spin_xRotMin = QtWidgets.QSpinBox()
        self.gridlay.addWidget(self.spin_xRotMin, 3, 1)
        self.spin_xRotMin.setRange(0, 360)
        self.spin_xRotMin.setMaximumWidth(100)
        self.spin_xRotMin.valueChanged.connect(self.valueChanged)
        self.spin_xRotMax = QtWidgets.QSpinBox()
        self.gridlay.addWidget(self.spin_xRotMax, 3, 2)
        self.spin_xRotMax.setRange(0, 360)
        self.spin_xRotMax.setMaximumWidth(100)
        self.spin_xRotMax.valueChanged.connect(self.valueChanged)

        self.spin_yRotMin = QtWidgets.QSpinBox()
        self.gridlay.addWidget(self.spin_yRotMin, 4, 1)
        self.spin_yRotMin.setRange(0, 360)
        self.spin_yRotMin.setMaximumWidth(100)
        self.spin_yRotMin.valueChanged.connect(self.valueChanged)
        self.spin_yRotMax = QtWidgets.QSpinBox()
        self.gridlay.addWidget(self.spin_yRotMax, 4, 2)
        self.spin_yRotMax.setRange(0, 360)
        self.spin_yRotMax.setMaximumWidth(100)
        self.spin_yRotMax.valueChanged.connect(self.valueChanged)

        self.spin_zRotMin = QtWidgets.QSpinBox()
        self.gridlay.addWidget(self.spin_zRotMin, 5, 1)
        self.spin_zRotMin.setRange(0, 360)
        self.spin_zRotMin.setMaximumWidth(100)
        self.spin_zRotMin.valueChanged.connect(self.valueChanged)
        self.spin_zRotMax = QtWidgets.QSpinBox()
        self.gridlay.addWidget(self.spin_zRotMax, 5, 2)
        self.spin_zRotMax.setRange(0, 360)
        self.spin_zRotMax.setMaximumWidth(100)
        self.spin_zRotMax.valueChanged.connect(self.valueChanged)

        self.spin_xScaleMin = QtWidgets.QSpinBox()
        self.gridlay.addWidget(self.spin_xScaleMin, 6, 1)
        self.spin_xScaleMin.setRange(1, 10)
        self.spin_xScaleMin.setMaximumWidth(100)
        self.spin_xScaleMin.valueChanged.connect(self.valueChanged)
        self.spin_xScaleMax = QtWidgets.QSpinBox()
        self.gridlay.addWidget(self.spin_xScaleMax, 6, 2)
        self.spin_xScaleMax.setRange(1, 10)
        self.spin_xScaleMax.setMaximumWidth(100)
        self.spin_xScaleMax.valueChanged.connect(self.valueChanged)

        self.spin_yScaleMin = QtWidgets.QSpinBox()
        self.gridlay.addWidget(self.spin_yScaleMin, 7, 1)
        self.spin_yScaleMin.setRange(1, 10)
        self.spin_yScaleMin.setMaximumWidth(100)
        self.spin_yScaleMin.valueChanged.connect(self.valueChanged)
        self.spin_yScaleMax = QtWidgets.QSpinBox()
        self.gridlay.addWidget(self.spin_yScaleMax, 7, 2)
        self.spin_yScaleMax.setRange(1, 10)
        self.spin_yScaleMax.setMaximumWidth(100)
        self.spin_yScaleMax.valueChanged.connect(self.valueChanged)

        self.spin_zScaleMin = QtWidgets.QSpinBox()
        self.gridlay.addWidget(self.spin_zScaleMin, 8, 1)
        self.spin_zScaleMin.setRange(1, 10)
        self.spin_zScaleMin.setMaximumWidth(100)
        self.spin_zScaleMin.valueChanged.connect(self.valueChanged)
        self.spin_zScaleMax = QtWidgets.QSpinBox()
        self.gridlay.addWidget(self.spin_zScaleMax, 8, 2)
        self.spin_zScaleMax.setRange(1, 10)
        self.spin_zScaleMax.setMaximumWidth(100)
        self.spin_zScaleMax.valueChanged.connect(self.valueChanged)

        self.scatter_btn = QtWidgets.QPushButton("Scatter")
        self.gridlay.addWidget(self.scatter_btn, 9, 0)
        self.scatter_btn.setMaximumWidth(80)
        self.scatter_btn.clicked.connect(scatter_objects)

    def user_input(self):
        self.max_rotX.setText("User Entered Something")

    def input_value(self):
        return self.max_rotX.text()

    def valueChanged(self):
        global xRot_min, xRot_max, yRot_min, yRot_max, zRot_min, zRot_max, \
            xScale_min, xScale_max, yScale_min, yScale_max, zScale_min, zScale_max

        xRot_min = self.spin_xRotMin.value()
        xRot_max = self.spin_xRotMax.value()
        yRot_min = self.spin_yRotMin.value()
        yRot_max = self.spin_yRotMax.value()
        zRot_min = self.spin_zRotMin.value()
        zRot_max = self.spin_zRotMax.value()
        xScale_min = self.spin_xScaleMin.value()
        xScale_max = self.spin_xScaleMax.value()
        yScale_min = self.spin_yScaleMin.value()
        yScale_max = self.spin_yScaleMax.value()
        zScale_min = self.spin_zScaleMin.value()
        zScale_max = self.spin_zScaleMax.value()

@QtCore.Slot()
def scatter_objects():
    order = cmds.ls(orderedSelection=True)

    # if order length is 2 do this

    # "order: %s" % (result)

    toInstance = order[0]  # geometries stores name of first selected object
    instanceTo = order[1]

    vtx_selection = cmds.polyListComponentConversion(instanceTo, toVertex=True)
    vtx_selection = cmds.filterExpand(vtx_selection, selectionMask=31)

    cmds.select(vtx_selection)

    for vtx in vtx_selection:
        scatter_instance = cmds.instance(toInstance, name="pInstance *")
        pos = cmds.xform([vtx], query=True, translation=True)  # use this if you need sclae and rotation
        cmds.xform(scatter_instance, translation=pos)

        xRot = random.uniform(xRot_min, xRot_max)
        yRot = random.uniform(yRot_min, yRot_max)
        zRot = random.uniform(zRot_min, zRot_max)

        # print (xx)
        cmds.rotate(xRot, yRot, zRot, scatter_instance)

        xScale = random.uniform(xScale_min, xScale_max)
        yScale = random.uniform(yScale_min, yScale_max)
        zScale = random.uniform(zScale_min, zScale_max)

        cmds.scale(xScale, yScale, zScale, scatter_instance)


