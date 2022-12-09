## Import 'pyautogui'.
import pyautogui

## Uncomment to test the device screen resolution.
# print(pyautogui.size())

## Use 'moveTo' to move the mouse across to the Brave icon.
pyautogui.moveTo(460, 1080, duration=1)

## Use 'moveTo' to move the mouse to it's relative position (adjust itself on the Brave icon).
pyautogui.moveRel(-10, 0, duration=1)

## Use 'click' to click on the Brave icon.
pyautogui.click(button='right')

## Use 'moveTo' to move the mouse upwards to select a New Window.
pyautogui.moveTo(430, 880, duration=1)

## Use 'click' to click on New Window.
pyautogui.click(button='right')

## Use 'moveTo' to move the mouse upwards to middle of the screen.
## Use 'scroll' to scroll down the News.
pyautogui.moveTo(680, 680, duration=1)
pyautogui.vscroll(-5000000, x=680, y=680)