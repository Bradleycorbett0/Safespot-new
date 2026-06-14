import json
import os
import webbrowser

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class EmergencyContactsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        scroll = ScrollView(size_hint=(1, 1))

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12,
            size_hint_y=None
        )
        layout.bind(minimum_height=layout.setter("height"))

        title = Label(
            text="Emergency Contacts",
            font_size="24sp",
            size_hint_y=None,
            height=70
        )
        layout.add_widget(title)

        contacts = self.load_contacts()

        for contact in contacts:
            name = contact.get("name", "Unknown")
            phone = contact.get("phone", "")

            btn = Button(
                text=f"{name}\n{phone}",
                size_hint_y=None,
                height=90
            )
            btn.bind(on_press=lambda instance, value=phone: self.open_contact(value))
            layout.add_widget(btn)

        back_btn = Button(
            text="Back",
            size_hint_y=None,
            height=70
        )
        back_btn.bind(on_press=lambda x: setattr(self.manager, "current", "home"))
        layout.add_widget(back_btn)

        scroll.add_widget(layout)
        self.add_widget(scroll)

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
            {"name": "Emergency Services (999)", "phone": "999"},
            {"name": "NHS (111)", "phone": "111"},
            {"name": "Samaritans", "phone": "116123"}
        ]

    def open_contact(self, value):
        if value.startswith("http"):
            webbrowser.open(value)
        else:
            webbrowser.open(f"tel:{value}")
