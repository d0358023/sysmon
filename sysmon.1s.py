#!/usr/bin/env python3
import psutil
import os
import time


def get_cpu_temp(label_hint="Package id 0"):
    try:
        temps = psutil.sensors_temperatures()
        for group in temps.values():
            for t in group:
                if label_hint in (t.label or "") or t.label == "":
                    return round(t.current)
    except:
        return "–"
    return "–"

def get_amd_gpu_usage():
    try:
        with open("/sys/class/drm/card1/device/gpu_busy_percent", "r") as f: #<- maybe adding an input option for the advanced information window
            return int(f.read().strip())
    except:
        return "–"

def get_amd_gpu_temp():
    try:
        for root, dirs, files in os.walk("/sys/class/drm/card1/device/hwmon"): #<- maybe adding an input option for the advanced information window
            for name in files:
                if name.startswith("temp") and name.endswith("_input"):
                    with open(os.path.join(root, name), "r") as f:
                        return round(int(f.read().strip()) / 1000)
    except:
        return "–"
    return "–"

def get_eth_usage(interface="enp39s0"): ##<- this neesds to be changed depend on your ip-link -> terminal command ip addr
    try:
        net1 = psutil.net_io_counters(pernic=True).get(interface)
        if not net1:
            return "–"
        time.sleep(0.1)
        net2 = psutil.net_io_counters(pernic=True).get(interface)
        if not net2:
            return "–"
        factor = 1/ 0.1 # calucalating units for 1 seconde   
        down = (net2.bytes_recv - net1.bytes_recv) / 1024 *factor # kB
        up = (net2.bytes_sent - net1.bytes_sent) / 1024 *factor
        return f"{int(down)}↓ / {int(up)}↑"
    except:
        return "–"

# --- collecting data ---
cpu = psutil.cpu_percent(interval=0.3)
cpu_temp = get_cpu_temp()
ram = psutil.virtual_memory().percent
gpu = get_amd_gpu_usage()
gpu_temp = get_amd_gpu_temp()
net = get_eth_usage("enp39s0")  #<- this neesds to be changed depend on your ip-link -> terminal command ip addr

# --- output ---
print(f"CPU:{cpu}% {cpu_temp}°C      RAM:{ram}%      GPU:{gpu}% {gpu_temp}°C     NET:{net}  kB/s")

