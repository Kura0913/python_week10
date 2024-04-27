from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent


class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_stu_widget")
        
        layout = QtWidgets.QGridLayout()
        # validator
        int_validator = QtGui.QIntValidator(0, 100)
        # font
        content_font = QtGui.QFont()
        content_font.setFamily("Arial")
        content_font.setPointSize(16)
        header_font = QtGui.QFont()
        header_font.setFamily("Arial")
        header_font.setPointSize(20)

        # label
        header_label = LabelComponent(20, "Add Student")
        header_label.setFont(header_font)
        name_label = LabelComponent(16, "Name: ")
        name_label.setFont(content_font)
        subject_label = LabelComponent(16, "Subject:")
        subject_label.setFont(content_font)
        score_label = LabelComponent(16, "Score:")
        score_label.setFont(content_font)
        self.info_label = LabelComponent(16, "")
        self.info_label.setFont(content_font)
        self.info_label.setStyleSheet("color: red;") # set text color
        # editor_label
        self.name_editor_label = LineEditComponent("Name")
        self.name_editor_label.mousePressEvent = self.clear_name_editor_content
        self.name_editor_label.textChanged.connect(self.name_editor_text_changed)
        
        self.subject_editor_label = LineEditComponent("Subject")
        self.subject_editor_label.mousePressEvent = self.clear_subject_editor_content
        self.subject_editor_label.setEnabled(False)

        self.score_editor_label = LineEditComponent("")
        self.score_editor_label.setValidator(int_validator)
        self.score_editor_label.setEnabled(False)
        
        # button
        self.query_btn = ButtonComponent("Query")
        self.query_btn.clicked.connect(self.query_action)
        self.query_btn.setEnabled(False)
        self.add_btn = ButtonComponent("Add")
        self.add_btn.clicked.connect(self.add_action)
        self.add_btn.setEnabled(False)
        self.send_btn = ButtonComponent("Send")
        self.send_btn.clicked.connect(self.send_action)

        # set label layout
        layout.addWidget(header_label, 0, 0, 1, 2)
        layout.addWidget(name_label, 1, 0, 1, 1)
        layout.addWidget(subject_label, 2, 0, 1, 1)
        layout.addWidget(score_label, 3, 0, 1, 1)
        layout.addWidget(self.info_label, 1, 3, 10, 10)
        # set editor label layout
        layout.addWidget(self.name_editor_label, 1, 1, 1, 1)
        layout.addWidget(self.subject_editor_label, 2, 1, 1, 1)
        layout.addWidget(self.score_editor_label, 3, 1, 1, 1)
        # set button layout
        layout.addWidget(self.query_btn, 1, 2, 1, 1)
        layout.addWidget(self.add_btn, 3, 2, 1, 1)
        layout.addWidget(self.send_btn, 5, 3, 1, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 3)
        layout.setColumnStretch(2, 2)
        layout.setColumnStretch(3, 4)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 2)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 2)

        self.setLayout(layout)
        self.score_dict = {}
    def clear_name_editor_content(self, event):
        self.name_editor_label.clear()

    def clear_subject_editor_content(self, event):
        self.subject_editor_label.clear()

    # query btn clicked event
    def query_action(self):
        cmd = {"command" : "query", "parameters" : {"Name" : self.name_editor_label.text()}}
        print(cmd)
        self.info_label.setText(f"The infomation {cmd} is sent")
        # if status == 'OK'
        self.setWidgetEnable(False, True, True, False)
        self.score_dict = {}
    
    # add btn clicked event
    def add_action(self):
        if self.subject_editor_label.text() != '' and self.score_editor_label.text() != '':
            self.score_dict[self.subject_editor_label.text()] = self.score_editor_label.text()
            print(f"add {self.subject_editor_label.text()} : {self.score_editor_label.text()}")
            self.info_label.setText(f"add {self.subject_editor_label.text()} : {self.score_editor_label.text()}")
            # print(f"score_dict: {self.score_dict}")
            self.subject_editor_label.setText('')
            self.score_editor_label.setText('')

    # send btn clicked event
    def send_action(self):
        if self.name_editor_label.text() != "Name" and not self.query_btn.isEnabled():
            cmd = {"command": "add", "parameters": {'name':self.name_editor_label.text(), 'scores': self.score_dict}}
            print(cmd)
            self.info_label.setText(f"The infomation {cmd} is sent")
            # reset component status
            self.score_dict = {}
            self.setWidgetEnable(True, False, False, False)
            self.name_editor_label.setText("Name")
            self.subject_editor_label.setText("Subject")
            
    # name editor label text changed event
    def name_editor_text_changed(self, text):
        self.name_editor_label.setText(text)

        if text == 'Name' or text == '':
            self.query_btn.setEnabled(False)
        else:
            self.query_btn.setEnabled(True)
    # widget enable setting
    def setWidgetEnable(self, name_editor_enable=True, subject_and_score_editor_enable=True, add_btn_enable=True, query_btn_enable=True):
        self.name_editor_label.setEnabled(name_editor_enable)
        self.subject_editor_label.setEnabled(subject_and_score_editor_enable)
        self.score_editor_label.setEnabled(subject_and_score_editor_enable)
        self.add_btn.setEnabled(add_btn_enable)
        self.query_btn.setEnabled(query_btn_enable)