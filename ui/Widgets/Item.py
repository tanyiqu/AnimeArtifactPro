from ui.ui_designer.ui_file.ui_widget_item import Ui_item


class Item(Ui_item):

    def __init__(self, title, cover, latest):
        self.title = title
        self.cover = cover
        self.latest = latest
        pass

    def init(self):
        self.lblTitle.setText(self.title)
        pass

    pass
