

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

# python for making random instances of a cube

import maya.cmds as cmds
import random

random.seed(1234)

result = cmds.ls( orderedSelection=True )

print 'result: #s' # (result)

transformName = result[0]

instanceGroupName = cmds.group(empty=True, name=transformName + '_instance_grp#')
for i in range(0, 50):
    instanceResult = cmds.instance(transformName, name=transformName + '_instance#')

    cmds.parent(instanceResult, instanceGroupName)

    # print 'instanceResult:'  + str(instanceResult)

    x = random.uniform(-10, 10)
    y = random.uniform(0, 20)
    z = random.uniform(-10, 10)

    cmds.move(x, y, z, instanceResult)

    xRot = random.uniform(0, 360)
    yRot = random.uniform(0, 360)
    zRot = random.uniform(0, 360)

    cmds.rotate(xRot, yRot, zRot, instanceResult)

    scalingFactor = random.uniform(0.3, 1.5)

    cmds.scale(scalingFactor, scalingFactor, scalingFactor, instanceResult)

cmds.hide(transformName)
cmds.xform(instanceGroupName, centerPivots=True)

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
        self.setMinimumWidth(400)
        self.setMinimumHeight(600)
        self.setWindowFlags(self.windowFlags() ^  # ^ means except
                            QtCore.Qt.WindowContextHelpButtonHint)  # controls icons like min and max and cancel
        self.create_ui()

    def create_ui(self):
        self.title_lbl = QtWidgets.QLabel("Scatter Tool")
        self.title_lbl.setStyleSheet("font:  bold 20px")

        self.main_lay = QtWidgets.QVBoxLayout()  # stacking top to bottom layout group
        self.main_lay.addWidget(self.title_lbl)
        self.setLayout(self.main_lay)