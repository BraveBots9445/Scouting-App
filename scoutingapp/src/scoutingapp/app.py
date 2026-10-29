
"""
A scouting app for team 9445 The Brave Bots
"""

import toga
from toga.style.pack import COLUMN, ROW


class ScoutingApp(toga.App):
    def startup(self):

        outer_box = toga.Box(
            direction=COLUMN,
            background_color="#000000"
        )


        main_box = toga.Box(
            direction=COLUMN,
            background_color="#242424",
            margin=20,
            padding=15,
            flex=1
        )

        regional_label = toga.Label(
            "Your regional:",
            width=210,
            margin=10,
            color="#FF9700"
        )

        competiton_label = toga.Label(
            "Your competition:",
            width=210,
            margin=10,
            color="#FF9700"
        )

        round_label = toga.Label(
            "Round number:",
            width=210,
            margin=10,
            color="#FF9700"
        )

        team_label = toga.Label(
            "Team number you're scouting:",
            width=210,
            margin=10,
            color="#FF9700"
        )

        self.regional_input = toga.TextInput(
            flex=1,
            margin=10,
            background_color="#404040",
            color="#FFFFFF"
        )

        self.competiton_input = toga.TextInput(
            flex=1,
            margin=10,
            background_color="#404040",
            color="#FFFFFF"
        )

        self.round_input = toga.TextInput(
            flex=1,
            margin=10,
            background_color="#404040",
            color="#FFFFFF"
        )

        self.team_input = toga.TextInput(
            flex=1,
            margin=10,
            background_color="#404040",
            color="#FFFFFF"
        )

        self.regional_box = toga.Box(direction=ROW, margin=5)
        self.regional_box.add(regional_label)
        self.regional_box.add(self.regional_input)

        self.competiton_box = toga.Box(direction=ROW, margin=5)
        self.competiton_box.add(competiton_label)
        self.competiton_box.add(self.competiton_input)

        self.round_box = toga.Box(direction=ROW, margin=5)
        self.round_box.add(round_label)
        self.round_box.add(self.round_input)

        self.team_box = toga.Box(direction=ROW, margin=5)
        self.team_box.add(team_label)
        self.team_box.add(self.team_input)

        def confirm(widget):
            print(self.regional_input.value)
            print(self.competiton_input.value)
            print(self.round_input.value)
            print(self.team_input.value)

        confirm_button = toga.Button(
            "Confirm",
            on_press=confirm,
            margin=20,
            color="#000000",
            background_color="#FF7900"
        )

        main_box.add(self.regional_box)
        main_box.add(self.competiton_box)
        main_box.add(self.round_box)
        main_box.add(self.team_box)
        main_box.add(confirm_button)

        outer_box.add(main_box)

        self.main_window = toga.MainWindow(
            title=self.formal_name
        )
        self.main_window.content = outer_box
        self.main_window.show()


def main():
    return ScoutingApp()
