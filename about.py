import os

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
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
            padding=[6, 6, 6, 6],
            spacing=14,
            size_hint_y=None
        )
        content.bind(minimum_height=content.setter("height"))

        logo_path = "safespot_logo.png"
        if not os.path.exists(logo_path):
            logo_path = "logo.png"

        if os.path.exists(logo_path):
            logo = Image(
                source=logo_path,
                size_hint_y=None,
                height=120,
                allow_stretch=True,
                keep_ratio=True
            )
            content.add_widget(logo)

        title = Label(
            text="[b]About SafeSpot[/b]",
            markup=True,
            font_size="26sp",
            color=(0.12, 0.08, 0.04, 1),
            size_hint_y=None,
            height=50,
            halign="center",
            valign="middle"
        )
        title.bind(size=title.setter("text_size"))
        content.add_widget(title)

        story_text = (
            "[b]Built from my own struggle.[/b]\n\n"
            "I’ve experienced homelessness, missed the last train, "
            "and spent nights sleeping outside.\n\n"
            "Those moments were hard, but they inspired me to create "
            "SafeSpot — a free app built to help people find safer places "
            "when they need them most.\n\n"
            "[b]SafeSpot is here to help people feel less alone.[/b]\n\n"
            "Whether someone is homeless, stuck after missing transport, "
            "feeling unsafe, struggling with their mental health, or simply "
            "needs somewhere calm to stop for a while, SafeSpot is designed "
            "to point them towards trusted spaces and emergency help.\n\n"
            "[b]What you can do with SafeSpot:[/b]\n\n"
            "✓ Find trusted safe places\n"
            "✓ Save your favourite locations\n"
            "✓ Read community comments\n"
            "✓ Add useful local spots\n"
            "✓ Access one-tap emergency contacts\n"
            "✓ Use a calm, simple design when under pressure\n\n"
            "[b]Why I built it[/b]\n\n"
            "When you are outside with nowhere safe to go, even one trusted "
            "place can make a difference. SafeSpot was created from real-life "
            "experience, not just an idea.\n\n"
            "This app is for people who need safety, support, direction, "
            "or a moment to breathe.\n\n"
            "[b]SafeSpot[/b] — built from survival, made to help others.\n\n"
            "#SafeSpotApp #BuiltFromSurvival #HomelessToHope\n"
            "#FindYourSafeSpot #SafeSpacesMatter #MentalHealth\n"
            "#EmergencyHelp #UrbanSafety #SurvivorMade"
        )

        story = Label(
            text=story_text,
            markup=True,
            font_size="15sp",
            color=(0.08, 0.08, 0.08, 1),
            size_hint_y=None,
            halign="center",
            valign="top"
        )
        story.bind(
            width=lambda instance, width: setattr(
                instance, "text_size", (width, None)
            )
        )
        story.bind(
            texture_size=lambda instance, size: setattr(
                instance, "height", size[1] + 20
            )
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
            background_color=(0.25, 0.15, 0.1, 1),
            color=(1, 1, 1, 1),
            font_size="16sp"
        )
        back_btn.bind(on_release=lambda x: setattr(self.manager, "current", "home"))
        root.add_widget(back_btn)

        self.add_widget(root)

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def show_privacy_policy(self, instance):
        content_text = (
            "[b]Privacy Policy[/b]\n\n"
            "SafeSpot respects your privacy.\n\n"
            "• Your data may be stored securely in Google Firebase.\n"
            "• No personal information is sold to third parties.\n"
            "• Location data is used only to show or save safe spots.\n"
            "• You can request deletion of your data.\n\n"
            "SafeSpot was created to protect — not to collect."
        )

        box = BoxLayout(
            orientation="vertical",
            padding=18,
            spacing=12
        )

        label = Label(
            text=content_text,
            markup=True,
            font_size="15sp",
            color=(0.08, 0.08, 0.08, 1),
            size_hint_y=None,
            halign="left",
            valign="top"
        )
        label.bind(
            width=lambda instance, width: setattr(
                instance, "text_size", (width, None)
            )
        )
        label.bind(
            texture_size=lambda instance, size: setattr(
                instance, "height", size[1] + 20
            )
        )

        close_btn = Button(
            text="Close",
            size_hint_y=None,
            height=50,
            background_color=(0.35, 0.25, 0.15, 1),
            color=(1, 1, 1, 1),
            font_size="15sp"
        )

        box.add_widget(label)
        box.add_widget(close_btn)

        popup = Popup(
            title="Privacy Policy",
            content=box,
            size_hint=(0.9, 0.7)
        )

        close_btn.bind(on_release=popup.dismiss)
        popup.open()
