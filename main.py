import video_utils
import os
import itertools as it
from manim import *


UIS_GREEN = "#67b93e"
PALETTE = {
    'PURPLE': '#673c4f',
    'LIGHT_PURPLE': '#7f557d',
    'VIOLET': '#726e97',
    'DARK_SKY_BLUE': '#7698b3',
    'SKY_BLUE': '#83b5d1'
}


class Intro(MovingCameraScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uis_logo = SVGMobject(file_name='.\\assets\\svg\\UIS.svg', fill_opacity=0.7,
                                   stroke_width=3, color=UIS_GREEN, stroke_color=WHITE)

        self.uis_logo[1].set_fill(color=WHITE, opacity=.8)
        self.uis_logo[:2].set_stroke(color=UIS_GREEN, width=5)
        self.uis_logo[0].set_fill(color=UIS_GREEN, opacity=.8)
        self.uis_logo[2:5].set_fill(color=UIS_GREEN, opacity=.8)

    def construct(self):

        self.play(Write(self.uis_logo), run_time=1.5)
        self.wait(1.5)

        self.play(FadeOut(self.uis_logo), run_time=1.5)

        title = Tex('HDLE')
        title.scale(2)
        title.align_on_border(UP, buff=2)

        subtitle = Tex(
            'O como colocar datos en términos de numeros (y viceversa)')
        subtitle.scale(0.8)
        subtitle.next_to(title, DOWN, buff=0.35)
        subtitle.set_color('#7698B3')

        self.play(Write(title))
        self.play(Write(subtitle))

        self.wait(0.8)

        author_scale = 0.7
        author_colors = it.cycle([PALETTE['LIGHT_PURPLE'],
                                  PALETTE['VIOLET'],
                                  PALETTE['DARK_SKY_BLUE'],
                                  PALETTE['SKY_BLUE']])

        by = Tex("By:")

        authors = VGroup(
            MathTex(r"\gamma \text{ Edward Parada - 2182070}"),
            MathTex(r"\pi \text{ Gian Estevez - 2102020}"),
            MathTex(r"\varepsilon \text{ José Silva - 2183075}"),
            MathTex(r"\mu \text{ Yuri Garcia - 2182697}")
        ).scale(author_scale)

        base_author = authors[0]
        base_author.set_color(next(author_colors))

        base_author.next_to(subtitle, DOWN, buff=1)
        base_author.align_on_border(LEFT, buff=2)

        authors.arrange_submobjects(DOWN, buff=0.2, center=False)

        author_anims = []

        for author in authors:
            color = next(author_colors)

            if author is not base_author:
                author.align_to(base_author, LEFT)

            author.set_color(color)

            author_anims.append(Write(author))

        by.scale(author_scale)
        by.next_to(base_author, LEFT, buff=.15)

        # animations
        self.play(Write(by))
        self.play(AnimationGroup(*author_anims, lag_ratio=0.2), run_time=3)

        lc_title_1 = Tex(
            'La vida es dura, ',
            alignment='\\justifying'
        )

        lc_title_2 = Tex(
            'pero mas dura es la verdura.',
            alignment='\\justifying'
        )

        lc_title_1.match_height(base_author)
        lc_title_2.match_height(base_author)

        lc_title_1.next_to(subtitle, DOWN, buff=1)
        lc_title_1.shift(RIGHT*3)

        lc_title_2.next_to(lc_title_1, DOWN, buff=.1)
        lc_title_2.align_to(lc_title_1, LEFT)

        lc_title = VGroup(lc_title_1, lc_title_2)
        lc_title.set_color(PALETTE["SKY_BLUE"])

        subtitle_auth = Tex('- Abraham Lincoln')
        subtitle_auth.set_color(PALETTE["VIOLET"])
        subtitle_auth.height = 0.235
        subtitle_auth.next_to(lc_title, DOWN, buff=0.2)
        subtitle_auth.align_on_border(RIGHT, buff=1)

        anim_group = AnimationGroup(
            Write(lc_title), Write(subtitle_auth), lag_ratio=0.5)

        self.play(anim_group, run_time=2.5)

        self.wait(3)

        # self.play(FadeOut(utils.get_vmobjects_from_scene(self)), FadeOut(VGroup(g, lc_title, subtitle_auth)))


class Test(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uis_logo = SVGMobject(file_name='.\\assets\\svg\\UIS.svg', fill_opacity=0.7,
                                   stroke_width=3, color=UIS_GREEN, stroke_color=WHITE)

        self.uis_logo[1].set_fill(color=WHITE, opacity=.8)
        self.uis_logo[:2].set_stroke(color=UIS_GREEN, width=5)
        self.uis_logo[0].set_fill(color=UIS_GREEN, opacity=.8)
        self.uis_logo[2:5].set_fill(color=UIS_GREEN, opacity=.8)

    def construct(self):
        self.play(Write(self.uis_logo), run_time=2)
        self.wait()
        self.play(VFadeOut(self.uis_logo), run_time=2)


if __name__ == "__main__":
    runner = video_utils.ManimRunner(
        scenes={
            'Test': ['-p', '-ql'],
            'Intro': ['-p', '-ql']
        },
        file_path=r'main.py',  # it's relative to cwd
        project_name='Godofredo'
    )

    runner.run_scenes()
    runner.concatenate_videos()
