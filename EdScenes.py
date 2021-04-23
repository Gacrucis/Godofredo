from enum import Enum
import os
import sys
import math
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

        PREVIOUS_MOBJECTS = self.mobjects

        self.play(
            FadeOutAndShift(paragraph, UP * 2),
            FadeOutAndShift(guillermo_image, UP * 2),
            run_time=2
        )

class XVICentury(GraphScene):

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

        self.graph_origin = (paragraph.get_corner(RIGHT) + RIGHT*frame_width*0.5) / 2
        self.x_axis_width = 5
        self.x_min = -2.5
        self.x_max = 2.5
        self.y_axis_height = 3
        self.y_max = 3
        self.setup_axes()

        def normal_dist(x):

            return  math.exp(-x**2 / 2) / math.sqrt(2 * math.pi)

        graph = self.get_graph(normal_dist, x_min=-2, x_max=2)

        # self.play(Write(paragraph), FadeIn(modelo_image))
        self.play(Write(paragraph), Create(graph))
        self.wait(2)

        self.play(
            FadeOutAndShift(paragraph, UP * 2),
            FadeOutAndShift(graph, UP * 2),
            FadeOutAndShift(self.axes, UP * 2),
        )

class Colombia1500(GraphScene):

    def construct(self):

        frame_height = self.camera.frame_height
        frame_width = self.camera.frame_width
        
        timeline = presets.TimeLine(**configs.timeline_config)
        timeline.next_to(REFERENCE_POINT, DOWN, buff=0)
        timeline.preload_for_scene(
            target_time='Siglo XVI',
            scene=self # pass the scene as parameter
        )

        self.play(timeline.next_time_scroll())

        text = 'La necesidad de usar la estadística en el 1500 surgió con la explotación minera y la necesidad de llevar un control sobre la moneda, el pago de tributos, y la administración de suministros enviados a las tropas.'

        paragraph = presets.text_to_paragraph(text, line_length=30, color=BEIGE)
        paragraph.height = frame_height/4
        paragraph.align_on_border(LEFT, buff=2.5)

        coins_svg = SVGMobject(file_name='./assets/svg/coins')
        coins_svg.width = 5
        coins_svg.next_to(paragraph, RIGHT, buff=0.5)

        pickaxe_svg = SVGMobject(file_name='./assets/svg/pickaxe')
        pickaxe_svg.width = 2
        # pickaxe_svg.set_color(WHITE)
        pickaxe_svg.move_to(coins_svg.get_center_of_mass())
        pickaxe_svg.shift(LEFT*0.4)

        # self.graph_origin = (paragraph.get_corner(RIGHT) + RIGHT*frame_width*0.5) / 2
        # self.x_axis_width = 5
        # self.x_min = -2.5
        # self.x_max = 2.5
        # self.y_axis_height = 3
        # self.y_max = 3
        # self.setup_axes()

        self.play(Write(paragraph), DrawBorderThenFill(coins_svg))
        self.play(DrawBorderThenFill(pickaxe_svg), run_time=2)
        # self.play(Write(paragraph), Create(graph))
        self.wait(2)

        self.play(
            FadeOutAndShift(paragraph, UP * 2),
            FadeOutAndShift(coins_svg, UP * 2),
            FadeOutAndShift(pickaxe_svg, UP * 2),
        )

class Colombia1800(GraphScene):

    def construct(self):

        frame_height = self.camera.frame_height
        frame_width = self.camera.frame_width
        
        timeline = presets.TimeLine(**configs.timeline_config)
        timeline.next_to(REFERENCE_POINT, DOWN, buff=0)
        timeline.preload_for_scene(
            target_time='Siglo XVI',
            scene=self # pass the scene as parameter
        )

        # self.play(timeline.next_time_scroll())

        text_points = [
            'Se hizo obligatorio dar un reporte a la hacienda pública y se estableció la metodología para realizar censos.',
            'Se creó la primer oficina de estadística nacional y se publicó el primer anuario'
        ]

        bullet_list = VGroup()
        for line in text_points:

            bullet_text = presets.text_to_paragraph(line, line_length=20)
            bullet_dot = MathTex(r'\cdot').scale(2)
            bullet_dot.next_to(bullet_text, UL)
            bullet_dot.align_to(point(bullet_text.get_center()),)

            bullet = VGroup(bullet_dot, bullet_text)

            bullet_list.add(bullet)

        bullet_list.arrange(DOWN, buff=0.3)
        



        self.play(Create(bullet_list))

        # self.play(Write(paragraph), DrawBorderThenFill(coins_svg))
        # self.play(DrawBorderThenFill(pickaxe_svg), run_time=2)
        # # self.play(Write(paragraph), Create(graph))
        self.wait(2)

        # self.play(
        #     FadeOutAndShift(paragraph, UP * 2),
        #     FadeOutAndShift(coins_svg, UP * 2),
        #     FadeOutAndShift(pickaxe_svg, UP * 2),
        # )

if __name__ == "__main__":
    runner = video_utils.ManimRunner(
        scenes={
            # 'England': [
            #     '-qh',
            #     # '-p'
            # ],
            # 'XVICentury': [
            #     '-qh',
            #     '-p'
            # ],
            # 'Colombia1500': [
            #     '-qh',
            #     '-p'
            # ],
            'Colombia1800': [
                '-qh',
                '-p'
            ],

        },
        file_path=r'EdScenes.py',  # it's relative to cwd
        project_name='Godofredo'
    )

    runner.run_scenes()
    # runner.concatenate_videos(run_output=True)