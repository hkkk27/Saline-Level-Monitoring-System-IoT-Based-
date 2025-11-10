import serial
import csv
import time
import os
import requests

SERIAL_PORT = 'COM9'
BAUD_RATE = 9600
CSV_FILE = 'water_level_log.csv'
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1363867155447418900/vYJxD1egY__BXC_PpAOJ3Vte0RFanjMzDtcT20YahsdqDMWt1mlkCwPkQMVO7afdQtPk'


# Alert flags and counters
sent_12 = False
sent_13 = False
sent_15_count = 0
MAX_15_ALERTS = 3

# Serial setup
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
time.sleep(2)

# Create CSV if missing
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'Distance (cm)'])

print("📡 Monitoring water level...")

while True:
    if ser.in_waiting:
        try:
            line = ser.readline().decode('utf-8').strip()
            distance = float(line)
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

            # Log the data
            with open(CSV_FILE, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, distance])

            print(f"{timestamp} - Distance: {distance} cm")

            message = None

            # 12 cm range
            if 11.5 <= distance < 12.5 and not sent_12:
                message = { "content": "⚠️ **Water level is low**. Please monitor the bottle." }
                sent_12 = True

            # 13 cm range
            if 12.5 <= distance < 13.5 and not sent_13:
                message = { "content": "🔎 **Please check the water bottle.** Level is getting low." }
                sent_13 = True

            # 15 cm or more: allow up to 3 messages
            if distance >= 15 and sent_15_count < MAX_15_ALERTS:
                message = { "content": "🚨 **Bottle is empty!** Please change the bottle immediately." }
                sent_15_count += 1

            # Reset if back to normal (e.g., filled again)
            if distance < 11.5:
                sent_12 = False
                sent_13 = False
                sent_15_count = 0

            # Send message if needed
            if message:
                response = requests.post(DISCORD_WEBHOOK_URL, json=message)
                if response.status_code == 204:
                    print("✅ Message sent to Discord")
                else:
                    print(f"❌ Failed to send message: {response.status_code}")

            time.sleep(1)

        except Exception as e:
            print("⚠️ Error:", e)
