import sys

from PyQt5.QtWidgets import QApplication, QWidget

from ui.Forms.MainForm import MainForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainForm()
    widget = QWidget()
    ui.setupUi(widget)
    ui.init(widget)
    widget.show()
    sys.exit(app.exec_())
    pass
