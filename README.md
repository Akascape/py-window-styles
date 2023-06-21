# py-window-styles
Customize your tkinter/pyqt window with awesome built-in windows header styles and themes.
**This is only for windows 11 (some themes may not work in windows 10).**

![Screenshot 2023-06-19 205353](https://github.com/Akascape/py-window-styles/assets/89206401/986062c0-30a0-4289-929a-e5e2440b8dd1)

# Window Styles
```python
import pywindowstyles
...
pywindowstyles.apply_style(window, style)
```
| Style Name | Image |
|-----------| ------------|
| mica |  ![](https://user-images.githubusercontent.com/89206401/222347983-d840bee2-a100-40b4-a418-1a604bfc67d4.jpg) |
| **acrylic** | ![](https://github.com/Akascape/py-window-styles/assets/89206401/cbd54b23-0626-44c7-a89a-6359517ed1a5) |
| aero | ![](https://user-images.githubusercontent.com/89206401/223035861-ca4a1c52-7475-43a9-b197-1c06bb4ecec7.jpg)|
| transparent | ![](https://github.com/Akascape/py-window-styles/assets/89206401/317e9c4e-be27-444e-aa22-02b625e94960)  |
| optimised | ![](https://user-images.githubusercontent.com/89206401/246128698-726ba674-843b-46ef-8a4d-8732b66a13a3.jpg) |
| win7 | ![](https://github.com/Akascape/py-window-styles/assets/89206401/b01585b4-0e50-471d-ae34-c3eec9607511) |
| inverse | ![](https://github.com/Akascape/py-window-styles/assets/89206401/b7c18335-7498-43ca-bea2-6c35255a7c92) |
| native |  ![](https://github.com/Akascape/py-window-styles/assets/89206401/3047d165-006f-4386-88a8-b5272f740ed2) |
| popup | ![](https://github.com/Akascape/py-window-styles/assets/89206401/dac6672e-99e8-4abc-b779-aed25c32ed09) |
| dark | ![](https://github.com/Akascape/py-window-styles/assets/89206401/ca41fa22-ed9d-437f-8574-bf0a13218747) |

# Custom Colors
![](https://user-images.githubusercontent.com/89206401/222352861-8af5703c-a64c-4c67-9192-29ffa0e3b4b5.jpg)
## Changing Title Bar Color
```python
pywindowstyles.change_header_color(window, red=10, blue=50, green=50) # rgb order is manual
```
## Changing Title Text Color
```python
pywindowstyles.change_title_color(window, red=100, blue=100, green=100) # 100 is maximum strength
```
## Change Border Color
```python
pywindowstyles.change_border_color(root, red=10, blue=100, green=100) # there is also a border color
```

