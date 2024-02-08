from kivymd.app import MDApp
from vumeter import VuMeter


class MainApp(MDApp):
    def build(self):
        layout=VuMeter()
        layout.level=65        
        return layout


if __name__ == "__main__":
    MainApp().run()