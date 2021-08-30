import itertools as it

from manim import *

import sys
import os

# add Godofredo/utils to path
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(FILE_PATH, os.pardir)))

from utils import video_utils, presets


UIS_GREEN = "#67b93e"
SKY_BLUE = "#98D2EB"
FAWN = "#E5A361"
LIGHT_PURPLE = "#B2B1CF"
DARK_PURPLE = "#412234"
COFFEE = "#735A45"
# EGGPLANT = "#6C464F"
# TERRA_COOTA = "#E26D5C"
# BLUE_CORNFLOWER = "#7F96FF"
# LIGHT_BLUE = "#A6CFD5"
# LIGHT_CYAN = "#DBFCFF"
PALETTE = [FAWN, SKY_BLUE, LIGHT_PURPLE, DARK_PURPLE, COFFEE]


class Intro(MovingCameraScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uis_logo = SVGMobject(file_name=f"{FILE_PATH}/assets/svg/UIS.svg").scale(
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
        subtitle_auth.set_color(DARK_PURPLE)
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
            color=PURPLE,
        )

        animations = chapter[0]

        for animation in animations:
            self.play(animation)

        self.wait()


class DataAndSubjectOfStudy(MovingCameraScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # stem and leaf
        self.sl_config = {"bar": {"stroke_width": 1, "color": LIGHT_PURPLE}}

    def diagram_scene(func):
        def wrapper(self, title: str, *args, **kwargs):
            txt = Tex(title, stroke_width=1.5)
            self.play(Write(txt))
            self.play(txt.animate.to_edge(UP, buff=0.4), run_time=0.5)

            func(self, *args, **kwargs)

        return wrapper

    def construct(self):
        # self.scene_dot_plot(title="Diagrama de Puntos")
        # self.scene_stem_and_leaf(title="Diagrama de Tallo y Hoja")
        self.scene_bar_plot(title="Diagrama de barras")
        # self.scene_time_series(title="Gráfica Serie de Tiempo")

    @diagram_scene
    def scene_dot_plot(self):
        diagram = (
            ImageMobject(filename_or_array=f"{FILE_PATH}/assets/images/dot-plot.png")
            .scale_to_fit_width(12)
            .shift(DOWN * 0.5)
        )

        self.play(FadeIn(diagram, shift=DOWN), run_time=2)

        self.wait()

    @diagram_scene
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
            .shift(RIGHT * 1.5)
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
            start=stems.get_top(), end=stems.get_bottom(), **self.sl_config["bar"]
        ).next_to(stems, direction=RIGHT, buff=0.25)

        text = (
            VGroup(
                presets.PTex(
                    "El tallo consta de todos los dígitos del número excepto el último, el cual es la hoja.",
                    alignment="left",
                    line_length=30,
                    interline_space=0.2,
                ).scale(TEXT_SCALE),
                presets.PTex(
                    "Los valores del indicador de uso presentan una tendencia central, esto significa que los estudiantes usan “medianamente” las aulas virtuales.",
                    alignment="left",
                    line_length=30,
                    interline_space=0.2,
                ).scale(TEXT_SCALE),
            )
            .arrange_submobjects(DOWN, aligned_edge=LEFT, buff=1)
            .shift(LEFT * 3)
        )

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
        self.wait()

        # self.add(*leaves)
        # self.wait()

    @diagram_scene
    def scene_bar_plot(self):
        plot = (
            ImageMobject(filename_or_array=f"{FILE_PATH}/assets/images/bar-plot.png")
            .scale_to_fit_width(8)
            .to_edge(LEFT, buff=0.7)
            .shift(DOWN * 0.5)
        )
        TEXT_SCALE = 0.5

        text = (
            VGroup(
                presets.PTex(
                    "Los valores utilizados fueron el semestre y el dispositivo utilizado para recibir las clases virtuales.",
                    alignment="right",
                    line_length=30,
                    interline_space=0.2,
                ).scale(TEXT_SCALE),
                presets.PTex(
                    "Para presentar los datos se hizo una normalización de los mismos por cada semestre.",
                    alignment="right",
                    line_length=30,
                    interline_space=0.2,
                ).scale(TEXT_SCALE),
            )
            .arrange_submobjects(DOWN, aligned_edge=RIGHT, buff=1)
            .to_edge(edge=RIGHT, buff=1)
        )

        self.play(
            FadeIn(plot, shift=LEFT),
            AnimationGroup(Wait(1.5), Write(text[0]), lag_ratio=1),
            run_time=3,
        )
        self.wait()
        self.play(Write(text[1]), run_time=2)
        self.wait()

        # self.add(*leaves)
        # self.wait()

    @diagram_scene
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
            line[0].set_color(PALETTE[1])
        plot = (
            ImageMobject(filename_or_array=f"{FILE_PATH}/assets/images/time-series.png")
            .scale_to_fit_width(6)
            .shift(DOWN * 0.5)
        )

        # self.add(plot, bl)
        self.play(FadeIn(plot), run_time=1.5)
        self.wait()
        self.play(
            plot.animate.to_edge(LEFT, buff=1.5),
            AnimationGroup(Wait(1.2), Create(bl), lag_ratio=1),
            run_time=2,
        )
        self.wait()


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
            title="Conclusiones",
            subtitle="O los resultados e inferencias más relevantes del estudio",
            scale_factor=0.9,
            color=PURPLE,
        )

        animations = chapter[0]

        for animation in animations:
            self.play(animation)

        self.wait()


class Conclusions(MovingCameraScene):
    def construct(self):
        self.play(Write(Text("Conclusiones Yeah.")))
        self.wait()


class Bibliography(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ref_point = UP * 3 + LEFT * 5
        self.text_config = {"stroke_width": 1, "alignment": "left", "line_length": 50}
        self.header_config = {"stroke_width": 1}
        self.dot_config = {
            "radius": 0.07,
            "color": LIGHT_PURPLE,
            "sheen_factor": 0.2,
            "sheen_direction": DR,
        }

    def construct(self):
        srcs = VGroup(
            presets.PTex(
                r"S. Hernandez G. (2005, Mayo-Agosto). Historia de la estadística. [Online]. Available: https://www.uv.mx/cienciahombre/revistae/vol18num2/articulos/historia/",
                **self.text_config,
            ),
            presets.PTex(
                r"Some book name or source. [Online]. Available: <link>",
                **self.text_config,
            ),
            presets.PTex(
                r"M.H. Badii, J. Castillo, J. Landeros \& K. Cortez. (2007, Enero-Junio). Papel de la estadística en la investigación científica. [Online]. Available: http://revistainnovaciones.uanl.mx/index.php/revin/article/view/180",
                **self.text_config,
            ),
            presets.PTex(
                r"Some book name or source. [Online]. Available: <link>",
                **self.text_config,
            ),
        ).scale(1.8)

        for mob in srcs:
            mob.scale(0.3)

        srcs.move_to(self.ref_point)
        srcs.arrange_submobjects(DOWN, buff=0.5)
        dots = VGroup()

        interline_space = 0.1

        for mob in srcs:
            mob.align_to(self.ref_point, LEFT)
            # mob[1].next_to(mob[0], DOWN, buff=interline_space).align_to(
            #     self.ref_point, LEFT
            # )
            dot = Dot(**self.dot_config)
            dot.next_to(mob[0], LEFT, buff=0.2)
            dots.add(dot)

        header = Title("Bibliografía", **self.header_config)

        self.play(Write(header), run_time=2)

        self.play(
            Write(srcs),
            AnimationGroup(Wait(1), DrawBorderThenFill(dots), lag_ratio=1),
            run_time=4,
        )
        self.wait()
        self.play(
            # FadeOut(header),
            FadeOut(srcs, shift=DOWN),
            FadeOut(dots, shift=DOWN),
            run_time=2,
        )

    def get_srcs_anim(self, mobs, buff=0.3):
        anims = []
        for index, mob in enumerate(mobs):
            mob.scale(0.3)
            VGroup(*mob).arrange_submobjects(DOWN, buff=3)
            if index == 0:
                mob.move_to(self.ref_point)
            # else:
            #     # mob.align_to(mobs[index - 1], LEFT)
            #     mob.move_to(mobs[index - 1].get_start()*LEFT + self.ref_point*UP + DOWN * index *buff)

            anims.append(
                AnimationGroup(
                    Write(mob[0]),
                    AnimationGroup(Wait(1), Write(mob[1]), lag_ratio=1),
                    run_time=2,
                )
            )
        return anims


class Test(Scene):
    def construct(self):
        l = BulletedList(
            r"Docena de huevos a \$1.800 ",
            "De que me hablas viejo?",
            "GREEEEEEEN ",
        )
        VGroup(
            l[0][0],
            l[1][0],
        ).set_color(SKY_BLUE)
        self.add(l)
        self.wait()


if __name__ == "__main__":
    runner = video_utils.ManimRunner(
        scenes={
            "DataAndSubjectOfStudy": [
                "-ql",
                "-ps",
                # "--disable_caching",
            ],
        },
        file_path="ft_form/main.py",
        project_name="Godofredo",
    )

    runner.run_scenes()
    # runner.concatenate_videos(run_output=True)
