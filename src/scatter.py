import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import maya.cmds as cmds
import random
import pymel.core as pm

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
        self.density_guide_lbl = QtWidgets.QLabel("1 = 100%")
        self.density_guide_lbl.setStyleSheet("font:  bold 10px")
        self.offset_lbl = QtWidgets.QLabel("Create Offset")
        self.offset_lbl.setStyleSheet("font:  bold 12px")
        self.offset_x_lbl = QtWidgets.QLabel("Offset X")
        self.offset_x_lbl.setStyleSheet("font:  bold 10px")
        self.offset_y_lbl = QtWidgets.QLabel("Offset Y")
        self.offset_y_lbl.setStyleSheet("font:  bold 10px")
        self.offset_z_lbl = QtWidgets.QLabel("Offset Z")
        self.offset_z_lbl.setStyleSheet("font:  bold 10px")



        """spin box creation"""
        self.spin_xrot_min = QtWidgets.QSpinBox()
        self.spin_xrot_max = QtWidgets.QSpinBox()
        self.spin_yrot_min = QtWidgets.QSpinBox()
        self.spin_yrot_max = QtWidgets.QSpinBox()
        self.spin_zrot_min = QtWidgets.QSpinBox()
        self.spin_zrot_max = QtWidgets.QSpinBox()
        self.spin_xscale_min = QtWidgets.QSpinBox()
        self.spin_xscale_max = QtWidgets.QSpinBox()
        self.spin_yscale_min = QtWidgets.QSpinBox()
        self.spin_yscale_max = QtWidgets.QSpinBox()
        self.spin_zscale_min = QtWidgets.QSpinBox()
        self.spin_zscale_max = QtWidgets.QSpinBox()
        self.spin_density = QtWidgets.QDoubleSpinBox()
        self.spin_x_offset_min = QtWidgets.QSpinBox()
        self.spin_x_offset_max = QtWidgets.QSpinBox()
        self.spin_y_offset_min = QtWidgets.QSpinBox()
        self.spin_y_offset_max = QtWidgets.QSpinBox()
        self.spin_z_offset_min = QtWidgets.QSpinBox()
        self.spin_z_offset_max = QtWidgets.QSpinBox()




    def scatter_button(self):
        self.scatter_btn = QtWidgets.QPushButton("Scatter")
        self.gridlay.addWidget(self.scatter_btn, 14, 0)
        self.scatter_btn.setMaximumWidth(80)
        self.scatter_btn.clicked.connect(self.scatter_slot)

    def interactables_constraints(self):
        self.spin_xrot_min.setRange(0, 360)
        self.spin_xrot_min.setMaximumWidth(100)
        self.spin_xrot_max.setRange(0, 360)
        self.spin_xrot_max.setMaximumWidth(100)
        self.spin_yrot_min.setRange(0, 360)
        self.spin_yrot_min.setMaximumWidth(100)
        self.spin_yrot_max.setRange(0, 360)
        self.spin_yrot_max.setMaximumWidth(100)
        self.spin_zrot_min.setRange(0, 360)
        self.spin_zrot_min.setMaximumWidth(100)
        self.spin_zrot_max.setRange(0, 360)
        self.spin_zrot_max.setMaximumWidth(100)
        self.spin_xscale_min.setRange(1, 10)
        self.spin_xscale_min.setMaximumWidth(100)
        self.spin_xscale_max.setRange(1, 10)
        self.spin_xscale_max.setMaximumWidth(100)
        self.spin_yscale_min.setRange(1, 10)
        self.spin_yscale_min.setMaximumWidth(100)
        self.spin_yscale_max.setRange(1, 10)
        self.spin_yscale_max.setMaximumWidth(100)
        self.spin_zscale_min.setRange(1, 10)
        self.spin_zscale_min.setMaximumWidth(100)
        self.spin_zscale_max.setRange(1, 10)
        self.spin_zscale_max.setMaximumWidth(100)
        self.spin_density.setRange(0, 1)
        self.spin_density.setMaximumWidth(100)
        self.spin_density.setSingleStep(.01)
        self.spin_density.setValue(1)
        self.spin_x_offset_min.setRange(0, 10)
        self.spin_x_offset_min.setMaximumWidth(100)
        self.spin_x_offset_max.setRange(0, 10)
        self.spin_x_offset_max.setMaximumWidth(100)
        self.spin_y_offset_min.setRange(0, 10)
        self.spin_y_offset_min.setMaximumWidth(100)
        self.spin_y_offset_max.setRange(0, 10)
        self.spin_y_offset_max.setMaximumWidth(100)
        self.spin_z_offset_min.setRange(0, 10)
        self.spin_z_offset_min.setMaximumWidth(100)
        self.spin_z_offset_max.setRange(0, 10)
        self.spin_z_offset_max.setMaximumWidth(100)



    def interactables_layout(self):
        self.gridlay.addWidget(self.spin_xrot_min, 3, 1)
        self.gridlay.addWidget(self.spin_xrot_max, 3, 2)
        self.gridlay.addWidget(self.spin_yrot_min, 4, 1)
        self.gridlay.addWidget(self.spin_yrot_max, 4, 2)
        self.gridlay.addWidget(self.spin_zrot_min, 5, 1)
        self.gridlay.addWidget(self.spin_zrot_max, 5, 2)
        self.gridlay.addWidget(self.spin_xscale_min, 6, 1)
        self.gridlay.addWidget(self.spin_xscale_max, 6, 2)
        self.gridlay.addWidget(self.spin_yscale_min, 7, 1)
        self.gridlay.addWidget(self.spin_yscale_max, 7, 2)
        self.gridlay.addWidget(self.spin_zscale_min, 8, 1)
        self.gridlay.addWidget(self.spin_zscale_max, 8, 2)
        self.gridlay.addWidget(self.spin_density, 9, 1)
        self.gridlay.addWidget(self.spin_x_offset_min, 11, 1)
        self.gridlay.addWidget(self.spin_x_offset_max, 11, 2)
        self.gridlay.addWidget(self.spin_y_offset_min, 12, 1)
        self.gridlay.addWidget(self.spin_y_offset_max, 12, 2)
        self.gridlay.addWidget(self.spin_z_offset_min, 13, 1)
        self.gridlay.addWidget(self.spin_z_offset_max, 13, 2)




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
        self.gridlay.addWidget(self.density_guide_lbl, 9, 2)
        self.gridlay.addWidget(self.offset_lbl, 10, 0)
        self.gridlay.addWidget(self.offset_x_lbl, 11, 0)
        self.gridlay.addWidget(self.offset_y_lbl, 12, 0)
        self.gridlay.addWidget(self.offset_z_lbl, 13, 0)



        self.setLayout(self.gridlay)

    @QtCore.Slot()
    def scatter_slot(self):
        self._set_scatter_properties_from_ui()
        self.scatter.scatter_objects()

    def _set_scatter_properties_from_ui(self):
        self.scatter.x_rot_min = self.spin_xrot_min.value()
        self.scatter.x_rot_max = self.spin_xrot_max.value()
        self.scatter.y_rot_min = self.spin_yrot_min.value()
        self.scatter.y_rot_max = self.spin_yrot_max.value()
        self.scatter.z_rot_min = self.spin_zrot_min.value()
        self.scatter.z_rot_max = self.spin_zrot_max.value()
        self.scatter.x_scale_min = self.spin_xscale_min.value()
        self.scatter.x_scale_min = self.spin_xscale_max.value()
        self.scatter.y_scale_min = self.spin_yscale_min.value()
        self.scatter.y_scale_max = self.spin_yscale_max.value()
        self.scatter.z_scale_min = self.spin_zscale_min.value()
        self.scatter.z_scale_max = self.spin_zscale_max.value()
        self.scatter.spin_density = self.spin_density.value()
        self.scatter.spin_x_offset_min = self.spin_x_offset_min.value()
        self.scatter.spin_x_offset_max = self.spin_x_offset_max.value()
        self.scatter.spin_y_offset_min = self.spin_y_offset_min.value()
        self.scatter.spin_y_offset_max = self.spin_y_offset_max.value()
        self.scatter.spin_z_offset_min = self.spin_z_offset_min.value()
        self.scatter.spin_z_offset_max = self.spin_z_offset_max.value()

class Scatter(object):

    def __init__(self):
        self.x_rot_min = 0
        self.x_rot_max = 0
        self.y_rot_min = 0
        self.y_rot_max = 0
        self.z_rot_min = 0
        self.z_rot_max = 0
        self.x_scale_min = 1
        self.x_scale_max = 1
        self.y_scale_min = 1
        self.y_scale_max = 1
        self.z_scale_min = 1
        self.z_scale_max = 1
        self.spin_density = 1.0
        self.spin_x_offset_min = 0
        self.spin_x_offset_max = 0
        self.spin_y_offset_min = 0
        self.spin_y_offset_max = 0
        self.spin_z_offset_min = 0
        self.spin_z_offset_max = 0



    def scatter_objects(self):
        order = cmds.ls(orderedSelection=True)

        to_instance = order[0]
        instance_to = order[1:]
        #mesh_vert = pm.MeshVertex(vert)
       # mesh_vert.getNormal()


        vtx_selection = cmds.polyListComponentConversion(instance_to, toVertex=True)
        vtx_selection = cmds.filterExpand(vtx_selection, selectionMask=31)
# only use a percent of selcted vets
        len(vtx_selection)
        random_amount = int(round(len(vtx_selection) * self.spin_density))
        percentage_selection = random.sample(vtx_selection, k=random_amount)
        cmds.select(percentage_selection)


        for vtx in percentage_selection:

            scatter_instance = cmds.instance(to_instance, name="pInstance *")
            pos = cmds.xform([vtx], query=True, translation=True)
            cmds.xform(scatter_instance, translation=pos)

            #constrain = cmds.normalConstraint([toInstance, instanceTo])



            x_rot = random.uniform(self.x_rot_min, self.x_rot_max)
            y_rot = random.uniform(self.y_rot_min, self.y_rot_max)
            z_rot = random.uniform(self.z_rot_min, self.z_rot_max)

            cmds.rotate(x_rot, y_rot, z_rot, scatter_instance)

            x_scale = random.uniform(self.x_scale_min, self.x_scale_max)
            y_scale = random.uniform(self.y_scale_min, self.y_scale_max)
            z_scale = random.uniform(self.z_scale_min, self.z_scale_max)

            cmds.scale(x_scale, y_scale, z_scale, scatter_instance)

            """
            x_tran = random.uniform(self.spin_x_offset_min, self.spin_x_offset_max)
            y_tran = random.uniform(self.spin_y_offset_min, self.spin_y_offset_max)
            z_tran = random.uniform(self.spin_z_offset_min, self.spin_z_offset_max)

            cmds.moveXYZ(x_tran, y_tran, z_tran, scatter_instance)
"""