#!/usr/bin/env python3

import subprocess
import json
import sys
def get_disk_info(custom_text):
    try:
        # Run df command to get disk info for root (/)
        cmd = "df -H --output=size,avail,used / | tail -n1 | tr -s ' '"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception("df command failed")

        # Parse output
        disk = result.stdout.strip().split()
        if len(disk) < 3:
            raise Exception("Unexpected df output")

        total, free, used = disk
        # Calculate usage percentage
        used_bytes = float(used.rstrip('G'))
        total_bytes = float(total.rstrip('G'))
        usage_percent = (used_bytes / total_bytes) * 100

        # Determine color based on usage percentage
        if usage_percent > 80:
            color = "#FF0000"  # Red for high usage (>80%)
        elif usage_percent > 50:
            color = "#FFFF00"  # Yellow for medium usage (>50%)
        else:
            color = "#00FF00"  # Green for low usage

        # Format output
        display = f"{custom_text}: {used}/{total} ({usage_percent:.0f}%)"
        return {
            "full_text": display,
            "color": color
        }

    except Exception as e:
        return {
            "full_text": f"{custom_text}: Error ({str(e)})",
            "color": "#FF0000"  # Red for errors
        }

if __name__ == "__main__":
    custom_text = "Root"
    if len(sys.argv) > 1:
        custom_text = sys.argv[1]
    output = get_disk_info(custom_text)
    print(json.dumps(output))
