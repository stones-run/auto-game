import time

import pyautogui


class Base(object):
    def click_image(self, image_name, click_count=1, is_raise=False):
        try:
            join_pos = pyautogui.locateOnScreen("images/" + image_name)
        except pyautogui.ImageNotFoundException:
            print(f"点击图片失败:{image_name}")
            if is_raise:
                raise pyautogui.ImageNotFoundException
            return False
        join_pos = pyautogui.center(join_pos)
        pyautogui.moveTo(join_pos)
        for i in range(click_count):
            # time.sleep(0.5)
            pyautogui.click()
        print(f"点击图片成功:{image_name}")
        return True
