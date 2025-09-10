#!/usr/bin/env python3
import json
def get_memory_usage():
    # Read memory info from /proc/meminfo
    with open('/proc/meminfo', 'r') as f:
        lines = f.readlines()

    # Parse relevant fields
    mem_total = 0
    mem_free = 0
    buffers = 0
    cached = 0

    for line in lines:
        if line.startswith('MemTotal:'):
            mem_total = int(line.split()[1]) * 1024  # Convert kB to bytes
        elif line.startswith('MemFree:'):
            mem_free = int(line.split()[1]) * 1024
        elif line.startswith('Buffers:'):
            buffers = int(line.split()[1]) * 1024
        elif line.startswith('Cached:'):
            cached = int(line.split()[1]) * 1024

    # Calculate used memory (total - free - buffers - cached)
    used = mem_total - mem_free - buffers - cached
    percent = (used / mem_total) * 100
    used = used / (1024 ** 3)
    mem_total = mem_total / (1024 ** 3)
    color = "#00FF00"
    if percent > 90:
        color = "#FF0000"  # Red for high usage
    elif percent > 75:
        color = "#FFFF00"  # Yellow for medium-high usage
    return json.dumps({"full_text": f"{used:.1f}G/{mem_total:.1f}G {percent:.2f}%", "color": color})


if __name__ == "__main__":
   print(get_memory_usage())
