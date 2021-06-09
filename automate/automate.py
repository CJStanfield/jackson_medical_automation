from pynput.mouse import Button, Controller
from keyboard import keyboard
from mouse import mouse_pos
import pandas as pd

mouse = Controller()
MOVE_TASK = 'move_mouse'
CLICK_TASK = 'click_mouse'
KEYBOARD_TASK = 'keystroke'
automation_cols = ['x', 'y', 'task']

def create_automation(filename):
    automation = pd.DataFrame(columns=automation_cols)
    print("Press escap")
    keyboard.start_keyboard_listener()
    mouse_pos.start_listen()
    pd.DataFrame.to_csv(filename)



def complete_task(x, y, task):
    if task == MOVE_TASK:
        mouse.position = (x, y)
    elif task == CLICK_TASK:
        mouse.press(Button.left)
        mouse.release(Button.left)
    elif task == KEYBOARD_TASK:
        return
    else:
        print('Invalid instruction: ' + task)
    return


def automate(instruction_path):
    instructions = pd.read_csv(instruction_path)
    instructions.apply(lambda x: complete_task(x.x, x.y, x.task), axis=1)
    return



# Read pointer position
# print('The current pointer position is {0}'.format(
#     mouse.position))

# Set pointer position
# mouse.position = (43, 65)
# print('Now we have moved it to {0}'.format(
#     mouse.position))

# # Move pointer relative to current position
# mouse.move(5, -5)
#
# Press and release
# mouse.press(Button.left)
# mouse.release(Button.left)
#
# # Double click; this is different from pressing and releasing
# # twice on macOS
# mouse.click(Button.left, 2)
#
# # Scroll two steps down
# mouse.scroll(0, 2)
