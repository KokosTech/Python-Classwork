import os
import requests

OWNER = "Kaloyan"
files_to_download = ["tiktaktoe.py", "ex1_2.py"]

try:
    os.mkdir(OWNER)
except FileExistsError:
    pass

os.chdir(OWNER)

for i in files_to_download:
    r = requests.get("https://raw.githubusercontent.com/KokosTech/Python-HW/main/Holiday-HW/" + i)
    with open(i, "wb") as f:
        for i in r.iter_content(chunk_size=8192):
            f.write(i)