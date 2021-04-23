from enum import Enum
import os
import sys
import itertools as it
from colour import Color
from manim import *  # type: ignore

from manim.mobject.svg.text_mobject import remove_invisible_chars

import video_utils
import presets


UIS_GREEN = "#67b93e"
PURPLE = '#673c4f'
LIGHT_PURPLE = '#7f557d'
VIOLET = '#726e97'
DARK_SKY_BLUE = '#7698b3'
SKY_BLUE = '#83b5d1'
BEIGE = '#7c795d'

PALETTE = [PURPLE, VIOLET, LIGHT_PURPLE, SKY_BLUE, DARK_SKY_BLUE]

TIMELINE_TIMES = [
    "Epoca antigua",
    "3000 A.C.",
    "Biblia",
    "762 A.C.",
    "594 A.C.",
    "Imperio Romano",
    "1066",
    "Siglo XVI", # General y Colombia
    "1800", # Colombia
    "Siglo XX", # General y Colombia
    "2000", # Colombia
    "2020" # Colombia
]

TIMELINE_LENGTH = 20

class Intro(MovingCameraScene):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uis_logo = SVGMobject(
            file_name='.\\assets\\svg\\UIS.svg').scale(1.2)

        self.uis_logo[1].set_fill(color=WHITE, opacity=.9)
        self.uis_logo[5:].set_fill(color=WHITE, opacity=.9)

        self.names_config = {
            "stroke_width": 1,
            "background_stroke_width": 5,
            "background_stroke_color": BLACK,
            "sheen_factor": .2,
            "sheen_direction": UR,
        }

    def construct(self):
        title = Tex('HDLE')
        title.scale(2)
        title.align_on_border(UP, buff=2)

        subtitle = Tex(
            'O como colocar datos en términos de numeros (y viceversa)')
        subtitle.scale(0.8)
        subtitle.next_to(title, DOWN, buff=0.35)
        subtitle.set_color(DARK_SKY_BLUE)

        author_scale = 0.7
        author_colors = it.cycle(
            [
                PURPLE,
                LIGHT_PURPLE,
                VIOLET,
                DARK_SKY_BLUE,
                SKY_BLUE
            ]
        )

        by = Tex("By:")

        authors = VGroup(
            MathTex(
                r"\gamma \text{ Edward Parada - 2182070}", **self.names_config),
            MathTex(
                r"\Omega \text{ Gian Estevez - 2102020}", **self.names_config),
            MathTex(
                r"\varepsilon \text{ José Silva - 2183075}", **self.names_config),
            MathTex(r"\mu \text{ Yuri Garcia - 2182697}", **self.names_config)
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
        by.next_to(base_author, LEFT, buff=.15)

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
        lc_title.set_color(DARK_SKY_BLUE)

        subtitle_auth = Tex('- Abraham Lincoln')
        subtitle_auth.set_color(VIOLET)
        subtitle_auth.height = 0.235
        subtitle_auth.next_to(lc_title, DOWN, buff=0.2)
        subtitle_auth.align_on_border(RIGHT, buff=1)

        # animations
        self.play(Write(self.uis_logo), run_time=3)
        self.wait(1.5)

        # self.play(FadeOut(self.uis_logo), run_time=1.5)

        # self.play(Write(title))
        # self.play(Write(subtitle))

        # self.play(Write(by))
        # self.play(AnimationGroup(*author_anims, lag_ratio=0.2), run_time=3)

        # self.wait(0.8)

        # anim_group = AnimationGroup(
        #     Write(lc_title), Write(subtitle_auth), lag_ratio=0.2)

        # self.play(anim_group, run_time=2.5)

        # self.wait(3)

        # # lc_title.anim

        # self.play(
        #     FadeOut(presets.get_vmobjects_from_scene(self)),
        #     FadeOut(VGroup(authors, lc_title, subtitle_auth))
        # )

        # self.wait()

class FirstChapterIntro(MovingCameraScene):

    def construct(self):

        chapter = presets.create_chapter(
            title='Inicios de la estadística',
            subtitle='El comienzo de un servicio del estado para el pueblo',
            scale_factor=0.9,
            color=PURPLE
        )

        animations = chapter[0]

        for animation in animations:
            self.play(animation)

        self.wait()

class FirstChapter(MovingCameraScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        default_text_config = {
            "stroke_width": 0.7,
            "background_stroke_width": 5,
            "background_stroke_color": BLACK,
            "sheen_factor": .2,
            "sheen_direction": UR,
        }
        self.text_config = {
            **default_text_config,
            'color': "#c7c7c7"
        }
        self.paragraph_config = {
            **self.text_config,
            "line_spacing": 0.8,

        }
        self.title_config = {
            **default_text_config,
            'color': BEIGE
        }
        self.main_title_config = {
            **self.title_config,
            "color": SKY_BLUE
        }
        self.source_config = {
            'color': GRAY,
            "stroke_width": 0.7,
            "background_stroke_width": 5,
            "background_stroke_color": BLACK,
            "opacity": 0.6
        }

        self.timeline_config = {
            "times" : TIMELINE_TIMES,
            "direction": DOWN,
            "length": TIMELINE_LENGTH,
            "arrow_scale": 1,
            "time_buff": 0.25,
            "time_scale": 0.4,
            "dot_colors": [
                PURPLE,
                LIGHT_PURPLE,
                VIOLET,
                DARK_SKY_BLUE,
                SKY_BLUE
            ]
        }

        self.points = {
            "reference": coord(-6, 1),
            "image start": LEFT * 1.5,
            "out screen up": UP * 10,
            "out screen down": DOWN * 10,
        }

        self.txt_up_shift = UP * 0.5
        self.scales = {
            "title": 0.5,
            "source": 0.4
        }
        self.buffs = {
            "title": 0.3,
            "text": 0.3,
            "source": 0.1,
            "left border": 1.5
        }
        self.shifts = {
            "text": UP * 0.5
        }

    def construct(self):

        # time line

        timeline = presets.TimeLine(**self.timeline_config)
        timeline.next_to(self.points["reference"], DOWN, buff=0)

        header = Tex(
            "Historia de la ",
            "Estádistica",
            **self.main_title_config
        ).scale(1.2)

        header.align_on_border(UP, buff=0.8)

        equal = MathTex("=", **self.text_config)

        etimology = VGroup(
            header[18:],
            Tex(
                "Stat","istic","us",
                **self.text_config
            ),
            Tex(
                "Status",
                **self.text_config
            ).set_color(RED)
        )

        to_highlight = VGroup(
            etimology[1][0],
            etimology[1][-1]
        )

        # images and text

        manuscript = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\1_manuscrito.jpeg')),
            "title": Tex(
                "Manuscrito recuperado",
                **self.text_config
            ),
            "src": Tex(
                "https://bit.ly/3dJRdQ5",
                **self.source_config
            )
        }
        emperor = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\2_emperador_chino.jpg')),
            "title": Tex(
                "Dinastia china",
                **self.text_config
            ),
            "src": Tex(
                "https://bit.ly/3v7qBy8",
                **self.source_config
            )
        }
        players = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\3_jugadores_dados.jpg')),
            "title": Tex(
                "Nacimiento de las probabilidades",
                **self.text_config
            ),
            "src": Tex(
                "https://bit.ly/2QkTLLi",
                **self.source_config
            )
        }

        image_space_between=1.3

        manuscript["image"].scale(1.2).align_on_border(LEFT, buff=1)
        emperor["image"].scale(0.8).next_to(manuscript["image"], buff=image_space_between)
        players["image"].scale(1.7).next_to(emperor["image"], buff=image_space_between)

        manuscript["title"].scale(0.5).next_to(manuscript["image"], UP, buff=self.buffs["title"])
        emperor["title"].scale(0.6).next_to(emperor["image"], UP, buff=self.buffs["title"])
        players["title"].scale(0.5).next_to(players["image"], UP, buff=self.buffs["title"])

        manuscript["src"].scale(self.scales["source"]).next_to(manuscript["image"], DOWN, buff=0.1)
        emperor["src"].scale(self.scales["source"]).next_to(emperor["image"], DOWN, buff=0.1)
        players["src"].scale(self.scales["source"]).next_to(players["image"], DOWN, buff=0.1)


        # animations

        self.play(
            Write(header),
            run_time=2
        )

        self.play(
            FadeIn(manuscript["image"]),
            FadeIn(emperor["image"]),
            FadeIn(players["image"]),
            AnimationGroup(
                Wait(1),
                AnimationGroup(
                    Write(manuscript["title"]),
                    Write(emperor["title"]),
                    Write(players["title"])
                ),
                lag_ratio=1
            ),
            AnimationGroup(
                Wait(1.5),
                FadeIn(
                    VGroup(
                    manuscript["src"],
                    emperor["src"],
                    players["src"]
                    )
                ),
                lag_ratio=1
            ),
            run_time=3
        )
        self.wait()

        self.play(
            header[1].animate.move_to(LEFT * 2).match_height(etimology[-1]),
            FadeOut(header[0]),
            FadeOut(manuscript["image"]),
            FadeOut(emperor["image"]),
            FadeOut(players["image"]),
            FadeOut(
                VGroup(
                    manuscript["title"],
                    emperor["title"],
                    players["title"],
                    manuscript["src"],
                    emperor["src"],
                    players["src"]
                )
            ),
            run_time=2
        )
        header = header[1]
        etimology[1].next_to(equal, RIGHT, buff=0.2)

        self.play(
            header.animate.next_to(equal, LEFT, buff=0.2),
            FadeInFrom(equal, direction=equal.get_center()),
            Write(etimology[1]),
            run_time=0.8
        )

        self.play(
            etimology[1].animate.move_to(ORIGIN),
            FadeOut(equal),
            FadeOut(header),
            run_time=2
        )

        self.play(
            Indicate(to_highlight, scale_factor=1.1, color=RED)
        )

        self.play(
            to_highlight[0].animate.next_to(ORIGIN, LEFT,buff=0.01),
            to_highlight[1].animate.next_to(ORIGIN, RIGHT,buff=0).align_to(to_highlight[0], DOWN),
            FadeOut(etimology[1][1]),
            run_time=1
        )

        self.wait()

        self.play(
            FadeOut(to_highlight),
            timeline.create(with_arrow=True, with_time=True),
            run_time=2
        )

        self.wait()

class AncientTime(FirstChapter):
    def __init__(self, start_time="Epoca antigua", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timeline = presets.TimeLine(**self.timeline_config)
        self.timeline.next_to(self.points["reference"], DOWN, buff=0)

        print(start_time)

        self.timeline.preload_for_scene(
            target_time=start_time,
            scene=self
        )

        self.paragraph_config["line_length"] = 35

    def construct(self):

        # images and text
        
        farming = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\4_farming.jfif')),
            "title": Tex(
                "Registro de ganado",
                **self.title_config
            ),
            "text": presets.text_to_paragraph(
                "Se encontraron registros de rocas que habian sido empleadas para registrar la cantidad de ganado, alimento o personas en aldeas",
                # alignment="left",
                **self.paragraph_config
            ),
            "src": Tex(
                "https://bit.ly/3dJRdQ5",
                **self.source_config
            )
        }
        egyptians = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\5_egyptians.jfif')),
            "title": Tex(
                "Antiguo Egipto",
                **self.title_config
            ),
            "text": presets.text_to_paragraph(
                "Esta organización permite la construcción de piramides en Egipto y la elaboración de censos de población",
                # alignment="right",
                **self.paragraph_config
            ),
            "src": Tex(
                "https://bit.ly/3v7qBy8",
                **self.source_config
            )
        }

        src_scale=0.4
        vertical_shift = UP * 0.5

        farming["image"].scale(1.2).move_to(self.points["image start"])
        egyptians["image"].scale(0.85).align_on_border(RIGHT, buff=1)
        
        farming["title"].scale(self.scales["title"]).next_to(farming["image"], UP, buff=self.buffs["title"])
        egyptians["title"].scale(self.scales["title"]).next_to(egyptians["image"], UP, buff=self.buffs["title"])



        farming["text"].scale(0.45).next_to(farming["image"], RIGHT, buff=0.3).shift(self.shifts["text"])
        egyptians["text"].scale(0.45).next_to(egyptians["image"], LEFT, buff=0.3).shift(self.shifts["text"])

        farming["src"].scale(self.scales["source"]).next_to(farming["image"], DOWN, buff=0.1)
        egyptians["src"].scale(self.scales["source"]).next_to(egyptians["image"], DOWN, buff=0.1)

        # self.add(
        #     # farming["image"], farming["text"], farming["src"],
        #     egyptians["image"], egyptians["text"], egyptians["src"],
        # )

        self.play(
            FadeIn(farming["image"]),
            AnimationGroup(
                Wait(0.2),
                DrawBorderThenFill(farming["title"]),
                lag_ratio=1
            ),
            AnimationGroup(
                Wait(0.3),
                Write(farming["text"]),
                lag_ratio=1
            ),
            AnimationGroup(
                Wait(0.5),
                FadeIn(farming["src"]),
                lag_ratio=1
            ),
            run_time=2
        )
        self.wait()

        self.play(
            FadeOut(farming["image"]),
            FadeOut(
                VGroup(
                    farming["text"],
                    farming["title"],
                    farming["src"]
                )
            ),
            AnimationGroup(
                Wait(1),
                FadeIn(egyptians["image"]),
                DrawBorderThenFill(egyptians["title"]),
                lag_ratio=1
            ),
            AnimationGroup(
                Wait(1.5),
                AnimationGroup(
                    FadeIn(egyptians["text"]),
                    FadeIn(egyptians["src"])
                ),
                lag_ratio=1
            ),
            run_time=4
        )


        self.wait()

    def get_scroll_animation(self, mob_dict):
        return [
            AnimationGroup(
                Wait(1),
                FadeInFrom(mob_dict["image"], self.points["out screen down"]),
                DrawBorderThenFill(mob_dict["title"]),
                lag_ratio=1
            ),
            AnimationGroup(
                Wait(1),
                FadeInFrom(
                    mob_dict["text"] if "text" in mob_dict else mob_dict["list"],
                    self.points["out screen down"]
                ),
                lag_ratio=1
            ),
            AnimationGroup(
                Wait(1.5),
                FadeIn(mob_dict["src"]),
                lag_ratio=1
            )
        ]

class BC3000(AncientTime):
    def __init__(self, *args, **kwargs):
        super().__init__(start_time="Epoca antigua", *args, **kwargs)

        # image is set apart since can't be in a VGroup
        self.previous = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\5_egyptians.jfif')),
            "group": VGroup(
                Tex(
                    "Pirámides de Egipto",
                    **self.title_config
                ),
                presets.text_to_paragraph(
                    "Esta organización permite la construcción de piramides en Egipto y la elaboración de censos de población",
                    **self.paragraph_config
                ),
                Tex(
                    "https://bit.ly/3v7qBy8",
                    **self.source_config
                )
            )
        }

        self.scales["text"] = 0.4
        self.scales["source"] = 0.38

        self.previous["image"].scale(0.85).align_on_border(RIGHT, buff=1)
        self.previous["group"][0].scale(self.scales["title"]).next_to(self.previous["image"], UP, buff=self.buffs["title"])
        self.previous["group"][1].scale(0.45).next_to(self.previous["image"], LEFT, buff=0.3).shift(self.shifts["text"])
        self.previous["group"][2].scale(self.scales["source"]).next_to(self.previous["image"], DOWN, buff=0.1)


        self.add(*self.previous.values())

    def construct(self):

        # images and text
        
        clay_splints = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\6_clay_splints.jpg')),
            "title": Tex(
                "Babilonios", 
                **self.title_config
            ),
            "text": presets.text_to_paragraph(
                "Tablillas de arcilla",
                **self.paragraph_config
            ),
            "src": Tex(
                "https://bit.ly/3dE4YQa", # update
                **self.source_config
            )
        }

        pyramids = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\7_pyramids.jpg')),
            "title": Tex(
                "Egipcios", 
                **self.title_config
            ),
            "text": presets.text_to_paragraph(
                "La organización del pueblo condujo a la construcción de las piramides",
                **self.paragraph_config
            ),
            "src": Tex(
                "https://bit.ly/3v7qBy8",
                **self.source_config
            )
        }

        chinese_agriculture = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\8_chinese_agriculture.jpg')),
            "title": Tex(
                "Chinos", 
                **self.title_config
            ),
            "text": presets.text_to_paragraph(
                "Estadística agricola, comercial e industrial",
                alignment="left",
                **self.paragraph_config
            ),
            "src": Tex(
                "https://bit.ly/3auJLWE",
                **self.source_config
            )
        }

        img_spacing=1
        img_scale=0.42

        # position images
        clay_splints["image"].scale(img_scale).next_to(self.timeline.get_arrow(), RIGHT, buff=3).shift(UP * 1.2)
        pyramids["image"].match_width(clay_splints["image"]).next_to(clay_splints["image"], DOWN, buff=img_spacing).align_to(clay_splints["image"], LEFT)
        chinese_agriculture["image"].match_width(clay_splints["image"]).next_to(pyramids["image"], DOWN, buff=img_spacing).align_to(pyramids["image"], LEFT)

        clay_splints["text"].scale(self.scales["text"]).next_to(clay_splints["image"], RIGHT, buff=self.buffs["text"])
        pyramids["text"].scale(self.scales["text"]).next_to(pyramids["image"], RIGHT, buff=self.buffs["text"])
        chinese_agriculture["text"].scale(self.scales["text"]).next_to(chinese_agriculture["image"], RIGHT, buff=self.buffs["text"])

        clay_splints["title"].scale(self.scales["title"]).next_to(clay_splints["image"], UP, buff=self.buffs["title"])
        pyramids["title"].scale(self.scales["title"]).next_to(pyramids["image"], UP, buff=self.buffs["title"])
        chinese_agriculture["title"].scale(self.scales["title"]).next_to(chinese_agriculture["image"], UP, buff=self.buffs["title"])

        clay_splints["src"].scale(self.scales["source"]).next_to(clay_splints["image"], DOWN, buff=self.buffs["source"])
        pyramids["src"].scale(self.scales["source"]).next_to(pyramids["image"], DOWN, buff=self.buffs["source"])
        chinese_agriculture["src"].scale(self.scales["source"]).next_to(chinese_agriculture["image"], DOWN, buff=self.buffs["source"])

        # self.add(
        #     clay_splints["image"], pyramids["image"], chinese_agriculture["image"],
        #     clay_splints["title"], pyramids["title"], chinese_agriculture["title"],
        #     clay_splints["text"], pyramids["text"], chinese_agriculture["text"],
        #     clay_splints["src"], pyramids["src"], chinese_agriculture["src"],
        # )

        self.play(
            self.timeline.next_time_scroll(),
            # fade out previous mobs
            FadeOutAndShift(self.previous["image"], self.points["out screen up"]),
            FadeOutAndShift(self.previous["group"], self.points["out screen up"]),

            AnimationGroup(
                Wait(1),
                AnimationGroup(
                    FadeInFrom(clay_splints["image"]),
                    FadeInFrom(pyramids["image"]),
                    FadeInFrom(chinese_agriculture["image"])
                ),
                DrawBorderThenFill(
                    VGroup(
                        clay_splints["title"],
                        pyramids["title"],
                        chinese_agriculture["title"]
                    )
                ),
                lag_ratio=1
            ),
            AnimationGroup(
                Wait(1.2),
                # write content
                AnimationGroup(
                    Write(clay_splints["text"]),
                    Write(pyramids["text"]),
                    Write(chinese_agriculture["text"]),
                    lag_ratio=0
                ),
                # fade srcs
                FadeIn(
                    VGroup(
                        clay_splints["src"],
                        pyramids["src"],
                        chinese_agriculture["src"]
                    )
                ),
                lag_ratio=1
            ),
            run_time=2
        )
        self.wait()

class Biblia(AncientTime):
    def __init__(self, *args, **kwargs):
        super().__init__(start_time="3000 A.C.", *args, **kwargs)

        self.paragraph_config["line_length"] = 40

        # image is set apart since can't be in a VGroup
        self.previous = {
            "images": [
                ImageMobject(filename_or_array=image_path('.\\history\\6_clay_splints.jpg')),
                ImageMobject(filename_or_array=image_path('.\\history\\7_pyramids.jpg')),
                ImageMobject(filename_or_array=image_path('.\\history\\8_chinese_agriculture.jpg')),
            ],
            "group": VGroup(
                Tex(
                    "Babilonios",
                    **self.title_config
                ),
                presets.text_to_paragraph(
                    "Tablillas de arcilla",
                    **self.paragraph_config
                ),
                Tex(
                    "https://bit.ly/3dE4YQa",
                    **self.source_config
                ),
                Tex(
                    "Egipcios",
                    **self.title_config
                ),
                presets.text_to_paragraph(
                    "La organización del pueblo condujo a la construcción de las piramides",
                    **self.paragraph_config
                ),
                Tex(
                    "https://bit.ly/3v7qBy8",
                    **self.source_config
                ),
                Tex(
                    "Chinos",
                    **self.title_config
                ),
                presets.text_to_paragraph(
                    "Tablillas de arcilla",
                    **self.paragraph_config
                ),
                Tex(
                    "https://bit.ly/3dE4YQa",
                    **self.source_config
                ),
            )
        }

        text_scale  = 0.4
        source_scale = 0.38
        buff_title=0.3

        img_spacing=1
        img_scale=0.42

        # position images
        self.previous["images"][0].scale(img_scale).next_to(self.timeline.get_arrow(), RIGHT, buff=3).shift(DOWN * 0.8)

        self.previous["images"][1].match_width(self.previous["images"][0]).next_to(self.previous["images"][0], DOWN, buff=img_spacing)
        self.previous["images"][1].align_to(self.previous["images"][0], LEFT)

        self.previous["images"][2].match_width(self.previous["images"][0]).next_to(self.previous["images"][1], DOWN, buff=img_spacing)
        self.previous["images"][2].align_to(self.previous["images"][1], LEFT)

        self.previous["group"][0].scale(self.scales["title"]).next_to(self.previous["images"][0], UP, buff=buff_title)
        self.previous["group"][1].scale(text_scale).next_to(self.previous["images"][0], RIGHT, buff=self.buffs["text"])
        self.previous["group"][2].scale(source_scale).next_to(self.previous["images"][0], DOWN, buff=self.buffs["source"])

        self.previous["group"][3].scale(self.scales["title"]).next_to(self.previous["images"][1], UP, buff=buff_title)
        self.previous["group"][4].scale(text_scale).next_to(self.previous["images"][1], RIGHT, buff=self.buffs["text"])
        self.previous["group"][5].scale(source_scale).next_to(self.previous["images"][1], DOWN, buff=self.buffs["source"])

        self.previous["group"][6].scale(self.scales["title"]).next_to(self.previous["images"][2], UP, buff=buff_title)
        self.previous["group"][7].scale(text_scale).next_to(self.previous["images"][2], RIGHT, buff=self.buffs["text"])
        self.previous["group"][8].scale(source_scale).next_to(self.previous["images"][2], DOWN, buff=self.buffs["source"])

        self.add(
            *self.previous["images"],
            self.previous["group"]
        )

        self.buffs["text"] = 0.6

    def construct(self):
        # images and text

        pentateuco = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\9_pentateuco.png')),
            "title": Tex(
                "Pentateuco", 
                **self.title_config
            ),
            "text": presets.text_to_paragraph(
                "Se observa en el pentateuco (libro de números) un censo realizado por moisés en su salida de Egipto",
                **self.paragraph_config
            ),
            "src": Tex(
                "https://bit.ly/3nb4Ydq", # update
                **self.source_config
            )
        }

        pentateuco["image"].scale(0.8).align_on_border(RIGHT, buff=self.buffs["left border"])
        pentateuco["title"].scale(self.scales["title"]).next_to(pentateuco["image"], UP, buff=self.buffs["title"])
        pentateuco["text"].scale(0.45).next_to(pentateuco["image"], LEFT, buff=self.buffs["text"]).shift(self.shifts["text"])
        pentateuco["src"].scale(self.scales["source"]).next_to(pentateuco["image"], DOWN, buff=self.buffs["source"])

        # animations
        # self.add(
        #     pentateuco["image"], 
        #     pentateuco["text"], 
        #     pentateuco["title"],
        #     pentateuco["src"],
        # )
        self.play(
            self.timeline.next_time_scroll(),
            # fade out previous mobs
            AnimationGroup(
                *[FadeOutAndShift(image, self.points["out screen up"]) for image in self.previous["images"]],
                lag_ratio=0
            ),
            FadeOutAndShift(self.previous["group"], self.points["out screen up"]),
            *self.get_scroll_animation(pentateuco),
            run_time=4
        )
        
        self.wait()
    
class BC762(AncientTime):
    def __init__(self, *args, **kwargs):
        super().__init__(start_time="Biblia", *args, **kwargs)

        self.previous = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\9_pentateuco.png')),
            "group": VGroup(
                Tex(
                    "Pentateuco", 
                    **self.title_config
                ),
                presets.text_to_paragraph(
                    "Se observa en el pentateuco (libro de números) un censo realizado por moisés en su salida de Egipto",
                    **self.paragraph_config
                ),
                Tex(
                    "https://bit.ly/3nb4Ydq", # update
                    **self.source_config
                )
            )
        }

        text_buff = 0.6

        # previous config
        self.previous["image"].scale(0.8).align_on_border(RIGHT, buff=self.buffs["left border"])
        self.previous["group"][0].scale(self.scales["title"]).next_to(self.previous["image"], UP, buff=self.buffs["title"])
        self.previous["group"][1].scale(0.45).next_to(self.previous["image"], LEFT, buff=text_buff).shift(self.shifts["text"])
        self.previous["group"][2].scale(self.scales["source"]).next_to(self.previous["image"], DOWN, buff=self.buffs["source"])

        self.add(
            self.previous["image"],
            self.previous["group"],
        )

        self.shifts["text"] = UP

    def construct(self):
        # images and text
        
        sargon = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\10_sargon_library.jpg')),
            "title": Tex(
                "Biblioteca de Ashurbanipal",
                **self.title_config
            ),
            "text": presets.text_to_paragraph(
                "Sargon II Fundo una biblioteca en nínive donde recopila:",
                **self.paragraph_config
            ),
            "list": BulletedList(
                "Hechos e historias a la fecha",
                "Documentos religiosos",
                "Datos estadisticos sobre producción \\\\y cuentas en general",
                dot_scale_factor=2
            ),
            "src": Tex(
                "https://bit.ly/3dJoRFA",
                **self.source_config
            )
        }

        sargon["image"].scale(1.2).move_to(self.points["image start"])
        sargon["title"].scale(self.scales["title"]).next_to(sargon["image"], UP, buff=self.buffs["title"])
        sargon["src"].scale(self.scales["source"]).next_to(sargon["image"], DOWN, buff=self.buffs["source"])

        sargon["text"].scale(0.4).next_to(sargon["image"], RIGHT, buff=self.buffs["text"]).shift(self.shifts["text"])
        
        sargon["list"].scale(0.5).next_to(sargon["text"], DOWN, buff=0.5)

        # animations
        # self.add(
        #     sargon["image"], 
        #     sargon["text"], 
        #     sargon["title"],
        #     sargon["list"],
        #     sargon["src"]
        # )

        self.play(
            self.timeline.next_time_scroll(),
            # fade out previous mobs
            FadeOutAndShift(self.previous["image"], self.points["out screen up"]),
            FadeOutAndShift(self.previous["group"], self.points["out screen up"]),

            *self.get_scroll_animation(sargon),
            run_time=4
        )
        
        self.wait()
    
    def get_scroll_animation(self, mob_dict):
        return [
            AnimationGroup(
                Wait(1),
                FadeInFrom(mob_dict["image"], self.points["out screen down"]),
                DrawBorderThenFill(mob_dict["title"]),
                lag_ratio=1
            ),
            AnimationGroup(
                Wait(1.2),
                FadeInFrom(
                    VGroup(
                        mob_dict["text"],
                        mob_dict["list"]
                    ),
                    self.points["out screen down"]
                ),
                lag_ratio=1
            ),
            AnimationGroup(
                Wait(1.5),
                FadeIn(mob_dict["src"]),
                lag_ratio=1
            )
        ]

class BC594(AncientTime):
    def __init__(self, *args, **kwargs):
        super().__init__(start_time="762 A.C.", *args, **kwargs)

        self.previous = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\10_sargon_library.jpg')),
            "group": VGroup(
                Tex(
                    "Biblioteca de Ashurbanipal", 
                    **self.title_config
                ),
                presets.text_to_paragraph(
                    "Sargon II Fundo una biblioteca en nínive donde recopila:",
                    **self.paragraph_config
                ),
                BulletedList(
                    "Hechos e historias a la fecha",
                    "Documentos religiosos",
                    "Datos estadisticos sobre producción \\\\y cuentas en general",
                    dot_scale_factor=2
                ),
                Tex(
                    "https://bit.ly/3dJoRFA",
                    **self.source_config
                )
            )
        }

        text_shift = UP

        self.previous["image"].scale(1.2).move_to(self.points["image start"])
        # title
        self.previous["group"][0].scale(self.scales["title"]).next_to(self.previous["image"], UP, buff=self.buffs["title"])
        # text
        self.previous["group"][1].scale(0.4).next_to(self.previous["image"], RIGHT, buff=self.buffs["text"]).shift(text_shift)
        # list
        self.previous["group"][2].scale(0.5).next_to(self.previous["group"][1], DOWN, buff=0.5)
        # src
        self.previous["group"][3].scale(self.scales["source"]).next_to(self.previous["image"], DOWN, buff=self.buffs["source"])

        self.add(
            self.previous["image"],
            self.previous["group"],
        )

        self.paragraph_config["line_length"] = 30


    def construct(self):
        greeks = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\11_greek_census.jpg')),
            "title": Tex(
                "Estádistica en Grecia",
                **self.title_config
            ),
            "text": presets.text_to_paragraph(
                "Realizaron estadística sobre distribución de terreno y servicio militar, también se registraron censos para el cálculo de impuestos y derechos de voto",
                **self.paragraph_config
            ),
            "src": Tex(
                "https://bit.ly/3veq1Pk",
                **self.source_config
            )
        }

        greeks["image"].scale(0.75).align_on_border(RIGHT, buff=self.buffs["left border"])
        greeks["title"].scale(self.scales["title"]).next_to(greeks["image"], UP, buff=self.buffs["title"])
        greeks["text"].scale(0.42).next_to(greeks["image"], LEFT, buff=self.buffs["text"]).shift(self.shifts["text"])
        greeks["src"].scale(self.scales["source"]).next_to(greeks["image"], DOWN, buff=self.buffs["source"])

        # animations

        # self.add(
        #     greeks["image"], 
        #     greeks["text"], 
        #     greeks["title"],
        #     greeks["src"]
        # )
        
        self.play(
            self.timeline.next_time_scroll(),
            # fade out previous mobs
            FadeOutAndShift(self.previous["image"], self.points["out screen up"]),
            FadeOutAndShift(self.previous["group"], self.points["out screen up"]),

            *self.get_scroll_animation(greeks),
            run_time=4
        )
        
        self.wait()

class RomanEmpire(AncientTime):
    def __init__(self, *args, **kwargs):
        super().__init__(start_time="594 A.C.", *args, **kwargs)

        mod_paragraph_config = {
            **self.paragraph_config,
            "line_length": 30
        }

        self.previous = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\11_greek_census.jpg')),
            "group": VGroup(
                Tex(
                    "Estádistica en Grecia", 
                    **self.title_config
                ),
                presets.text_to_paragraph(
                    "Realizaron estadística sobre distribución de terreno y servicio militar, también se registraron censos para el cálculo de impuestos y derechos de voto",
                    **mod_paragraph_config
                ),
                Tex(
                    "https://bit.ly/3veq1Pk", # update
                    **self.source_config
                )
            )
        }

        self.previous["image"].scale(0.75).align_on_border(RIGHT, buff=self.buffs["left border"])
        self.previous["group"][0].scale(self.scales["title"]).next_to(self.previous["image"], UP, buff=self.buffs["title"])
        self.previous["group"][1].scale(0.42).next_to(self.previous["image"], LEFT, buff=self.buffs["text"]).shift(self.shifts["text"])
        self.previous["group"][2].scale(self.scales["source"]).next_to(self.previous["image"], DOWN, buff=self.buffs["source"])

        self.add(
            self.previous["image"],
            self.previous["group"],
        )

    def construct(self):
        romans = {
            "image": ImageMobject(filename_or_array=image_path('.\\history\\13_romans_2.jpg')),
            "title": Tex(
                "Imperio romano",
                **self.title_config
            ),
            "list": BulletedList(
                "Realizaban censos cada 5 años", 
                "sus funcionarios recopilaban los datos sobre \\\\nacimiento, defunciones y matrimonios",
                "Recuentos de ganado, terreno y riquezas \\\\obtenidas en las tierras conquistadas",
                dot_scale_factor=2
            ),
            "src": Tex(
                "https://bit.ly/3gvbB94",
                **self.source_config
            )
        }

        romans["image"].scale(0.9).move_to(self.points["image start"])
        romans["title"].scale(self.scales["title"]).next_to(romans["image"], UP, buff=self.buffs["title"])
        romans["list"].scale(0.5).next_to(romans["image"], RIGHT, buff=self.buffs["text"]).shift(self.shifts["text"])
        romans["src"].scale(self.scales["source"]).next_to(romans["image"], DOWN, buff=self.buffs["source"])

        # animations

        # self.add(
        #     romans["image"], 
        #     romans["list"], 
        #     romans["title"],
        #     romans["src"]
        # )

        self.play(
            self.timeline.next_time_scroll(),

            # fade out previous mobs
            FadeOutAndShift(self.previous["image"], self.points["out screen up"]),
            FadeOutAndShift(self.previous["group"], self.points["out screen up"]),

            *self.get_scroll_animation(romans),
            run_time=4
        )
        
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
            "color": LIGHT_PURPLE,
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

        header = Title("Bibliografía", **self.text_config)

        self.play(Write(header), run_time=2)

        self.play(
            Write(srcs),
            AnimationGroup(
                Wait(1),
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
                        Wait(1),
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
            "sheen_factor": .1,
            "scale": 0.3,
            "sheen_direction": UR,
        }
        self.gradient = [BLUE, YELLOW]

    def construct(self):

        author_scale = 0.7
        author_width = 2

        mobs = VGroup()
        header = Text("Creado por:", **self.text_config)
        mobs = VGroup()

        student_info = VGroup(
            MathTex(r"\gamma \text{ Edward Parada }",
                    color=PURPLE,  **self.names_config),
            MathTex(r"\Omega \text{ Gian Estevez }",
                    color=LIGHT_PURPLE, **self.names_config),
            MathTex(r"\varepsilon \text{ José Silva }",
                    color=VIOLET, **self.names_config),
            MathTex(r"\mu \text{ Yuri Garcia }",
                    color=DARK_SKY_BLUE, ** self.names_config),
        ).scale(author_scale)

        student_images = [
            ImageMobject(filename_or_array=image_path("ed.png")),
            ImageMobject(filename_or_array=image_path("ed.png")),
            ImageMobject(filename_or_array=image_path("jose.png")),
            ImageMobject(filename_or_array=image_path("jose.png")),
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
            image.next_to(student, DOWN, buff=student_buff/2)

        motor = Text(
            "Motor de animación: ",
            color=SKY_BLUE,
            # **self.text_config
        )

        banner = ManimBanner().scale(0.5)

        header.shift(UP*3 + LEFT*3)
        motor.shift(UP * 3 + LEFT * 3)

        header.set_color_by_gradient(*[color for color in PALETTE])

        # self.add(header.move_to(UP * 2.5), jose, yuri, ed, gian, student_info)

        self.play(
            DrawBorderThenFill(header),
            MoveAlongPath(
                header,
                ArcBetweenPoints(header.get_center(), UP*2.5, angle=TAU/8),
                rate_func=exponential_decay
            ),
            run_time=3
        )

        self.play(
            *[FadeIn(image) for image in student_images],
            *[Write(student) for student in student_info],
        )
        mobs.add(student_info, header)
        self.wait(2)
        self.play(
            *[FadeOutAndShift(image, DOWN) for image in student_images],
            FadeOutAndShift(mobs, DOWN),
            run_time=3
        )

        self.play(
            Write(motor),
            MoveAlongPath(
                motor,
                ArcBetweenPoints(motor.get_center(), UP*2.5, angle=TAU/8),
                rate_func=exponential_decay
            ),
            run_time=3
        )
        self.play(DrawBorderThenFill(banner), run_time=3)
        self.play(
            banner.animate.shift(RIGHT * 1.2),
            run_time=0.5
        )
        self.play(banner.expand())
        self.wait(2)
        self.play(FadeOut(banner), FadeOut(motor))

class Test(Scene):
    def construct(self):
        paragraph = presets.PTex(
            "Esto es un texto de prueba to see whether this works or not. It seems is working as I expect.",
            alignment="right",
            interline_space=0.2,
            line_length=25
        )
        txt = ['Esto es un texto de prueba to see whether\\\\', 'this works or not.\\\\']
        self.add(paragraph)
        self.wait()

def image_path(name: str) -> str:
    path = os.path.join("assets", "images", name)
    if not os.path.exists(path):
        raise Exception(f"{path} does not exist.")
    return path

def coord(x: float, y: float) -> "ndarray":
    return RIGHT * x + UP * y

if __name__ == "__main__":
    runner = video_utils.ManimRunner(
        scenes={
            # 'FirstChapter': [
            #     '-sql',
            #     '-p'
            # ],
            # 'AncientTime': [
            #     '-sql',
            #     '-p'
            # ],
            # 'BC3000': [
            #     '-sql',
            #     '-p'
            # ],
            # 'Biblia': [
            #     '-sql',
            #     '-p'
            # ],
            # 'BC762': [
            #     '-sql',
            #     '-p'
            # ],
            # 'BC594': [
            #     '-sql',
            #     '-p'
            # ],
            # 'RomanEmpire': [
            #     '-sql',
            #     '-p'
            # ],
            # 'Bibliography': [
            #     '-sql',
            #     '-p'
            # ],
            # 'Outro': [
            #     '-ql',
            #     '-p'
            # ],
            'Test': [
                '-sql',
                '-p'
            ]
        },
        file_path=r'main.py',  # it's relative to cwd
        project_name='Godofredo'
    )

    runner.run_scenes()
    # runner.concatenate_videos(run_output=True)
