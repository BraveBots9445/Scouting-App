
"""
A scouting app for team 9445 The Brave Bots
"""

import toga
import time
import asyncio
from toga.style.pack import COLUMN, ROW


class ScoutingApp(toga.App):
    def startup(self):

        self.regional = ""
        self.competiton = ""
        self.round = ""
        self.team = ""
        self.score = 0
        self.defend_time = 0
        self.defending = False

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

        scouting_outer_box = toga.Box(
            direction=COLUMN,
            background_color="#000000"
        )

        scouting_box = toga.Box(
            direction=COLUMN,
            background_color="#242424",
            margin=20,
            padding=15,
            flex=1
        )

        defend_label = toga.Label(
            "Not defending",
            margin=10,
            color="#FF9700",
        )

        defend_time_label = toga.Label(
            "Defend Time: 0.0 seconds",
            margin=10,
            color="#FF9700",
        )

        score_label = toga.Label(
            f"Score: {self.score}",
            margin=10,
            color="#FF9700",
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

        async def timer():
            while self.defending:
                self.defend_time += 0.1

                defend_time_label.text = (
                    f"Defend Time: {round(self.defend_time, 1)} seconds"
                )

                await asyncio.sleep(0.1)

        def confirm(widget):
            self.regional = self.regional_input.value
            self.competiton = self.competiton_input.value
            self.round = self.round_input.value
            self.team = self.team_input.value

            scouting_outer_box.add(scouting_box)
            self.main_window.content = scouting_outer_box

        def score(widget):
            self.score += 1
            score_label.text = f"Score: {self.score}"

        def defend(widget):
            if self.defending == False:
                self.defending = True
                defend_label.text = "Defending"

                asyncio.create_task(timer())

            else:
                self.defending = False
                defend_label.text = "Not defending"

        confirm_button = toga.Button(
            "Confirm",
            on_press=confirm,
            margin=20,
            color="#000000",
            background_color="#FF9700"
        )

        score_button = toga.Button(
            on_press=score,
            margin=10,
            width=100,
            height=100,
            background_color="#FF9700",
            color="#FFFFFF",
            padding=10,
            icon=toga.Icon("score_icon.png")
        )

        defend_button = toga.Button(
            on_press=defend,
            margin=10,
            color="#000000",
            background_color="#FF9700",
            width=100,
            height=100,
            padding=10,
            icon=toga.Icon("defend_icon.png")
        )

        score_box = toga.Box(
            direction=COLUMN,
            margin=20
        )
        score_box.add(score_button)
        score_box.add(score_label)

        defend_box = toga.Box(
            direction=COLUMN,
            margin=20
        )
        defend_box.add(defend_button)
        defend_box.add(defend_label)
        defend_box.add(defend_time_label)

        buttons_box = toga.Box(
            direction=ROW,
            margin=10
        )
        buttons_box.add(score_box)
        buttons_box.add(defend_box)

        main_box.add(self.regional_box)
        main_box.add(self.competiton_box)
        main_box.add(self.round_box)
        main_box.add(self.team_box)
        main_box.add(confirm_button)

        scouting_box.add(buttons_box)

        outer_box.add(main_box)

        self.main_window = toga.MainWindow(
            title=self.formal_name
        )

        self.main_window.content = outer_box
        self.main_window.show()


def main():
    return ScoutingApp()
