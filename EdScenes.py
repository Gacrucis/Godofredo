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

UP_SCREEN = UP * 10
DOWN_SCREEN = DOWN * 10

REFERENCE_POINT = presets.get_coords(-6, 1)


class England(MovingCameraScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.timeline = presets.TimeLine(**configs.timeline_config)
        self.timeline.next_to(REFERENCE_POINT, DOWN, buff=0)
        self.timeline.preload_for_scene(
            target_time='Imperio Romano',
            scene=self # pass the scene as parameter
        )

        current_time = self.timeline.get_current_time()

        self.wait() # this fix bug of miss position text due to updaters

        title_config = {
            "stroke_width": 1,
            "background_stroke_width": 3,
            "background_stroke_color": BLACK,
            'color': PURPLE
        }
        paragraph_config = {
            "stroke_width": 1,
            "background_stroke_width": 3,
            "background_stroke_color": BLACK,
            "line_length": 35,
            "interline_scape": 0.3,
            "color": BEIGE

        }
        self.previous = {
            "image": ImageMobject(filename_or_array=presets.image_path('.\\history\\13_romans_2.jpg')),
            "title": Tex(
                "Imperio romano",
                **title_config
            ),
            "list": BulletedList(
                "Realizaban censos cada 5 años",
                "sus funcionarios recopilaban los datos \\\\sobre nacimiento, defunciones y \\\\matrimonios",
                "Recuentos de ganado, terreno y \\\\riquezas obtenidas en las tierras \\\\conquistadas",
                dot_scale_factor=2,
                **paragraph_config
            )
        }

        for line in self.previous["list"]:
            line[0].set_color(SKY_BLUE).scale(1.05)



        self.previous["list"].scale(0.6).next_to(current_time, RIGHT).align_on_border(
            RIGHT, 1).shift(DOWN * 0.5)
        self.previous["image"].scale(0.9).next_to(
            self.previous["list"], LEFT, buff=0.4)
        self.previous["title"].scale(0.5).next_to(self.previous["image"], UP, buff=0.3)

        self.add(*self.previous.values())

    def construct(self):

        frame_height = self.camera.frame_height
        frame_width = self.camera.frame_width

        self.play(
            self.timeline.next_time_scroll(),
            # fade out previous mobs
            FadeOutAndShift(
                self.previous["image"],
                UP_SCREEN
            ),
            FadeOutAndShift(
                VGroup(
                    self.previous["title"],
                    self.previous["list"]
                ),
                UP_SCREEN
            ),
            run_time=3
        )

        # self.add(timeline)
        
        text = 'Rey Guillermo I encarga censo en el Domesday Book, documento acerca de la propiedad, extensión y valor de las tierras.'

        paragraph = presets.text_to_paragraph(text, line_length=20, color=BEIGE)
        paragraph.height = frame_height/3
        paragraph.align_on_border(LEFT, buff=3)

        guillermo_image = ImageMobject(filename_or_array=presets.image_path('guillermo.jpg'))
        guillermo_image.width = frame_width/3.5
        guillermo_image.next_to(paragraph, RIGHT, buff=0.5)

        self.play(Write(paragraph), FadeIn(guillermo_image))
        self.wait(3)

        PREVIOUS_MOBJECTS = self.mobjects

        self.play(
            FadeOutAndShift(paragraph, UP_SCREEN),
            FadeOutAndShift(guillermo_image, UP_SCREEN),
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
        paragraph.align_on_border(LEFT, buff=3)

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
            FadeOutAndShift(paragraph, UP_SCREEN),
            FadeOutAndShift(graph, UP_SCREEN),
            FadeOutAndShift(self.axes, UP_SCREEN),
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

        # self.play(timeline.next_time_scroll())

        text = 'La necesidad de usar la estadística en el 1500 surgió con la explotación minera y la necesidad de llevar un control sobre la moneda, el pago de tributos, y la administración de suministros enviados a las tropas.'

        paragraph = presets.text_to_paragraph(text, line_length=30, color=BEIGE)
        paragraph.height = frame_height/4
        paragraph.align_on_border(LEFT, buff=3)

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
            FadeOutAndShift(paragraph, UP_SCREEN),
            FadeOutAndShift(coins_svg, UP_SCREEN),
            FadeOutAndShift(pickaxe_svg, UP_SCREEN),
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

        self.play(timeline.next_time_scroll())

        line_alignment = 'left'
        line_length = 35
        paragraph_width = frame_width/2.4

        text_points = [
            'Se hizo obligatorio dar un reporte a la hacienda pública y se estableció la metodología para realizar censos.',
            'Se creó la primer oficina de estadística nacional y se publicó el primer anuario'
        ]

        joined_text = '\n'.join(text_points)

        bullet_points = VGroup()

        for line in text_points:
            paragraph = presets.PTex(
            text=line,
            alignment=line_alignment,
            line_length=line_length,
            interline_space=0.2,
            **configs.text_config
            )          

            bullet_dot = MathTex(r'\cdot').scale(2)
            bullet_dot.next_to(paragraph.submobjects[0], LEFT, buff=0.3)

            bullet_points.add(VGroup(bullet_dot, paragraph))
        
        bullet_points.width = paragraph_width

        bullet_points.arrange(DOWN, buff=0.5)
        
        for prev_index, current in enumerate(bullet_points[1:]):

            current.align_to(bullet_points[prev_index], LEFT, LEFT)
        
        bullet_points.align_on_border(LEFT, buff=3)
        remaining_space = (Point().align_on_border(RIGHT, buff=0).get_center()) - (bullet_points.get_corner(RIGHT))
        # remaining_midpoint = (Point().align_on_border(RIGHT, buff=0).get_center()) + (bullet_points.get_corner(RIGHT))/2

        # Imagen

        stats_image = ImageMobject(filename_or_array=presets.image_path('dane.png'))
        stats_image.scale_to_fit_width(remaining_space - 1.5)
        stats_image.stretch_to_fit_height(5)

        stats_image.next_to(bullet_points, RIGHT, buff=1)
        

        self.play(Write(bullet_points), FadeIn(stats_image), run_time=3)

        # self.play(Write(paragraph), DrawBorderThenFill(coins_svg))
        # self.play(DrawBorderThenFill(pickaxe_svg), run_time=2)
        # # self.play(Write(paragraph), Create(graph))
        self.wait(2)

        self.play(
            FadeOutAndShift(bullet_points, UP_SCREEN),
            FadeOutAndShift(stats_image, UP_SCREEN),
            # FadeOutAndShift(pickaxe_svg, UP_SCREEN),
        )

class XXCentury(GraphScene):

    def construct(self):

        frame_height = self.camera.frame_height
        frame_width = self.camera.frame_width
        
        line_alignment = 'left'
        line_length = 40
        paragraph_width = frame_width/2.2

        timeline = presets.TimeLine(**configs.timeline_config)
        timeline.next_to(REFERENCE_POINT, DOWN, buff=0)
        timeline.preload_for_scene(
            target_time='1800',
            scene=self # pass the scene as parameter
        )

        self.play(timeline.next_time_scroll())

        texts = [
            'Estadística y probabilidad van de la mano, Bernoulli, Maseres, Lagrange y Laplace desarrollaron la teoría de probabilidades',
            'Fisher y Pearson contribuyen a la estadística como disciplina científica, elaboran herramientas para la planeación y análisis de experimentos (varianza y análisis multivariante)',
            'Crece la estadística descriptiva en lo social y económico',
            'Actualmente la estadística es un método interdisciplinar que permite describir con la mayor exactitud datos de diferentes campos: político, social, psicológico, biológico y físico. Es importante la interpretación de los datos tomados',
        ]

        images = [
            'laplace.jpg',
            'fisher.jpg',
            'pearson.jpg',
            'stats_modern.svg'
        ]

        image_scales = [
            1,
            0.35,
            0.6,
            1
        ]

        for i, text in enumerate(texts):
            paragraph = presets.PTex(
            text=text,
            alignment=line_alignment,
            line_length=line_length,
            interline_space=0.1,
            **configs.text_config
            )

            paragraph.width = paragraph_width          
            paragraph.align_on_border(LEFT, buff=3)

            remaining_space = (Point().align_on_border(RIGHT, buff=0).get_center()) - (paragraph.get_corner(RIGHT))

            # Imagen

            if i < 3:
                stats_image = ImageMobject(filename_or_array=presets.image_path(images[i]))
                # stats_image.scale_to_fit_width(remaining_space - 1)
                # stats_image.height = 5
            
            else:
                stats_image = SVGMobject(file_name=os.path.join('assets', 'svg', images[i]))
                stats_image.set_color(WHITE)
                # stats_image.scale_to_fit_width(remaining_space - 1)

            stats_image.scale(image_scales[i])
            stats_image.next_to(paragraph, RIGHT, buff=0.7)

            if i < 3:
                self.play(Write(paragraph), FadeIn(stats_image), run_time=3)
            
            else:
                self.play(Write(paragraph), DrawBorderThenFill(stats_image), run_time=3)

            self.wait(2)

            self.play(
                Uncreate(paragraph),
                FadeOut(stats_image),
                # FadeOutAndShift(pickaxe_svg, UP_SCREEN),
            )

            self.wait()

        # self.play(
        #     FadeOutAndShift(paragraph, UP),
        #     FadeOutAndShift(stats_image, UP),
        #     # FadeOutAndShift(pickaxe_svg, UP_SCREEN),
        # )

class Colombia1900(GraphScene):

    def construct(self):

        frame_height = self.camera.frame_height
        frame_width = self.camera.frame_width
        
        timeline = presets.TimeLine(**configs.timeline_config)
        timeline.next_to(REFERENCE_POINT, DOWN, buff=0)
        timeline.preload_for_scene(
            target_time='Siglo XX',
            scene=self # pass the scene as parameter
        )

        # self.play(timeline.next_time_scroll())

        line_alignment = 'left'
        line_length = 40
        paragraph_width = frame_width/2.2

        text_points = [
            'El BR genera promedios de precios de productos alimenticios',
            'Se mide el costo de vida en las ciudades a través de encuestas',
            'Se crea el departamento nacional de estadística (DANE) y se ofrece la información al público',
            'Se realizó el primer censo nacional agropecuario',
            'Se realizó el censo de industria, comercio y servicios',
            'Se implementa la encuesta nacional de hogares, la de ingresos y gastos, y la de calidad de vida',
        ]

        bullet_points = VGroup()

        for line in text_points:
            paragraph = presets.PTex(
            text=line,
            alignment=line_alignment,
            line_length=line_length,
            interline_space=0.1,
            **configs.text_config
            )          

            bullet_dot = MathTex(r'\cdot').scale(2)
            bullet_dot.next_to(paragraph.submobjects[0], LEFT, buff=0.3)

            bullet_points.add(VGroup(bullet_dot, paragraph))
        
        bullet_points.width = paragraph_width

        bullet_points.arrange(DOWN, buff=0.5)
        
        for prev_index, current in enumerate(bullet_points[1:]):

            current.align_to(bullet_points[prev_index], LEFT, LEFT)
        
        bullet_points.align_on_border(LEFT, buff=3)
        # bullet_points.shift(DOWN)
        remaining_space = (Point().align_on_border(RIGHT, buff=0).get_center()) - (bullet_points.get_corner(RIGHT))
        # remaining_midpoint = (Point().align_on_border(RIGHT, buff=0).get_center()) + (bullet_points.get_corner(RIGHT))/2

        # Imagen

        stats_image = ImageMobject(filename_or_array=presets.image_path('danelogo.png'))
        stats_image.scale(0.6)
        # stats_image.scale_to_fit_width(remaining_space - 1)
        # stats_image.heigh = frame

        stats_image.next_to(bullet_points, RIGHT, buff=0.7)
        

        self.play(Write(bullet_points), FadeIn(stats_image), run_time=3)

        # self.play(Write(paragraph), DrawBorderThenFill(coins_svg))
        # self.play(DrawBorderThenFill(pickaxe_svg), run_time=2)
        # # self.play(Write(paragraph), Create(graph))
        self.wait(2)

        self.play(
            FadeOutAndShift(bullet_points, UP_SCREEN),
            FadeOutAndShift(stats_image, UP_SCREEN),
            # FadeOutAndShift(pickaxe_svg, UP_SCREEN),
        )

class Colombia2000(GraphScene):

    def construct(self):

        frame_height = self.camera.frame_height
        frame_width = self.camera.frame_width
        
        line_alignment = 'left'
        line_length = 40
        paragraph_width = frame_width/2.2

        timeline = presets.TimeLine(**configs.timeline_config)
        timeline.next_to(REFERENCE_POINT, DOWN, buff=0)
        timeline.preload_for_scene(
            target_time='Siglo XX',
            scene=self # pass the scene as parameter
        )

        self.play(timeline.next_time_scroll())

        text_points = [
            'Se realiza un censo general de población',
            'El DANE registra los damnificados de la ola invernal 2010-2011 y esto ayudó a orientar proyectos para soportar a dicha población',
            'Se aplicó la encuesta de convivencia y seguridad ciudadana',
            'El DANE oficialmente mide la pobreza monetaria y multidimensional (2011)',
        ]

        bullet_points = VGroup()

        for line in text_points:
            paragraph = presets.PTex(
            text=line,
            alignment=line_alignment,
            line_length=line_length,
            interline_space=0.1,
            **configs.text_config
            )          

            bullet_dot = MathTex(r'\cdot').scale(2)
            bullet_dot.next_to(paragraph.submobjects[0], LEFT, buff=0.3)

            bullet_points.add(VGroup(bullet_dot, paragraph))
        
        bullet_points.width = paragraph_width

        bullet_points.arrange(DOWN, buff=0.5)
        
        for prev_index, current in enumerate(bullet_points[1:]):

            current.align_to(bullet_points[prev_index], LEFT, LEFT)
        
        bullet_points.align_on_border(LEFT, buff=3)
        # bullet_points.shift(DOWN)
        remaining_space = (Point().align_on_border(RIGHT, buff=0).get_center()) - (bullet_points.get_corner(RIGHT))
        # remaining_midpoint = (Point().align_on_border(RIGHT, buff=0).get_center()) + (bullet_points.get_corner(RIGHT))/2

        # Imagen

        stats_image = ImageMobject(filename_or_array=presets.image_path('censo.jpg'))
        stats_image.scale(0.6)
        # stats_image.scale_to_fit_width(remaining_space - 1)
        # stats_image.heigh = frame

        stats_image.next_to(bullet_points, RIGHT, buff=0.7)
        

        self.play(Write(bullet_points), FadeIn(stats_image), run_time=3)

        # self.play(Write(paragraph), DrawBorderThenFill(coins_svg))
        # self.play(DrawBorderThenFill(pickaxe_svg), run_time=2)
        # # self.play(Write(paragraph), Create(graph))
        self.wait(2)

        self.play(
            FadeOutAndShift(bullet_points, UP_SCREEN),
            FadeOutAndShift(stats_image, UP_SCREEN),
            # FadeOutAndShift(pickaxe_svg, UP_SCREEN),
        )

class Colombia2020(GraphScene):

    def construct(self):

        frame_height = self.camera.frame_height
        frame_width = self.camera.frame_width
        
        line_alignment = 'left'
        line_length = 40
        paragraph_width = frame_width/2.2

        timeline = presets.TimeLine(**configs.timeline_config)
        timeline.next_to(REFERENCE_POINT, DOWN, buff=0)
        timeline.preload_for_scene(
            target_time='2000',
            scene=self # pass the scene as parameter
        )

        self.play(timeline.next_time_scroll())

        text = 'Se desarrollaron indicadores de bienestar subjetivo y sentimientos socioeconómicos sobre las percepciones de hogares y empresas con el fin de medir el impacto del COVID-19'

        paragraph = presets.PTex(
        text=text,
        alignment=line_alignment,
        line_length=line_length,
        interline_space=0.1,
        **configs.text_config
        )

        paragraph.width = paragraph_width
        paragraph.align_on_border(LEFT, buff=2.5)

        remaining_space = (Point().align_on_border(RIGHT, buff=0).get_center()) - (paragraph.get_corner(RIGHT))

        # Imagen

        stats_image = ImageMobject(filename_or_array=presets.image_path('danecovid.jpg'))
        stats_image.scale(0.5)
        # stats_image.scale_to_fit_width(remaining_space - 1)
        # stats_image.heigh = frame

        stats_image.next_to(paragraph, RIGHT, buff=0.7)
        

        self.play(Write(paragraph), FadeIn(stats_image), run_time=3)

        # self.play(Write(paragraph), DrawBorderThenFill(coins_svg))
        # self.play(DrawBorderThenFill(pickaxe_svg), run_time=2)
        # # self.play(Write(paragraph), Create(graph))
        self.wait(2)

        self.play(
            FadeOutAndShift(paragraph, UP_SCREEN),
            FadeOutAndShift(stats_image, UP_SCREEN),
        )

        self.wait(2)

if __name__ == "__main__":
    runner = video_utils.ManimRunner(
        scenes={
            'England': [
                '-ql',
                '-p'
            ],
            # 'XVICentury': [
            #     '-qh',
            #     # '-p'
            # ],
            # 'Colombia1500': [
            #     '-qh',
            #     # '-p'
            # ],
            # 'Colombia1800': [
            #     '-qh',
            #     # '-p'
            # ],
            # 'XXCentury': [
            #     '-qh',
            #     # '-p'
            # ],
            # 'Colombia1900': [
            #     '-qh',
            #     # '-p'
            # ],
            # 'Colombia2000': [
            #     '-qh',
            #     # '-p'
            # ],
            # 'Colombia2020': [
            #     '-qh',
            #     '-p'
            # ],

        },
        file_path=r'EdScenes.py',  # it's relative to cwd
        project_name='Godofredo'
    )

    runner.run_scenes()
    # runner.concatenate_videos(run_output=True)