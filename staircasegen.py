from PySide6 import QtWidgets, QtCore


import maya.cmds as cmds


class Staircase():

    def __init__(self):
        self.braceWidth = 1
        self.braceHeight = 10
        self.braceDepth = .5

    def create(self):
        self.create_braces()
        # self.create_steps()
        cmds.group(["*brace*"], name="Staircase")

    def create_braces(self):
        self.brace_obj, self.brace_node = cmds.polyCube(name="rightbrace#",\
             width=self.braceWidth, height=self.braceHeight, depth=self.braceDepth)
        cmds.xform(translation=[0, 0, -2])
        cmds.xform(rotation=[0, 0, 45])
        self.brace_obj, self.brace_node = cmds.polyCube(name="leftbrace#",\
             width=self.braceWidth, height=self.braceHeight, depth=self.braceDepth)
        cmds.xform(translation=[0, 0, 2])
        cmds.xform(rotation=[0, 0, 45])

staircase1 = Staircase()
staircase1.create()