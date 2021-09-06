from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar


class App(MDApp):
    def flip(self):
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "inverted"
            self.input.text = "invertation"

            self.converted.text = ''
            self.label.text = ""
        else:
            self.state = 0
            self.toolbar.title = "non inverted"
            self.input.text = "non invertation"

            self.converted.text = ''
            self.label.text = ""

    def work(self, args):
        if self.state == 0:
            x = int(self.input.text, 2)
            self.converted.text = str(x)
            self.label.text = "result: "
        else:
            x = int(self.input.text, 2)
            self.converted.text = str(x)
            self.label.text = "result: "

    def build(self):
        self.state = 0
        self.theme_cls.primary_palette = "Amber"
        screen = MDScreen()

        self.toolbar = MDToolbar(title="my app")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)
        # screen.add_widget(Image(
        #    source="logo.png",
        #    pos_hint={"center_x":0.5,"center_y":0.7}
        #    ))
        self.input = MDTextField(
            text="give the number",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size=22
        )
        screen.add_widget(self.input)
        self.label = MDLabel(
            # text="result: ",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color="Secondary"
        )

        self.converted = MDLabel(
            # text="777 ",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            theme_text_color="Primary",
            font_style="H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        screen.add_widget(MDFillRoundFlatButton(
            text="Count",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=self.work
        ))

        return screen


if __name__ == '__main__':
    App().run()
