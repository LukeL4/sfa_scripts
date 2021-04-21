import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import maya.cmds as cmds
import random

def maya_main_window():
    """return the maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class ScatterUI(QtWidgets.QDialog):
    """ Simple UI class"""

    def __init__(self):
        """contructor"""
        super(ScatterUI, self).__init__(parent=maya_main_window())
        self.scatter = Scatter() #can now refer to scatter.method
        self.setWindowTitle("Scatter Tool")
        self.setMinimumWidth(275)
        self.setMaximumWidth(275)
        self.setMinimumHeight(300)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.create_ui()
        self.label_layout()
        self.interactables_layout()
        self.interactables_constraints()
        self.scatter_button()

    def create_ui(self):
        # need to seperate out ui layout stuff and ui creation stuff
        """ label creation"""
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
        self.density_lbl = QtWidgets.QLabel("Scatter density")
        self.density_lbl.setStyleSheet("font:  bold 10px")

        """spin box creation"""
        self.spin_xRotMin = QtWidgets.QSpinBox()
        self.spin_xRotMax = QtWidgets.QSpinBox()
        self.spin_yRotMin = QtWidgets.QSpinBox()
        self.spin_yRotMax = QtWidgets.QSpinBox()
        self.spin_zRotMin = QtWidgets.QSpinBox()
        self.spin_zRotMax = QtWidgets.QSpinBox()
        self.spin_xScaleMin = QtWidgets.QSpinBox()
        self.spin_xScaleMax = QtWidgets.QSpinBox()
        self.spin_yScaleMin = QtWidgets.QSpinBox()
        self.spin_yScaleMax = QtWidgets.QSpinBox()
        self.spin_zScaleMin = QtWidgets.QSpinBox()
        self.spin_zScaleMax = QtWidgets.QSpinBox()
        self.spin_density = QtWidgets.QDoubleSpinBox()


    def scatter_button(self):
        self.scatter_btn = QtWidgets.QPushButton("Scatter")
        self.gridlay.addWidget(self.scatter_btn, 10, 0)
        self.scatter_btn.setMaximumWidth(80)
        self.scatter_btn.clicked.connect(self.scatter_slot)

    def interactables_constraints(self):
        self.spin_xRotMin.setRange(0, 360)
        self.spin_xRotMin.setMaximumWidth(100)
        self.spin_xRotMax.setRange(0, 360)
        self.spin_xRotMax.setMaximumWidth(100)
        self.spin_yRotMin.setRange(0, 360)
        self.spin_yRotMin.setMaximumWidth(100)
        self.spin_yRotMax.setRange(0, 360)
        self.spin_yRotMax.setMaximumWidth(100)
        self.spin_zRotMin.setRange(0, 360)
        self.spin_zRotMin.setMaximumWidth(100)
        self.spin_zRotMax.setRange(0, 360)
        self.spin_zRotMax.setMaximumWidth(100)
        self.spin_xScaleMin.setRange(1, 10)
        self.spin_xScaleMin.setMaximumWidth(100)
        self.spin_xScaleMax.setRange(1, 10)
        self.spin_xScaleMax.setMaximumWidth(100)
        self.spin_yScaleMin.setRange(1, 10)
        self.spin_yScaleMin.setMaximumWidth(100)
        self.spin_yScaleMax.setRange(1, 10)
        self.spin_yScaleMax.setMaximumWidth(100)
        self.spin_zScaleMin.setRange(1, 10)
        self.spin_zScaleMin.setMaximumWidth(100)
        self.spin_zScaleMax.setRange(1, 10)
        self.spin_zScaleMax.setMaximumWidth(100)
        self.spin_density.setRange(0, 1)
        self.spin_density.setMaximumWidth(100)
        self.spin_density.setSingleStep(.01)

    def interactables_layout(self):
        self.gridlay.addWidget(self.spin_xRotMin, 3, 1)
        self.gridlay.addWidget(self.spin_xRotMax, 3, 2)
        self.gridlay.addWidget(self.spin_yRotMin, 4, 1)
        self.gridlay.addWidget(self.spin_yRotMax, 4, 2)
        self.gridlay.addWidget(self.spin_zRotMin, 5, 1)
        self.gridlay.addWidget(self.spin_zRotMax, 5, 2)
        self.gridlay.addWidget(self.spin_xScaleMin, 6, 1)
        self.gridlay.addWidget(self.spin_xScaleMax, 6, 2)
        self.gridlay.addWidget(self.spin_yScaleMin, 7, 1)
        self.gridlay.addWidget(self.spin_yScaleMax, 7, 2)
        self.gridlay.addWidget(self.spin_zScaleMin, 8, 1)
        self.gridlay.addWidget(self.spin_zScaleMax, 8, 2)
        self.gridlay.addWidget(self.spin_density, 9, 1)



    def label_layout(self):
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
        self.gridlay.addWidget(self.density_lbl, 9, 0)
        self.setLayout(self.gridlay)

    @QtCore.Slot()
    def scatter_slot(self):
        self._set_scatter_properties_from_ui()
        self.scatter.scatter_objects()

    def _set_scatter_properties_from_ui(self):
        self.scatter.xRotMin = self.spin_xRotMin.value()
        self.scatter.xRotMax = self.spin_xRotMax.value()
        self.scatter.yRotMin = self.spin_yRotMin.value()
        self.scatter.yRotMax = self.spin_yRotMax.value()
        self.scatter.zRotMin = self.spin_zRotMin.value()
        self.scatter.zRotMax = self.spin_zRotMax.value()
        self.scatter.xScaleMin = self.spin_xScaleMin.value()
        self.scatter.xScaleMin = self.spin_xScaleMax.value()
        self.scatter.yScaleMin = self.spin_yScaleMin.value()
        self.scatter.yScaleMax = self.spin_yScaleMax.value()
        self.scatter.zScaleMin = self.spin_zScaleMin.value()
        self.scatter.zScaleMax = self.spin_zScaleMax.value()
        self.scatter.spin_density = self.spin_density.value()



# change from having 2 types of naming conventions to only one using refactor

class Scatter(object):

    def __init__(self):
        self.xRotMin = 0
        self.xRotMax = 0
        self.yRotMin = 0
        self.yRotMax = 0
        self.zRotMin = 0
        self.zRotMax = 0
        self.xScaleMin = 1
        self.xScaleMax = 1
        self.yScaleMin = 1
        self.yScaleMax = 1
        self.zScaleMin = 1
        self.zScaleMax = 1
        self.spin_density = 1.0


    def scatter_objects(self):
        order = cmds.ls(orderedSelection=True)

        toInstance = order[0]
        instanceTo = order[1:]

        vtx_selection = cmds.polyListComponentConversion(instanceTo, toVertex=True)
        vtx_selection = cmds.filterExpand(vtx_selection, selectionMask=31)
# only use a percent of selcted vets
        len(vtx_selection)
        random_amount = int(round(len(vtx_selection) * self.spin_density))
        print(random_amount)
        percentage_selection = random.sample(vtx_selection, k=random_amount)
        cmds.select(percentage_selection)

        #cmds.select(vtx_selection)

        for vtx in percentage_selection:
        #for vtx in vtx_selection:
            scatter_instance = cmds.instance(toInstance, name="pInstance *")
            pos = cmds.xform([vtx], query=True, translation=True)
            cmds.xform(scatter_instance, translation=pos)

            xRot = random.uniform(self.xRotMin, self.xRotMax)
            yRot = random.uniform(self.yRotMin, self.yRotMax)
            zRot = random.uniform(self.zRotMin, self.zRotMax)

            cmds.rotate(xRot, yRot, zRot, scatter_instance)

            xScale = random.uniform(self.xScaleMin, self.xScaleMax)
            yScale = random.uniform(self.yScaleMin, self.yScaleMax)
            zScale = random.uniform(self.zScaleMin, self.zScaleMax)

            cmds.scale(xScale, yScale, zScale, scatter_instance)
