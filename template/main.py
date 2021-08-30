import itertools as it

from manim import *

import sys
import os

# add Godofredo/utils to path
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(FILE_PATH, os.pardir)))

from utils import video_utils, presets


UIS_GREEN = "#67b93e"
PURPLE = "#673c4f"
LIGHT_PURPLE = "#7f557d"
VIOLET = "#726e97"
DARK_SKY_BLUE = "#7698b3"
SKY_BLUE = "#83b5d1"
BEIGE = "#7c795d"
BEIGE_B = "#a9a689"


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
        title = Tex("Historia de la Estadística")
        title.scale(1.5)
        title.align_on_border(UP, buff=2)

        subtitle = Tex("O como colocar hechos en términos de numeros (y viceversa)")
        subtitle.scale(0.8)
        subtitle.next_to(title, DOWN, buff=0.35)
        subtitle.set_color(DARK_SKY_BLUE)

        author_scale = 0.7
        author_colors = it.cycle(
            [PURPLE, LIGHT_PURPLE, VIOLET, DARK_SKY_BLUE, SKY_BLUE]
        )

        by = Tex("By:")

        authors = VGroup(
            MathTex(r"\gamma \text{ Edward Parada - 2182070}", **self.names_config),
            MathTex(r"\Omega \text{ Gian Estevez - 2183074}", **self.names_config),
            MathTex(r"\varepsilon \text{ José Silva - 2183075}", **self.names_config),
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

        lc_title_1 = Tex("El 98 \% de las estadísticas")

        lc_title_2 = Tex("son inventadas.")

        lc_title_1.match_height(base_author)
        lc_title_2.match_height(base_author)

        lc_title_1.next_to(subtitle, DOWN, buff=1)
        lc_title_1.shift(RIGHT * 3)

        lc_title_2.next_to(lc_title_1, DOWN, buff=0.1)
        lc_title_2.align_to(lc_title_1, LEFT)

        lc_title = VGroup(lc_title_1, lc_title_2)
        lc_title.set_color(DARK_SKY_BLUE)

        subtitle_auth = Tex("- Anónimo")
        subtitle_auth.set_color(VIOLET)
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

        self.play(
            FadeOut(presets.get_vmobjects_from_scene(self)),
            FadeOut(VGroup(authors, lc_title, subtitle_auth)),
        )

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
            "Docena de huevos a $1.800 😎",
            "De que me hablas viejo?",
            "GREEEEEEEN 🟢",
            dot_scale=2,
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
            "Intro": [
                "-ql",
                "-p",
                "--disable_caching",
            ],
        },
        file_path="template/main.py",
        project_name="Godofredo",
    )

    runner.run_scenes()
    # runner.concatenate_videos(run_output=True)
