from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Приложение"

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Главная'
            icon: 'home'

            MDLabel:
                text: 'Главная'
                halign: 'center'

            MDBoxLayout:
                orientation: "horizontal"
                padding: [15,15,15,15]
                spacing: 25

                MDSmartTile:
                    radius: 24
                    box_radius: [0, 0, 24, 24]
                    box_color: 1, 1, 1, .2
                    source: "cats.jpg"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint: None, None
                    size: "200dp", "200dp"

                    MDIconButton:
                        icon: "heart-outline"
                        theme_icon_color: "Custom"
                        icon_color: 1, 0, 0, 1
                        pos_hint: {"center_y": .5}
                        on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                    MDLabel:
                        text: "Julia and Julie"
                        bold: True
                        color: 1, 1, 1, 1

                MDSmartTile:
                    radius: 24
                    box_radius: [0, 0, 24, 24]
                    box_color: 1, 1, 1, .2
                    source: "cats.jpg"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint: None, None
                    size: "200dp", "200dp"

                    MDIconButton:
                        icon: "heart-outline"
                        theme_icon_color: "Custom"
                        icon_color: 1, 0, 0, 1
                        pos_hint: {"center_y": .5}
                        on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                    MDLabel:
                        text: "Julia and Julie"
                        bold: True
                        color: 1, 1, 1, 1

                MDSmartTile:
                    radius: 24
                    box_radius: [0, 0, 24, 24]
                    box_color: 1, 1, 1, .2
                    source: "cats.jpg"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint: None, None
                    size: "200dp", "200dp"

                    MDIconButton:
                        icon: "heart-outline"
                        theme_icon_color: "Custom"
                        icon_color: 1, 0, 0, 1
                        pos_hint: {"center_y": .5}
                        on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                    MDLabel:
                        text: "Julia and Julie"
                        bold: True
                        color: 1, 1, 1, 1

                MDSmartTile:
                    radius: 24
                    box_radius: [0, 0, 24, 24]
                    box_color: 1, 1, 1, .2
                    source: "cats.jpg"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint: None, None
                    size: "200dp", "200dp"

                    MDIconButton:
                        icon: "heart-outline"
                        theme_icon_color: "Custom"
                        icon_color: 1, 0, 0, 1
                        pos_hint: {"center_y": .5}
                        on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                    MDLabel:
                        text: "Julia and Julie"
                        bold: True
                        color: 1, 1, 1, 1
                
                MDSmartTile:
                    radius: 24
                    box_radius: [0, 0, 24, 24]
                    box_color: 1, 1, 1, .2
                    source: "cats.jpg"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint: None, None
                    size: "200dp", "200dp"

                    MDIconButton:
                        icon: "heart-outline"
                        theme_icon_color: "Custom"
                        icon_color: 1, 0, 0, 1
                        pos_hint: {"center_y": .5}
                        on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                    MDLabel:
                        text: "Julia and Julie"
                        bold: True
                        color: 1, 1, 1, 1

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Каталог'
            icon: 'text-search-variant'
            badge_icon: "numeric-10"

            MDLabel:
                text: 'Каталог'
                halign: 'center'

            MDScrollView:

                MDList:
                    id: container

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Связаться'
            icon: 'chat-question-outline'
            badge_icon: "numeric-5"

            MDLabel:
                text: 'Связаться'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Профиль'
            icon: 'account'

            MDLabel:
                text: 'Профиль'
                halign: 'center'
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(20):
            self.root.ids.container.add_widget(
                OneLineListItem(text=f"Single-line item {i}")
            )

Example().run()
