from kivy.app import App
from kivy.uix.label import Label

class ContoUP(App):
    def build(self):
        return Label(text='Benvenuti in ContoUP!\nPronto per NFC')

if __name__ == '__main__':
    ContoUP().run()
