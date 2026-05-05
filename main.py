import time
import RPi.GPIO as GPIO

# Disable warnings
GPIO.setwarnings(False)

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Input pin (connect your switch here)
sensor_pin = 3
GPIO.setup(sensor_pin, GPIO.IN)

# Parameters
phantom_power = 5.0   # watts
tariff = 6.0          # Rs per unit (1 kWh)
energy = 0

print("Phantom Power Detection System Started\n")

try:
    while True:
        state = GPIO.input(sensor_pin)

        if state == 1:
            power = phantom_power
            status = "PHANTOM POWER"
        else:
            power = 0
            status = "OFF"

        # Energy calculation (kWh)
        energy += (power / 1000) * (1 / 3600)

        # Cost calculation
        cost = energy * tariff

        # Display output
        print("----------------------------")
        print("Status :", status)
        print(f"Power  : {power:.2f} W")
        print(f"Energy : {energy:.5f} kWh")
        print(f"Cost   : Rs {cost:.2f}")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram stopped")

finally:
    GPIO.cleanup()