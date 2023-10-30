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

key1_state = 1
key1 = False

try:
     while True:


        # Read the button state
        if GPIO.input(button_pin) == 0 and key1_state == 1:
            if key1 == False:
                #start conntrol
                key1 = True
            else:
                #stop 
                key1 = False
               
        key1_state = GPIO.input(button_pin)
        print(key1)
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
