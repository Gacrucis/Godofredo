from manim import *

import utils


class Intro(Scene):
    def construct(self):
        self.show_uis_logo()

    def show_uis_logo(self):
        uis = utils.get_uis_logo()
        self.play(DrawBorderThenFill(uis), run_time=2)
        self.wait()
        self.play(VFadeOut(uis), run_time=2)


if __name__ == "__main__":
    utils.ManimRunner(
        class_to_render='Intro',
        file_path=r'main.py',  # it's relative to cwd
        args=["-p", "-ql"],
        project_name="Godofredo"
    )
