from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class ScatterTextWidget(BoxLayout):
    pass


class Kidsapp(App):
    def build(self):
        return ScatterTextWidget()

def some_function(*args):
    print('text changed')

if __name__ == "__main__":
    Kidsapp().run()
