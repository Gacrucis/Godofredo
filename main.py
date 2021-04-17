import os
import sys
from manim import *

sys.path.insert(1, f'{os.path.dirname(os.path.realpath(__file__))}')

import video_utils
import compileutils

UIS_GREEN = "#67b93e"


class Intro(Scene):
    def __init__(self):
        self.uis_logo = SVGMobject(file_name='.\\assets\\svg\\UIS.svg', fill_opacity=0.7,
                                   stroke_width=3, color=UIS_GREEN, stroke_color=WHITE)

        self.uis_logo[1].set_fill(color=WHITE, opacity=.8)
        self.uis_logo[:2].set_stroke(color=UIS_GREEN, width=5)
        self.uis_logo[0].set_fill(color=UIS_GREEN, opacity=.8)
        self.uis_logo[2:5].set_fill(color=UIS_GREEN, opacity=.8)

    def construct(self):

        self.wait(1)
        # self.add_sound('introsound')

        uis_logo = SVGMobject('.\\assets\\svg_images\\UIS.svg',
                              fill_opacity=0.7, stroke_width=2, fill_color=UIS_GREEN)

        uis_logo[1].set_fill(color=WHITE, opacity=0.6)

        letter_bg = uis_logo[2].get_fill_rgbas().tolist()[0]

        letter_bg[0:3] = [color*.8*255 for color in letter_bg[0:3]]
        letter_bg[0:3] = [f'{int(color):x}' for color in letter_bg[0:3]]
        letter_bg_hex = ''.join(letter_bg[0:3])
        letter_bg_hex = f'#{letter_bg_hex}'
        letter_bg_opacity = letter_bg[3]

        for logo in uis_logo[2:5]:
            logo.set_fill(color=letter_bg_hex, opacity=letter_bg_opacity)

        self.play(DrawBorderThenFill(uis_logo), run_time=1.5)
        self.wait(1.5)

        self.play(FadeOut(uis_logo), run_time=1.5)

        self.wait(1)
        # self.add_sound('introsound')
        
        title = Tex('HDLE')
        title.scale(2)
        title.align_on_border(UP, buff=2)
        
        subtitle = Tex('O como colocar datos en términos de numeros (y viceversa)')
        subtitle.scale(0.8)
        subtitle.next_to(title, DOWN, buff=0.35)
        subtitle.set_color(RED)

        self.play(Write(title))
        self.play(Write(subtitle))

        # self.wait(3)

        # self.play(Uncreate(VGroup(title, subtitle)), run_time=2.5)

        self.wait(0.8)

        author_scale = 0.7

        by = Tex("By:")

        authors = [
            MathTex(r"\gamma \text{ Edward Parada - 2182070}"),
            MathTex(r"\pi \text{ Gian Estevez - 2102020}"),
            MathTex(r"\varepsilon \text{ José Silva - 2183075}"),
            MathTex(r"\mu \text{ Yuri Garcia - 2182697}")
        ]

        author_colors = [
            '#D9E4E1',
            '#736357',
            '#ac6c2d',
            '#D9E4E1'
        ]


        base_author = authors[0]
        base_author.scale(author_scale)
        base_author.next_to(subtitle, DOWN, buff=1)
        base_author.align_on_border(LEFT, buff=2)
        base_author.set_color(author_colors[0])
        
        for prev, author in enumerate(authors[1:]):
            author.scale(author_scale)
            prev_author = authors[prev]
            color = author_colors[prev+1]

            author.next_to(prev_author, DOWN, buff=0.2)
            author.align_to(base_author, LEFT)
            author.set_color(color)

        by.scale(author_scale)
        by.next_to(base_author, LEFT, buff = .15)
        

        # authors = [g, e, t]
        # authors = [g]
        author_anims = []

        for author in authors:
            
            author_anims.append(Write(author))

        # animations
        self.play(Write(by))
        self.play(AnimationGroup(*author_anims, lag_ratio=0.2), run_time=3)

        lc_title_1 = Tex(
            'La trigonometría es más sobre circulos',
            alignment='\\justifying'
        )

        lc_title_2 = Tex(
            'que sobre triangulos.',
            alignment='\\justifying'
        )

        lc_title_1.match_height(base_author)
        lc_title_2.match_height(base_author)

        lc_title_1.next_to(subtitle, DOWN, buff=1)
        lc_title_1.shift(RIGHT*3)

        lc_title_2.next_to(lc_title_1, DOWN, buff=.1)
        lc_title_2.align_to(lc_title_1, LEFT)

        lc_title = VGroup(lc_title_1, lc_title_2)
        lc_title.set_color(RED_A)

        subtitle_auth = Tex('- Anónimo')
        subtitle_auth.set_color(RED)
        subtitle_auth.height = 0.235
        subtitle_auth.next_to(lc_title, DOWN, buff=0.2)
        subtitle_auth.align_on_border(RIGHT, buff=1)

        anim_group = AnimationGroup(
            Write(lc_title), Write(subtitle_auth), lag_ratio=0.5)

        self.play(anim_group, run_time=2.5)

        self.wait(3)

        # self.play(FadeOut(utils.get_vmobjects_from_scene(self)), FadeOut(VGroup(g, lc_title, subtitle_auth)))

    def show_uis_logo(self):
        self.play(DrawBorderThenFill(self.uis_logo), run_time=2)
        self.wait()
        self.play(VFadeOut(self.uis_logo), run_time=2)


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
        self.play(DrawBorderThenFill(self.uis_logo), run_time=2)
        self.wait()
        self.play(VFadeOut(self.uis_logo), run_time=2)


def main():

    scenes = []
    scenes.append('Intro')
    # scenes.append('BasicIntroScene')
    # scenes.append('QuoteScene')

    args = '-'
    args += 'p'
    args += 'q'
    args += 'h'
    # args += 'm'
    # args += 'l'
    # args += 'k'
    # args += 's'

    # args += ' -c #00ff00'

    compileutils.compile_videos(scenes, args, concatenate=False)
    # compileutils.concatenate_videos(name_list=scenes)


if __name__ == "__main__":
    video_utils.ManimRunner(
        class_to_render='Test',
        file_path=r'main.py',  # it's relative to cwd
        project_name="Godofredo",
        manim_args=["-p", "-ql"],
    )
