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

```md
![Circuit Diagram](./Documentation/Images/circuit_diagram.png)
