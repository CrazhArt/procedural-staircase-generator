from PySide6 import QtWidgets, QtCore


import maya.cmds as cmds


class StaircaseGUI(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.staircase_generator = Staircase()
        self.setWindowTitle("Procedural Staircase")
        self.create_layout()
        self.create_connections()
        self.resize(500, 200)

    def create_layout(self):
        self.main_lay = QtWidgets.QVBoxLayout()
        self._form_ui()
        self.create_btn = QtWidgets.QPushButton("Create Staircase")
        self.main_lay.addWidget(self.create_btn)
        self.main_lay.addStretch()
        self.main_lay.addSpacing(200)
        self.setLayout(self.main_lay)

    def _form_ui(self):
        self.form_lay = QtWidgets.QFormLayout()
        self.case_height_spinbox = QtWidgets.QSpinBox()
        self.case_height_spinbox.setValue(10)
        self.case_depth_spinbox = QtWidgets.QSpinBox()
        self.case_depth_spinbox.setValue(5)
        self.form_lay.addRow("Staircase height", self.case_height_spinbox)
        self.form_lay.addRow("Staircase width", self.case_depth_spinbox)
        self.main_lay.addLayout(self.form_lay)

    def create_connections(self):
        self.create_btn.clicked.connect(self.create)

    @QtCore.Slot()
    def create(self):
        self.staircase_generator.stepCount = self.case_height_spinbox.value()
        self.staircase_generator.stepDepth = self.case_depth_spinbox.value()
        self.staircase_generator.create()

class Staircase():

    def __init__(self):
        self.braceWidth = 2
        self.braceHeight = 5
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
             width=self.braceWidth, height=self.stepCount, depth=self.braceDepth)
        cmds.xform(translation=[0, 0, self.stepDepth/-2])
        cmds.xform(rotation=[0, 0, 45])

        self.brace_obj, self.brace_node = cmds.polyCube(name="leftbrace#",\
             width=self.braceWidth, height=self.stepCount, depth=self.braceDepth)
        cmds.xform(translation=[0, 0, self.stepDepth/2])
        cmds.xform(rotation=[0, 0, 45])

    def create_steps(self):
        for i in range(int(self.stepCount/2)):
            newStep = cmds.polyCube(w = 2, h = .5, d = self.stepDepth, cuv = 4, name='step#')
            y = (self.stepCount/self.stepCount)*(-i)
            x = i
            cmds.move(x, y, 0, newStep)

        for i in range(int(self.stepCount/2)):
            newStep = cmds.polyCube(w = 2, h = .5, d = self.stepDepth, cuv = 4, name='step#')
            y = (self.stepCount/self.stepCount)*(i)
            x = -i
            cmds.move(x, y, 0, newStep)

# staircase1 = Staircase()
# staircase1.create()