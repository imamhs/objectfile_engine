# Copyright (c) 2021, Md Imam Hossain (emamhd at gmail dot com)
# see LICENSE.txt for details

"""
Object file object
"""

import os

from .sys import get_shell_output
from .sys import get_file_md5

class OFE_file():
    def __init__(self, _name, _location):

        self.name = _name
        self.location = _location
        self.path = ""
        self.file = ""
        self.size = -1
        self.ck = -1
        self.arch = -1
        self.type = -1 #1: dyn exec file, 2: static exec file, 3: dyn so file, 4: static so file
        self.stripped = -1
        self.provide = []
        self.deps = []
        self.glibc_versions = []
        self.glibcxx_versions = []

        self.path = get_shell_output('readlink -z -f "' + os.path.join(_location, _name) + '"')

        self.file = os.path.basename('"' + self.path + '"')

        try:
            self.size = os.path.getsize(self.path)
        except FileNotFoundError:
            print("Error: file not found")
            return
        except:
            print("Error: unknown error occurred (file size)")
            return

        try:
            self.ck = get_file_md5(self.path)
        except:
            print("Error: unknown error occurred (file checksum)")

        file_command_output = get_shell_output('file -b -p "' + self.path + '"').split(", ")

        if len(file_command_output) > 3:

            file_command_output_arch = file_command_output[0].split(" ")[1]

            if file_command_output_arch == '32-bit':
                self.arch = 32
            elif file_command_output_arch == '64-bit':
                self.arch = 64

            file_command_output_type = file_command_output[0].split(" ")[3]
            file_command_output_linking = file_command_output[3].split(" ")[0]

            if file_command_output_type == 'executable' and file_command_output_linking == 'dynamically':
                self.type = 1
            elif file_command_output_type == 'executable' and file_command_output_linking == 'statically':
                self.type = 2
            elif file_command_output_type == 'shared' and file_command_output_linking == 'dynamically':
                self.type = 3
            elif file_command_output_type == 'shared' and file_command_output_linking == 'statically':
                self.type = 4

            file_command_output_strip = file_command_output[-1].split(" ")[0]

            if file_command_output_strip == 'stripped':
                self.stripped = 1
            elif file_command_output_strip == 'not':
                self.stripped = 0

        self.provide = [l.replace(" ", "")[6:] for l in get_shell_output('objdump -p "' + self.path + '" | grep SONAME').split("\n") if len(l) > 0 and l.find("SONAME")]

        self.deps = [os.path.basename(l.replace(" ", "")[6:]) for l in get_shell_output('objdump -p "' + self.path + '" | grep NEEDED').split("\n") if len(l) > 0]

        self.glibc_versions = [l[l.find("GLIBC_")+6:] for l in get_shell_output('objdump -p "' + self.path + '" | grep GLIBC_').split("\n") if len(l) > 0 and l.find("GLIBC_")]

        self.glibcxx_versions = [l[l.find("GLIBCXX_") + 8:] for l in get_shell_output('objdump -p "' + self.path + '" | grep GLIBCXX_').split("\n") if len(l) > 0 and l.find("GLIBCXX_")]
