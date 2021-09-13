import pyautogui
from PIL import Image
import time

def main():
    count = 0
    pointer_image = Image.open('images/pointer.png')
    left_bound_image = Image.open('images/box_left.png')
    right_bound_image = Image.open('images/box_right.png')
    pyautogui.PAUSE = 0.01

    while True:
        ptr_region = pyautogui.locateOnScreen(pointer_image, confidence=0.75, grayscale=True, region=(800, 140, 800, 40))
        left_bound = pyautogui.locateOnScreen(left_bound_image, confidence=0.6, grayscale=True, region=(800, 140, 800, 40))
        right_bound = pyautogui.locateOnScreen(right_bound_image, confidence=0.6, grayscale=True, region=(800, 140, 800, 40))
        print("ptr: " + str(ptr_region))
        # print("left: " + str(left_bound))
        # print("right: " + str(right_bound))
        if ptr_region:
            print(str(count) + ': pointer found')
            box_left_val = box_right_val = -1
            if left_bound:
                box_left_val = left_bound.left + left_bound.width / 2
            if right_bound:
                box_right_val = right_bound.left + right_bound.width / 2
            # box_middle_val = (box_left_val + box_right_val) / 2
            ptr_middle_val = ptr_region.left + ptr_region.width / 2
            if box_left_val <= ptr_middle_val < box_right_val:
                pyautogui.click()
            elif ptr_middle_val < box_left_val:
                pyautogui.mouseDown()
                time.sleep(1)
                pyautogui.mouseUp()
        else:
            print(str(count) + ': no pointer')
        
        count += 1

if __name__ == "__main__":
    main()