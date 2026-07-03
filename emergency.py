import webbrowser
import requests

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle

FIREBASE_URL = "https://safespot-4f250-default-rtdb.europe-west1.firebasedatabase.app"


class EmergencyContactsScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(1, 0.98, 0.94, 1)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self._update_bg, pos=self._update_bg)

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def on_pre_enter(self):
        self.load_contacts()

    def load_contacts(self):

        self.clear_widgets()

        scroll = ScrollView(size_hint=(1, 1))

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=14,
            size_hint_y=None
        )

        layout.bind(minimum_height=layout.setter("height"))

        title = Label(
            text="[b]Emergency Help[/b]",
            markup=True,
            font_size="28sp",
            size_hint_y=None,
            height=60,
            color=(0.1, 0.1, 0.1, 1)
        )

        layout.add_widget(title)

        intro = Label(
            text="If you're in danger or need support, choose one of the services below.",
            size_hint_y=None,
            height=70,
            font_size="17sp",
            halign="center",
            valign="middle",
            color=(0.2, 0.2, 0.2, 1)
        )
        intro.bind(size=intro.setter("text_size"))

        layout.add_widget(intro)

        try:

            response = requests.get(
                f"{FIREBASE_URL}/emergency.json",
                timeout=15
            )

            if response.status_code == 200 and response.json():

                data = response.json()

                for key, contact in data.items():

                    name = contact.get("name", "")
                    phone = contact.get("phone", "")
                    note = contact.get("note", "")

                    text = f"{name}\n{phone}"

                    if note:
                        text += f"\n{note}"

                    btn = Button(
                        text=text,
                        size_hint_y=None,
                        height=110,
                        font_size="17sp",
                        background_color=(0.35, 0.35, 0.35, 1),
                        color=(1, 1, 1, 1)
                    )

                    btn.bind(
                        on_press=lambda instance, value=phone:
                        self.open_contact(value)
                    )

                    layout.add_widget(btn)

            else:

                layout.add_widget(
                    Label(
                        text="No emergency contacts available.",
                        size_hint_y=None,
                        height=60
                    )
                )

        except Exception as e:

            layout.add_widget(
                Label(
                    text=f"Error loading contacts\n{e}",
                    size_hint_y=None,
                    height=80
                )
            )

        warning = Label(
            text="[b]In an emergency always call 999 immediately.[/b]",
            markup=True,
            size_hint_y=None,
            height=60,
            color=(0.6, 0, 0, 1)
        )

        layout.add_widget(warning)

        back_btn = Button(
            text="Back to Home",
            size_hint_y=None,
            height=65,
            font_size="18sp",
            background_color=(0.25, 0.15, 0.1, 1),
            color=(1, 1, 1, 1)
        )

        back_btn.bind(
            on_press=lambda x:
            setattr(self.manager, "current", "home")
        )

        layout.add_widget(back_btn)

        scroll.add_widget(layout)

        self.add_widget(scroll)

    def open_contact(self, value):

        if value.startswith("http"):
            webbrowser.open(value)
        else:
            webbrowser.open(f"tel:{value}")
