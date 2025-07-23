import psutil
import os
import time
#If there is a nvidia gpu the code will use pynvml. If there isn't one we go through the system data
try:
    from pynvml import *
    nvmlInit()
    gpu_handle = nvmlDeviceGetHandleByIndex(0)
    use_nvidia = True    
except:
    use_nvidia = False

def get_gpu_usage():
    if use_nvidia:
        return nvmlDeviceGetUtilizationRates(gpu_handle).gpu
    try:
        #Alternative way to get the gpu data if it isn't a nvidia gpu
        with open("/sys/class/drm/card1/device/gpu_busy_percent", "r") as f:
            return int(f.read().strip())
    except:
        #If the file is not readeable or missing none will be returned
        return None
    
def get_cpu_temp():
    try: 
        temps = psutil.sensors_temperatures()
        for name in temps:
            for entry in temps[name]:
                if entry.label == "package id 0" or entry.label == "":
                    return round(entry.current, 1)
    except:
        return None

def get_gpu_temp():
    try:
        if use_nvidia:
            return nvmlDeviceGetTemperature(gpu_handle,NVML_TEMPERATURE_GPU)
    except:
        return None
    else:
        return get_amd_gpu_temp()

def get_amd_gpu_temp():
    try: 
        base_path = "/sys/class/hwmon"
        for entry in os.listdir(base_path):
            name_path = os.path.join(base_path, entry , "name")
            if os.path.exists(name_path):
                with open (name_path) as f:
                    if "amdgpu" in f.read():
                        temp_path = os.path.join(base_path, entry, "temp1_input")
                        with open(temp_path) as tf:
                            return round(int(tf.read().strip())/ 1000 , 1)
    except:
        return None

def get_eth_usage(interface="enp39s0"):
    try:
        net1 = psutil.net_io_counters(pernic=True).get(interface)
        if not net1:
            return "–"
        time.sleep(0.1)
        net2 = psutil.net_io_counters(pernic=True).get(interface)
        if not net2:
            return "–"
        factor = 1/ 0.1 # Umrechung auf 1 Sekunde    
        down = (net2.bytes_recv - net1.bytes_recv) / 1024 *factor # kB
        up = (net2.bytes_sent - net1.bytes_sent) / 1024 *factor
        return f"{int(down)}↓ / {int(up)}↑"
    except:
        return "–"


def get_system_usage():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    gpu = get_gpu_usage()
    cpu_temp = get_cpu_temp()
    gpu_temp = get_gpu_temp()
    eth_usage = get_eth_usage()
    return cpu, cpu_temp, gpu , gpu_temp, ram, eth_usage

