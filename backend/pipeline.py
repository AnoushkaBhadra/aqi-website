import serial
import time
import sqlite3


ser = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)  
print("Serial connection established.")

conn = sqlite3.connect('aqi_data.db')
cursor = conn.cursor()


current_data = {}

try:
    while True:
        line = ser.readline().decode('utf-8').strip()

        if not line or "-----" in line or "----" in line:
            continue

        try:
            key, value = line.split(":", 1)
            value = value.strip().split(" ")[0]
            value = float(value)
            key = key.upper()

            
            if key in ["NO", "NO2", "NOX", "NH3", "CO", "BENZENE", "TOLUENE", "XYLENE", "AQI"]:
                current_data[key] = value

            
            if len(current_data) == 9:
                
                cursor.execute("SELECT COUNT(*) FROM aqi_readings")
                count = cursor.fetchone()[0]

                if count >= 5040:
                    cursor.execute("DELETE FROM aqi_readings WHERE id = (SELECT id FROM aqi_readings ORDER BY id LIMIT 1)")

                
                cursor.execute("""
                    INSERT INTO aqi_readings (NO, NO2, NOx, NH3, CO, Benzene, Toluene, Xylene, AQI)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    current_data["NO"],
                    current_data["NO2"],
                    current_data["NOX"],
                    current_data["NH3"],
                    current_data["CO"],
                    current_data["BENZENE"],
                    current_data["TOLUENE"],
                    current_data["XYLENE"],
                    current_data["AQI"]
                ))
                conn.commit()
                print("New data inserted. Total rows maintained: ")
                current_data.clear()  

        except ValueError:
            pass  

except KeyboardInterrupt:
    print("\n--- Data Collection Stopped ---")
    ser.close()
    conn.close()
