

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

'''
cubeList = cmds.ls( 'myCube*')
if len( cubeList) > 0:
    cmds.delete( cubeList)
'''

result = cmds.polyCube(w=1, h=1, d=1, name='myCube#')

# print 'result: ' + str(result)

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
