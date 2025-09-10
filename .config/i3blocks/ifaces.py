#!/usr/bin/env python3

import subprocess
import re
import json

def get_network_info():
    try:
        # Get network interfaces
        result = subprocess.run(['ip', 'link'], capture_output=True, text=True)
        interfaces = result.stdout.splitlines()

        # Look for Ethernet (en*) and Wi-Fi (wl*) interfaces
        eth_interface = None
        wlan_interface = None
        for line in interfaces:
            if 'state UP' in line:
                # Check for Ethernet interfaces
                eth_match = re.match(r'^\d+:\s(en\w+):', line)
                if eth_match:
                    eth_interface = eth_match.group(1)
                # Check for Wi-Fi interfaces
                wlan_match = re.match(r'^\d+:\s(wl\w+):', line)
                if wlan_match:
                    wlan_interface = wlan_match.group(1)

        # Prioritize Ethernet if available, otherwise use Wi-Fi
        active_interface = eth_interface or wlan_interface
        if active_interface:
            # Get IP address and subnet mask
            ip_result = subprocess.run(['ip', 'addr', 'show', active_interface], 
                                    capture_output=True, text=True)
            ip_match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)/(\d+)', ip_result.stdout)
            if ip_match:
                ip_address = ip_match.group(1)
                subnet_mask = ip_match.group(2)
                ip_display = f"{ip_address}/{subnet_mask}"
            else:
                ip_display = "No IP"
            # Connected state: Green (prefix with interface type)
            interface_type = "ETH" if active_interface == eth_interface else "WLAN"
            return {
                "full_text": f"{interface_type}: {active_interface} ({ip_display})",
                "color": "#00FF00"  # Green for connected
            }
        else:
            # Disconnected state: Red
            return {
                "full_text": "NET: Disconnected",
                "color": "#FF0000"  # Red for disconnected
            }

    except Exception as e:
        # Error state: Yellow
        return {
            "full_text": f"NET: Error ({str(e)})",
            "color": "#FFFF00"  # Yellow for error
        }

if __name__ == "__main__":
    output = get_network_info()
    print(json.dumps(output))
