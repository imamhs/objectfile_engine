# Copyright (c) 2021, Md Imam Hossain (emamhd at gmail dot com)
# see LICENSE.txt for details

import subprocess
import hashlib


def get_shell_output(_command):
    p = subprocess.Popen(_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    return p.stdout.read().decode('ascii')[0:-1]


def get_file_md5(_filename):
    md5o = hashlib.md5()
    with open(_filename, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            md5o.update(chunk)
    return md5o.hexdigest()
