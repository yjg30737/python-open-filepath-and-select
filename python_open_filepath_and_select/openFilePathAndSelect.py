import subprocess


def open_file_path_and_select(filename: str):
    path = filename.replace('/', '\\')
    subprocess.Popen(r'explorer /select,"' + path + '"')
