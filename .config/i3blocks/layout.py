#!/usr/bin/env python3

import subprocess

def get_layout():
    lang = subprocess.getoutput("xset -q|grep LED| awk '{ print $10 }'")
    match lang:
        case "00000000":
            return "us"
        case "00001000":
           return "ru"

if __name__ == "__main__":
    print(get_layout())
