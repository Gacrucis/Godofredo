import shutil

import os

from pathlib import Path

from manim import SVGMobject, WHITE



UIS_COLOR = "#67b93e"


def get_uis_logo():
    logo = SVGMobject(file_name='assets\\svg_images\\UIS.svg', fill_opacity=0.7,
                      stroke_width=3, color=UIS_COLOR, stroke_color=WHITE)

    logo[1].set_fill(color=WHITE, opacity=.8)
    logo[:2].set_stroke(color=UIS_COLOR, width=5)
    logo[0].set_fill(color=UIS_COLOR, opacity=.8)
    logo[2:5].set_fill(color=UIS_COLOR, opacity=.8)
    return logo


class ManimRunner(object):
    def __init__(self, class_to_render, file_path, args=[], **kwargs):
        """
            args: <list type> [manim raw args such as '-pql' or '-a']
            readable kwargs:
                            - project_name: name of the folder where media will be saved
        """
        # default args
        self.args = {
            "-p": "",
            "raw": ' '.join(args)
        }
        self.src = read_path(file_path)
        self.output_dir = Path(Path.home() / "Videos" / "Manim")
        self.class_name = class_to_render

        self.digest_args(**kwargs)
        self.execute_scene()

    def digest_args(self, **kwargs):
        path = self.src
        if not os.path.isabs(self.src):
            path = Path(Path.cwd() / self.src)

        if "project_name" in kwargs:
            folder_name = read_path(kwargs["project_name"])
            self.output_dir /= folder_name
            try:
                if not self.output_dir.exists():
                    self.output_dir.mkdir(parents=True)
            except FileExistsError:
                pass

        self.args.setdefault("file", path)
        self.parse_dir_name()

    def execute_scene(self):
        CLI_MEDIA_PATH = str(path_to_CLI(self.output_dir))
        FILE_PATH = str(path_to_CLI(self.args["file"]))
        command = ' '.join([
            "manim",
            FILE_PATH,
            self.class_name,
            self.args["raw"],
            "--media_dir",
            CLI_MEDIA_PATH
        ])

        print(f"[INFO] Executing {command}")
        os.system(command)

    def parse_dir_name(self):
        assert "file" in self.args and isinstance(
            self.args["file"], Path)
        self.dir_name = self.args["file"].name

    def del_storage_path(self):
        if not hasattr(self, "quality_arg"):
            folder = self.quality["m"]
        else:
            folder = self.quality[self.quality_arg]
        path = os.path.join(
            self.args["--media_dir"], "videos", self.dir_name, folder)
        if os.path.exists(path):
            shutil.rmtree(path, ignore_errors=True)


def read_path(path):
    if (isinstance(path, list) or
            isinstance(path, tuple)):
        return Path(Path.cwd() / "/".join(path))
    return Path(path)


def path_to_CLI(path):
    """ given a path, turn it into a valid command line path
        this is especially useful when directory name within path has whitespaces
    """
    wpath = path
    if isinstance(path, Path):
        wpath = str(path)

    if " " in wpath:
        new_path = f'"{wpath}"'
        return Path(new_path)
    else:
        return path
