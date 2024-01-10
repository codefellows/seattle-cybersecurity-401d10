#!/usr/bin/env python3

# Script:         Ops 401 Class 2 - Ops Challenge 2
# Purpose:        Work with DatTime
# Why:            Ops Challenge
# Other:          ping3 must be installed with pip or pip3

import time
from ping3 import ping, verbose_ping


def get_target():
    target = input("Please Enter the target IP: ")
    if not target:
        target = "8.8.8.8."
    return target

def uptime_sensor(target_ip, interval_seconds=2):
    while True:
        try:
            response = ping(target_ip, timeout=1)

            if response is not None:
                status = "Network Active"
            else:
                status = "Network Inactive"

            timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            print(f"{timestamp} {status} to {target_ip}")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(interval_seconds)

if __name__ == "__main__":
    
    try:
        target_ip = get_target() # Replace with the desired IP address
        uptime_sensor(target_ip)
    except KeyboardInterrupt:
        print("\nExiting the script")
        exit()  
