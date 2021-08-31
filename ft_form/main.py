import itertools as it

from manim import *

import sys
import os

from custom import Clock, ClockPassesTime

# add Godofredo/utils to path
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(ROOT_PATH, os.pardir)))

from utils import video_utils, presets


UIS_GREEN = "#67b93e"
SKY_BLUE = "#98D2EB"
FAWN = "#E5A361"
LIGHT_PURPLE = "#B2B1CF"
DARK_PURPLE = "#412234"
COFFEE = "#735A45"
EGGPLANT = "#6C464F"
# TERRA_COOTA = "#E26D5C"
# BLUE_CORNFLOWER = "#7F96FF"
# LIGHT_BLUE = "#A6CFD5"
# LIGHT_CYAN = "#DBFCFF"
PALETTE = [FAWN, SKY_BLUE, LIGHT_PURPLE, DARK_PURPLE, COFFEE]


class Intro(MovingCameraScene):
    def end_with_fadeout(func):
        def wrapper(self, run_time=1.5, *args, **kwargs):
            func(self, *args, **kwargs)

            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=run_time)
            self.wait()

        return wrapper

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uis_logo = SVGMobject(file_name=f"{ROOT_PATH}/assets/svg/UIS.svg").scale(
            1.2
        )

        self.uis_logo[1].set_fill(color=WHITE, opacity=0.9)
        self.uis_logo[5:].set_fill(color=WHITE, opacity=0.9)

        self.names_config = {
            "stroke_width": 1,
            "background_stroke_width": 5,
            "background_stroke_color": BLACK,
            "sheen_factor": 0,
            "sheen_direction": UR,
        }

    @end_with_fadeout
    def construct(self):
        title = Tex("Encuesta sobre Aulas Virtuales")
        title.scale(1.5)
        title.align_on_border(UP, buff=2)

        subtitle = Tex("Un estudio de las aulas virtuales pre y post pandémico")
        subtitle.scale(0.8)
        subtitle.next_to(title, DOWN, buff=0.35)
        subtitle.set_color(LIGHT_PURPLE)
        # subtitle.set_color(LIGHT_BLUE)

        author_scale = 0.7
        author_colors = it.cycle([DARK_PURPLE, SKY_BLUE, LIGHT_PURPLE, FAWN, COFFEE])
        # author_colors = it.cycle(
        # [TERRA_COOTA, EGGPLANT, BLUE_CORNFLOWER, LIGHT_BLUE, LIGHT_CYAN]
        # )

        by = Tex("By:")

        authors = VGroup(
            MathTex(r"\varepsilon \text{ José Silva - 2183075}", **self.names_config),
            MathTex(r"\gamma \text{ Edward Parada - 2182070}", **self.names_config),
            MathTex(r"\Omega \text{ Gian Estevez - 2183074}", **self.names_config),
            MathTex(r"\mu \text{ Yuri Garcia - 2182697}", **self.names_config),
        ).scale(author_scale)

        base_author = authors[0]
        current_color = next(author_colors)
        base_author.set_color(current_color)  # type: ignore

        base_author.next_to(subtitle, DOWN, buff=1)
        base_author.align_on_border(LEFT, buff=2)

        authors.arrange_submobjects(DOWN, buff=0.2, center=False)

        author_anims = []

        for author in authors:
            current_color = next(author_colors)

            if author is not base_author:
                author.align_to(base_author, LEFT)

            author.set_color(current_color)  # type: ignore
            author_anims.append(Write(author))  # type: ignore

        by.scale(author_scale)
        by.next_to(base_author, LEFT, buff=0.15)

        lc_title_1 = Tex("“Los datos! ¡Los datos! Los datos! “, gritó con ")

        lc_title_2 = Tex("impaciencia. “No puedo hacer ladrillos sin arcilla!”")

        lc_title_1.match_height(base_author)
        lc_title_2.match_height(base_author)

        lc_title_1.next_to(subtitle, DOWN, buff=1)
        lc_title_1.shift(RIGHT * 3)

        lc_title_2.next_to(lc_title_1, DOWN, buff=0.1)
        lc_title_2.align_to(lc_title_1, LEFT)

        lc_title = VGroup(lc_title_1, lc_title_2)
        lc_title.set_color(LIGHT_GRAY)

        subtitle_auth = Tex("- Sherlock Holmes")
        subtitle_auth.set_color(EGGPLANT)
        # subtitle_auth.set_color(TERRA_COOTA)
        subtitle_auth.height = 0.235
        subtitle_auth.next_to(lc_title, DOWN, buff=0.2)
        subtitle_auth.align_on_border(RIGHT, buff=1)

        # animations
        self.play(Write(self.uis_logo), run_time=3)
        self.wait(1.5)

        self.play(FadeOut(self.uis_logo), run_time=1.5)

        self.play(Write(title))
        self.play(Write(subtitle))

        self.play(Write(by))
        self.play(AnimationGroup(*author_anims, lag_ratio=0.2), run_time=3)

        self.wait(0.8)

        anim_group = AnimationGroup(
            Write(lc_title), Write(subtitle_auth), lag_ratio=0.2
        )

        self.play(anim_group, run_time=2.5)

        self.wait(3)

        # lc_title.anim

        # self.play(
        #     FadeOut(presets.get_vmobjects_from_scene(self)),
        #     FadeOut(VGroup(authors, lc_title, subtitle_auth)),
        # )

        self.wait()


class DataAndSubjectOfStudyIntro(MovingCameraScene):
    def construct(self):
        chapter = presets.create_chapter(
            title="Introducción",
            subtitle="¿Qué datos se recolectarón y de quienes se obtuvieron?",
            scale_factor=0.9,
            color=FAWN,
        )

        animations = chapter[0]

        for animation in animations:
            self.play(animation)

        self.wait()


class DataAndSubjectOfStudy(Intro):
    def end_with_fadeout(func):
        def wrapper(self, run_time=1.5, *args, **kwargs):
            # run scene
            func(self, *args, **kwargs)

            # at the end applies a fade out

            # allow defining self.mob_ignore to avoid fading out specific mobs
            if hasattr(self, "ignore_mobs") and isinstance(self.ignore_mobs, list):
                self.play(
                    *[
                        FadeOut(mob)
                        for mob in self.mobjects
                        if not mob in self.ignore_mobs
                    ],
                    run_time=run_time,
                )
            else:
                self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=run_time)

            self.wait()

        return wrapper

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = {
            "text": {"stroke_width": 1, "height": 0.25},
            "vtext": {"stroke_width": 1},
            "varrows": {
                "color": LIGHT_PURPLE,
                "stroke_width": 4,
                "tip_length": 0.2,
                "max_tip_length_to_length_ratio": 0.4,
                "max_stroke_width_to_length_ratio": 10,
            },
            "clock": {
                "circle": {
                    "color": WHITE,
                    "stroke_color": DARK_GRAY,
                    "fill_opacity": 1,
                    "stroke_width": 5,
                },
                "hands": {"color": DARK_BLUE},
                "ticks": {"color": DARK_GRAY, "stroke_width": 5},
            },
        }

    def construct(self):
        self.title = Title("Recolección de datos").to_edge(edge=UP, buff=1)
        self.play(Write(self.title), run_time=1.5)
        self.scene_population()
        self.scene_variables()

    @end_with_fadeout
    def scene_population(self):
        text = (
            VGroup(
                Tex("Población: ", "estudiantes de la UIS", **self.config["text"]),
                Tex("Muestra: ", "45 estudiantes", **self.config["text"]),
                Tex(
                    "Tiempo de recolección: ",
                    "una semana aproximadamente",
                    **self.config["text"],
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            .to_edge(edge=LEFT, buff=2)
            .shift(UP)
        )

        text[0][0].set_color(PALETTE[1])
        text[1][0].set_color(PALETTE[0])
        text[2][0].set_color(PALETTE[2])

        self.uis_logo.scale(0.8).shift(DOWN)

        population = SVGMobject(
            file_name=f"{ROOT_PATH}/assets/svg/crowd.svg",
            stroke_color=BLACK,
            color=WHITE,
        ).scale(1.1)

        clock = Clock(
            circle_config=self.config["clock"]["circle"],
            hands_config=self.config["clock"]["hands"],
            ticks_config=self.config["clock"]["ticks"],
        ).scale(0.5)

        self.play(
            AnimationGroup(Wait(1), Write(text[0]), lag_ratio=1),
            FadeIn(self.uis_logo, shift=UP),
            run_time=2,
        )
        self.wait()

        self.play(self.uis_logo.animate.to_edge(DOWN, buff=1.2), run_time=0.5)
        population.to_edge(DOWN, buff=0.9)
        self.play(
            DrawBorderThenFill(population),
            AnimationGroup(Wait(1), Write(text[1]), lag_ratio=1),
            run_time=1.5,
        )
        self.wait()

        clock.next_to(self.uis_logo, direction=UR, buff=0).shift((DOWN + LEFT) * 0.5)

        self.play(GrowFromCenter(clock), run_time=0.8)
        self.play(
            ClockPassesTime(clock, hours_passed=1),
            AnimationGroup(Wait(1), Write(text[2]), lag_ratio=1),
            run_time=1.5,
        )

        self.wait()

        self.ignore_mobs = [self.title]

    @end_with_fadeout
    def scene_variables(self):
        text = VGroup(
            Tex("Variables", **self.config["vtext"]),
            Tex("Cualitativas", **self.config["vtext"]),
            Tex("Cuantitativas", **self.config["vtext"]),
            Tex("Facultad", **self.config["vtext"]),
            Tex("Dispositivo", **self.config["vtext"]),
            Tex("Semestre", **self.config["vtext"]),
            Tex("Indicador \\\\ de Uso \\\\ (IU)", **self.config["vtext"]),
            Tex("Cantidad \\\\ Aulas \\\\ Virtuales", **self.config["vtext"]),
            Tex("nominal", **self.config["vtext"]),
            Tex("nominal", **self.config["vtext"]),
            Tex("ordinal", **self.config["vtext"]),
            Tex("continua", **self.config["vtext"]),
            Tex("discreta", **self.config["vtext"]),
        ).scale(0.6)

        LVL_BUFF = 1

        self.play(Create(text[0]), run_time=1.2)
        self.play(text[0].animate.shift(UP * 1.2).set_color(FAWN).scale(1.1))

        # align text in hiearchy-like
        text[1:3].arrange(RIGHT, buff=4).next_to(text[0], DOWN, buff=LVL_BUFF)
        text[3:6].arrange(RIGHT, buff=0.4).next_to(text[1], direction=DOWN, buff=1)
        text[6:8].arrange(RIGHT, buff=0.4, aligned_edge=UP).next_to(
            text[2], direction=DOWN, buff=LVL_BUFF
        )

        text[8].next_to(text[3], direction=DOWN, buff=LVL_BUFF)
        text[9].next_to(text[4], direction=DOWN, buff=LVL_BUFF)
        text[10].next_to(text[5], direction=DOWN, buff=LVL_BUFF)

        text[11].next_to(text[6], direction=DOWN, buff=LVL_BUFF)
        text[12].next_to(text[7], direction=DOWN, buff=LVL_BUFF)

        arrows = VGroup(
            Arrow(
                start=text[0].get_bottom(),
                end=text[1].get_top(),
                **self.config["varrows"],
            ),
            Arrow(
                start=text[1].get_bottom(),
                end=text[3].get_top(),
                **self.config["varrows"],
            ),
            Arrow(
                start=text[3].get_bottom(),
                end=text[8].get_top(),
                **self.config["varrows"],
            ),
            Arrow(
                start=text[1].get_bottom(),
                end=text[4].get_top(),
                **self.config["varrows"],
            ),
            Arrow(
                start=text[4].get_bottom(),
                end=text[9].get_top(),
                **self.config["varrows"],
            ),
            Arrow(
                start=text[1].get_bottom(),
                end=text[5].get_top(),
                **self.config["varrows"],
            ),
            Arrow(
                start=text[5].get_bottom(),
                end=text[10].get_top(),
                **self.config["varrows"],
            ),
            Arrow(
                start=text[0].get_bottom(),
                end=text[2].get_top(),
                **self.config["varrows"],
            ),
            Arrow(
                start=text[2].get_bottom(),
                end=text[6].get_top(),
                **self.config["varrows"],
            ),
            Arrow(
                start=text[6].get_bottom(),
                end=text[11].get_top(),
                **self.config["varrows"],
            ),
            Arrow(
                start=text[2].get_bottom(),
                end=text[7].get_top(),
                **self.config["varrows"],
            ),
            Arrow(
                start=text[7].get_bottom(),
                end=text[-1].get_top(),
                **self.config["varrows"],
            ),
        )

        # ordered indices of text so they are showed properly in hiearchy
        order = (1, 3, 8, 4, 9, 5, 10, 2, 6, 11, 7, -1)

        for i, index in enumerate(order):
            self.show_hierarchy(text[index], arrows[i])
            self.wait()

        # self.add(text, arrows)
        self.wait()

    def show_hierarchy(self, text: Tex, arrow: Arrow) -> None:
        self.play(
            AnimationGroup(Wait(0.8), FadeIn(text), lag_ratio=1),
            GrowArrow(arrow),
            run_time=1.5,
        )


class DataTreatmentIntro(MovingCameraScene):
    def construct(self):
        chapter = presets.create_chapter(
            title="Tratamiento de datos",
            subtitle="O como conseguir información a partir de los datos",
            scale_factor=0.9,
            color=PURPLE,
        )

        animations = chapter[0]

        for animation in animations:
            self.play(animation)

        self.wait()


class DataTreatment(MovingCameraScene):
    def construct(self):
        self.play(Write(Text("Tratamiento de datos. Yeah.")))
        self.wait()


class ConclusionsIntro(MovingCameraScene):
    def construct(self):
        chapter = presets.create_chapter(
            title="Resultados y Conclusiones",
            subtitle="Análisis más relevante de lo obtenido con el estudio",
            scale_factor=0.9,
            color=FAWN,
        )

        animations = chapter[0]

        for animation in animations:
            self.play(animation)

        self.wait()


class Conclusions(MovingCameraScene):
    def end_with_fadeout(func):
        def wrapper(self, run_time=1.5, *args, **kwargs):
            # run scene
            func(self, *args, **kwargs)

            # at the end applies a fade out

            # allow defining self.mob_ignore to avoid fading out specific mobs
            if hasattr(self, "ignore_mobs") and isinstance(self.ignore_mobs, list):
                anims = [
                    FadeOut(mob) for mob in self.mobjects if not mob in self.ignore_mobs
                ]
            else:
                anims = [FadeOut(mob) for mob in self.mobjects]

            if anims:
                self.play(*anims, run_time=run_time)

            self.wait()

        return wrapper

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # stem and leaf
        self.config = {
            "stem_and_leaf": {"bar": {"stroke_width": 1, "color": LIGHT_PURPLE}},
            "title": {"stroke_width": 1.5},
        }

    def construct(self):
        self.title = Tex("Diagrama de Puntos", **self.config["title"])
        self.play(Write(self.title))
        self.play(self.title.animate.to_edge(UP, buff=0.7), run_time=0.8)
        self.wait()

        self.scene_dot_plot()
        self.scene_stem_and_leaf()
        self.scene_bar_plot()
        self.scene_histogram()
        self.scene_time_series()
        self.scene_box_plot()

    @end_with_fadeout
    def scene_dot_plot(self):
        diagram = (
            ImageMobject(filename_or_array=f"{ROOT_PATH}/assets/images/dot-plot.png")
            .scale_to_fit_width(8.5)
            .shift(DOWN * 0.3)
        )

        self.play(FadeIn(diagram, shift=UP), run_time=2)

        self.wait(3)

        self.ignore_mobs = [self.title]

    @end_with_fadeout
    def scene_stem_and_leaf(self):
        data = {
            "0": ["7"],
            "2": ["1"],
            "3": ["8"],
            "4": ["0", "8"],
            "5": ["2", "4", "8"],
            "6": ["3", "4", "6", "8"],
            "7": ["2", "8"],
            "8": ["6", "7"],
            "9": ["0", "3", "3", "3", "6", "6", "6", "9"],
            "10": ["2", "2", "2", "4", "4", "8", "8"],
            "11": ["6", "6", "6"],
            "12": ["0", "4"],
            "13": ["2", "6"],
            "14": ["0", "0"],
            "15": ["2", "2"],
            "16": ["4", "4"],
            "18": ["4"],
        }
        TEXT_SCALE = 0.7
        SL_TEXT_SCALE = 0.4

        stems = (
            VGroup(*[Tex(stem).scale(SL_TEXT_SCALE) for stem in data.keys()])
            .arrange_in_grid(cols=1, buff=0.15)
            .shift(RIGHT * 1.5 + DOWN * 0.3)
        )

        leaves = []
        for stem, data_leaves in zip(stems, data.values()):
            vleaves = (
                VGroup(*[Tex(leaf) for leaf in data_leaves])
                .arrange_in_grid(rows=1, buff=0.5)
                .scale(SL_TEXT_SCALE)
            )
            vleaves.next_to(stem, direction=RIGHT, buff=0.75)

            if leaves:
                vleaves.align_to(leaves[0], direction=LEFT)

            leaves.append(vleaves)

        stems_bar = Line(
            start=stems.get_top(),
            end=stems.get_bottom(),
            **self.config["stem_and_leaf"]["bar"],
        ).next_to(stems, direction=RIGHT, buff=0.25)

        text = VGroup(
            Tex(
                "El ",
                "tallo ",
                "consta de todos los dígitos \\\\",
                "del número excepto el último el \\\\",
                "cual es la ",
                "hoja",
                ".",
            ).set_color_by_tex_to_color_map({"tallo": EGGPLANT, "hoja": EGGPLANT}),
            Tex(
                "Los valores del ",
                "indicador de uso \\\\",
                "presentan una tendencia central, \\\\",
                "esto significa que los estudiantes \\\\",
                "usan “medianamente” las aulas \\\\",
                "virtuales.",
            ).set_color_by_tex("indicador de uso", EGGPLANT),
        ).scale(TEXT_SCALE)

        # align syntethic paragraph
        VGroup(text[0][:3], text[0][3], text[0][4:]).arrange(DOWN, aligned_edge=LEFT)
        VGroup(text[1][:2], *text[1][2:]).arrange(DOWN, aligned_edge=LEFT)

        text.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=1).shift(
            LEFT * 3 + DOWN * 0.3
        )

        self.play(
            Transform(
                self.title,
                Tex("Diagrama de Tallo y Hoja", **self.config["title"]).move_to(
                    self.title
                ),
            ),
            run_time=1.2,
        )
        self.wait()

        # show from top to bottom the stems with a lag ratio of 0.1
        anims = [
            AnimationGroup(Wait(0.1 * i), GrowFromCenter(stem), lag_ratio=1)
            for i, stem in enumerate(stems)
        ]

        self.play(
            *anims,
            AnimationGroup(Wait(1.5), Write(text[0]), lag_ratio=1),
            run_time=2,
        )
        self.play(
            *[
                AnimationGroup(Wait(0.6), FadeIn(vleaves), lag_ratio=1)
                for vleaves in leaves
            ],
            GrowFromEdge(stems_bar, edge=UP),
            run_time=1.5,
        )
        self.play(Write(text[1]), run_time=2)
        anims = [
            Indicate(mob, color=FAWN, scale_value=1.1)
            for mob in [stems[8], stems[9], *leaves[8], *leaves[9]]
        ]
        self.play(*anims, run_time=2)
        self.wait(3)

        self.ignore_mobs = [self.title]

    @end_with_fadeout
    def scene_bar_plot(self):
        plot = (
            ImageMobject(filename_or_array=f"{ROOT_PATH}/assets/images/bar-plot.png")
            .scale_to_fit_width(7)
            .to_edge(LEFT, buff=0.7)
        )
        TEXT_SCALE = 0.5

        text = VGroup(
            Tex(
                "Los valores utilizados fueron el ",
                "semestre \\\\",
                "y el ",
                "dispositivo ",
                " empleado para recibir las \\\\",
                "clases virtuales.",
            ).set_color_by_tex_to_color_map(
                {"semestre": SKY_BLUE, "dispositivo": SKY_BLUE}
            ),
            presets.PTex(
                "Los datos fueron normalizados para apreciar de mejor manera la proporción de uso de los dispositivos por semestre.",
                alignment="left",
                line_length=32,
                interline_space=0.2,
            ),
        )

        # align paragraph lines
        VGroup(text[0][:2], text[0][2:5], text[0][-1]).arrange(DOWN, aligned_edge=LEFT)
        text.scale(TEXT_SCALE).arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=1
        ).to_edge(edge=RIGHT, buff=1)

        self.play(
            Transform(
                self.title,
                Tex("Diagrama de Barras", **self.config["title"]).move_to(self.title),
            ),
            run_time=1.2,
        )
        self.wait()

        self.play(
            FadeIn(plot, shift=RIGHT),
            AnimationGroup(Wait(2), Write(text[0]), lag_ratio=1),
            run_time=3,
        )
        self.wait()
        self.play(Write(text[1]), run_time=2)
        self.wait()

        self.play(
            FadeOut(text),
            AnimationGroup(
                Wait(1),
                plot.animate.scale_to_fit_width(9).move_to(DOWN * 0.5),
                lag_ratio=1,
            ),
            run_time=2,
        )

        self.wait(3)
        self.ignore_mobs = [self.title]

    @end_with_fadeout
    def scene_histogram(self):
        plot = (
            ImageMobject(filename_or_array=f"{ROOT_PATH}/assets/images/histogram.png")
            .scale_to_fit_width(9)
            .shift(DOWN * 0.5)
        )

        self.play(
            Transform(
                self.title,
                Tex("Histograma", **self.config["title"]).move_to(self.title),
            ),
            run_time=1.2,
        )
        self.wait()

        self.play(FadeIn(plot, shift=UP), run_time=1.2)
        self.wait(3)

        self.ignore_mobs = [self.title]

    @end_with_fadeout
    def scene_time_series(self):
        bl = (
            BulletedList(
                "Fuente de datos: integrantes del grupo",
                "Carrera: Ing. de Sistemas",
                "Semestre actual: Sexto",
                dot_scale_factor=3,
            )
            .scale(0.5)
            .to_edge(RIGHT, buff=1.5)
        )

        # add colors to bullet list dots
        for line in bl:
            line[0].set_color(EGGPLANT)
        plot = (
            ImageMobject(filename_or_array=f"{ROOT_PATH}/assets/images/time-series.png")
            .scale_to_fit_width(6)
            .to_edge(LEFT, buff=1.5)
        )

        self.play(
            Transform(
                self.title,
                Tex("Gráfica Serie de Tiempo", **self.config["title"]).move_to(
                    self.title
                ),
            ),
            run_time=1.2,
        )
        self.wait()

        self.play(
            FadeIn(plot),
            AnimationGroup(Wait(1.2), Create(bl), lag_ratio=1),
            run_time=2,
        )
        self.wait()

        self.play(
            FadeOut(bl),
            AnimationGroup(
                Wait(0.8),
                plot.animate.scale_to_fit_width(8.6).move_to(DOWN * 0.5),
                lag_ratio=1,
            ),
            run_time=2,
        )
        self.wait(3)

        self.ignore_mobs = [self.title]

    @end_with_fadeout
    def scene_box_plot(self):
        plot = (
            ImageMobject(filename_or_array=f"{ROOT_PATH}/assets/images/box-plot.png")
            .scale_to_fit_width(10)
            .shift(DOWN * 0.5)
        )
        self.play(
            Transform(
                self.title,
                Tex("Gráfica de Caja", **self.config["title"]).move_to(self.title),
            ),
            run_time=1.2,
        )
        self.wait()

        self.play(FadeIn(plot, shift=UP), run_time=1.5)
        self.wait(3)

        self.ignore_mobs = [self.title]


class Outro(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = {
            "text": {
                "stroke_width": 0.8,
                "background_stroke_width": 5,
                "background_stroke_color": BLACK,
                "sheen_direction": UR,
            },
            "names": {
                "stroke_width": 1,
                "background_stroke_width": 5,
                "background_stroke_color": BLACK,
                "sheen_direction": UR,
            },
        }
        self.gradient = [BLUE, YELLOW]

    def construct(self):

        author_scale = 0.7
        author_width = 2

        header = Text("Creado por:", **self.config["text"])

        student_info = VGroup(
            MathTex(
                r"\varepsilon \text{ José Silva }",
                color=SKY_BLUE,
                **self.config["names"],
            ),
            MathTex(
                r"\gamma \text{ Edward Parada }",
                color=LIGHT_PURPLE,
                **self.config["names"],
            ),
            MathTex(
                r"\Omega \text{ Gian Estevez }",
                color=FAWN,
                **self.config["names"],
            ),
            MathTex(r"\mu \text{ Yuri Garcia }", color=COFFEE, **self.config["names"]),
        ).scale(author_scale)

        student_images = [
            ImageMobject(filename_or_array=f"{ROOT_PATH}/assets/images/jose_chad.png"),
            ImageMobject(filename_or_array=f"{ROOT_PATH}/assets/images/ed_chad.png"),
            ImageMobject(filename_or_array=f"{ROOT_PATH}/assets/images/gian_chad.png"),
            ImageMobject(filename_or_array=f"{ROOT_PATH}/assets/images/yuri_chad.png"),
        ]

        for image in student_images:
            image.width = author_width

        start_coord = LEFT * 4.5 + UP * 1
        student_buff = 1

        base_student = student_info[0]
        base_student.move_to(start_coord)

        for prev, image in enumerate(student_info[1:]):
            image.next_to(student_info[prev], RIGHT, buff=student_buff)

        for student, image in zip(student_info, student_images):
            # image : Mobject
            image.next_to(student, DOWN, buff=student_buff / 2)

        motor = Text(
            "Motor de animación: ",
            color=SKY_BLUE,
            # **self.text_config
        )

        # banner = ManimBanner()

        header.shift(UP * 3 + LEFT * 3)
        motor.shift(UP * 3 + LEFT * 3)

        # header.set_color_by_gradient(*[color for color in PALETTE])
        header.set_color(SKY_BLUE)

        # self.add(header.move_to(UP * 2.5), jose, yuri, ed, gian, student_info)

        self.play(
            DrawBorderThenFill(header),
            MoveAlongPath(
                header,
                ArcBetweenPoints(header.get_center(), UP * 2.5, angle=TAU / 8),
                rate_func=exponential_decay,
            ),
            run_time=3,
        )

        self.play(
            *[FadeIn(image) for image in student_images],
            *[Write(student) for student in student_info],
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=3,
        )

        # self.play(
        #     Write(motor),
        #     MoveAlongPath(
        #         motor,
        #         ArcBetweenPoints(motor.get_center(), UP * 2.5, angle=TAU / 8),
        #         rate_func=exponential_decay,
        #     ),
        #     run_time=3,
        # )
        # self.play(DrawBorderThenFill(banner), run_time=3)
        # self.play(banner.animate.shift(RIGHT * 1.2), run_time=0.5)
        # self.play(banner.expand())
        # self.wait(2)
        # self.play(FadeOut(banner), FadeOut(motor))


class Test(Scene):
    def construct(self):
        cl = Clock(
            circle_config={
                "color": WHITE,
                "stroke_color": DARK_GRAY,
                "fill_opacity": 1,
                "stroke_width": 5,
            },
            hands_config={"color": DARK_BLUE},
            ticks_config={"color": DARK_GRAY, "stroke_width": 5},
        )

        self.add(cl)

        self.play(ClockPassesTime(cl, hours_passed=1), run_time=2)

        self.wait()


if __name__ == "__main__":
    runner = video_utils.ManimRunner(
        scenes={
            # "Intro": [
            # "DataAndSubjectOfStudy": [
            # "Conclusions": [
            # "Outro": [
            # "DataAndSubjectOfStudyIntro": [
            # "DataTreatmentIntro": [
            "ConclusionsIntro": [
                # "Test": [
                "-qh",
                "-p",
                # "-ps",
                "--disable_caching",
            ],
        },
        file_path="ft_form/main.py",
        project_name="Godofredo",
    )

    runner.run_scenes()
    # runner.concatenate_videos(run_output=True)
