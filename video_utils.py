import shutil

import os

from pathlib import Path

from manim import SVGMobject, WHITE


UIS_COLOR = "#67b93e"


class ManimRunner(object):
    def __init__(self, class_to_render, file_path, project_name, manim_args=[], output_dir=None):
        """
            args: <list type> [manim raw args such as '-pql' or '-a']
            readable kwargs:
                            - project_name: name of the folder where media will be saved
        """
        # default args
        self.args = {
            "raw": ' '.join(manim_args)
        }
        self.file_path = ManimRunner.read_path(file_path)

        if not output_dir:
            output_dir = Path(Path.home() / "Videos" / "Manim")

        self.class_name = class_to_render

        if not os.path.isabs(self.file_path):
            self.file_path = Path(Path.cwd() / self.file_path)

        if project_name:
            output_dir = Path(output_dir / project_name)
            ManimRunner.create_folder(output_dir)

        self.execute_scene(output_dir, manim_args)

    def execute_scene(self, output_dir, args):
        command = ' '.join([
            "manim",
            f'"{self.file_path}"',
            self.class_name,
            self.args["raw"],
            "--media_dir",
            f'"{output_dir}"',
            *args
        ])

        print(f"[RUNNER INFO] Executing {command}")
        os.system(command)

    @staticmethod
    def create_folder(path):
        assert isinstance(path, Path)
        if not path.exists():
            path.mkdir(parents=True)
        return path

    @staticmethod
    def read_path(path):
        """
            convert string path or list of folders to Path object
            INPUT: str or list
            OUTPUT: Path object

        """
        if (isinstance(path, list) or
                isinstance(path, tuple)):
            return Path(Path.cwd() / "/".join(path))
        return Path(path)
