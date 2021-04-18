import os
import itertools as it
from enum import Enum
from manim import *

import video_utils
import presets

UIS_GREEN = "#67b93e"


class Palette(Enum):
    PURPLE = '#673c4f'
    LIGHT_PURPLE = '#7f557d'
    VIOLET = '#726e97'
    DARK_SKY_BLUE = '#7698b3'
    SKY_BLUE = '#83b5d1'


class Pause(Animation):
    def __init__(self, duration):
        super().__init__(Mobject(), run_time=duration)


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
        author_colors = it.cycle([Palette.LIGHT_PURPLE,
                                  Palette.VIOLET,
                                  Palette.DARK_SKY_BLUE,
                                  Palette.SKY_BLUE])

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
        lc_title.set_color(Palette.SKY_BLUE)

        subtitle_auth = Tex('- Abraham Lincoln')
        subtitle_auth.set_color(Palette.VIOLET)
        subtitle_auth.height = 0.235
        subtitle_auth.next_to(lc_title, DOWN, buff=0.2)
        subtitle_auth.align_on_border(RIGHT, buff=1)

        anim_group = AnimationGroup(
            Write(lc_title), Write(subtitle_auth), lag_ratio=buff)

        self.play(anim_group, run_time=2.5)

        self.wait(3)

        # lc_title.anim

        # self.play(FadeOut(utils.get_vmobjects_from_scene(self)), FadeOut(VGroup(g, lc_title, subtitle_auth)))


class FirstChapter(MovingCameraScene):

    def construct(self):

        chapter = presets.create_chapter(
            title='El ataque de los patos',
            subtitle='4K FHD'
        )

        animations = chapter[0]

        for animation in animations:
            self.play(animation)

        self.wait()


class Bibliography(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ref_point = UP * 3 + LEFT * 3.5
        self.text_config = {
            "stroke_width": .7,
            "alignment": LEFT
        }
        self.dot_config = {
            "radius": .07,
            "color": Palette.LIGHT_PURPLE.value,
            "sheen_factor": .2,
            "sheen_direction": DR
        }

    def construct(self):
        srcs = VGroup(
            Tex(r"Forinash, K. (2018). Fourier Series. compadre. ",
                r"https://www.compadre.org/osp/EJSS/4487/272.htm", **self.text_config),
            Tex(r"Franco García, A. (2010). Análisis de Fourier. Sc.ehu. ",
                r"http://www.sc.ehu.es/sbweb/fisica/ondas/fourier/Fourier.html", **self.text_config),
            Tex(r"What makes an object into a musical instrument? (2019, 4 diciembre). ",
                r"https://plus.maths.org/content/what-makes-object-musical", **self.text_config),
            Tex(r"Fourier Analysis and Synthesis. (2017). hyperphysics. ",
                r"http://hyperphysics.phy-astr.gsu.edu/hbasees/Audio/Fourier.html", **self.text_config),
        ).scale(1.8)

        for mob in srcs:
            mob.scale(.3)

        srcs.move_to(self.ref_point)
        srcs.arrange_submobjects(DOWN, buff=.5)
        dots = VGroup()

        interline_space = 0.1

        for mob in srcs:
            mob[0].align_to(self.ref_point, LEFT)
            mob[1].next_to(mob[0], DOWN, buff=interline_space).align_to(
                self.ref_point, LEFT)
            dot = Dot(**self.dot_config)
            dot.next_to(mob[0], LEFT, buff=.2)
            dots.add(dot)

        header = Title("Bibliografia", **self.text_config)

        self.play(Write(header), run_time=2)

        self.play(
            Write(srcs),
            AnimationGroup(
                Pause(1),
                DrawBorderThenFill(dots), lag_ratio=1
            ), run_time=4
        )
        self.wait()
        self.play(
            # FadeOut(header),
            FadeOutAndShift(srcs, DOWN),
            FadeOutAndShift(dots, DOWN),
            run_time=2,
        )

    def get_srcs_anim(self, mobs, buff=.3):
        anims = []
        for index, mob in enumerate(mobs):
            mob.scale(.3)
            VGroup(*mob).arrange_submobjects(DOWN, buff=3)
            if index == 0:
                mob.move_to(self.ref_point)
            # else:
            #     # mob.align_to(mobs[index - 1], LEFT)
            #     mob.move_to(mobs[index - 1].get_start()*LEFT + self.ref_point*UP + DOWN * index *buff)

            anims.append(
                AnimationGroup(
                    Write(mob[0]),
                    AnimationGroup(
                        Pause(1),
                        Write(mob[1]), lag_ratio=1
                    ), run_time=2)
            )
        return anims


class Outro(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text_config = {
            "stroke_width": 0.8,
            "background_stroke_width": 5,
            "background_stroke_color": BLACK,
            "sheen_factor": .9,
            "sheen_direction": UR,
        }
        self.names_config = {
            "stroke_width": 1,
            "background_stroke_width": 5,
            "background_stroke_color": BLACK,
            # "sheen_factor": .9,
            "scale": 0.3,
            "sheen_direction": UR,
        }
        self.gradient = [BLUE, YELLOW]

    def construct(self):
        mobs = VGroup()
        header = Text("Creado por:", **self.text_config)
        mobs = VGroup()

        student_info = VGroup(
            MathTex(r"\varepsilon \text{ José Silva }",
                    color=Palette.DARK_SKY_BLUE.value, **self.names_config),
            MathTex(r"\gamma \text{ Edward Parada }",
                    color=Palette.LIGHT_PURPLE.value,  **self.names_config),
            MathTex(r"\mu \text{ Yuri Garcia }",
                    color=Palette.SKY_BLUE.value, ** self.names_config),
            MathTex(r"\pi \text{ Gian Estevez }",
                    color=Palette.VIOLET.value, **self.names_config),
        ).scale(0.7)

        author_scale = 0.7

        jose = ImageMobject(filename_or_array=".\\assets\\images\\jose.png")
        ed = ImageMobject(filename_or_array=".\\assets\\images\\jose.png")
        yuri = ImageMobject(filename_or_array=".\\assets\\images\\jose.png")
        gian = ImageMobject(
            filename_or_array=".\\assets\\images\\jose.png")

        start_coord = LEFT * 4.5 + DOWN * .6
        buff = 1

        jose.scale(author_scale).shift(start_coord)
        yuri.scale(author_scale).next_to(jose, RIGHT, buff=buff)
        ed.scale(author_scale).next_to(yuri, RIGHT, buff=buff)
        gian.scale(author_scale).next_to(ed, RIGHT, buff=buff)

        student_info[0].next_to(jose, UP, buff=.3)
        student_info[1].next_to(yuri, UP, buff=.3)
        student_info[2].next_to(ed, UP, buff=.3)
        student_info[3].next_to(gian, UP, buff=.3)

        motor = Text("Motor de animacion: ",
                     color=Palette.SKY_BLUE.value, **self.text_config)

        banner = ManimBanner().scale(0.5)

        header.shift(UP*3 + LEFT*3)
        motor.shift(UP * 3 + LEFT * 3)

        header.set_color_by_gradient(*[color.value for color in Palette])

        # self.add(header.move_to(UP * 2.5), jose, yuri, ed, gian, student_info)

        self.play(
            DrawBorderThenFill(header),
            MoveAlongPath(header,
                          ArcBetweenPoints(
                              header.get_center(), UP*2.5, angle=TAU/8), rate_func=exponential_decay),
            run_time=3)

        self.play(FadeIn(jose),
                  FadeIn(yuri),
                  FadeIn(ed),
                  FadeIn(gian),
                  Write(student_info[0]),
                  Write(student_info[1]),
                  Write(student_info[2]),
                  Write(student_info[3]),
                  )
        mobs.add(student_info, header)
        self.wait(2)
        self.play(
            FadeOutAndShift(jose, DOWN),
            FadeOutAndShift(gian, DOWN),
            FadeOutAndShift(ed, DOWN),
            FadeOutAndShift(yuri, DOWN),
            FadeOutAndShift(mobs, DOWN), run_time=3)

        self.play(
            MoveAlongPath(motor,
                          ArcBetweenPoints(
                              motor.get_center(), UP*2.5, angle=TAU/8), rate_func=exponential_decay),
            run_time=3)
        self.play(FadeIn(banner), run_time=3)
        self.play(
            banner.animate.shift(RIGHT),
            run_time=0.6
        )
        self.play(banner.expand())
        self.wait(2)
        self.play(FadeOut(banner), FadeOut(motor))


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
            # 'Test': ['-p', '-qh'],
            'Bibliography': ['-p', '-sql', '--disable_caching', '--flush_cache']
        },
        file_path=r'main.py',  # it's relative to cwd
        project_name='Godofredo'
    )

    runner.run_scenes()
    # runner.concatenate_videos()
