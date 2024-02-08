from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import NumericProperty
class VuMeter(MDBoxLayout):
    level = NumericProperty(0)
    def __init__(self, **kwargs):
        super(VuMeter, self).__init__(**kwargs)
        self.cols=1
        self.size_hint=(0.1,1)
        self.spacing=1
        self.orientation="vertical"
        self.md_bg_color="#00000010"
        self.elements=[]
        for _ in range(25):
            green_label = MDLabel(text='', halign='center', theme_text_color='Custom',
                                   size_hint_y=0.01)
            green_label.md_bg_color = "#FF0000" 
            self.elements.append(green_label)
            self.add_widget(green_label)    
        for _ in range(25):
            green_label = MDLabel(text='', halign='center', theme_text_color='Custom',
                                   size_hint_y=0.01)
            green_label.md_bg_color = "#FFFF00" 
            self.elements.append(green_label)
            self.add_widget(green_label)   
        for _ in range(50):
            green_label = MDLabel(text='', halign='center', theme_text_color='Custom',
                                   size_hint_y=0.01)
            green_label.md_bg_color = (0, 0.5, 0, 1) 
            self.elements.append(green_label)
            self.add_widget(green_label)
        
    def on_level(self, instance, level):
        
        value=100-level
        for i in range(value):
            if i<value:
                self.elements[i].opacity=0
            else:
                self.elements[i].opacity=1