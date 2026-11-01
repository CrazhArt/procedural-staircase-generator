from PySide6 import QtWidgets, QtCore


import maya.cmds as cmds


class Staircase():

    def __init__(self):
        self.braceWidth = 1
        self.braceHeight = 10
        self.braceDepth = .5
        self.stepDepth = 4
        self.stepHeight = .5
        self.stepCount = 10
        self.base = self.stepCount

    def create(self):
        self.create_braces()
        self.create_steps()
        cmds.group(["*brace*", "step*"], name="Staircase")

    def create_braces(self):
        self.brace_obj, self.brace_node = cmds.polyCube(name="rightbrace#",\
             width=self.braceWidth, height=self.braceHeight, depth=self.braceDepth)
        cmds.xform(translation=[0, 0, -2])
        cmds.xform(rotation=[0, 0, 45])
        self.brace_obj, self.brace_node = cmds.polyCube(name="leftbrace#",\
             width=self.braceWidth, height=self.braceHeight, depth=self.braceDepth)
        cmds.xform(translation=[0, 0, 2])
        cmds.xform(rotation=[0, 0, 45])

    def create_steps(self):

        for i in range(int(self.stepCount/2)):
            newStep = cmds.polyCube(w = 2, h = .5, d = self.stepDepth, cuv = 4, name='step#')
            y = (self.stepCount/self.base)*(-i)
            x = i
            cmds.move(x-2, y+2, 0, newStep)

staircase1 = Staircase()
staircase1.create()