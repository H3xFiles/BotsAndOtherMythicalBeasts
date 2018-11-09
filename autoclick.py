import win32gui as win32gui
import win32api, win32con
import time




def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


for i in range(100000):
    x, y = win32gui.GetCursorPos()
    click(x, y)
time.sleep(1)
