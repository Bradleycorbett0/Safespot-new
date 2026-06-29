from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window

import requests
import webbrowser


BASE_URL = "https://safespot-4f250-default-rtdb.europe-west1.firebasedatabase.app/spots"


class SpotsScreen(Screen):
    def on_pre_enter(self):
        self.load_cities()

    def load_cities(self):
        self.clear_widgets()

        scroll = ScrollView(size_hint=(1, 1))

        container = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            padding=20,
            spacing=12
        )
        container.bind(minimum_height=container.setter("height"))

        title = Label(
            text="[b]Saved Safe Spots[/b]",
            markup=True,
            size_hint_y=None,
            height=60,
            font_size="24sp",
            color=(0, 0, 0, 1)
        )
        container.add_widget(title)

        try:
            response = requests.get(f"{BASE_URL}.json", timeout=15)

            if response.status_code == 200:
                data = response.json()

                if data:
                    for city_name in sorted(data.keys()):
                        btn = Button(
                            text=city_name.title().replace("_", " "),
                            size_hint_y=None,
                            height=70,
                            font_size="20sp",
                            background_color=(0.15, 0.15, 0.15, 1),
                            color=(1, 1, 1, 1)
                        )
                        btn.bind(
                            on_press=lambda instance, city=city_name: self.show_spots(city)
                        )
                        container.add_widget(btn)
                else:
                    container.add_widget(self.message_label("No saved spots yet."))
            else:
                container.add_widget(
                    self.message_label(
                        f"Firebase error:\n{response.status_code}\n{response.text}"
                    )
                )

        except Exception as e:
            container.add_widget(self.message_label(f"Error:\n{e}"))

        back_btn = Button(
            text="← Back to Home",
            size_hint_y=None,
            height=65,
            font_size="18sp",
            background_color=(0.2, 0.2, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        back_btn.bind(on_press=lambda x: self.go_home())
        container.add_widget(back_btn)

        scroll.add_widget(container)
        self.add_widget(scroll)

    def go_home(self):
        self.manager.current = "home"

    def show_spots(self, city):
        self.clear_widgets()

        scroll = ScrollView(size_hint=(1, 1))

        container = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            padding=18,
            spacing=18
        )
        container.bind(minimum_height=container.setter("height"))

        title = Label(
            text=f"[b]{city.title().replace('_', ' ')} Safe Spots[/b]",
            markup=True,
            size_hint_y=None,
            height=60,
            font_size="23sp",
            color=(0, 0, 0, 1)
        )
        container.add_widget(title)

        try:
            response = requests.get(f"{BASE_URL}/{city}.json", timeout=15)

            if response.status_code == 200:
                data = response.json()

                if data:
                    for spot_id, spot_info in data.items():
                        if not isinstance(spot_info, dict):
                            continue

                        name = spot_info.get("name", "Unknown")
                        desc = spot_info.get("description", "No description available")
                        location = spot_info.get("location", f"{name}, {city}")

                        card = BoxLayout(
                            orientation="vertical",
                            size_hint_y=None,
                            spacing=10,
                            padding=10
                        )
                        card.bind(minimum_height=card.setter("height"))

                        lbl = Label(
                            text=f"[b]{name}[/b]\n{desc}",
                            markup=True,
                            halign="left",
                            valign="top",
                            size_hint_y=None,
                            text_size=(Window.width - 60, None),
                            font_size="17sp",
                            color=(0, 0, 0, 1)
                        )
                        lbl.bind(
                            texture_size=lambda instance, value: setattr(
                                instance,
                                "height",
                                value[1] + 25
                            )
                        )

                        btn_row = BoxLayout(
                            orientation="horizontal",
                            size_hint_y=None,
                            height=58,
                            spacing=10
                        )

                        directions_btn = Button(
                            text="📍 Get Directions",
                            size_hint_x=0.5,
                            font_size="17sp",
                            background_color=(0.1, 0.5, 0.1, 1),
                            color=(1, 1, 1, 1)
                        )
                        directions_btn.bind(
                            on_press=lambda x, loc=location: self.open_directions(loc)
                        )

                        delete_btn = Button(
                            text="🗑 Delete",
                            size_hint_x=0.5,
                            font_size="17sp",
                            background_color=(0.6, 0, 0, 1),
                            color=(1, 1, 1, 1)
                        )
                        delete_btn.bind(
                            on_press=lambda x, cid=city, sid=spot_id, sname=name:
                            self.confirm_delete(cid, sid, sname)
                        )

                        btn_row.add_widget(directions_btn)
                        btn_row.add_widget(delete_btn)

                        card.add_widget(lbl)
                        card.add_widget(btn_row)
                        container.add_widget(card)

                else:
                    container.add_widget(
                        self.message_label("No safe spots found for this city.")
                    )
            else:
                container.add_widget(
                    self.message_label(
                        f"Firebase error:\n{response.status_code}\n{response.text}"
                    )
                )

        except Exception as e:
            container.add_widget(self.message_label(f"Error:\n{e}"))

        back_btn = Button(
            text="← Back to Cities",
            size_hint_y=None,
            height=65,
            font_size="18sp",
            background_color=(0.2, 0.2, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        back_btn.bind(on_press=lambda x: self.load_cities())
        container.add_widget(back_btn)

        scroll.add_widget(container)
        self.add_widget(scroll)

    def open_directions(self, location):
        maps_url = (
            "https://www.google.com/maps/search/?api=1&query="
            + location.replace(" ", "+")
        )
        webbrowser.open(maps_url)

    def confirm_delete(self, city, spot_id, name):
        box = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        msg = Label(
            text=f"Are you sure you want to delete:\n[b]{name}[/b]?",
            markup=True,
            color=(0, 0, 0, 1),
            halign="center",
            valign="middle"
        )
        msg.bind(size=msg.setter("text_size"))

        btn_row = BoxLayout(
            spacing=10,
            size_hint_y=None,
            height=55
        )

        yes_btn = Button(
            text="Yes, Delete",
            background_color=(0.7, 0, 0, 1),
            color=(1, 1, 1, 1)
        )

        no_btn = Button(
            text="Cancel",
            background_color=(0.2, 0.2, 0.2, 1),
            color=(1, 1, 1, 1)
        )

        popup = Popup(
            title="Confirm Delete",
            content=box,
            size_hint=(0.85, 0.42)
        )

        yes_btn.bind(
            on_press=lambda x: (
                self.delete_spot(city, spot_id),
                popup.dismiss()
            )
        )
        no_btn.bind(on_press=lambda x: popup.dismiss())

        btn_row.add_widget(yes_btn)
        btn_row.add_widget(no_btn)

        box.add_widget(msg)
        box.add_widget(btn_row)

        popup.open()

    def delete_spot(self, city, spot_id):
        try:
            response = requests.delete(
                f"{BASE_URL}/{city}/{spot_id}.json",
                timeout=15
            )

            if response.status_code == 200:
                self.show_spots(city)
            else:
                self.show_popup(
                    f"Delete failed:\n{response.status_code}\n{response.text}"
                )

        except Exception as e:
            self.show_popup(f"Delete error:\n{e}")

    def show_popup(self, message):
        label = Label(
            text=message,
            halign="center",
            valign="middle"
        )
        label.bind(size=label.setter("text_size"))

        Popup(
            title="SafeSpot",
            content=label,
            size_hint=(0.85, 0.4)
        ).open()

    def message_label(self, message):
        label = Label(
            text=message,
            size_hint_y=None,
            height=80,
            color=(0, 0, 0, 1),
            halign="center",
            valign="middle"
        )
        label.bind(size=label.setter("text_size"))
        return label
