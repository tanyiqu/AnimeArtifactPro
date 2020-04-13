import sys

from PyQt5.QtWidgets import QApplication

from ui.Forms.MainForm import MainForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainForm()
    widget.show()
    sys.exit(app.exec_())
    pass
