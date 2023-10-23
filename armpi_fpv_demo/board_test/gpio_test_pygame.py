# import pygame

# pygame.init()
# pygame.joystick.init()

# # Check if there's any joystick available
# if pygame.joystick.get_count() > 0:
#     joystick = pygame.joystick.Joystick(0)
#     joystick.init()

#     print(f"Joystick Name: {joystick.get_name()}")
#     print(f"Number of Buttons: {joystick.get_numbuttons()}")

#     try:
#         while True:
#             pygame.event.pump()
#             for event in pygame.event.get():
#                 if event.type == pygame.JOYBUTTONDOWN:
#                     button_id = event.button
#                     print(f"Button {button_id} Pressed")
#                 elif event.type == pygame.JOYBUTTONUP:
#                     button_id = event.button
#                     print(f"Button {button_id} Released")
    
#     except KeyboardInterrupt:
#         pygame.quit()

import pygame
import RPi.GPIO as GPIO

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 13  # Replace with the GPIO pin connected to your button
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize pygame
pygame.init()

# Set up display
win = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Button Test")

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read button input
    button_state = GPIO.input(BUTTON_PIN)

    # Draw button state on the screen
    win.fill((255, 255, 255))  # Clear screen
    font = pygame.font.Font(None, 36)
    text = font.render("Button State: {}".format(button_state), True, (0, 0, 0))
    win.blit(text, (20, 80))
    pygame.display.update()

# Clean up
pygame.quit()
GPIO.cleanup()

