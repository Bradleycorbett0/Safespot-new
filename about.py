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
                height=130,
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
            height=45,
            halign="center",
            valign="middle"
        )
        title.bind(size=title.setter("text_size"))
        content.add_widget(title)

        tagline = Label(
            text="[b]Built from my own struggle.[/b]",
            markup=True,
            font_size="18sp",
            color=(0.18, 0.12, 0.06, 1),
            size_hint_y=None,
            height=40,
            halign="center",
            valign="middle"
        )
        tagline.bind(size=tagline.setter("text_size"))
        content.add_widget(tagline)

        story_text = (
            "Built from my own struggle.[/B]\n\n"
            "But I used those moments — on city benches,and in dark corners — "
            "to write my books, dream of building my games, and dream up SafeSpot.\n\n"
            "It’s more than an app. It’s a map of quiet places, trusted "
            "locations, and emergency help for anyone who needs safety on the go."
     — whether you’re "
    "a traveller, in crisis, or just need a breather.\n\n"
    "✓ Save spots\n"
    "✓ Add real-life comments\n"
    "✓ Emergency contacts ready\n"
    "✓ Calm design. Real impact.\n\n"
    "[b]Download SafeSpot now[/b] — because sometimes one safe space is "
    "all it takes to change everything.\n\n"
    "#SafeSpotApp #BuiltFromSurvival #HomelessToHope\n"
    "#FindYourSafeSpot #SafeSpacesMatter #MentalHealth\n"
    "#EmergencyHelp #UrbanSafety #SurvivorMade"
        )
        )

        story = Label(
            text=story_text,
            font_size="16sp",
            color=(0.08, 0.08, 0.08, 1),
            size_hint_y=None,
            height=190,
            halign="center",
            valign="top"
        )
        story.bind(size=story.setter("text_size"))
        content.add_widget(story)

        features_title = Label(
            text="[b]What SafeSpot helps with[/b]",
            markup=True,
            font_size="18sp",
            color=(0.12, 0.08, 0.04, 1),
            size_hint_y=None,
            height=40,
            halign="center",
            valign="middle"
        )
        features_title.bind(size=features_title.setter("text_size"))
        content.add_widget(features_title)

        features = [
            "• Save safe spots",
            "• Add real comments",
            "• Keep emergency contacts ready",
            "• Simple, calm design",
            "• Built for real-life safety"
        ]

        for feature in features:
            lbl = Label(
                text=feature,
                font_size="16sp",
                color=(0.08, 0.08, 0.08, 1),
                size_hint_y=None,
                height=34,
                halign="left",
                valign="middle"
            )
            lbl.bind(size=lbl.setter("text_size"))
            content.add_widget(lbl)

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
            halign="left",
            valign="top"
        )
        label.bind(size=label.setter("text_size"))

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
            size_hint=(0.9, 0.75)
        )

        close_btn.bind(on_release=popup.dismiss)
        popup.open()
