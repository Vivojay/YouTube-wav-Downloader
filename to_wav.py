import ffmpeg
import subprocess
import os

def convert_to_wav(Dir, path, show_command = False):
    os.chdir(Dir)
    ffmpeg_conversion_script_command = f'ffmpeg -i "{path}" "{os.path.splitext(path)[0]+".wav"}" -loglevel warning'
    if show_command:
        os.chdir(Dir)
        print('running command\n    > '+ffmpeg_conversion_script_command)
    subprocess.call(ffmpeg_conversion_script_command, stdout=subprocess.PIPE, shell = True)

    try:
        os.remove(path)
    except FileNotFoundError:
        pass
