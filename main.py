from kivy.app import App
from kivy.uix.button import Button


class UngDungThu(App):
    def build(self):
        return Button(text="Xin chào APK Python")


if __name__ == "__main__":
    UngDungThu().run()
