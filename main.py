import tkinter as tk
from monitor import get_system_usage
import threading
import time
import csv
from datetime import datetime

# Logging status flag
logging_active = False
logging_thread = None

def log_usage():
    with open("usage_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "CPU%", "CPU-Temp", "GPU%", "GPU-Temp", "RAM", "Network"])
        while logging_active:
            cpu, cpu_temp, gpu, gpu_temp, ram, eth = get_system_usage()
            now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            writer.writerow([now, cpu, cpu_temp, gpu, gpu_temp, ram, eth])
            time.sleep(1)

def toggle_logging(button):
    global logging_active, logging_thread
    if not logging_active:
        logging_active = True
        button.config(text="Stop Logging", bg="red")
        logging_thread = threading.Thread(target=log_usage, daemon=True)
        logging_thread.start()
    else:
        logging_active=False
        button.config(text="Start Logging", bg="green")

def stop_logging():
    global logging_active
    logging_active = False

def start_window():
    win = tk.Tk()
    win.title("System utilization")
    win.resizable(True, True)
    win.geometry("500x300")
    win.configure(bg="#252424")

    label = tk.Label(win, font=("Arial", 14), justify="left", bg="#252424", fg="white")
    label.pack(padx=20, pady=10)

    def update():
        cpu, ram, gpu, cpu_temp, gpu_temp, eth_usage = get_system_usage()
        gpu_str = f"{gpu}%" if gpu is not None else "GPU data not found"
        cpu_t_str = f"{cpu_temp}°C" if cpu_temp is not None else "CPU temperature data not found"
        gpu_t_str = f"{gpu_temp}°C" if gpu_temp is not None else "GPU temperature data not found"
        label.config(text=(
            f"CPU: {cpu}% Temperature: {cpu_t_str}\n"
            f"RAM: {ram}%\n"
            f"GPU: {gpu_str} Temperature: {gpu_t_str}\n"
            f"Network: {eth_usage}"
        ))
        win.after(1000, update)

    update()

    # Button
    btn_toggle = tk.Button(win, text="Start Logging", bg="green", command=lambda: toggle_logging(btn_toggle))
    btn_toggle.pack(pady=10)


    win.mainloop()

if __name__ == "__main__":
    start_window()
