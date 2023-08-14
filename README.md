# py-window-styles

Customize your UI window with awesome built-in Windows 11 header styles and themes.
**Windows 10 is also supported (only themes).**

![Screenshot](https://github.com/Akascape/py-window-styles/assets/89206401/986062c0-30a0-4289-929a-e5e2440b8dd1)

## Supported UI Libraries
- Win32
- Tkinter
- Customtkinter
- PyQt
- PySide
- WxPython
- Pygame
- Kivy
- PySimpleGUI
- more...

[<img src="https://img.shields.io/badge/View-Examples-informational?&color=darkblue&style=for-the-badge" width="150">](https://github.com/Akascape/py-window-styles/blob/main/Example_Documentation.md)

## Installation
```
pip install pywinstyles
```
<img src="https://img.shields.io/badge/Platform-Windows-informational?" width="150"> [<img src="https://img.shields.io/pypi/v/pywinstyles?style=flat" width="90">](https://pypi.org/project/pywinstyles)
[<img src="https://static.pepy.tech/badge/pywinstyles" width="130">](https://pepy.tech/project/pywinstyles)

## Window Styles
```python
import pywinstyles
...
pywinstyles.apply_style(window, style)
...
```
| Style Name | Preview |
|-----------| ------------|
| mica |  ![](https://user-images.githubusercontent.com/89206401/222347983-d840bee2-a100-40b4-a418-1a604bfc67d4.jpg) |
| acrylic | ![](https://github.com/Akascape/py-window-styles/assets/89206401/cbd54b23-0626-44c7-a89a-6359517ed1a5) |
| aero | ![](https://user-images.githubusercontent.com/89206401/223035861-ca4a1c52-7475-43a9-b197-1c06bb4ecec7.jpg)|
| transparent | ![](https://github.com/Akascape/py-window-styles/assets/89206401/317e9c4e-be27-444e-aa22-02b625e94960)  |
| optimised | ![](https://user-images.githubusercontent.com/89206401/246128698-726ba674-843b-46ef-8a4d-8732b66a13a3.jpg) |
| win7 | ![](https://github.com/Akascape/py-window-styles/assets/89206401/b01585b4-0e50-471d-ae34-c3eec9607511) |
| inverse | ![](https://github.com/Akascape/py-window-styles/assets/89206401/b7c18335-7498-43ca-bea2-6c35255a7c92) |
| native |  ![](https://github.com/Akascape/py-window-styles/assets/89206401/3047d165-006f-4386-88a8-b5272f740ed2) |
| popup | ![](https://github.com/Akascape/py-window-styles/assets/89206401/dac6672e-99e8-4abc-b779-aed25c32ed09) |
| dark | ![](https://github.com/Akascape/py-window-styles/assets/89206401/ca41fa22-ed9d-437f-8574-bf0a13218747) |

## Custom Window Colors (Only works in windows 11)
![](https://user-images.githubusercontent.com/89206401/222352861-8af5703c-a64c-4c67-9192-29ffa0e3b4b5.jpg)
### Changing Title Bar Color
```python
pywinstyles.change_header_color(window, color="#00524d")  
```
### Changing Title Text Color
```python
pywinstyles.change_title_color(window, color="white") 
```
### Change Border Color
```python
pywinstyles.change_border_color(window, color="#00ffff")
```

### Getting Windows Accent Color
```python
default_color = pywinstyles.get_accent_color()
```

**Hope this package can help in UI development with python**

**Author: Akash Bora**

