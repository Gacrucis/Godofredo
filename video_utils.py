import traceback

import os

from pathlib import Path


class ManimRunner(object):
    def __init__(self,
                 scenes, file_path, project_name=None, output_dir=None):
        """
            scenes: <dict> look like: {'class_name': [arg1, arg2]}
            file_path: <str or Path>
            manim_args: <list> [manim raw args such as '-pql' or '-a'],
            output_dir: <str or Path> place where the media files for each scene will be stored


        """
        self.file_path = ManimRunner.read_path(file_path)

        if not output_dir:
            output_dir = Path(Path.home() / "Videos" / "Manim")

        self.output_dir = output_dir

        if not os.path.isabs(self.file_path):
            self.file_path = Path(Path.cwd() / self.file_path)

        if project_name:
            self.output_dir /= project_name
            ManimRunner.create_folder(output_dir)

        self.scenes = scenes

    def run_scenes(self):
        assert hasattr(self, 'scenes')
        # scenes meta has the name of the output folder where
        # are the videos of rendered scenes
        self._scenes_meta = {}
        for scene, args in self.scenes.items():
            try:
                self.run_scene(scene, args)
                self._scenes_meta.setdefault(
                    scene,
                    ManimRunner.get_media_output_folder(args)
                )
            except Exception:
                traceback.print_exc()
                continue

    def run_scene(self, scene_name, args):
        """
            scene_name: <str>,
            args: <list>
        """
        command = ' '.join([
            "manim",
            ManimRunner.clean_path(self.file_path),
            scene_name,
            "--media_dir",
            ManimRunner.clean_path(self.output_dir),
            *args
        ])

        print(f"[RUNNER INFO] Executing {command}")
        os.system(command)

    def concatenate_videos(self, run_output=False):
        if len(self.scenes) <= 1:
            print("[INFO] Requires 2 or more videos to concatenate.")
            return
        temp_name = 'temp.txt'
        output_name = 'out.mp4'

        videos_dict = {}
        manim_file_name = self.get_file_name(with_ext=False)
        for scene in self.scenes:
            videos_dict.setdefault(
                scene.lower(),
                self.get_video_name(scene)
            )

        videos_path = self.output_dir / 'videos' / manim_file_name

        with open(temp_name, 'w') as f:
            for scene_name, video_name in videos_dict.items():
                full_path = videos_path / video_name
                line = f'file \'{full_path}\'\n'
                f.write(line)

        ffmpeg_command = f'echo y | ( ffmpeg -f concat -safe 0 -i {temp_name} -c copy {output_name} )'
        os.system(ffmpeg_command)

        os.remove(temp_name)

        if run_output:
            os.system(f'start {output_name}')

    def get_video_name(self, scene_name, ext=".mp4"):
        assert scene_name in self._scenes_meta
        folder_name = self._scenes_meta[scene_name]
        return Path(folder_name) / f"{scene_name}{ext}"

    def get_file_name(self, with_ext=True):
        file_name = self.file_path.name
        if with_ext:
            return file_name
        return file_name.split('.')[0]

    @staticmethod
    def clean_path(path):
        """
            clean Path object to string like: "'path'"
        """
        return f'"{path}"'

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

    @staticmethod
    def get_media_output_folder(args):
        """
            associate 'ql', 'qh'  with folder names
            such as 480p15 or 1080p30
        """
        str_args = ' '.join(args)
        if any([arg in str_args for arg in ["-ql", "--low_quality", "--quality l"]]):
            return "480p15"
        elif any([arg in str_args for arg in ["-qm", "--medium_quality", "--quality m"]]):
            return "720p30"

        elif any([arg in str_args for arg in ["-qh", "--high_quality", "--quality h"]]):
            return "1080p60"

        elif any([arg in str_args for arg in ["-qk", "--fourk_quality", "--quality k"]]):
            return "2160p60"

        elif any([arg in str_args for arg in ["-qp", "--production_quality", "--quality p"]]):
            return "1440p60"
