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

<img width="503" height="334" alt="Bildschirmfoto vom 2025-07-23 10-23-06" src="https://github.com/user-attachments/assets/b9e9a458-a372-42b6-acb1-7b74f662c945" />

GUI Window     


<img width="481" height="90" alt="Bildschirmfoto vom 2025-07-23 10-24-26" src="https://github.com/user-attachments/assets/2520d598-d94d-43ce-b188-5647c785ae25" />

Logging     


<img width="997" height="33" alt="Bildschirmfoto vom 2025-07-23 10-22-34" src="https://github.com/user-attachments/assets/fe499c59-4230-4e68-9532-27c608b32823" />

The optional intergration in the top bar                                                                          
## Requirements:

- Python 3.8+
- Linux (Ubuntu recommended)
- Dependencies:
 ```bash
 pip install psutil pynvml pillow pystray


