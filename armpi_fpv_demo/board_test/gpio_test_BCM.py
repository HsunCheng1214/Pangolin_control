import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin number you connected the button to
# key1(BCM) = 13
# key2(BCM) = 23
x = input("pin: ")
button_pin = int(x)

# Setup the button pin as input with pull-up resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

key1 = 1

try:
     while True:
        # Read the button state
        button_pressed = GPIO.input(button_pin) == GPIO.LOW
        
        # Check if the button is pressed and the state is not already "button pressed"
        if button_pressed and not button_state:
            print("Button pressed")
            button_state = True
        # Check if the button is pressed and the state is already "button pressed"
        elif button_pressed and button_state:
            print("Button released")
            button_state = False
        
        # Add a small delay to debounce the button (optional)
        time.sleep(0.1)


    # while True:
    #     # Read the button state
    #     button_state = GPIO.input(button_pin)

    #     # Check for button press
    #     if button_state and not prev_button_state:
    #         print("Button pressed")
    #     elif not button_state and prev_button_state:
    #         print("Button released")

    #     # Update previous button state
    #     prev_button_state = button_state

    #     # Add a small delay to debounce the button
    #     time.sleep(0.1)


except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt (Ctrl+C)
    GPIO.cleanup()
