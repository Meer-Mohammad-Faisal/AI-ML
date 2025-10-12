import pyautogui
import time 
import pyperclip

#step1 : click on the crome  icon at coordinate ()
pyautogui.click(1508,1768)
time.sleep(1)

#step2 Drag the mouse from (992, 197) to (2208,1286)
pyautogui.moveTo(992, 197)
pyautogui.dragTo(2208,1286, duration=1.0,button='left')

#step 3 copy the selected text to the clopboard
pyautogui.hotkey('ctrl','c')
time.sleep(1)

#step 4 retrive the  text from clipboard and store it in a variable
text = pyperclip.paste()

print(text)