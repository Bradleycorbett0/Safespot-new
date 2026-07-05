# -*- coding: utf-8 -*-
import re
import traceback

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.core.window import Window

from firebase_config import save_data


class AddSpotScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.softinput_mode = "resize"

        layout = BoxLayout(orientation="vertical", padding=14, spacing=14)
        scroll = ScrollView(size_hint=(1, 1))

        box = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=14,
            size_hint_y=None
        )
        box.bind(minimum_height=box.setter("height"))

        title = Label(
            text="[b]Add a New Safe Spot[/b]",
            markup=True,
            font_size="18sp",
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=75,
            halign="center",
            valign="middle"
        )
        title.bind(size=title.setter("text_size"))
        box.add_widget(title)

        cities = sorted([
            "Aberdeen", "Bangor", "Bath", "Belfast", "Birmingham", "Blackpool",
            "Bolton", "Bournemouth", "Bradford", "Brighton", "Bristol",
            "Cambridge", "Canterbury", "Cardiff", "Carlisle", "Chelmsford",
            "Chester", "Colchester", "Coventry", "Derby", "Dundee", "Durham",
            "Edinburgh", "Exeter", "Glasgow", "Gloucester", "Hereford",
            "Inverness", "Kingston upon Hull", "Lancaster", "Leeds", "Leicester",
            "Lincoln", "Liverpool", "London", "Luton", "Manchester",
            "Middlesbrough", "Milton Keynes", "Newcastle", "Newport", "Norwich",
            "Nottingham", "Oxford", "Peterborough", "Plymouth", "Portsmouth",
            "Preston", "Reading", "Sheffield", "Southampton", "St Albans",
            "Stoke-on-Trent", "Sunderland", "Swansea", "Truro", "Wakefield",
            "Wolverhampton", "Worcester", "York"
        ])

        self.city_spinner = Spinner(
            text="Select a City",
            values=cities,
            size_hint_y=None,
            height=78,
            font_size="24sp",
            background_color=(0.35, 0.35, 0.35, 1),
            color=(1, 1, 1, 1)
        )
        box.add_widget(self.city_spinner)

        self.name_input = TextInput(
            hint_text="Safe Spot Name",
            multiline=False,
            size_hint_y=None,
            height=90,
            font_size="26sp",
            padding=[12, 24, 12, 18],
            foreground_color=(0, 0, 0, 1),
            hint_text_color=(0.45, 0.45, 0.45, 1),
            background_color=(1, 1, 1, 1)
        )
        box.add_widget(self.name_input)

        self.desc_input = TextInput(
            hint_text="Describe this safe spot",
            multiline=True,
            size_hint_y=None,
            height=230,
            font_size="22sp",
            padding=[12, 24, 12, 18],
            foreground_color=(0, 0, 0, 1),
            hint_text_color=(0.45, 0.45, 0.45, 1),
            background_color=(1, 1, 1, 1)
        )
        box.add_widget(self.desc_input)

        save_btn = Button(
            text="💾 Save Spot to Cloud",
            size_hint_y=None,
            height=75,
            font_size="22sp",
            background_color=(0, 0.45, 0, 1),
            color=(1, 1, 1, 1)
        )
        save_btn.bind(on_release=self.save_spot)
        box.add_widget(save_btn)

        back_btn = Button(
            text="⬅ Back to Home",
            size_hint_y=None,
            height=75,
            font_size="22sp",
            background_color=(0.45, 0, 0, 1),
            color=(1, 1, 1, 1)
        )
        back_btn.bind(
            on_release=lambda x: setattr(App.get_running_app().root, "current", "home")
        )
        box.add_widget(back_btn)

        scroll.add_widget(box)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def safe_key(self, text):
        text = text.lower().strip()
        text = re.sub(r"[^a-z0-9]+", "_", text)
        text = text.strip("_")
        return text or "unnamed"

    def save_spot(self, instance):
        city = self.city_spinner.text.strip()
        name = self.name_input.text.strip()
        desc = self.desc_input.text.strip()

        if city == "Select a City":
            self.show_popup("Please select a city.")
            return

        if not name:
            self.show_popup("Please enter a name.")
            return

        if not desc:
            self.show_popup("Please enter a description.")
            return

        city_key = self.safe_key(city)
        spot_key = self.safe_key(name)

        data = {
            "city": city,
            "city_key": city_key,
            "spot_key": spot_key,
            "name": name,
            "description": desc,
            "location": f"{name}, {city}"
        }

        try:
            result = save_data(f"spots/{city_key}/{spot_key}", data)

            if isinstance(result, dict) and result.get("success") is True:
                self.show_popup("✅ Spot saved successfully!")
                self.city_spinner.text = "Select a City"
                self.name_input.text = ""
                self.desc_input.text = ""

            elif isinstance(result, dict) and result.get("success") is False:
                self.show_popup(
                    "❌ Firebase error:\n\n"
                    f"{result.get('error', 'Unknown error')}"
                )

            elif result is not None:
                self.show_popup("✅ Spot saved successfully!")
                self.city_spinner.text = "Select a City"
                self.name_input.text = ""
                self.desc_input.text = ""

            else:
                self.show_popup(
                    "❌ Failed to save to Firebase.\n\n"
                    "No response returned from firebase_config.py"
                )

        except Exception:
            self.show_popup(traceback.format_exc())

    def show_popup(self, message):
        label = Label(
            text=message,
            halign="center",
            valign="middle",
            font_size="16sp"
        )
        label.bind(size=label.setter("text_size"))

        Popup(
            title="SafeSpot",
            content=label,
            size_hint=(0.9, 0.45)
        ).open()
