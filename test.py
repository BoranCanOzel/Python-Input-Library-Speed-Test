import time
import keyboard
import mouse
import pyautogui
from pynput.mouse import Controller as PynputController

def move_mouse_with_mouse():
    mouse.move(1, 1, absolute=False, duration=0)

def move_mouse_with_pyautogui():
    pyautogui.move(1, 1, duration=0)

def move_mouse_with_pynput():
    pynput_controller = PynputController()
    current_position = pynput_controller.position
    pynput_controller.move(current_position[0] + 1, current_position[1] + 1)

def compare_speed():
    print("Press 'A' to move mouse with 'mouse' library.")
    print("Press 'B' to move mouse with 'pyautogui' library.")
    print("Press 'C' to move mouse with 'pynput' library.")
    print("Press 'Q' to quit.")

    while True:
        if keyboard.is_pressed("q"):
            print("Exiting the program...")
            break
        elif keyboard.is_pressed("a"):
            start_time = time.time()
            move_mouse_with_mouse()
            end_time = time.time()
            print(f"Time taken with 'mouse' library: {end_time - start_time} seconds")
        elif keyboard.is_pressed("b"):
            start_time = time.time()
            move_mouse_with_pyautogui()
            end_time = time.time()
            print(f"Time taken with 'pyautogui' library: {end_time - start_time} seconds")
        elif keyboard.is_pressed("c"):
            start_time = time.time()
            move_mouse_with_pynput()
            end_time = time.time()
            print(f"Time taken with 'pynput' library: {end_time - start_time} seconds")

compare_speed()
