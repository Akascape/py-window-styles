Examples for all the supported libraries:

# Win32
```c++
#ifndef UNICODE
#define UNICODE
#endif 

#include <windows.h>

#pragma comment(lib, "user32.lib")

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE, PWSTR pCmdLine, int nCmdShow)
{

    const wchar_t CLASS_NAME[]  = L"Mica Window Class";
    
    WNDCLASS wc = { };

    wc.lpfnWndProc   = WindowProc;
    wc.hInstance     = hInstance;
    wc.lpszClassName = CLASS_NAME;

    RegisterClass(&wc);

    HWND hwnd = CreateWindowEx(
        NULL,
        CLASS_NAME,
        L"Win32 Application",
        WS_OVERLAPPEDWINDOW,

        CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT,

        NULL, 
        NULL,
        hInstance,
        NULL
        );

    if (hwnd == NULL)
    {
        return 0;
    }
	
    ShowWindow(hwnd, nCmdShow);

    MSG msg = { };
    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
    case WM_DESTROY:
        PostQuitMessage(0);
        return 0;

    case WM_PAINT:
        {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hwnd, &ps);

            FillRect(hdc, &ps.rcPaint, (HBRUSH) (COLOR_WINDOW+1));
            EndPaint(hwnd, &ps);
        }
        return 0;
    }
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}
```
```python
from pywinstyles import change_header_color
from ctypes import windll, c_char_p

hwnd: int = windll.user32.FindWindowW(c_char_p(None), "Win32 Application")

change_header_color(hwnd, color="blue")
```

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

# Other UI Libraries
Any other python UI libraries are also supported if you can retrieve the **HWND (window handle)** of the required window and pass it in pywinstyles. Commonly used libraries are supported by default as shown above, so you don't have to do this extra work for them.

```python
from ctypes import windll
import pywinstyles
...
hwnd = windll.user32.GetActiveWindow()
# Or get the target winow hwnd
from ctypes import c_char_p
hwnd = windll.user32.FindWindowW(c_char_p(None), "{Target Window Name}")


pywinstyles.change_header_color(hwnd, color="blue")
```
Note: If you are applying themes like *acrylic*, then paint your UI window with black using suitable methods. Otherwise those theme doesn't work properly.
