from PIL.ImageOps import grayscale
import pyautogui
from PIL import Image
import time

def main():
    count = 0
    pointer_image = Image.open('images/pointer.png')
    while True:
        ptr_region = pyautogui.locateOnScreen(pointer_image, confidence=0.75, grayscale=True, region=(800, 80, 800, 100))
        box_region = pyautogui.locateOnScreen(pointer_image, confidence=0.75, grayscale=True, region=(800, 80, 800, 100))
        print(ptr_region)
        if ptr_region:
            print(str(count) + ': pointer found')
            pyautogui.click()
        else:
            print(str(count) + ': no pointer')
        
        count += 1

if __name__ == "__main__":
    main()