from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class AboutScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(1, 0.98, 0.94, 1)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self._update_bg, pos=self._update_bg)

        root = BoxLayout(
            orientation="vertical",
            padding=[18, 18, 18, 12],
            spacing=10
        )

        scroll = ScrollView(size_hint=(1, 1))

        content = BoxLayout(
            orientation="vertical",
            padding=[6, 6, 6, 20],
            spacing=14,
            size_hint_y=None
        )
        content.bind(minimum_height=content.setter("height"))

        # Spacer to keep title below Android status bar
        content.add_widget(
            Widget(
                size_hint_y=None,
                height=50
            )
        )

        title = Label(
            text="[b]About SafeSpot[/b]",
            markup=True,
            font_size="26sp",
            color=(0.12, 0.08, 0.04, 1),
            size_hint_y=None,
            height=45
        )
        title.bind(size=title.setter("text_size"))
        content.add_widget(title)

        story_text = (
            "[b]Built from my own struggle.[/b]\n\n"
            "I've experienced homelessness, missed the last train and spent nights sleeping outside.\n\n"
            "Those experiences inspired me to create SafeSpot — a free app built to help people find safer places when they need them most.\n\n"
            "[b]It's more than an app.[/b]\n\n"
            "SafeSpot is a map of trusted places, quiet locations and emergency help. "
            "Whether you're homeless, travelling, stranded after missing transport, "
            "feeling unsafe or simply need somewhere calm to stop, SafeSpot is here to help.\n\n"
            "[b]Features[/b]\n\n"
            "✓ Find trusted safe places\n"
            "✓ Save your favourite locations\n"
            "✓ Read community comments\n"
            "✓ Add useful local spots\n"
            "✓ One-tap emergency contacts\n"
            "✓ Calm, simple design\n\n"
            "[b]Why I built SafeSpot[/b]\n\n"
            "When you've been in difficult situations yourself, you realise that one safe place can change everything. "
            "SafeSpot was created from real-life experience and is built to help others.\n\n"
            "[b]Built from survival. Made to help others.[/b]"
        )

        story = Label(
            text=story_text,
            markup=True,
            font_size="16sp",
            color=(0.08, 0.08, 0.08, 1),
            size_hint_y=None,
            halign="center",
            valign="top"
        )

        story.bind(
            width=lambda instance, width:
            setattr(instance, "text_size", (width, None))
        )

        story.bind(
            texture_size=lambda instance, size:
            setattr(instance, "height", size[1] + 20)
        )

        content.add_widget(story)

        scroll.add_widget(content)
        root.add_widget(scroll)

        privacy_btn = Button(
            text="View Privacy Policy",
            size_hint_y=None,
            height=52,
            background_color=(0.35, 0.25, 0.15, 1),
            color=(1, 1, 1, 1),
            font_size="16sp"
        )
        privacy_btn.bind(on_release=self.show_privacy_policy)
        root.add_widget(privacy_btn)

        back_btn = Button(
            text="Back to Home",
            size_hint_y=None,
            height=52,
            background_color=(0.25, 0.15, 0.10, 1),
            color=(1, 1, 1, 1),
            font_size="16sp"
        )
        back_btn.bind(
            on_release=lambda x: setattr(
                self.manager,
                "current",
                "home"
            )
        )
        root.add_widget(back_btn)

        self.add_widget(root)

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def show_privacy_policy(self, instance):

        content_text = (
            "[b]Privacy Policy[/b]\n\n"
            "SafeSpot is designed to help people find safe places and useful community information.\n\n"
            "[b]Information you provide[/b]\n"
            "• Safe spots you add\n"
            "• Comments you post\n"
            "• Event information you submit\n\n"
            "[b]How your data is used[/b]\n"
            "• To display safe locations.\n"
            "• To help other SafeSpot users.\n"
            "• To improve the app.\n\n"
            "[b]Storage[/b]\n"
            "Information is stored securely using Google Firebase.\n\n"
            "[b]We do NOT[/b]\n"
            "• Sell your personal information.\n"
            "• Share your data with advertisers.\n"
            "• Track your location without permission.\n\n"
            "[b]Your Choices[/b]\n"
            "You can request removal of content that you have added.\n\n"
            "[b]Disclaimer[/b]\n"
            "SafeSpot provides community information only. "
            "Always use your own judgement and contact the emergency services "
            "if you are in immediate danger.\n\n"
            "For emergencies call 999."
        )

        root = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        scroll = ScrollView(size_hint=(1, 1))

        label = Label(
            text=content_text,
            markup=True,
            font_size="16sp",
            color=(0.08, 0.08, 0.08, 1),
            size_hint_y=None,
            halign="left",
            valign="top"
        )

        label.bind(
            width=lambda instance, width:
            setattr(instance, "text_size", (width, None))
        )

        label.bind(
            texture_size=lambda instance, size:
            setattr(instance, "height", size[1] + 20)
        )

        scroll.add_widget(label)
        root.add_widget(scroll)

        close_btn = Button(
            text="Close",
            size_hint_y=None,
            height=50,
            background_color=(0.35, 0.25, 0.15, 1),
            color=(1, 1, 1, 1),
            font_size="16sp"
        )

        root.add_widget(close_btn)

        popup = Popup(
            title="Privacy Policy",
            content=root,
            size_hint=(0.9, 0.8)
        )

        close_btn.bind(on_release=popup.dismiss)

        popup.open()
