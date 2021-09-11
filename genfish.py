import pyautogui

def main():
    while True:
        
        if pyautogui.locateOnScreen('images/box.png', confidence=0.8):
            print('box found')
            pyautogui.click()
        else:
            print('no box')

if __name__ == "__main__":
    main()