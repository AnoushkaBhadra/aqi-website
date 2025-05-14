import serial
import time

# Connect to Arduino
ser = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)  # Allow Arduino to reset
print("Serial connection established.")

# Data lists
co_list, smoke_list, hydrogen_list = [], [], []
nh3_list, co2_list = [], []
benzene_list, toluene_list, xylene_list = [], [], []
no_list, no2_list, nox_list = [], [], []
lpg_list, aqi_list = [], []

try:
    while True:
        line = ser.readline().decode('utf-8').strip()

        # Skip empty lines or separators
        if not line or "-----" in line or "----" in line:
            continue

        try:
            key, value = line.split(":", 1)
            value = value.strip().split(" ")[0]  # Get just the number
            value = float(value)

            # Map each value to its respective list
            key = key.upper()
            if key == "CO":
                co_list.append(value)
            elif key == "SMOKE":
                smoke_list.append(value)
            elif key == "HYDROGEN":
                hydrogen_list.append(value)
            elif key == "NH3":
                nh3_list.append(value)
            elif key == "CO2":
                co2_list.append(value)
            elif key == "BENZENE":
                benzene_list.append(value)
            elif key == "TOLUENE":
                toluene_list.append(value)
            elif key == "XYLENE":
                xylene_list.append(value)
            elif key == "NO":
                no_list.append(value)
            elif key == "NO2":
                no2_list.append(value)
            elif key == "NOX":
                nox_list.append(value)
            elif key == "LPG":
                lpg_list.append(value)
            elif key == "AQI":
                aqi_list.append(value)

        except ValueError:
            # Ignore any parsing errors silently
            pass

except KeyboardInterrupt:
    print("\n\n--- Data Collection Stopped ---")
    print("Collected Data:")
    print(f"NO: {no_list}")
    print(f"NO2: {no2_list}")
    print(f"NOx: {nox_list}")
    print(f"NH3: {nh3_list}")
    print(f"CO: {co_list}")
    print(f"Benzene: {benzene_list}")
    print(f"Toluene: {toluene_list}")
    print(f"Xylene: {xylene_list}")
    #print(f"Smoke: {smoke_list}")
    #print(f"Hydrogen: {hydrogen_list}")
    
    #print(f"CO2: {co2_list}")
    
    
    #print(f"LPG: {lpg_list}")
    print(f"AQI: {aqi_list}")
    ser.close()
