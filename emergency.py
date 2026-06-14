import json
import os
import webbrowser

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class EmergencyContactsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=12)

        title = Label(
            text="Emergency Contacts",
            font_size="24sp",
            size_hint_y=None,
            height=60
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

        self.add_widget(layout)

    def load_contacts(self):
        file_path = "emergency.json"

        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as f:
                    return json.load(f)
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
