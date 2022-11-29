import win32api;
import win32con;
import time;

w, h = [win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)];

def click(x,y):
    win32api.SetCursorPos((x,y));
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0);
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0);



pressed = False;

while True:
	time.sleep(0.1);
	if win32api.GetAsyncKeyState(ord('0')):
		pressed = not pressed;
	if pressed:
		click(int(w*80/100), int(h*75/100));
	