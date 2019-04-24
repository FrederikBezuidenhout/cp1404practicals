from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):

    def __init__(self):
        super().__init__()
        self.names = ['Tom', 'Richard', 'Harry']

    def build(self):
        self.title = "Dynamic Widget"
        self.root = Builder.load_file('dynamic_widget.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        self.root.ids.entries_box.clear_widgets()
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicWidgetsApp().run()
