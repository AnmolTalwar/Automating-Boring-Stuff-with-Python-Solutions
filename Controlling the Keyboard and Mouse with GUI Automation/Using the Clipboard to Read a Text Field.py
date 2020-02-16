import pyautogui,pyperclip

a = pyautogui.getWindowsWithTitle('Notepad')
a[0].activate()

pyautogui.moveTo(953,552)
pyautogui.click()

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

b=pyperclip.paste()
print(b)

#a[0].close()
