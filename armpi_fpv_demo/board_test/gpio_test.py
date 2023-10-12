import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin number you connected the button to
x = input("pin: ")
button_pin = int(x)

# Setup the button pin as input with pull-up resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Read the button state
        button_state = GPIO.input(button_pin)

        # Check if the button is pressed
        if button_state == GPIO.LOW:
            print("Button pressed!")
        else:
            print("Button released!")

        # Wait for a short duration to avoid rapid button presses
        time.sleep(0.2)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt (Ctrl+C)
    GPIO.cleanup()
