#!/usr/bin/env python3

import os
import subprocess

def get_battery_info():
    # Path to battery info (adjust BAT0 to your battery name if different)
    bat_path = "/sys/class/power_supply/BAT0"
    if not os.path.exists(bat_path):
        return "No battery", "red"

    # Read capacity
    with open(f"{bat_path}/capacity", "r") as f:
        capacity = int(f.read().strip())

    # Read status
    with open(f"{bat_path}/status", "r") as f:
        status = f.read().strip()

    # Determine icon and color based on status and capacity
    if status == "Charging":
        icon = "⚡️"
        color = "#FFFFFF"  # White for charging
    else:
        if capacity > 80:
            icon = "🔋"
            color = "#00FF00"  # Green for high
        elif capacity > 40:
            icon = "🪫"
            color = "#FFFF00"  # Yellow for medium
        else:
            icon = "🪫"
            color = "#FF0000"  # Red for low

    # Format output
    output = f"{icon} {capacity}%"
    return output, color

def main():
    output, color = get_battery_info()
    print(output)
    print(output)  # Repeated for i3blocks short text
    print(color)   # Color for i3blocks

if __name__ == "__main__":
    main()
