Examples for all the supported libraries are given here, just adding one line of code can take your application to the next level! 🔥

# Tkinter
```python
import tkinter
import pywinstyles

root = tkinter.Tk()

pywinstyles.change_header_color(root, color="blue")

root.mainloop()
```

# CustomTkinter
```python
import customtkinter
import pywinstyles

root = customtkinter.CTk()

pywinstyles.change_header_color(root, color="blue")

root.mainloop()
```

# PyGame
```python
import pygame
import pywinstyles

screen = pygame.display.set_mode((300, 200))

hwnd = pygame.display.get_wm_info()["window"]
pywinstyles.change_header_color(hwnd, color="blue")

pygame.display.flip()
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
```

# PyQt
```python
import sys
from PyQt5 import QtWidgets
import pywinstyles

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()

pywinstyles.change_header_color(window, color="blue")

window.show()
sys.exit(app.exec_())
```
# PySide
```python
from PySide2.QtWidgets import QApplication, QWidget
import sys
import pywinstyles

app = QApplication(sys.argv)
window = QWidget()

pywinstyles.change_header_color(window, color="blue")

window.show()
app.exec_()
```

# WxPython
```python
import wx
import pywinstyles

app = wx.App()

frame = wx.Frame(parent=None, title='wx-python')

pywinstyles.change_header_color(frame, color="blue")

frame.Show()
app.MainLoop()
```

# PySimpleGUI
```python
import PySimpleGUI as sg
import pywinstyles

layout = [[sg.Text("pywinstyles example")], [sg.Button("OK")]]

window = sg.Window("Demo", layout, finalize=True) # finalize the window

pywinstyles.change_header_color(window.TKroot, color="blue")
    
while True:    
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
```

# Other UI Libraries
Any other python UI libraries, like kivy, are also supported. You just have to retrieve the **HWND (window handle)** of the window and pass it to pywinstyles. Commonly used libraries are supported by default as shown above, so you don't have to do this extra work for them.

```python
from ctypes import windll
import pywinstyles
...
# use this method for any other libraries
hwnd = windll.user32.GetActiveWindow()
# alternate method to find the window by name:
# hwnd = windll.user32.FindWindowW(None, window_name)

pywinstyles.change_header_color(hwnd, color="blue")
```

Note: If you are applying themes like *acrylic*, then paint your UI window with black color using suitable methods.
