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

REFERENCE_POINT = presets.get_coords(-6, 3)


class England(MovingCameraScene):

    def construct(self):

        frame_height = self.camera.frame_height
        frame_width = self.camera.frame_width

        timeline = presets.TimeLine(**configs.timeline_config)
        timeline.next_to(REFERENCE_POINT, DOWN, buff=0)
        timeline.preload_for_scene(
            target_time='594 A.C.',
            scene=self # pass the scene as parameter
        )

        self.play(timeline.next_time_scroll())

        # self.add(timeline)
        
        text = 'Rey Guillermo I encarga censo en el Domesday Book, documento acerca de la propiedad, extensión y valor de las tierras.'

        paragraph = presets.text_to_paragraph(text, line_length=20, color=BEIGE)
        paragraph.height = frame_height/3
        paragraph.align_on_border(LEFT, buff=2.5)

        guillermo_image = ImageMobject(filename_or_array=presets.image_path('guillermo.jpg'))
        guillermo_image.width = frame_width/3.5
        guillermo_image.next_to(paragraph, RIGHT, buff=0.5)

        self.play(Write(paragraph), FadeIn(guillermo_image))
        self.wait(3)

        self.play(
            FadeOutAndShift(paragraph, UP * 2),
            FadeOutAndShift(guillermo_image, UP * 2),
            run_time=2
        )

class XVICentury(MovingCameraScene):

    def construct(self):

        frame_height = self.camera.frame_height
        frame_width = self.camera.frame_width
        
        timeline = presets.TimeLine(**configs.timeline_config)
        timeline.next_to(REFERENCE_POINT, DOWN, buff=0)
        timeline.preload_for_scene(
            target_time='1066',
            scene=self # pass the scene as parameter
        )

        self.play(timeline.next_time_scroll())

        text = 'En este siglo se realizó el primer censo estadístico moderno, gracias al trabajo de John Graunt en la inferencia y teoría estadística, se pudo predecir la cantidad de personas que morirían por diversas enfermedades, se realizó la primera tabla de probabilidades por género y edades.'

        paragraph = presets.text_to_paragraph(text, line_length=30, color=BEIGE)
        paragraph.height = frame_height/3
        paragraph.align_on_border(LEFT, buff=2.5)

        modelo_image = ImageMobject(filename_or_array=presets.image_path('modelo.jpg'))
        modelo_image.width = frame_width/3.5
        modelo_image.next_to(paragraph, RIGHT, buff=0.5)

        self.play(Write(paragraph), FadeIn(modelo_image))
        self.wait(2)

        self.play(
            FadeOutAndShift(paragraph, UP * 2),
            FadeOutAndShift(modelo_image, UP * 2),
        )

if __name__ == "__main__":
    runner = video_utils.ManimRunner(
        scenes={
            'England': [
                '-qh',
                # '-p'
            ],
            'XVICentury': [
                '-qh',
                # '-p'
            ],
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
    runner.concatenate_videos(run_output=True)