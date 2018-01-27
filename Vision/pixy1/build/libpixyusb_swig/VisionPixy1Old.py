from pixy import *
from ctypes import *
from networktables import NetworkTables

NetworkTables.initialize(server='10.1.44.2')
table = NetworkTables.getTable('SmartDashboard')
subtable = table.getSubTable('Vision')

print ("Initialized NetworkTables")

pixy_init()

print ("Initialized PixyCam")

class Blocks (Structure):
    _fields_= [("type", c_uint),
               ("signature",c_uint),
               ("x", c_uint),
               ("y", c_uint),
               ("width", c_uint),
               ("height", c_uint),
               ("angle", c_uint) ]
blocks = BlockArray(100)
frame = 0
while 1:
    count = pixy_get_blocks(100, blocks)

    if count > 0:
        print 'frame %3d:' % frame
        frame = frame + 1
        for index in range (0,count):
            print '[BLOCK_TYPE=%d SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks[index].type, blocks[index].signature, blocks[index].x, blocks[index].y, blocks[index].width, blocks[index].height)
            table.putString('pixy', '[BLOCK_TYPE=%d SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks[index].type, blocks[index].signature, blocks[index].x, blocks[index].y, blocks[index].width, blocks[index].height))
