from PyQt5.QtWidgets import QPushButton


class EpisodeButton(QPushButton):
    """
    显示集数的按钮
    """

    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("""
QPushButton{
background-color: #2e2e36;
color: #bababa;
font: 10pt "微软雅黑";
border: 1px solid #bababa;
}
QPushButton:hover{
background-color: #ff5246;
color: #ffffff;
}
QPushButton:pressed{
background-color: #000000;
color: #ffffff;
}
        """)
        pass

    pass