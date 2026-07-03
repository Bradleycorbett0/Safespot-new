import json
import os
import webbrowser

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle


class EmergencyContactsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(1, 0.98, 0.94, 1)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self._update_bg, pos=self._update_bg)

        scroll = ScrollView(size_hint=(1, 1))

        layout = BoxLayout(
            orientation="vertical",
            padding=[18, 20, 18, 20],
            spacing=14,
            size_hint_y=None
        )
        layout.bind(minimum_height=layout.setter("height"))

        title = Label(
            text="[b]Emergency Help[/b]",
            markup=True,
            font_size="28sp",
            color=(0.1, 0.1, 0.1, 1),
            size_hint_y=None,
            height=55,
            halign="center",
            valign="middle"
        )
        title.bind(size=title.setter("text_size"))
        layout.add_widget(title)

        intro = Label(
            text=(
                "If you feel unsafe, need urgent help, or just need someone "
                "to talk to, use one of the options below."
            ),
            font_size="16sp",
            color=(0.15, 0.15, 0.15, 1),
            size_hint_y=None,
            height=80,
            halign="center",
            valign="middle"
        )
        intro.bind(size=intro.setter("text_size"))
        layout.add_widget(intro)

        contacts = self.load_contacts()

        for contact in contacts:
            name = contact.get("name", "Unknown")
            phone = contact.get("phone", "")
            note = contact.get("note", "")

            button_text = f"{name}\n{phone}"
            if note:
                button_text += f"\n{note}"

            btn = Button(
                text=button_text,
                size_hint_y=None,
                height=105,
                font_size="17sp",
                background_color=(0.22, 0.22, 0.22, 1),
                color=(1, 1, 1, 1),
                halign="center",
                valign="middle"
            )
            btn.bind(on_press=lambda instance, value=phone: self.open_contact(value))
            layout.add_widget(btn)

        warning = Label(
            text="In immediate danger, call 999.",
            font_size="17sp",
            bold=True,
            color=(0.5, 0, 0, 1),
            size_hint_y=None,
            height=50,
            halign="center",
            valign="middle"
        )
        warning.bind(size=warning.setter("text_size"))
        layout.add_widget(warning)

        back_btn = Button(
            text="Back to Home",
            size_hint_y=None,
            height=65,
            font_size="20sp",
            background_color=(0.25, 0.15, 0.1, 1),
            color=(1, 1, 1, 1)
        )
        back_btn.bind(on_press=lambda x: setattr(self.manager, "current", "home"))
        layout.add_widget(back_btn)

        scroll.add_widget(layout)
        self.add_widget(scroll)

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def load_contacts(self):
        file_path = "emergency.json"

        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as f:
                    data = json.load(f)
                    return data if isinstance(data, list) else []
            except Exception as e:
                print(f"Error loading emergency.json: {e}")

        return [
            {
                "name": "Emergency Services",
                "phone": "999",
                "note": "Police, fire or ambulance"
            },
            {
                "name": "NHS 111",
                "phone": "111",
                "note": "Medical help when it is not 999"
            },
            {
                "name": "Samaritans",
                "phone": "116123",
                "note": "Free emotional support"
            }
        ]

    def open_contact(self, value):
        if value.startswith("http"):
            webbrowser.open(value)
        else:
            webbrowser.open(f"tel:{value}")
