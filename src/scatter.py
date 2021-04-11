

# mel script to add object to verts of another
{
    string $selection[] = `ls -os -fl`;

    string $vertexNames[] = `filterExpand -selectionMask 31  -expand true $selection`;

   // print $vertexNames;

    string $objectToInstance = $selection[0];

    if ( `objectType $objectToInstance` == "transform") {

        string $vertex;
        for( $vertex in $vertexNames ) {

            string $newInstance[] = `instance $objectToInstance`;

            vector $position = `pointPosition -w  $vertex`;

            move -a -ws ($position.x) ($position.y) ($position.z) $newInstance;

        }

    } else {

        print "please ensure the first object you select is a transform.";
    }

}

# python for making random instances of a 1st selected onto 2nd selected

import maya.cmds as cmds
import random

order = cmds.ls(orderedSelection=True)
print
"order: %s" % (result)

toInstance = order[0]  # geometries stores name of first selected object
instanceTo = order[1]
print
toInstance
print
instanceTo

vtx_selection = cmds.polyListComponentConversion(instanceTo, toVertex=True)
vtx_selection = cmds.filterExpand(vtx_selection, selectionMask=31)

cmds.select(vtx_selection)

for vtx in vtx_selection:
    scatter_instance = cmds.instance(toInstance, name="pInstance *")
    pos = cmds.xform([vtx], query=True, translation=True)  # use this if you need sclae and rotation
    cmds.xform(scatter_instance, translation=pos)

    xRot = random.uniform(0, 360)
    yRot = random.uniform(0, 360)
    zRot = random.uniform(0, 360)

    cmds.rotate(xRot, yRot, zRot, scatter_instance)

    scalingFactor = random.uniform(0.3, 1.5)

    cmds.scale(scalingFactor, scalingFactor, scalingFactor, scatter_instance)

# creating the ui

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
        self.scale_lbl = QtWidgets.QLabel("Scale")
        self.scale_lbl.setStyleSheet("font:  bold 10px")

        self.gridlay = QtWidgets.QGridLayout()
        self.gridlay.addWidget(self.title_lbl, 0, 0)
        self.gridlay.addWidget(self.random_lbl, 1, 0)
        self.gridlay.addWidget(self.arg_lbl, 2, 0)
        self.gridlay.addWidget(self.min_lbl, 2, 1)
        self.gridlay.addWidget(self.max_lbl, 2, 2)
        self.gridlay.addWidget(self.rotX_lbl, 3, 0)
        self.gridlay.addWidget(self.rotY_lbl, 4, 0)
        self.gridlay.addWidget(self.rotZ_lbl, 5, 0)
        self.gridlay.addWidget(self.scale_lbl, 6, 0)
        self.setLayout(self.gridlay)

# line edit boxs
        self.max_rotX = QtWidgets.QLineEdit()
        self.gridlay.addWidget(self.max_rotX, 3, 1)
        self.max_rotX.setMaximumWidth(80)
        self.min_rotX = QtWidgets.QLineEdit()
        self.gridlay.addWidget(self.min_rotX, 3, 2)
        self.min_rotX.setMaximumWidth(80)

        self.max_rotY = QtWidgets.QLineEdit()
        self.gridlay.addWidget(self.max_rotY, 4, 1)
        self.max_rotY.setMaximumWidth(80)
        self.min_rotY = QtWidgets.QLineEdit()
        self.gridlay.addWidget(self.min_rotY, 4, 2)
        self.min_rotY.setMaximumWidth(80)

        self.max_rotZ = QtWidgets.QLineEdit()
        self.gridlay.addWidget(self.max_rotZ, 5, 1)
        self.max_rotZ.setMaximumWidth(80)
        self.min_rotZ = QtWidgets.QLineEdit()
        self.gridlay.addWidget(self.min_rotZ, 5, 2)
        self.min_rotZ.setMaximumWidth(80)

        self.max_scale = QtWidgets.QLineEdit()
        self.gridlay.addWidget(self.max_scale, 6, 1)
        self.max_scale.setMaximumWidth(80)
        self.min_scale = QtWidgets.QLineEdit()
        self.gridlay.addWidget(self.min_scale, 6, 2)
        self.min_scale.setMaximumWidth(80)

        self.scatter_btn = QtWidgets.QPushButton("Scatter")
        self.gridlay.addWidget(self.scatter_btn, 7, 0)
        self.scatter_btn.setMaximumWidth(80)

# instance  onto hard  coded object
import maya.cmds as cmds

geometries = cmds.ls(geometry=True)
cmds.select(geometries)

xform = cmds.ls("*Cube1",  transforms=True)[0]
cmds.setAttr(xform + ".translateY", 2)

cmds.ls("pCubeShape1.vtx[*]", flatten=True)
cmds.select("pCubeShape1.vtx[0:2]")

cmds.move(0,2 ,2, ['pCube1'])

vtx_selection = cmds.polyListComponentConversion("pCube1", toVertex=True) # get list of verts
cmds.filterExpand(vtx_selection, selectionMask  = 31)# get non compact form of all verts list
# add len() to get number of verts
cmds.instance("pCube1", name = "pCube5")

pos = cmds.xform(["pSphere1.vtx[276]"], query=True, translation=True)  #where is this vertex -> store it ina varible fro later use
cmds.move(pos[0], pos[1], pos[2], "pCube1") # move to the vertex we have above


vtx_selection = cmds.polyListComponentConversion("pSphere1", toVertex=True)
vtx_selection = cmds.filterExpand(vtx_selection, selectionMask  = 31)

cmds.select(vtx_selection)

for vtx in  vtx_selection:
    scatter_instance = cmds.instance("pCube1", name = "pCube5")
    pos = cmds.xform([vtx], query=True, translation=True)  # use this if you need sclae and rotation
    cmds.xform(scatter_instance, translation=pos)


#at 1:50 in lecture

