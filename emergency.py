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
            padding=[18, 14, 18, 18],
            spacing=12,
            size_hint_y=None
        )
        layout.bind(minimum_height=layout.setter("height"))

        title = Label(
            text="[b]Emergency Help[/b]",
            markup=True,
            font_size="26sp",
            size_hint_y=None,
            height=65,
            color=(0.1, 0.1, 0.1, 1),
            halign="center",
            valign="middle"
        )
        title.bind(size=title.setter("text_size"))
        layout.add_widget(title)

        intro = Label(
            text="If you are in danger or need support, choose a service below.",
            size_hint_y=None,
            height=65,
            font_size="16sp",
            halign="center",
            valign="middle",
            color=(0.2, 0.2, 0.2, 1)
        )
        intro.bind(size=intro.setter("text_size"))
        layout.add_widget(intro)

        try:
            response = requests.get(f"{FIREBASE_URL}/emergency.json", timeout=15)

            if response.status_code == 200 and response.json():
                data = response.json()

                for key, contact in data.items():
                    if not isinstance(contact, dict):
                        continue

                    name = contact.get("name", "Emergency Contact")
                    phone = contact.get("phone", "")
                    note = contact.get("note", "")

                    card = BoxLayout(
                        orientation="vertical",
                        size_hint_y=None,
                        height=118,
                        padding=[10, 8, 10, 8],
                        spacing=4
                    )

                    title_lbl = Label(
                        text=f"[b]{name}[/b]",
                        markup=True,
                        font_size="18sp",
                        color=(0.05, 0.05, 0.05, 1),
                        size_hint_y=None,
                        height=65,
                        halign="center",
                        valign="middle"
                    )
                    title_lbl.bind(size=title_lbl.setter("text_size"))

                    detail_text = phone
                    if note:
                        detail_text += f"\n{note}"

                    detail_lbl = Label(
                        text=detail_text,
                        font_size="14sp",
                        color=(0.15, 0.15, 0.15, 1),
                        size_hint_y=None,
                        height=65,
                        halign="center",
                        valign="middle"
                    )
                    detail_lbl.bind(size=detail_lbl.setter("text_size"))

                    action_btn = Button(
                        text="Open Website" if phone.startswith("http") else f"Call {phone}",
                        size_hint_y=None,
                        height=65,
                        font_size="15sp",
                        background_color=(0.18, 0.18, 0.18, 1),
                        color=(1, 1, 1, 1)
                    )
                    action_btn.bind(
                        on_press=lambda instance, value=phone: self.open_contact(value)
                    )

                    card.add_widget(title_lbl)
                    card.add_widget(detail_lbl)
                    card.add_widget(action_btn)
                    layout.add_widget(card)

            else:
                layout.add_widget(self.message_label("No emergency contacts available."))

        except Exception as e:
            layout.add_widget(self.message_label(f"Error loading contacts\n{e}"))

        warning = Label(
            text="[b]In an emergency, always call 999 immediately.[/b]",
            markup=True,
            size_hint_y=None,
            height=65,
            font_size="15sp",
            color=(0.6, 0, 0, 1),
            halign="center",
            valign="middle"
        )
        warning.bind(size=warning.setter("text_size"))
        layout.add_widget(warning)

        back_btn = Button(
            text="Back to Home",
            size_hint_y=None,
            height=65,
            font_size="18sp",
            background_color=(0.25, 0.15, 0.1, 1),
            color=(1, 1, 1, 1)
        )
        back_btn.bind(on_press=lambda x: setattr(self.manager, "current", "home"))
        layout.add_widget(back_btn)

        scroll.add_widget(layout)
        self.add_widget(scroll)

    def message_label(self, text):
        label = Label(
            text=text,
            size_hint_y=None,
            height=80,
            font_size="16sp",
            color=(0.1, 0.1, 0.1, 1),
            halign="center",
            valign="middle"
        )
        label.bind(size=label.setter("text_size"))
        return label

    def open_contact(self, value):
        if value.startswith("http"):
            webbrowser.open(value)
        else:
            webbrowser.open(f"tel:{value}")
