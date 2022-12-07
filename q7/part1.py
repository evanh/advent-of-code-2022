from __future__ import annotations

import sys
sys.path.append("..")

from lineparser import readfile
from dataclasses import dataclass
from typing import Optional

@dataclass
class Folder:
    name: str
    parent: Optional[Folder]
    folders: dict[str, Folder]
    files: dict[str, File]
    _size: Optional[int] = None

    def pprint(self, indent=""):
        print(f"{indent}{self.name}/")
        for f in self.folders:
            self.folders[f].pprint(indent + "    ")
        for f in self.files:
            self.files[f].pprint(indent + "    ")

    def size(self):
        if self._size is None:
            mysize = sum(f.size for f in self.files.values())
            mysize += sum(f.size() for f in self.folders.values())
            self._size = mysize
        return self._size


@dataclass
class File:
    name: str
    size: int

    def pprint(self, indent=""):
        print(f"{indent}{self.name} {self.size}")



class FolderParser:
    def __init__(self):
        self.cur_dir = None
        self.root = Folder("/", None, {}, {})

    def add_to_cur_dir(self, line):
        if line.startswith("dir"):
            _, dir_name = line.split(" ", 1)
            if dir_name not in self.cur_dir.folders:
                self.cur_dir.folders[dir_name] = Folder(dir_name, self.cur_dir, {}, {})
        else:
            file_size, name = line.split(" ", 1)
            if name not in self.cur_dir.files:
                new_file = File(name, int(file_size))
                self.cur_dir.files[name] = new_file

    def update_cur_dir(self, cmd):
        _, arg = cmd.split(" ", 1)
        if arg == "/":
            self.cur_dir = self.root
        elif arg == "..":
            self.cur_dir = self.cur_dir.parent
        else:
            self.cur_dir = self.cur_dir.folders[arg]

    def process(self):
        for line in readfile():
            if line.startswith("$"):
                _, cmd = line.split(" ", 1)
                if cmd.startswith("cd"):
                    self.update_cur_dir(cmd)
            else:
                self.add_to_cur_dir(line)

    def calculate_sizes(self, sizes, folder = None, prefix=""):
        if folder is None:
            folder = self.root

        size = folder.size()
        if size <= 100000:
            sizes.append((folder.name, size))

        for f in folder.folders.values():
            self.calculate_sizes(sizes, f)




f = FolderParser()
f.process()
f.root.pprint()
sizes = []
f.calculate_sizes(sizes)
print(sizes)
print(sum(s[1] for s in sizes))

# total = {k: v for k, v in sizes.items() if v <= 100000}
# print(total)
# print(sum(total.values()))
"""
e has total size 584
a has total size 94853
d has total size 24933642
/ has total size 48381165
"""