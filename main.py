from kivy.app import App
from kivy.uix.button import Button

class ContoUP(App):
    def build(self):
        # Un bottone gigante che occupa tutta la schermata
        return Button(text='ContoUP Attivo!\nPremi qui per iniziare', font_size=30)

if __name__ == '__main__':
    ContoUP().run()
