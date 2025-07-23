# SysMon - lightweight system monitor for Linux

SysMon is a lightweight, Python-based system monitoring tool designed for Linux evironments. It provides real-time stats for CPU, RAM, GPU, temperature sensors, and network traffic. All displayed in a simple GUI window built with Tkinter. Logging and export functionality is included for performance tracking and analysis.

## Features

- Real time monitoring of:
  
  - CPU usage and temperature
  - GPU usage and temperature
  - RAM usage
  - Network stream
- Optional Argos integration for GNOME top bar
- Logging to CSV file with manual start/stop button 

## Preview 

<img width="503" height="334" alt="Bildschirmfoto vom 2025-07-23 10-23-06" src="https://github.com/user-attachments/assets/e1ac7b62-33eb-4bc9-b476-b50b0ec93f65" />


GUI Window     



<img width="481" height="90" alt="Bildschirmfoto vom 2025-07-23 10-24-26" src="https://github.com/user-attachments/assets/20ae46ff-23e2-41d6-9448-6113635859fa" />


Logging     

<img width="997" height="33" alt="Bildschirmfoto vom 2025-07-23 10-22-34" src="https://github.com/user-attachments/assets/2da818e3-0c03-460d-a1e6-8f13e5f0434c" />



The optional intergration in the top bar                                                                          
## Requirements:

- Python 3.8+
- Linux (Ubuntu recommended)
- Dependencies:
 ```bash
 pip install psutil pynvml pillow pystray
```
## Getting Started

Clone the repository and run the GUI:

```bash
git clone https://github.com/dein-user/sysmon.git
cd sysmon
python3 main.py
```
## File Structure
```bash
.
├── main.py # GUI and application logic
├── monitor.py # System usage functions (CPU, RAM, GPU, network)
├── sysmon.1s.sh # Optional Argos plugin for GNOME panel
├── usage_log.csv # Output log file (generated)
└── README.md
```
## Argos Intergration for GNOME Topbar
The Argos intergration is not requiered for the GUI to function. It can also be used as a standalone tool. Here are the steps to install it.
### Step 1. Install Argos  
- Follow the steps in the documentaion from the Argos [Github](https://github.com/p-e-w/argos)
### Step 2. Creat Argos plugin folder (if not present):
```bash
mkdir -p~/.config/argos
```
### Step 3. Copy the plugin script:
Copy sysmon.1s.py from this repo into your argos folder: 
```bash
cp sysmon.1s.py ~/.config/argos/
chomd +x ~/.config/argos/sysmon.1s.py
```
### Step 4. Run it:
The system monitor will appear in your GNOME top bar as soon as Argos picks it up (usually instantly). It refreshes every second.
## Roadmap

### Completed
- GUI window with real-time system data
- Logging to CSV file with start/stop toggle
- Argos integration for GNOME panel

### In Progress
- Real-time usage charts (line graph)
- Unified system tray support

### Planned
- Logging to database
- Settings window (interval, export options)
- Notification system for thresholds

## Why I Built This

SysMon was created as a personal learning project to improve my skills in Python, Linux system monitoring, and GUI design. It also reflects my interest in efficient, minimal tooling and system-level programming.


## About the Developer

Built by Daniel Hochkeppel – feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/daniel-hochkeppel-000336233/)
