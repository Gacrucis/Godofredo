from enum import Enum
import os
import sys
import itertools as it
from colour import Color
from manim import *  # type: ignore

import video_utils
import presets

import configs


UIS_GREEN = "#67b93e"
PURPLE = '#673c4f'
LIGHT_PURPLE = '#7f557d'
VIOLET = '#726e97'
DARK_SKY_BLUE = '#7698b3'
SKY_BLUE = '#83b5d1'
BEIGE = '#7c795d'

PALETTE = [PURPLE, VIOLET, LIGHT_PURPLE, SKY_BLUE, DARK_SKY_BLUE]


class England(MovingCameraScene):

    def construct(self):

        ref_point = presets.get_coords(-6, 3)

        timeline = presets.TimeLine(**configs.timeline_config)
        timeline.preload_for_scene(
            target_time='1066',
            scene=self # pass the scene as parameter
        )

        # self.add(timeline)

        frame_height = self.camera.frame_height
        
        text = 'Rey Guillermo I encarga censo en el Domesday Book, documento acerca de la propiedad, extensión y valor de las tierras.'
        paragraph = presets.text_to_paragraph(text, line_length=20, color=BEIGE)

        # paragraph = Paragraph('\n'.join(paragraph), color=BEIGE)
        paragraph.height = frame_height/3
        paragraph.align_on_border(LEFT, buff=3)

        self.play(Write(paragraph))
        self.wait(2)

if __name__ == "__main__":
    runner = video_utils.ManimRunner(
        scenes={
            'England': [
                '-qh',
                '-p'
            ],
            # 'FirstChapterIntro': [
            #     '-sql',
            #     '-p'
            # ],
            # 'FirstChapter': [
            #     '-qh',
            #     '-p'
            # ],
            # 'SecondChapter': [
            #     '-qh',
            #     '-p'
            # ],

        },
        file_path=r'EdScenes.py',  # it's relative to cwd
        project_name='Godofredo'
    )

    runner.run_scenes()
    # runner.concatenate_videos(run_output=True)