import os

localpath = os.path.abspath(os.getcwd())
print(localpath)
os.system(f"{localpath}/temp4.py 123")