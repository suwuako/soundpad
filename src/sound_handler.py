import os

async def play(path):
    localpath = f"{os.path.abspath(os.getcwd())}\{path}"
    print(localpath)
    # os.system(f"{localpath}/src/playsound.py {path}")
    os.system(localpath)