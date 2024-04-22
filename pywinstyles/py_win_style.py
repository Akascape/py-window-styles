"""
Py-Win-Styles
Author: Akash Bora
Version: 1.8
"""

from __future__ import annotations
from typing import Any, Union, Callable

try:
    import winreg
    from ctypes import (POINTER, Structure, byref, c_int, pointer, sizeof,
                        windll, c_buffer, WINFUNCTYPE, c_uint64)
    from ctypes.wintypes import DWORD, ULONG
    import platform

except ImportError:
    raise ImportError("pywinstyles import errror: No windows environment detected!")


class ACCENT_POLICY(Structure):
    _fields_ = [
        ("AccentState", DWORD),
        ("AccentFlags", DWORD),
        ("GradientColor", DWORD),
        ("AnimationId", DWORD),
    ]


class WINDOW_COMPOSITION_ATTRIBUTES(Structure):
    _fields_ = [
        ("Attribute", DWORD),
        ("Data", POINTER(ACCENT_POLICY)),
        ("SizeOfData", ULONG),
    ]


class MARGINS(Structure):
    _fields_ = [
        ("cxLeftWidth", c_int),
        ("cxRightWidth", c_int),
        ("cyTopHeight", c_int),
        ("cyBottomHeight", c_int),
    ]


class apply_style():
    """different styles for windows"""

    def __init__(self, window, style: str) -> None:

        styles = ["dark", "mica", "aero", "transparent", "acrylic", "win7",
                "inverse", "popup", "native", "optimised", "light", "normal"]

        if style not in styles:
            raise ValueError(
                f"Invalid style name! No such window style exists: {style} \nAvailable styles: {styles}"
            )

        self.HWND = detect(window)

        if style == "mica":
            ChangeDWMAttrib(self.HWND, 19, c_int(1))
            ChangeDWMAttrib(self.HWND, 1029, c_int(0x01))
        elif style == "optimised":
            ChangeDWMAccent(self.HWND, 30, 1)
        elif style == "dark":
            ChangeDWMAttrib(self.HWND, 19, c_int(1))
            ChangeDWMAttrib(self.HWND, 20, c_int(1))
        elif style == "light":
            ChangeDWMAttrib(self.HWND, 19, c_int(0))
            ChangeDWMAttrib(self.HWND, 20, c_int(0))
        elif style == "inverse":
            ChangeDWMAccent(self.HWND, 6, 1)
        elif style == "win7":
            ChangeDWMAccent(self.HWND, 11, 1)
        elif style == "aero":
            paint(window)
            ChangeDWMAccent(self.HWND, 30, 2)
            ChangeDWMAccent(self.HWND, 19, 3, color=0x000000)
        elif style == "acrylic":
            paint(window)
            ChangeDWMAttrib(self.HWND, 20, c_int(1))
            ChangeDWMAccent(self.HWND, 30, 3, color=0x292929)
            ExtendFrameIntoClientArea(self.HWND)
        elif style == "popup":
            ChangeDWMAccent(self.HWND, 4, 1)
        elif style == "native":
            ChangeDWMAccent(self.HWND, 30, 2)
            ChangeDWMAccent(self.HWND, 19, 2)
        elif style == "transparent":
            paint(window)
            ChangeDWMAccent(self.HWND, 30, 2)
            ChangeDWMAccent(self.HWND, 19, 4, color=0)
        elif style == "normal":
            ChangeDWMAccent(self.HWND, 6, 0)
            ChangeDWMAccent(self.HWND, 4, 0)
            ChangeDWMAccent(self.HWND, 11, 0)
            ChangeDWMAttrib(self.HWND, 19, c_int(0))
            ChangeDWMAttrib(self.HWND, 20, c_int(0))
            ChangeDWMAccent(self.HWND, 30, 0)
            ChangeDWMAccent(self.HWND, 19, 0)
            DisableFrameIntoClientArea(self.HWND)

class change_header_color():
    """change the titlebar background color"""

    def __init__(self, window: Any, color: str) -> None:

        self.HWND = detect(window)

        if color == "transparent":
            ChangeDWMAccent(self.HWND, 30, 2)
            return
        else:
            ChangeDWMAccent(self.HWND, 30, 0)

        self.color = DWORD(int(convert_color(color), base=16))
        self.attrib = 35
        ChangeDWMAttrib(self.HWND, self.attrib, self.color)


class change_border_color():
    """change the window border color"""

    def __init__(self, window: Any, color: str) -> None:

        self.HWND = detect(window)
        self.color = DWORD(int(convert_color(color), base=16))
        self.attrib = 34
        ChangeDWMAttrib(self.HWND, self.attrib, self.color)


class change_title_color():
    """change the title color"""

    def __init__(self, window: Any, color: str) -> None:

        self.HWND = detect(window)
        self.color = DWORD(int(convert_color(color), base=16))
        self.attrib = 36
        ChangeDWMAttrib(self.HWND, self.attrib, self.color)


class set_opacity():
    """change opacity of individual widgets"""

    def __init__(self, widget: int, value: float = 1.0, color: str = None) -> None:

        try:
            # check for tkinter widgets exclusively
            widget = widget.winfo_id()
        except:
            pass
        if not isinstance(widget, int):
            raise ValueError("widget ID should be passed, not the widget name.")

        self.widget_id = widget
        self.opacity = int(255 * value)
        self.color = 1 if color is None else DWORD(int(convert_color(color), base=16))
        wnd_exstyle = windll.user32.GetWindowLongA(self.widget_id, -20)
        new_exstyle = wnd_exstyle | 0x00080000
        windll.user32.SetWindowLongA(self.widget_id, -20, new_exstyle)
        windll.user32.SetLayeredWindowAttributes(
            self.widget_id, self.color, self.opacity, 3
        )

class apply_dnd():
    """apply file drag and drop in a widget"""
    
    def __init__(self, widget: int, func: Callable, char_limit: int=260) -> None:

        try:
            # check for tkinter widgets exclusively
            hwnd = widget.winfo_id()
        except:
            hwnd = widget
        if not isinstance(hwnd, int):
            raise ValueError("widget ID should be passed, not the widget name.")
        
        if platform.architecture()[0] == "32bit":
            GetWindowLong = windll.user32.GetWindowLongW
            SetWindowLong = windll.user32.SetWindowLongW
            typ = DWORD

        if platform.architecture()[0] == "64bit":
            GetWindowLong = windll.user32.GetWindowLongPtrA
            SetWindowLong = windll.user32.SetWindowLongPtrA
            typ = c_uint64

        prototype = WINFUNCTYPE(typ, typ, typ, typ, typ)
        WM_DROP_FILES = 0x233
        GWL_WND_PROC = -4
        create_buffer = c_buffer
        func_DragQueryFile = (windll.shell32.DragQueryFile)

        def py_drop_func(hwnd, msg, wp, lp):
            global files
            if msg == WM_DROP_FILES:
                count = func_DragQueryFile(typ(wp), -1, None, None)
                file_buffer = create_buffer(char_limit)
                files = []
                for i in range(count):
                    func_DragQueryFile(typ(wp), i, file_buffer, sizeof(file_buffer))
                    drop_name = file_buffer.value.decode("utf-8")
                    files.append(drop_name)
                func(files)
                windll.shell32.DragFinish(typ(wp))

            return windll.user32.CallWindowProcW(
                *map(typ, (globals()[old], hwnd, msg, wp, lp))
            )

        """ Allow upto 10 widgets only to have dnd feature in one window, reduces system uses"""
        limit_num = 10
        for i in range(limit_num):
            if i + 1 == limit_num:
                raise OverflowError("DND limit reached for this session!")
            owp = f"old_wnd_proc_{i}"
            if owp not in globals():
                old, new = owp, f"new_wnd_proc_{i}"
                break

        globals()[old] = None
        globals()[new] = prototype(py_drop_func)

        windll.shell32.DragAcceptFiles(hwnd, True)
        globals()[old] = GetWindowLong(hwnd, GWL_WND_PROC)
        SetWindowLong(hwnd, GWL_WND_PROC, globals()[new])
        
def ChangeDWMAttrib(hWnd: int, attrib: int, color) -> None:
    windll.dwmapi.DwmSetWindowAttribute(hWnd, attrib, byref(color), sizeof(c_int))

def ChangeDWMAccent(hWnd: int, attrib: int, state: int, color: Union[str, None] = None) -> None:
    accentPolicy = ACCENT_POLICY()

    winCompAttrData = WINDOW_COMPOSITION_ATTRIBUTES()
    winCompAttrData.Attribute = attrib
    winCompAttrData.SizeOfData = sizeof(accentPolicy)
    winCompAttrData.Data = pointer(accentPolicy)

    accentPolicy.AccentState = state
    if color:
        accentPolicy.GradientColor = color

    windll.user32.SetWindowCompositionAttribute(hWnd, pointer(winCompAttrData))


def ExtendFrameIntoClientArea(HWND: int) -> None:
    margins = MARGINS(-1, -1, -1, -1)
    windll.dwmapi.DwmExtendFrameIntoClientArea(HWND, byref(margins))
    
def DisableFrameIntoClientArea(HWND: int) -> None:
    margins = MARGINS(0, 0, 0, 0)
    windll.dwmapi.DwmExtendFrameIntoClientArea(HWND, byref(margins))


def get_accent_color() -> str:
    """returns current accent color of windows
    code provided by Zane (Zingzy) https://github.com/Zingzy
    """
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\DWM")
    value, type = winreg.QueryValueEx(key, "ColorizationAfterglow")
    winreg.CloseKey(key)
    color = f"#{str(hex(value))[4:]}"
    return color


def detect(window: Any):
    """detect the type of UI library and return HWND"""
    try:  # tkinter
        window.update()
        return windll.user32.GetParent(window.winfo_id())
    except:
        pass
    try:  # pyqt/pyside
        return window.winId().__int__()
    except:
        pass
    try:  # wxpython
        return window.GetHandle()
    except:
        pass
    if isinstance(window, int):
        return window  # other ui windows hwnd
    else:
        return windll.user32.GetActiveWindow()  # get active hwnd


def paint(window: Any) -> None:
    """paint black color in background for acrylic/aero to work"""
    try:  # tkinter
        window.config(bg="black")
        return
    except:
        pass
    try:  # pyqt/pyside
        window.setStyleSheet("background-color: transparent;")
        return
    except:
        pass
    try:  # wxpython
        window.SetBackgroundColour("black")
        return
    except:
        pass
    print("Don't know what the window type is, please paint it black")


def convert_color(color_name: str) -> str:
    """convert colors to the required API"""

    NAMES_TO_HEX = {
        "aliceblue": "#f0f8ff",
        "antiquewhite": "#faebd7",
        "aqua": "#00ffff",
        "aquamarine": "#7fffd4",
        "azure": "#f0ffff",
        "beige": "#f5f5dc",
        "bisque": "#ffe4c4",
        "black": "#000000",
        "blanchedalmond": "#ffebcd",
        "blue": "#0000ff",
        "blueviolet": "#8a2be2",
        "brown": "#a52a2a",
        "burlywood": "#deb887",
        "cadetblue": "#5f9ea0",
        "chartreuse": "#7fff00",
        "chocolate": "#d2691e",
        "coral": "#ff7f50",
        "cornflowerblue": "#6495ed",
        "cornsilk": "#fff8dc",
        "crimson": "#dc143c",
        "cyan": "#00ffff",
        "darkblue": "#00008b",
        "darkcyan": "#008b8b",
        "darkgoldenrod": "#b8860b",
        "darkgray": "#a9a9a9",
        "darkgrey": "#a9a9a9",
        "darkgreen": "#006400",
        "darkkhaki": "#bdb76b",
        "darkmagenta": "#8b008b",
        "darkolivegreen": "#556b2f",
        "darkorange": "#ff8c00",
        "darkorchid": "#9932cc",
        "darkred": "#8b0000",
        "darksalmon": "#e9967a",
        "darkseagreen": "#8fbc8f",
        "darkslateblue": "#483d8b",
        "darkslategray": "#2f4f4f",
        "darkslategrey": "#2f4f4f",
        "darkturquoise": "#00ced1",
        "darkviolet": "#9400d3",
        "deeppink": "#ff1493",
        "deepskyblue": "#00bfff",
        "dimgray": "#696969",
        "dimgrey": "#696969",
        "dodgerblue": "#1e90ff",
        "firebrick": "#b22222",
        "floralwhite": "#fffaf0",
        "forestgreen": "#228b22",
        "fuchsia": "#ff00ff",
        "gainsboro": "#dcdcdc",
        "ghostwhite": "#f8f8ff",
        "gold": "#ffd700",
        "goldenrod": "#daa520",
        "gray": "#808080",
        "grey": "#808080",
        "green": "#008000",
        "greenyellow": "#adff2f",
        "honeydew": "#f0fff0",
        "hotpink": "#ff69b4",
        "indianred": "#cd5c5c",
        "indigo": "#4b0082",
        "ivory": "#fffff0",
        "khaki": "#f0e68c",
        "lavender": "#e6e6fa",
        "lavenderblush": "#fff0f5",
        "lawngreen": "#7cfc00",
        "lemonchiffon": "#fffacd",
        "lightblue": "#add8e6",
        "lightcoral": "#f08080",
        "lightcyan": "#e0ffff",
        "lightgoldenrodyellow": "#fafad2",
        "lightgray": "#d3d3d3",
        "lightgrey": "#d3d3d3",
        "lightgreen": "#90ee90",
        "lightpink": "#ffb6c1",
        "lightsalmon": "#ffa07a",
        "lightseagreen": "#20b2aa",
        "lightskyblue": "#87cefa",
        "lightslategray": "#778899",
        "lightslategrey": "#778899",
        "lightsteelblue": "#b0c4de",
        "lightyellow": "#ffffe0",
        "lime": "#00ff00",
        "limegreen": "#32cd32",
        "linen": "#faf0e6",
        "magenta": "#ff00ff",
        "maroon": "#800000",
        "mediumaquamarine": "#66cdaa",
        "mediumblue": "#0000cd",
        "mediumorchid": "#ba55d3",
        "mediumpurple": "#9370db",
        "mediumseagreen": "#3cb371",
        "mediumslateblue": "#7b68ee",
        "mediumspringgreen": "#00fa9a",
        "mediumturquoise": "#48d1cc",
        "mediumvioletred": "#c71585",
        "midnightblue": "#191970",
        "mintcream": "#f5fffa",
        "mistyrose": "#ffe4e1",
        "moccasin": "#ffe4b5",
        "navajowhite": "#ffdead",
        "navy": "#000080",
        "oldlace": "#fdf5e6",
        "olive": "#808000",
        "olivedrab": "#6b8e23",
        "orange": "#ffa500",
        "orangered": "#ff4500",
        "orchid": "#da70d6",
        "palegoldenrod": "#eee8aa",
        "palegreen": "#98fb98",
        "paleturquoise": "#afeeee",
        "palevioletred": "#db7093",
        "papayawhip": "#ffefd5",
        "peachpuff": "#ffdab9",
        "peru": "#cd853f",
        "pink": "#ffc0cb",
        "plum": "#dda0dd",
        "powderblue": "#b0e0e6",
        "purple": "#800080",
        "red": "#ff0000",
        "rosybrown": "#bc8f8f",
        "royalblue": "#4169e1",
        "saddlebrown": "#8b4513",
        "salmon": "#fa8072",
        "sandybrown": "#f4a460",
        "seagreen": "#2e8b57",
        "seashell": "#fff5ee",
        "sienna": "#a0522d",
        "silver": "#c0c0c0",
        "skyblue": "#87ceeb",
        "slateblue": "#6a5acd",
        "slategray": "#708090",
        "slategrey": "#708090",
        "snow": "#fffafa",
        "springgreen": "#00ff7f",
        "steelblue": "#4682b4",
        "tan": "#d2b48c",
        "teal": "#008080",
        "thistle": "#d8bfd8",
        "tomato": "#ff6347",
        "turquoise": "#40e0d0",
        "violet": "#ee82ee",
        "wheat": "#f5deb3",
        "white": "#ffffff",
        "whitesmoke": "#f5f5f5",
        "yellow": "#ffff00",
        "yellowgreen": "#9acd32",
    }

    if not color_name.startswith("#"):
        if color_name in NAMES_TO_HEX:
            color = NAMES_TO_HEX[color_name]
        elif color_name.startswith("grey") or color_name.startswith("gray"):
            color = f"#{color_name[-2:]}{color_name[-2:]}{color_name[-2:]}"
        else:
            raise ValueError(f"Invalid color passed: {color_name}")
    else:
        color = color_name

    color = f"{color[5:7]}{color[3:5]}{color[1:3]}"
    return color
