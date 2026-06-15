from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.popup import Popup
from firebase_config import save_spot_to_firebase, initialize_firebase


class AddSpotScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.softinput_mode = "resize"
        
        # Initialize Firebase when screen is created
        initialize_firebase()

        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        scroll = ScrollView(size_hint=(1, 1))
        box = BoxLayout(orientation="vertical", padding=10, spacing=10, size_hint_y=None)
        box.bind(minimum_height=box.setter("height"))

        # Title
        title = Label(
            text="[b]Add a New Safe Spot[/b]",
            markup=True,
            font_size="26sp",
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=60
        )
        box.add_widget(title)

        # City dropdown
        default_cities = sorted([
            "Aberdeen", "Bangor", "Bath", "Belfast", "Birmingham", "Blackpool",
            "Bolton", "Bournemouth", "Bradford", "Brighton", "Bristol", "Cambridge",
            "Canterbury", "Cardiff", "Carlisle", "Chelmsford", "Chester", "Colchester",
            "Coventry", "Derby", "Dundee", "Durham", "Edinburgh", "Exeter", "Glasgow",
            "Gloucester", "Hereford", "Inverness", "Kingston upon Hull", "Lancaster",
            "Leeds", "Leicester", "Lincoln", "Liverpool", "London", "Luton",
            "Manchester", "Middlesbrough", "Milton Keynes", "Newcastle", "Newport",
            "Norwich", "Nottingham", "Oxford", "Peterborough", "Plymouth", "Portsmouth",
            "Preston", "Reading", "Sheffield", "Southampton", "St Albans",
            "Stoke-on-Trent", "Sunderland", "Swansea", "Truro", "Wakefield",
            "Wolverhampton", "Worcester", "York"
        ])

        self.city_spinner = Spinner(
            text="Select a City",
            values=default_cities,
            size_hint_y=None,
            height=55,
            background_color=(0.1, 0.2, 0.5, 1),
            color=(1, 1, 1, 1),
            font_size="18sp"
        )
        box.add_widget(self.city_spinner)

        # Safe Spot Name
        self.name_input = TextInput(
            hint_text="Enter Safe Spot name",
            multiline=False,
            size_hint_y=None,
            height=55,
            font_size="18sp"
        )
        box.add_widget(self.name_input)

        # Safe Spot Description
        self.desc_input = TextInput(
            hint_text="Describe the Safe Spot",
            multiline=True,
            size_hint_y=None,
            height=150,
            font_size="18sp"
        )
        box.add_widget(self.desc_input)

        # Save button
        save_button = Button(
            text="💾 Save Spot to Cloud",
            size_hint_y=None,
            height=55,
            background_color=(0, 0.4, 0, 1),
            color=(1, 1, 1, 1),
            font_size="18sp"
        )
        save_button.bind(on_release=self.save_spot)
        box.add_widget(save_button)

        # Back button
        back_button = Button(
            text="⬅ Back to Home",
            size_hint_y=None,
            height=55,
            background_color=(0.4, 0, 0, 1),
            color=(1, 1, 1, 1),
            font_size="18sp"
        )
        back_button.bind(on_release=lambda x: setattr(App.get_running_app().root, "current", "home"))
        box.add_widget(back_button)

        scroll.add_widget(box)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def save_spot(self, instance):
        city = self.city_spinner.text
        name = self.name_input.text.strip()
        desc = self.desc_input.text.strip()

        if not city or city == "Select a City":
            self.show_popup("Please select a city.")
            return
        if not name:
            self.show_popup("Please enter a name.")
            return
        if not desc:
            self.show_popup("Please add a description.")
            return

        # Save to Firebase using the new config module
        result = save_spot_to_firebase(city, name, desc)
        
        if result['success']:
            self.show_popup(result['message'])
            self.name_input.text = ""
            self.desc_input.text = ""
            self.city_spinner.text = "Select a City"
        else:
            self.show_popup(result['message'])

    def show_popup(self, message):
        Popup(
            title="SafeSpot",
            content=Label(text=message, font_size="18sp"),
            size_hint=(0.8, 0.3)
        ).open()
