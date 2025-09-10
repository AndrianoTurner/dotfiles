#!/usr/bin/env python3

import subprocess
import re
import os
import json
def toggle_mute():
    try:
        subprocess.run(["pactl", "set-sink-mute", "@DEFAULT_SINK@", "toggle"], check=True)
    except subprocess.CalledProcessError:
        pass  
def increase_volume():
    try:
        subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "+10%"], check=True)
    except subprocess.CalledProcessError:
        pass      
def decrease_volume():
    try:
        subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "-10%"], check=True)
    except subprocess.CalledProcessError:
        pass      

def get_volume_info():
    try:
        volume_output = subprocess.check_output(["pactl", "get-sink-volume", "@DEFAULT_SINK@"]).decode("utf-8","ignore")
        
        volume_match = re.search(r"front-left:.*?(\d+)%", volume_output)
        if not volume_match:
            return {"full_text": "ERR", "color": "#FF0000"}
        volume = float(volume_match.group(1))
        
        mute_output = subprocess.check_output(["pactl", "get-sink-mute", "@DEFAULT_SINK@"]).decode("utf-8","ignore")
        
        mute_match = re.search(r"Mute: (yes|no)", mute_output)
        if not mute_match:
            return {"full_text": "ERR", "color": "#FF0000"}
        muted = mute_match.group(1) == "yes"
        
        if muted:
            return {
                "full_text": "MUTE",
                "short_text": "MUTE",
                "color": "#FFFF00"  # Yellow for muted
            }
        else:
            text = f"{volume:.0f}%"
            return {
                "full_text": text,
                "short_text": text,
                "color": "#00FF00"  # Green for normal
            }
        
    except subprocess.CalledProcessError:
        return {"full_text": "ERR", "color": "#FF0000"}

def main():
    match os.environ.get("button"):
        case "1":
            toggle_mute()
        case "4":
            increase_volume()
        case "5":
            decrease_volume()    
    print(json.dumps(get_volume_info()))


if __name__ == "__main__":
    main()
