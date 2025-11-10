# Saline Level Monitoring System (IoT-Based)

An IoT-based smart saline monitoring system designed to continuously measure saline (IV fluid) levels and send automated alerts to prevent backflow and ensure patient safety. The system aims to replace manual monitoring in hospitals with a more reliable, real-time solution.

---

## 🚀 Project Overview

Traditional saline monitoring requires constant human supervision, which can lead to delays, backflow, and potential health risks when levels go unnoticed. This project automates the process by:

- Continuously monitoring saline fluid level using sensors
- Sending real-time alerts when the fluid is about to empty
- Reducing nursing workload and improving patient safety
- Providing data logging for further analytics

---

## 🧠 Key Features

✅ Real-time IV fluid level monitoring  
✅ Instant alert generation when level drops below threshold  
✅ Wireless communication for remote monitoring  
✅ Data logging for trend analysis and hospital records  
✅ Can be adapted for individual patient use or central monitoring system  

---

## 🛠️ Tech Stack

| Component | Technology Used |
|----------|------------------|
| Microcontroller | ESP8266 / ESP32 |
| Sensor | Load Cell with HX711 Amplifier |
| Communication | Wi-Fi (MQTT / HTTP) |
| Backend (Optional) | Python |
| Alert System | Buzzer / Notification System |
| Data Storage (Optional) | CSV / Cloud Storage |

---

## 📌 Working Principle

1. The saline bottle is placed on a load cell to measure weight.  
2. The HX711 amplifier converts weight data for the microcontroller.  
3. The ESP module processes the input and checks the threshold.  
4. When the saline level reaches the minimum limit, an alert is triggered.  
5. (Optional) Data is stored or sent to a dashboard/mobile notification system.  

---

## 🔧 Hardware Requirements

| Component | Quantity |
|----------|----------|
| ESP8266 / ESP32 | 1 |
| Load Cell (5kg recommended) | 1 |
| HX711 Load Cell Amplifier | 1 |
| Jumper Wires | As required |
| Power Supply | 5V |
| Buzzer (optional) | 1 |

---

## 📍 Circuit Diagram

(Add your circuit diagram image inside `/Documentation/Images` and embed it here)


![Circuit Diagram](./Documentation/Images/circuit_diagram.png)

---

## 🧪 How to Run

### **Arduino Code**

1. Open the `.ino` file located in `/Arduino`
2. Install necessary libraries:

   * HX711
   * WiFi / ESP libraries
3. Upload code to ESP module

### **Python Code (Optional)**

```bash
pip install -r requirements.txt
python water_monitor.py
```

---

## 📂 Repository Structure

```
Saline-Level-Monitoring-IoT/
│
├── Arduino/
│   ├── saline_monitor.ino
│   └── README.md
│
├── Python/
│   ├── water_monitor.py
│   └── requirements.txt
│
├── Documentation/
│   ├── Project_Report.pdf
│   ├── Presentation.pdf
│   ├── References.md
│   └── Images/
│       ├── block_diagram.png
│       ├── flowchart.png
│       └── circuit_diagram.png
│
├── Data_Logs/
│   └── sample_water_level_log.csv
│
├── LICENSE
├── README.md
└── .gitignore
```

---

## 📈 Future Enhancements

🔹 Mobile app for centralized monitoring across multiple beds
🔹 Battery-less design using energy harvesting
🔹 Integration with hospital management systems
🔹 GSM module for SMS alerts (for rural hospitals with no Wi-Fi)
🔹 AI-based analysis of usage trends

---

## 🏥 Real-World Impact

This system aims to:

* Reduce nurse workload
* Prevent saline backflow risks
* Provide reliable and automated monitoring
* Improve patient care in hospitals and clinics


