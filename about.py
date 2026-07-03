def show_privacy_policy(self, instance):
    from kivy.uix.scrollview import ScrollView

    content_text = (
        "[b]Privacy Policy[/b]\n\n"

        "SafeSpot is designed to help people find safe places and useful "
        "community information.\n\n"

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
        "SafeSpot provides community information only. Always use your own "
        "judgement and contact the emergency services if you are in immediate danger.\n\n"

        "For emergencies call 999."
    )

    root = BoxLayout(
        orientation="vertical",
        spacing=10,
        padding=15
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
