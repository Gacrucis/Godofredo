from enum import Enum
import os
import sys
import itertools as it
from colour import Color
from manim import *  # type: ignore

import video_utils
import presets


UIS_GREEN = "#67b93e"
PURPLE = '#673c4f'
LIGHT_PURPLE = '#7f557d'
VIOLET = '#726e97'
DARK_SKY_BLUE = '#7698b3'
SKY_BLUE = '#83b5d1'
BEIGE = '#7c795d'

PALETTE = [PURPLE, VIOLET, LIGHT_PURPLE, SKY_BLUE, DARK_SKY_BLUE]


class Intro(MovingCameraScene):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.uis_logo = SVGMobject(
    #         file_name='.\\assets\\svg\\UIS.svg').scale(1.2)

    #     self.uis_logo[1].set_fill(color=WHITE, opacity=.9)
    #     self.uis_logo[5:].set_fill(color=WHITE, opacity=.9)

    #     self.names_config = {
    #         "stroke_width": 1,
    #         "background_stroke_width": 5,
    #         "background_stroke_color": BLACK,
    #         "sheen_factor": .2,
    #         "sheen_direction": UR,
    #     }

    def construct(self):
        title = Tex('HDLE')

if __name__ == "__main__":
    runner = video_utils.ManimRunner(
        scenes={
            # 'Intro': [
            #     '-ql',
            #     '-p'
            # ],
            # 'FirstChapterIntro': [
            #     '-sql',
            #     '-p'
            # ],
            'FirstChapter': [
                '-qh',
                '-p'
            ],
            'SecondChapter': [
                '-qh',
                '-p'
            ],
            # 'Bibliography': [
            #     '-qh',
            #     # '-p'
            # ],
            # 'Outro': [
            #     '-ql',
            #     '-p'
            # ],
            # 'Test': [
            #     '-sql',
            #     '-p'
            # ]
        },
        file_path=r'main.py',  # it's relative to cwd
        project_name='Godofredo'
    )

    runner.run_scenes()
    runner.concatenate_videos(run_output=True)