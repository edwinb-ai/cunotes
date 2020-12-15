from pathlib import Path
from subprocess import run
from itertools import chain


src_dir = Path("notes/src")
target_dir = Path("notes/pdf")
cmd = ["pandoc"]
flags = ["-s", "-o"]

for s in src_dir.glob("*.md"):
    temp_1 = s.as_posix().split()
    temp_2 = target_dir.joinpath(s.with_suffix(".pdf").name)
    temp_2 = temp_2.as_posix().split()
    print(list(chain(cmd, temp_1, flags, temp_2)))
    run(list(chain(cmd, temp_1, flags, temp_2)))
