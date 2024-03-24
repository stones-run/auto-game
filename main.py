import time
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
time.sleep(2)
import pyautogui

x, y = pyautogui.position()
print(x, y)

screen = pyautogui.screenshot(region=(1366, 399, 1789 - 1366, 495 - 399))
screen.save("temp.png")

image = cv2.imread("temp.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite("temp1.png", binary)
image = cv2.imread("temp1.png")
text = pytesseract.image_to_string(image)
print(text)

import pynput.mouse as pm
import threading


def on_click(x, y, button, pressed):
    # 监听鼠标点击
    if pressed:
        print("按下坐标")
        mxy = "{},{}".format(x, y)
        print(mxy)
        print(button)
    if not pressed:
        print("松开坐标")
        mxy = "{},{}".format(x, y)
        print(mxy)
        print(button)


def ls_k_thread():
    while (1):
        with pm.Listener(on_click=on_click) as pmlistener:
            pmlistener.join()


def analyse_pic_thread():
    r = threading.Thread(target=ls_k_thread)
    r.start()


analyse_pic_thread()
