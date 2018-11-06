import time
import threading
from pynput.mouse import Button, Controller
import pynput.keyboard as kb
import random


delay = 30
button = Button.left
start_stop_key = kb.KeyCode(char='s')
exit_key = kb.KeyCode(char='e')

def action(self):
    arrow_keys = [kb.Key.up,kb.Key.down,kb.Key.right,kb.Key.left]
    return random.choice(arrow_keys)

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False



    def run(self):
        while self.program_running:
            while self.running:
                self.action1 = action(self)
                self.action2 = action(self)
                print("{}".format(self.action1))
                keyboard.press(self.action1)
                time.sleep(1)
                keyboard.release(self.action1)
                time.sleep(0.5)

                keyboard.press(kb.Key.enter) #open
                keyboard.release(kb.Key.enter)
                time.sleep(0.5)
                mouse.click(self.button)
                mouse.click(self.button)
                mouse.click(self.button) #enter the link
                time.sleep(0.5)
                keyboard.press(kb.Key.enter) #close
                keyboard.release(kb.Key.enter)

                time.sleep(0.5)
                print("{}".format(str(self.action2)))
                keyboard.press(self.action2)
                time.sleep(1)
                keyboard.release(self.action2)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
keyboard = kb.Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            print("Autobot is paused ...")
            click_thread.stop_clicking()
        else:
            print("Autobot is running ...")
            click_thread.start_clicking()
    elif key == exit_key:
        print("Autobot closed.")
        click_thread.exit()
        listener.stop()


with kb.Listener(on_press=on_press) as listener:
    listener.join()
