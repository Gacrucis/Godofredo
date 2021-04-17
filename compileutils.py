import os
import sys
import inspect

def concatenate_videos(path=None, name_list=None, ext_list=['.mp4']):

    if path is None:
        script_name = os.path.realpath(inspect.stack()[2][1])
        path = fr'{os.path.dirname(script_name)}\media\videos\{os.path.splitext(os.path.basename(script_name))[0]}\1440p60'

    tmp_name = 'tmp.txt'
    output_name = 'out.mp4'

    if not name_list:
        name_list = [os.path.splitext(file)[0] for file in os.listdir(path)]
    
    video_list = []
    path_file_list = [(os.path.splitext(file)[0], os.path.splitext(file)[1]) for file in os.listdir(path)]

    for name in name_list:
        for filename, ext in path_file_list:
            if name == filename and ext in ext_list:
                video_list.append(f'{filename}{ext}')
    
    print('[INFO] Videos a concatenar (en orden): ')

    for video in video_list:
        print(f'\t[VIDEO] {video}')

    # video_list = [file for file in os.listdir(path) if os.path.splitext(file)[0] in name_list and os.path.splitext(file)[1] in ext_list]

    with open(tmp_name, 'w') as f:

        for video in video_list:
            full_path = f'{path}\\{video}'
            line = f'file \'{full_path}\'\n'
            f.write(line)
    
    ffmpeg_command = f'echo y | ( ffmpeg -f concat -safe 0 -i {tmp_name} -c copy {output_name} )'
    os.system(ffmpeg_command)

    os.remove(tmp_name)


def compile_videos(scenes : list, args, verbose=True, concatenate=False, script_name=None, script_basename=None, script_folder=None, concatenate_folder=None):

    if script_name is None:
        script_name = os.path.realpath(inspect.stack()[2][1])
    
    if script_basename is None:
        script_basename = os.path.splitext(os.path.basename(script_name))[0]
    
    if script_folder is None:
        script_folder = os.path.dirname(script_name)
    
    if verbose:
        print(f'[SCENE] Current script: {script_name}')
    
    base_command = f'manim "{script_name}"'

    for scene in scenes:
        command = f'{base_command} {scene} {args}'

        if verbose:
            print(f'[SCENE] Executing command {command}')

        os.system(command)
    
    if concatenate:

        if concatenate_folder is None:
            concatenate_folder = fr'{script_folder}\media\videos\{script_basename}\1440p60'

        concatenate_videos(concatenate_folder, scenes)