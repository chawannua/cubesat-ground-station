### Hardware Setup
The physical Ground Control Station receiver and payload are built around the **Arduino Mega 2560** microcontroller. The Mega was specifically chosen for its multiple Hardware Serial ports, ensuring reliable and simultaneous communication between the GPS module and the LoRa transceiver without data bottlenecks.

![Hardware Setup](assets/hardware_setup.png)

### Telemetry Dashboard
The Python visualization dashboard plotting cleaned data, showcasing the extreme temperature drop (-45°C), flight path, and IMU status.

![Telemetry Dashboard](assets/dashboard_view.png)

## 📁 Project Structure
```text
cubesat-ground-station/
├── src/
│   ├── GCS_CSV_saver.py       # Live serial data logger (COM port)
│   ├── merge_data.py          # Data pipeline for cleaning & merging LoRa noise
│   └── telemetry_dashboard.py # Visualization dashboard
├── data/                      # Raw and merged flight CSV records
├── assets/                    # Dashboard screenshots and hardware setup
├── requirements.txt           # Python dependencies
└── README.md