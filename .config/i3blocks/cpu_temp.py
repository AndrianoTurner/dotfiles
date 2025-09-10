#!/usr/bin/env python3

import glob
import json

def get_cpu_temp():
    try:
        # Find thermal zone files
        thermal_zones = glob.glob("/sys/class/thermal/thermal_zone*/temp")
        if not thermal_zones:
            raise Exception("No thermal sensors found")

        # Read the first available thermal zone (usually CPU)
        with open(thermal_zones[0], 'r') as f:
            temp_millidegrees = int(f.read().strip())
        
        # Convert to degrees Celsius
        temp_celsius = temp_millidegrees / 1000

        # Determine color based on temperature
        if temp_celsius > 80:
            color = "#FF0000"  # Red for hot (>80°C)
        elif temp_celsius > 60:
            color = "#FFFF00"  # Yellow for warm (>60°C)
        else:
            color = "#00FF00"  # Green for safe

        # Format output with custom text appended
        display = f"Temp: {temp_celsius:.1f}°C"
        return {
            "full_text": display,
            "color": color
        }

    except Exception as e:
        return {
            "full_text": f"Temp: Error ({str(e)})",
            "color": "#FF0000"  # Red for errors
        }

if __name__ == "__main__":
    # Allow custom text via command-line argument (optional)
    output = get_cpu_temp()
    print(json.dumps(output))
